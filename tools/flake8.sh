#!/usr/bin/env bash
BOLD=$(tput bold)
UNDERLINE=$(tput smul)
NORMAL=$(tput sgr0)
RED=$(tput setaf 1)
YELLOW=$(tput setaf 3)
# List of codes to ignore
IGNORE="E501,E126,E121"


is_python() {
    if [[ -f "setup.py" ]]; then
      return 0
    fi
    return 1
}

is_flake8() {
    if [[ -x $(which flake8 || echo "None") ]]; then
      return 0
    fi
    printf "\n[${YELLOW}*${NORMAL}] ${UNDERLINE}For Python linting, install flake8:${NORMAL} pip install --upgrade flake8\n" && return 1
}


main() {
    is_python   || exit 0
    is_flake8 || exit 0
    printf "\n[${YELLOW}*${NORMAL}] ${BOLD}Validating python files for style...${NORMAL}\n"
    flake8 --ignore=${IGNORE} $(find . -type f -name "*.py" | egrep -v '__init__.py|schema.py')
    result=$?
    [[ $result -eq 0 ]] && printf "[${YELLOW}SUCCESS${NORMAL}] Passes flake8 linting\n" || printf "[${RED}FAIL${NORMAL}] Fails flake8 linting\n"
    return 0 # Make make happy :)
}

main
