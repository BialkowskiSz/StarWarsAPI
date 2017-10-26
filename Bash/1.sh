#!/usr/bin/env bash

url='https://swapi.co/api/vehicles'
response=$( curl -sL -H 'Accept: application/json' ${url})
counter=0
page=1
while true
do
	c=0
	while [ $c -le 9 ]
	do
		var="$(echo ${response} | jq ".results[${c}].vehicle_class")"
		if [[ $var == 'null' ]]
		then
			break 2
		fi
		counter=$((counter+1))
         	c=$((c+1))
	done
	page=$((page+1))
	response=$( curl -sL -H 'Accept: application/json' ${url}?page=${page} )
done
echo $counter
