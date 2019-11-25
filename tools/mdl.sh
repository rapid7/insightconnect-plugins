#!/usr/bin/env bash
BOLD=$(tput bold)
UNDERLINE=$(tput smul)
NORMAL=$(tput sgr0)
RED=$(tput setaf 1)
YELLOW=$(tput setaf 3)


is_help() {
    if [[ -f "help.md" ]]; then
      return 0
    fi
    printf "\n[${YELLOW}*${NORMAL}] Plugin is missing help.md, to generate it run: make help\n" && return 1
}

is_mdl() {
    if [[ -x $(which mdl || echo "None") ]]; then
      return 0
    fi
    printf "\n[${YELLOW}*${NORMAL}] ${UNDERLINE}For Markdown linting, install mdl:${NORMAL} gem install mdl\n" && return 1
}

main() {
    is_mdl || exit 0
    is_help || exit 0
    printf "\n[${YELLOW}*${NORMAL}] ${BOLD}Validating markdown...${NORMAL}\n"
    output=$(mdl help.md)
    # We don't rely on exit code due to the following rules we don't care about
    if echo "$output" | egrep -v "MD024|MD013|MD029|MD033|MD013|MD024|MD025" | fgrep 'help.md:'; then
      printf "[${RED}FAIL${NORMAL}] Fails markdown linting\n"
    else
      printf "[${YELLOW}SUCCESS${NORMAL}] Passes markdown linting\n"
    fi

    return 0 # Make make happy :)
}

main
