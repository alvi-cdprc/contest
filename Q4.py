from main import *

rm = data_rm
rl = data_rl

merge_array = []

for i in rm:
    merge_array += rm[i]

print(len(merge_array))

for k in rl:
    if int(k) not in merge_array:
        print(f"Resource ID: {k}, Name {rl[k]['name']}, Type: {rl[k]['type']}" )