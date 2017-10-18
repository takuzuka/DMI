#!/bin/bash

echo "input a"
read a
echo "input b"
read b
echo "input c"
read c
if (( a > b > c ))
then 
echo " a ir lielaks"
else
	if (( a < b > c ))
	then 
	echo "b ir lielaks"
else
 
		echo "c ir lielaks"
		fi
	
fi
