from main import *

tm = data_tm
rl = data_rl

merge_array = []

for i in tm:
  for j in tm[i]:
    merge_array +=tm[i][j]
    


for k in rl:
  print(rl[k])