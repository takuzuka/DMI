#!/bin/bash

echo "input a"
read a
echo "input b"
read b
c=`expr $a + $b`
echo "$a + $b =" $c
