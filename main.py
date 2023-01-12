#  file import
#  json read
#  print 

import json

data_pl = {}
data_tl ={}
data_rl = {}
data_rm ={}
data_tm ={}

#Read json :: Project_List_Data
with open('DataSet_A\Project_List_Data.json', 'r') as plist:
  data = json.load(plist)
  data_pl = data
print(data_pl) 


#Read json :: Task_List_Data
with open('DataSet_A\Resource_List_Data.json', 'r') as tlist:
  data = json.load(tlist)
  data_tl = data
print(data_tl) 


#Read json :: Resource_List_Data
with open('DataSet_A\Resource_Mapping_Data.json', 'r') as rlist:
  data = json.load(rlist)
  data_rl = data
print(data_rl) 


#Read json :: Resource_Mapping_Data
with open('DataSet_A\Task_List_Data.json', 'r') as rmap:
  data = json.load(rmap)
  data_rm = data
print(data_rm) 


#Read json :: Task_Mapping_Data
with open('DataSet_A\Task_Mapping_Data.json', 'r') as tmap:
  data = json.load(tmap)
  data_tm = data
print(data_tm) 
 
 