//
//  AppDelegate.h
//  ChaosReceiver
//
//  Created by Joseph Constan on 2/1/13.
//  Copyright (c) 2013 Joseph Constan. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "PGMidi.h"


@interface AppDelegate : NSObject <NSApplicationDelegate, NSSpeechRecognizerDelegate>

@property (weak, nonatomic) IBOutlet NSTextField *tempoField;

@end
