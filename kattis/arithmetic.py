import sys

def main():
  # oct -> dec -> hex
  print('{0:x}'.format(int(sys.stdin.readline(), 8)).upper())

if __name__ == '__main__':
  main()
