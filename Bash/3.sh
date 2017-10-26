#!/usr/bin/env bash
clear
url='https://swapi.co/api'
y=""

n=1
while true
do
	response=$( curl -sL -H 'Accept: application/json' ${url}/vehicles?page=${n} )
	if [[ ${response} =~ .*detail.*Not.* ]]; then
		break
	fi
	n=$((n + 1))
	for i in {0..10}
	do
		y+=$( echo ${response} | jq ".results[$i].name" | tr -d '"' | tr -d '-')
		y+="-"
		y+=$( echo ${response} | jq ".results[$i].cargo_capacity" | tr -d '"')
		y+=$'\n'
	done
done
echo "$y" | sort -n -t- -k2

# echo "$y" | sort -n -t- -k2 |
