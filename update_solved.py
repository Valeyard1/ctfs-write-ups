#!/usr/bin/env python3

import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Update list of solved challs')
parser.add_argument('--filename', metavar='FILE', type=str,
                    required=True, dest='filename',
                    help='The json file with the challs')
parser.add_argument('--solved-chall', metavar='CHALL', type=str,
                    required=True, dest='solved_chall',
                    help='Name of the chall to add to the list')

arguments = parser.parse_args()

filename = arguments.filename
solved_chall = arguments.solved_chall

with open(filename) as fd:
    json_data = json.load(fd)

json_data['solved'].append(solved_chall)

with open(filename, 'w') as fd:
    json.dump(json_data, fd, indent=4, sort_keys=True)


def help():
    print("Usage: {} solved.json <chall>" .format(sys.argv[0]))
    print("Example: {} fatec-ourinhos-2019/solved.json Belarus" .format(sys.argv[0]))
    return
