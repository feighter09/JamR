//
//  AppDelegate.m
//  ChaosReceiver
//
//  Created by Joseph Constan on 2/1/13.
//  Copyright (c) 2013 Joseph Constan. All rights reserved.
//

#import "AppDelegate.h"
#import "NSObject+Properties.h"

@interface AppDelegate()
{
    NSDictionary *midiCommands;
    PGMidi *midi;
}
@property (nonatomic) NSNumber *tempo;

@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    // Insert code here to initialize your application
    midi = [[PGMidi alloc] init];
    
    NSSpeechRecognizer *rec = [[NSSpeechRecognizer alloc] init];
    NSArray *vcs = [[NSArray alloc] initWithContentsOfFile:[[NSBundle mainBundle] pathForResource:@"voiceCommands"
                                                                                           ofType:@"plist"]];
    rec.commands = vcs;
    [self applyDefaults];
    
    rec.listensInForegroundOnly = NO;
    rec.blocksOtherRecognizers = YES;
    rec.delegate = self;
    [rec startListening];
}

- (void)applyDefaults
{
    midiCommands = [[NSDictionary alloc] initWithContentsOfFile:[[NSBundle mainBundle] pathForResource:@"midiCommands"
                                                                                            ofType:@"plist"]];
    NSDictionary *defaults = [[NSDictionary alloc] initWithContentsOfFile:[[NSBundle mainBundle] pathForResource:@"midiDefaults"
                                                                                                          ofType:@"plist"]];
    for (NSString *key in [defaults allKeys]) {
        NSNumber *param = defaults[key];
        if ([self hasPropertyNamed:key])
            [self setValue:param forKey:key];
        [self triggerCommand:key withParamater:param];
    }
}

- (void)shiftTempoPositive:(BOOL)positive
{
    NSUInteger newTempo = positive ? (self.tempo.unsignedIntValue * 1.2) : (self.tempo.unsignedIntValue / 1.2);
    self.tempo = @(newTempo);
    [self triggerCommand:@"tempo" withParamater:self.tempo];
}

- (void)setTempo:(NSNumber *)tempo
{
    _tempo = tempo;
    self.tempoField.stringValue = tempo.stringValue;
}

- (void)triggerCommand:(NSString *)command withParamater:(NSNumber *)param
{
    NSNumber *commandNum = midiCommands[command];
    NSLog(@"command: %@ commandnum: %d, param: %d", command, commandNum.unsignedIntValue, param.unsignedIntValue);
    const UInt8 note[3] = {0x90, commandNum.unsignedIntValue, param.unsignedIntValue};
    [midi sendBytes:note size:sizeof(note) channel:0];
}

- (void)speechRecognizer:(NSSpeechRecognizer *)sender didRecognizeCommand:(id)command
{
    if ([command hasSuffix:@"tempo"])
         [self shiftTempoPositive:[command hasPrefix:@"up"]];
    else
        [self triggerCommand:command withParamater:@1];
}

@end
