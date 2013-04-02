#!/bin/bash

help_text(){
	echo "available commands are:
install      install into local bin directory
clean        clean up local bin directory
python       runs the python version
shell        runs the shell version
java         runs the java version
c            runs the c version
p            same as python
s            same as shell
j            same as java
time         runs the time test on all 4"
}

if [ $# == 1 ]; then
	if [ $1 == install ]; then
		mkdir bin
		ln -s ../src/sh_write.sh bin/sh_write.sh
		ln -s ../src/py_write.py bin/py_write.py
		javac -sourcepath src -d bin src/j_write.java
		gcc src/c_write.c -o bin/c_write
		echo "install: success"
	elif [ $1 == clean ]; then
		rm bin/j_write.class
		rm bin/c_write
		rm bin/py_write.py
		rm bin/sh_write.sh
		rmdir bin/
		echo "cleaned up"
	else
		cd bin
		if [ $1 == java ] || [ $1 == j ]; then
			java j_write
		elif [ $1 == c ]; then
			./c_write
		elif [ $1 == python ] || [ $1 == p ]; then
			./py_write.py
		elif [ $1 == shell ] || [ $1 == s ]; then
			./sh_write.sh
		elif [ $1 == time ]; then
			echo python
			time ./py_write.py
			echo shell
			time ./sh_write.sh
			echo java
			time java j_write
			echo c
			time ./c_write
		else
			help_text
		fi
	fi
else
	help_text
fi
