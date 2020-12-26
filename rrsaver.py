#/usr/sbin/python3
import pyshark
import os
import configparser

config=configparser.ConfigParser()

try:
  config.read('.env')
except IOError:
  raise MyError()

pf=config['fileparams']['PCAPFILE']
capture = pyshark.FileCapture(pf)

for pkt in capture:
#  print(pkt)
#  pkt.pretty_print()
  print(pkt.sniff_time)
  pkt.sniff_timestamp
