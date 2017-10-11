#!/bin/bash

#4
if [ $# == 2 ]
# ja (if) skriptam nodoto argumentu skaits ($#) ir vienads (==) ar 2
then
#tad tiek izpilditas visas sekojusas darbibas lidz ...
a=$1
b=$2
val41=`expr $a + $b`
echo "$a+$b="$val41
val42=`expr $a - $b`
echo "$a-$b="$val42
val43=`expr $a \* $b`
echo "$a*$b="$val43
val44=`expr $a / $b`
echo "$a/$b="$val44
val45=`expr $a % $b`
echo "$a%$b="$val45
#... sai vietai
fi 

#3.piemers - operacijas ar mainigajiem
: <<"END"
a=56
b=32
val31=`expr $a + $b`
echo "$a+$b="$val31
val32=`expr $a - $b`
echo "$a-$b="$val32
val33=`expr $a \* $b`
echo "$a*$b="$val33
val34=`expr $a / $b`
echo "$a/$b="$val34
val35=`expr $a % $b`
echo "$a%$b="$val35
END
#2. piemers- operacijas ar konstantem
: <<"END"
val21=`expr 2 + 3`
echo "2+3="$val21
val22=`expr 2 - 3`
echo "2-3="$val22
val23=`expr 2 \* 3`
echo "2*3="$val23
val24=`expr 2 / 3`
echo "2/3="$val24
val25=`expr 2 % 3`
echo "2%3="$val25
END

#1. piemers - izteiksmes pieraksts
: <<"END"
 #komentara bloka sakums
val11=`expr 2 + 2`
echo "2+2=" $val11
END
 #komentara bloka beigas
