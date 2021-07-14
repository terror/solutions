default:
  just --list

rust *args:
  rustc {{args}}.rs && ./{{args}} && rm {{args}}

exec *name:
  python3 ./bin/{{name}}

update:
  python3 ./bin/update > ./README.md

fmt-py:
  yapf --in-place --recursive **/*.py
