from genie.testbed import load
import json
from jsonmerge import merge

tb = load('/opt/telegraf/testbed-asa.yaml')
dev = tb.devices['ASAv']
dev.connect(log_stdout=False)
dev.connect()


p1 = dev.parse('show vpn-sessiondb')
p2 = dev.parse('show resource usage')

p3 = merge(p1,p2)

print(json.dumps(p3))

