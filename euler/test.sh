# Used to ensure all solutions still give the correct result after some
# potential refactoring. The script also provides runtime information for
# each solution.
#
# Once a solution is solved it should be added to the `main` function.

RED=`echo -en "\e[31m"`
GREEN=`echo -en "\e[32m"`
NORMAL=`echo -en "\e[00m"`

pass() {
  printf "${GREEN}✔ %s${NORMAL}\n" "$@" >&2
}

fail() {
  printf "${RED}✖ %s${NORMAL}\n" "$@" >&2
}

assert() {
  expected="$1"
  actual="$2"
  msg="${3-}"

  if [ "$expected" = "$actual" ]; then
    pass "$expected == $actual :: PASS"
    return 0
  else
    [ "${#msg}" -gt 0 ] && fail "$expected == $actual :: $msg" || true
    return 1
  fi
}

test() {
  printf "[~] Running $1.py...\n\n"
  # TODO: support multiple languages
  time assert `python3 $1.py` $2 "FAIL"
  printf "\n"
}

main() {
  test 001 233168
  test 002 4613732
  test 003 6857
  test 004 906609
  test 006 25164150
  test 007 104743
  test 008 23514624000
  test 010 142913828922
  test 013 5537376230
  test 014 837799
  test 016 1366
  test 020 648
  test 025 4782
}

main
