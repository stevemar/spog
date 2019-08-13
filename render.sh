#!/bin/bash
set -ex
which j2 > /dev/null 2>&1 || (echo "Run 'pip install -r requirements.txt' first" && exit 1)
j2 index.j2 bugs.yaml > index.html
j2 stats.j2 stats.yaml > stats.html
