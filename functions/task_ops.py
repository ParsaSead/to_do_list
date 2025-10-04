import json
import os

FILE_name="tasks.json"

def load_tasks():
    if not os.path.exists(FILE_name):
        return []
    with open(FILE_name,'r',encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
def save_tasks(tasks):
     with open(FILE_name,'w',encoding="utf-8") as f: 
         json.dump(tasks,f,ensure_ascii=False,indent=4)             

