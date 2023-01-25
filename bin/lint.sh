#!/usr/bin/env bash

set -o errexit -o nounset -o xtrace

ERROR=0
LINT_PATHS=("src/")

# test we have arguments
if [[ $# -gt 0 ]]; then
    LINT_PATHS=("$@")
fi

# Lint the entire project using flake8 and mypy with settings defined in setup.cfg.
flake8 --count "${LINT_PATHS[@]}" || ERROR=1
black --check --diff "${LINT_PATHS[@]}" || ERROR=1
mypy --show-error-codes "${LINT_PATHS[@]}" || ERROR=1

exit $ERROR