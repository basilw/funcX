import subprocess
import pathlib
import json

import funcx
from funcx.utils.loggers import set_stream_logger
from funcx.sdk.client import FuncXClient
from funcx.serialize import FuncXSerializer

#set_stream_logger()
fxc = FuncXClient(funcx_service_address="http://localhost:500   1/v1")

subprocess.run(['funcx-endpoint', 'configure', 'testep'])
subprocess.run(['funcx-endpoint', 'start', 'testep'])
endpoint_json = '{}/.funcx/testep/endpoint.json'.format(pathlib.Path.home()) 
with open(endpoint_json, 'r') as f:
    testep_id = json.load(f)['endpoint_id']

status_path = f'endpoints/{testep_id}/status'
#print(fxc.get(status_path))
"""
payload = {'logs': [], 'status': 'online'}
r = fxc.post(status_path, json_body = payload)
print(r)
fxc.post()
"""
status = fxc.get_endpoint_status(testep_id)
#print(status)



#if __name__ == "__main__":

    #test_endpoint_status()
    #fxc.register_endpoint("abcd", "asdf")

import funcx
from funcx.sdk.client import FuncXClient
fxc = FuncXClient()
def hello_world():
    return "Hello World!"

func_uuid = fxc.register_function(hello_world)
endpoint_uuid = "805b466f-abd9-4920-bba8-b36bb28081c9"
res = fxc.run(endpoint_id=endpoint_uuid, function_id=func_uuid)

'''
import getpass
from parsl.addresses import address_by_hostname


global_options = {
    'username': getpass.getuser(),
    'email': 'USER@USERDOMAIN.COM',
    'broker_address': 'http://127.0.0.1:8080',
    'broker_test': True,
    'redis_host': '127.0.0.1',
    'endpoint_address': address_by_hostname(),
}
'''


