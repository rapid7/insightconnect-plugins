#!/bin/bash
DOMAIN="$1"
IP="$2"
RECORDS="A AAAA MX NS CNAME SOA SRV TXT SIG ANY"

die(){
  printf -- "$(tput setaf 1)$*$(tput sgr0)\n"
  exit 1
}

hi(){
  printf -- "$(tput setaf 3)$*$(tput sgr0)\n"
}

[[ $DOMAIN ]] && [[ $IP ]] || die "usage: $0 <domain> <ip>"

forward_schema(){
local qt=$1
cat <<EOF
{
  "body": {
    "action": "forward",
    "input": {
      "query": "$qt",
      "domain": "$DOMAIN"
    },
    "connection": null,
    "meta": {}
  },
  "version": "v1",
  "type": "action_start"
}
EOF
}

reverse_schema(){
cat <<EOF
{
  "body": {
    "action": "reverse",
    "input": {
      "address": "$IP"
    },
    "connection": null,
    "meta": {}
  },
  "version": "v1",
  "type": "action_start"
}
EOF
}

hi "- Testing Basic Forward Query"
forward_schema | docker run -i --rm  komand/dig --debug run | jq '.' || die "Docker failed"
printf "\n"

hi "- Testing Reverse Query"
reverse_schema | docker run -i --rm  komand/dig --debug run | jq '.' || die "Docker failed"
printf "\n"

hi "- Testing Forward Query with Records"
for record in $RECORDS; do
  hi "\n-- Record test: $record"
  forward_schema $record | docker run -i --rm  komand/dig --debug run | jq '.' || die "Docker failed"
  printf "\n"
done
