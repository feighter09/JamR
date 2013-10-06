#GIVEN: key & progression
#notes given as letter or letter+#
notes  = ["a","a#","b","c","c#","d","d#","e","f","f#","g","g#"]

scales = {}
for i in range(len(notes)):
  scales[ notes[i] ] = [notes[i],
                        notes[(i +  2) % 12], 
                        notes[(i +  4) % 12], 
                        notes[(i +  5) % 12], 
                        notes[(i +  7) % 12], 
                        notes[(i +  9) % 12], 
                        notes[(i + 11) % 12]]

Mchords = {}
for i in range(len(notes)):
  Mchords[ notes[i] ] = [notes[i], 
                        notes[(i +  4) % 12], 
                        notes[(i +  7) % 12]]

mchords = {}
for i in range(len(notes)):
  mchords[ notes[i] ] = [notes[i], 
                        notes[(i +  3) % 12],  
                        notes[(i +  7) % 12]]

dchords = {}
for i in range(len(notes)):
  dchords[ notes[i] ] = [notes[i], 
                        notes[(i +  3) % 12],  
                        notes[(i +  6) % 12]]

Mscales = {}
for i in range(len(notes)):
  Mscales[ notes[i] ] = [Mchords[notes[i]],mchords[scales[notes[i]][0]],mchords[scales[notes[i]][1]],
            Mchords[scales[notes[i]][2]],Mchords[scales[notes[i]][3]],mchords[scales[notes[i]][4]],
            dchords[scales[notes[i]][5]]]

mscales = {}
for i in range(len(notes)):
  mscales[ notes[i] ] = [mchords[notes[i]],Mchords[scales[notes[i]][0]],Mchords[scales[notes[i]][1]],
            mchords[scales[notes[i]][2]],dchords[scales[notes[i]][3]],Mchords[scales[notes[i]][4]],
            mchords[scales[notes[i]][5]]]

#key = letter, sign = major/minor, roman = [numbers of chord prog]
def makeProgression(key,sign,roman):
  result = []
  for i in roman:
    if sign == "major":
      result.append(Mscales[key][i-1])
    else:
      result.append(mscales[key][i-1])
  return result

print(makeProgression("c","major",[1,4,5]))
