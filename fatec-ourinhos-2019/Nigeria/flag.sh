#!/bin/sh

zip2john aGVhcnRibGVlZWQK_842a48b21382001eddcab759a507bc4a.zip > john.hash 2>/dev/null
passwd=$(john --show john.hash | awk -F: '{ print $2 }')
echo $passwd
unzip -P $passwd aGVhcnRibGVlZWQK_842a48b21382001eddcab759a507bc4a.zip

