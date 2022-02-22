import sys

d = {
  'Ab': 'G#',
  'G#': 'Ab',
  'Gb': 'F#',
  'F#': 'Gb',
  'Eb': 'D#',
  'D#': 'Eb',
  'Db': 'C#',
  'C#': 'Db',
  'Bb': 'A#',
  'A#': 'Bb'
}

case = 1
for i in sys.stdin:
  i = i.split()
  if len(i[0]) == 1:
    print("Case {0}: UNIQUE".format(case))
    break
  else:
    for key, val in d:
      if i[0] in d:
        print("Case {0}: {1} {2}".format(case, d[i[0]], i[1]))
        break
  case += 1
