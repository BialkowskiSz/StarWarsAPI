#!/usr/bin/env bash
clear
url='https://swapi.co/api'
y=""
num=0
biggest=""

n=1
while true
do
        response=$( curl -sL -H 'Accept: application/json' ${url}/people?page=${n} )
        if [[ ${response} =~ .*detail.*Not.* ]]; then
                break
        fi
        n=$((n + 1))
        for i in {0..10}
        do
            y=$( echo ${response} | jq ".results[$i].films[]" | tr -d '"' | tr -d '-' | wc -w)
            if [[ "$y" -gt "$num" ]]; then
                num=$y
                biggest=$( echo ${response} | jq ".results[$i].name" | tr -d '"')
            fi
        done
done
clear
echo "$biggest appeared in $num films"

n=1
while true
do
        response=$( curl -sL -H 'Accept: application/json' ${url}/people?page=${n} )
        if [[ ${response} =~ .*detail.*Not.* ]]; then
                break
        fi
        n=$((n + 1))
        for i in {0..10}
        do
            temp_name=$( echo ${response} | jq ".results[$i].name" | tr -d '"')
            if [ "$temp_name" == "$biggest" ] ; then
                # iterate through films
            fi
        done
done
