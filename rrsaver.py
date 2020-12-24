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
