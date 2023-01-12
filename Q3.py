from main import *

from main import *


merge_array_tl = []


  

TYPE = ["BE", "FE", "DB", "MGR", "AI", "BC","DOPS"]
tl = data_tl['taskList']
rl = data_rl
# print
# for i in rm:
#   for j in rm[i]:
#     merge_array_tl +=rm[i][j]

tempTL = []
tempRL = []
mainOPRL = []
#  check from task list
for key in tl:
  if tl[key]['resourceType'] not in tempTL:
    tempTL.append(tl[key]['resourceType'])
#  resource list
for key in rl :
  if rl[key]['type'] not in tempRL:
      tempRL.append(rl[key]['type'])

set1 = set(tempTL)
set2 = set(tempRL)

# using union 
union_elements = list(set1.union(set2))
#  output
for type in union_elements:
  if type not in TYPE:
    mainOPRL.append(type)
# output
print(mainOPRL)

  