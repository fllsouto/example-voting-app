import os

machines = [
  'manager1',
  'manager2',
  'manager3',
  'worker1',
  'worker2'
]

for machine in machines:
  cmd = f'docker-machine stop {machine}'
  os.system(cmd)
  print("-------")