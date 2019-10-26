#!/usr/bin/env python3

import sys
import json

filename = sys.argv[1]
solved_chall = sys.argv[2]


with open(filename) as fd:
    json_data = json.load(fd)

json_data['solved'].append(solved_chall)

with open(filename, 'w') as fd:
    json.dump(json_data, fd, indent=4, sort_keys=True)
