from main import *

tl = data_tl["taskList"]
tm = data_tm['TaskMap']

def findDepAndIndep(task):
    task_details = tl[str(task)]
    arr = []
    if task_details["dependsOn"] == "" :
        print(task)
        return task
        # return task
    else:
        # dep.append(task)

        dependsOnList = task_details["dependsOn"].split(",")
        
        for d in dependsOnList:
            print("dep",findDepAndIndep(d),sep=' ',)
            arr.append(findDepAndIndep(d))  
        # return findDepAndIndep()
    
    
    # if(independent):
    #     print(task)
    # else:
# print(tm)
for k in tm:
    print(f"Project {k}:")
    for task in tm[k]:
        findDepAndIndep(task)
         
    break

# print(data_pl)




# # import json
# from collections import defaultdict

# def build_dependency_tree(task_list, task_id, dependency_tree):
#     task = task_list[task_id]
#     depends_on = task["dependsOn"]
#     if depends_on != "":
#         # split depends_on string to list
#         depends_on_list = depends_on.split(',')
#         for id in depends_on_list:
#             if id in task_list:
#                 dependency_tree[id].append(task_id)
#                 build_dependency_tree(task_list, id, dependency_tree)
#     else:
#         dependency_tree[task_id].append(task_id)

# # Read the JSON data from a file
# # with open('data.json', 'r') as file:
# #     data = json.load(file)

# # Access the value of the "taskList" key
# task_list = data_tl["taskList"]

# # Create a default dict to store the dependency tree
# dependency_tree = defaultdict(list)

# # Iterate through the task_list
# for task_id in task_list:
#     build_dependency_tree(task_list, task_id, dependency_tree)

# # Print the dependency tree
# for task_id, dependencies in dependency_tree.items():
#     print(f"Task {task_id}: {dependencies}")

