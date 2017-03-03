#!/bin/bash

# this script measures memory consumption of process with given pid
pid=2791

# measurement period in seconds
# note: for <60s you would need to change timestamp format
period=60

while true; do
  mem_used=$(ps -o rss,size -p ${pid} | tail -1)
  timestamp=$(date +"%Y-%m-%dT%H:%M")
  echo ${timestamp} ${mem_used}
  sleep ${period}
done
