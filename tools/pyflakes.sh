#!/usr/bin/env bash
BOLD=$(tput bold)
UNDERLINE=$(tput smul)
NORMAL=$(tput sgr0)
RED=$(tput setaf 1)
YELLOW=$(tput setaf 3)


is_python() {
    if [[ -f "setup.py" ]]; then
      return 0
    fi
    return 1
}

is_pyflakes() {
    if [[ -x $(which pyflakes || echo "None") ]]; then
      return 0
    fi
    printf "\n${UNDERLINE}For Python linting, install pyflakes:${NORMAL} pip install --upgrade pyflakes\n" && return 1
}


main() {
    is_python   || exit 0
    is_pyflakes || exit 0
    printf "\n[${YELLOW}*${NORMAL}] ${BOLD}Validating python files...${NORMAL}\n"
    pyflakes $(find . -type f -name "*.py" | egrep -v '__init__.py|schema.py')
    result=$?
    [[ $result -eq 0 ]] && printf "[${YELLOW}SUCCESS${NORMAL}] Passes pyflakes linting\n" || printf "[${RED}FAIL${NORMAL}] Fails pyflakes linting\n"
    return 0 # Make make happy :)
}

main
