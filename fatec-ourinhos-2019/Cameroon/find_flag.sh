#!/bin/sh

python3 morse.py 76542cd6878315e4d1e3799a639fef4a_34ee865a7eca688fb3729afa8eb0971d > morse1.txt
python3 morse.py morse1.txt > morse2.txt
python3 morse.py morse2.txt > morse3.txt
python3 morse.py morse3.txt > morse4.txt
python3 morse.py morse4.txt > morse5.txt

