#!/usr/bin/env bash
clear
url='https://swapi.co/api'
y=""

n=1
while true
do
        response=$( curl -sL -H 'Accept: application/json' ${url}/planets?page=${n} )
        if [[ ${response} =~ .*detail.*Not.* ]]; then
                break
        fi
        n=$((n + 1))
        for i in {0..10}
        do
                y+=$( echo ${response} | jq ".results[$i].name" | tr -d '"' | tr -d '-')
                y+="-"
                y+=$( echo ${response} | jq ".results[$i].population" | tr -d '"')
                y+=$'\n'
        done
done
echo "$y" | sort -nr -t- -k2 | cut -f1 -d"-"
