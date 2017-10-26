#!/usr/bin/env bash

url='https://swapi.co/api'
speed=0
x=0
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
		x=$( echo ${response} | jq ".results[$i].max_atmosphering_speed" | tr -d '"')
		if [ $x != 'null' ] && [ $x != 'unknown' ] ; then
			if echo ${response} | jq ".results[$i].vehicle_class" | tr -d '"' | grep -Eq 'walker|\bspeeder\b|tank|wheeled'; then
				if [[ "$x" -gt "$speed" ]]; then
					y=$( echo ${response} | jq ".results[$i].name" | tr -d '"')
					speed=$x
				fi
			fi
		fi
	done
done

echo "$y is the fastest ground vehicle with a speed of $speed"
