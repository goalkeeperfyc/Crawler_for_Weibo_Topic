#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:02:18 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import json
import pandas as pd

def write_into_file(x, path):
    with open(path, "a", encoding="utf-8") as file:
        x = json.dumps(x)
        file.write(x)
        file.write("\n")

def file_to_csv(file_path, csv_path):
    file_list = []
    file = open(file_path)
    for line in file:
        info = json.loads(line)
        file_list.append(info)
    df = pd.DataFrame(file_list)
    df.to_csv(csv_path, index=False, encoding="gb18030")