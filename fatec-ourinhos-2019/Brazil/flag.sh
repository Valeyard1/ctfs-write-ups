#!/bin/sh

strings d2lyZXNoYXJrNjQK.pcapng | grep -i "==$" | base64 -d
