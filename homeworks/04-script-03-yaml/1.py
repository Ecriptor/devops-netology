#!/usr/bin/env python3

import os
import json

with open ('ex1.json', 'r') as json_file:
    json_dict = json.load(json_file)
print(type(json_dict))
print(json_dict)
