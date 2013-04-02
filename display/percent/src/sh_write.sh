#!/bin/bash
filename='../settings.txt'
num=$(head -1 $filename)
pre_wait_time=$(tail -1 $filename)
wait_time=$(bc <<< 'scale=2; '$pre_wait_time'/1000')
for i in $(seq 0 $num); do
		echo -en "\r$i%  ";
		sleep $wait_time;
done;
echo ""
