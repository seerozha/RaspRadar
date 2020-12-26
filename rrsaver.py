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
  print(pkt.sniff_timestamp)
  print(pkt['wlan'].ta)
  print(pkt['radiotap'].dbm_antsignal)
  print(pkt['wlan'].ssid)
