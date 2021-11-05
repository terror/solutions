export EDITOR := 'nvim'

alias e := exec
alias f := fmt

default:
  just --list

exec *name:
  python3 ./bin/{{name}}

update:
  python3 ./bin/update.py > ./README.md

fmt:
  yapf --in-place --recursive **/*.py
