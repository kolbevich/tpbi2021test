import pytest
import os

def testPython():
  res = os.system('python python.py')
  assert (res == 'Hello world from dev!')
