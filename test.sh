#!/bin/bash
set -ex

# Lint python code
flake8

# Lint YAML data
yamllint -d relaxed bugs.yaml
yamllint -d relaxed stats.yaml
