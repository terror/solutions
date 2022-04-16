d = {
  'clank':  'a',
  'bong':   'b',
  'click':  'c',
  'tap':    'd',
  'poing':  'e',
  'clonk':  'f',
  'clack':  'g',
  'ping':   'h',
  'tip':    'i',
  'cloing': 'j',
  'tic':    'k',
  'cling':  'l',
  'bing':   'm',
  'pong':   'n',
  'clang':  'o',
  'pang':   'p',
  'clong':  'q',
  'tac':    'r',
  'boing':  's',
  'boink':  't',
  'cloink': 'u',
  'rattle': 'v',
  'clock':  'w',
  'toc':    'x',
  'clink':  'y',
  'tuc':    'z',
  'whack':  ' '
}

def main(N):
  ans = []; cap = locked = False
  for _ in range(N):
    curr = input()
    if curr == 'pop':
      if ans:
        ans.pop()
    elif curr == 'bump':
      locked = not locked
    elif curr == 'dink':
      cap = True
    elif curr == 'thumb':
      cap = False
    else:
      ans.append((d[curr], d[curr].upper())[(locked and not cap) or (not locked and cap)])
  return ans

if __name__ == '__main__':
  print(''.join(main(int(input()))))
