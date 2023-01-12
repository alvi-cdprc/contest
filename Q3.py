import json

print("hello Q3")

#Read json :: Resource_List_Data
with open('E:\Contest\contest\DataSet_A\Resource_List_Data.json', 'r') as rlist:
  data = json.load(rlist)
  data_rl = data
print(data_rl) 


#Read json :: Resource_Mapping_Data
with open('E:\Contest\contest\DataSet_A\Resource_Mapping_Data.json', 'r') as rmap:
  data = json.load(rmap)
  data_rm = data
print(data_rm) 

