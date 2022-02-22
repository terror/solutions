export EDITOR := 'nvim'

alias e := exec
alias f := fmt

default:
  just --list

all: fmt readme

exec *name:
  python3 ./bin/{{name}}

fmt:
  yapf --in-place --recursive .

readme:
	./bin/gen-readme
