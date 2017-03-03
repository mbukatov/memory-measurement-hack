#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Matplotlib based plotting script which reads output from process-watch.sh
script.

Note that it's rather hack, reasonable practices are not fully followed.
"""

# Copyright 2016 Martin Bukatovič <mbukatov@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys


import matplotlib.cbook as cbook
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


with open("process-watch.example", "r") as conn_file:
    timestamps = []
    values_rss = []
    values_size = []
    for line in conn_file:
        timestamp, value_rss, value_size = line.split(" ")
        # both values are in kiloBytes
        timestamps.append(mdates.datestr2num(timestamp))
        values_rss.append(int(value_rss)/1024)
        values_size.append(int(value_size)/1024)
    # pyplot
    fig, ax = plt.subplots()
    ax.plot_date(timestamps, values_rss, "-", color="b", label="rss")
    # ax.plot_date(timestamps, values_size, "-", color="r", label="size")
    fig.autofmt_xdate()
    plt.title("Memory consumption of the process")
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Memory usage in MB', fontsize=14)
    plt.grid(True)
    plt.show()
