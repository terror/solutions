rust *args:
    rustc {{args}}.rs && ./{{args}} && rm {{args}}

exec *name:
    python3 ./bin/{{name}}

update:
    python3 ./bin/update > ./README.md
