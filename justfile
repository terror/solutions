rust *args:
    rustc {{args}}.rs && ./{{args}} && rm {{args}}

exec *name:
    python3 ./Scripts/{{name}}.py

update:
    python3 ./Scripts/update.py > ./README.md
