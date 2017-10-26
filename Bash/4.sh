#!/usr/bin/env bash
clear
url='https://swapi.co/api'
darth="https://swapi.co/api/people/4/"
luke="https://swapi.co/api/people/1/"
temp=""
counter=0

n=1
while true
do
	response=$( curl -sL -H 'Accept: application/json' ${url}/starships?page=${n} )
	if [[ ${response} =~ .*detail.*Not.* ]]; then
		break
	fi
	n=$((n + 1))
	for i in {0..10}
	do
        temp=$( echo ${response} | jq ".results[$i].pilots[]" | tr -d '"')
        if [[ $temp != 'null' ]] && [[ $temp != '' ]] ; then
            if echo ${temp} | grep -Eq "$darth"; then
                if echo ${temp} | grep -Eq "$luke"; then
                    counter=$((counter + 1))
                fi
            fi
        fi
	done
done
clear
echo $counter
