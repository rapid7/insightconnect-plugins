#!/usr/bin/env bash
BOLD=$(tput bold)
UNDERLINE=$(tput smul)
NORMAL=$(tput sgr0)
RED=$(tput setaf 1)
YELLOW=$(tput setaf 3)


is_misspell() {
    if [[ -x $(command -v misspell || echo "None") ]]; then
      return 0
    fi
    printf "\n[${YELLOW}*${NORMAL}] ${UNDERLINE}For spell checking, install misspell:${NORMAL} go get -u github.com/client9/misspell/cmd/misspell\n" && return 1
}

main () {
  is_misspell || exit 0
  printf "\n[${YELLOW}*${NORMAL}] ${BOLD}Checking for typos with Misspell...${NORMAL}\n"
  output=$(misspell .)
  if [[ "$output" ]]; then
      printf "[${RED}FAIL${NORMAL}] Fails Misspell check\n"
      echo $output
    else
      printf "[${YELLOW}SUCCESS${NORMAL}] Passes Misspell check\n"
  fi
  return 0
}

main