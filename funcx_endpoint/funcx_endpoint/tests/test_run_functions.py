from funcx.sdk.client import FuncXClient 
import subprocess
import pathlib
import json

fxc = FuncXClient()

subprocess.run(['funcx-endpoint', 'configure', 'testep'])
subprocess.run(['funcx-endpoint', 'start', 'testep'])

def hello():
    return "Hello World!"

def func(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return func3(arr, low, mid - 1, x)
        else:
            return func3(arr, mid + 1, high, x)
    else:
        return -1

arr2 = [-1,0,3,5,9,12]
func_id = fxc.register_function(hello)
func_id = fxc.register_function(func)

endpoint_json = '{}/.funcx/testep/endpoint.json'.format(pathlib.Path.home())
f = open(endpoint_json, 'r') 
endpoint_info = json.load(f)
testep_id = endpoint_info['endpoint_id']

res = fxc.run(endpoint_id=testep_id, function_id=func_id)
res1 = fxc.run(arr2, 0, 6, 9, endpoint_id=testep_id, function_id=func_id)
print(fxc.get_result(res))
print(fxc.get_result(res1))