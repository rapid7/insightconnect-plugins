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
    if [[ -x $(which bandit || echo "None") ]]; then
      return 0
    fi
    printf "\n[${YELLOW}*${NORMAL}] ${UNDERLINE}For Python security tests, install bandit:${NORMAL} pip install --upgrade bandit\n" && return 1
}


main() {
    is_python   || exit 0
    is_pyflakes || exit 0
    printf "\n[${YELLOW}*${NORMAL}] ${BOLD}Validating python files for security vulnerabilities...${NORMAL}\n"
    bandit -r .
    result=$?
    [[ $result -eq 0 ]] && printf "[${YELLOW}SUCCESS${NORMAL}] Passes bandit security checks\n" || printf "[${RED}FAIL${NORMAL}] Fails bandit security checks\n"
    return 0 # Make make happy :)
}

main
