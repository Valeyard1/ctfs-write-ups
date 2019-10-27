#!/bin/sh

cat p41n_a0f401ca7af79dff4671cd07e5992848.txt | base64 -d > p41n.png
steghide extract -sf p41n.png -p shinra
