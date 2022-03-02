keywords = {
  'and' : '&',
  'are' : 'r',
  'at'  : '@',
  'be'  : 'b',
  'bea' : 'b',
  'bee' : 'b',
  'eye' : 'i',
  'for' : '4',
  'four': '4',
  'oh'  : 'o',
  'one' : '1',
  'owe' : 'o',
  'sea' : 'c',
  'see' : 'c',
  'to'  : '2',
  'too' : '2',
  'two' : '2',
  'why' : 'y',
  'won' : '1',
  'you' : 'u'
}

cap = lambda a, b: (a, a.capitalize())[b.capitalize() == b]

def main(phrases):
  for phrase in phrases:
    output = []
    for word in phrase:
      i = 0
      curr = ''
      while i < len(word):
        for amt in [4, 3, 2]:
          if i + amt > len(word):
            continue
          candidate = word[i:i + amt].lower()
          if candidate in keywords:
            curr += cap(keywords[candidate], word[i:i + amt])
            i += amt
            break
        else:
          curr += word[i]
          i += 1
      output.append(curr)
    print(' '.join(output))

if __name__ == '__main__':
  main([input().split() for _ in range(int(input()))])
