# https://www.quora.com/How-do-I-write-a-Python-script-to-execute-bash-commands-Python-3-6
import os

machines = [
#  'manager1',
  'manager2',
  'manager3',
  'worker1',
  'worker2'
]
# https://www.programiz.com/python-programming/string-interpolation
for machine in machines:
  print(f"Creating machine: {machine}")
  cmd = f'docker-machine create --driver=virtualbox {machine}'
  os.system(cmd)
  print("-------")