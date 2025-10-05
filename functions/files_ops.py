from datetime import date
from functions.files_ops import load_tasks , save_tasks


def welcome():
    print("T0_DO list")
    print('افزودن کار:1')
    print('نمایش کار ها :2')
    print('نمایش کار ها:3')
    print('علامت گذاری انجام شده:4')
    print('خروج:5')
    
def add_task(title):
    if not title:
        print('عنوان نمی تواند خالی باشد')
        return
    tasks=load_tasks()
    tasks.append({
        "task":title,
        "done":False,
        "date":date.today.isoformat()
    }) 
    save_tasks(tasks)
    print(f"کار{title}اضافه شد")   

def show_tasks():
    tasks=load_tasks
    if not tasks:
        print('هیچ کاری موجود نیست')
        return
    print('\n =======لیست کار ها=======') 
    for i ,t in enumerate(tasks,start=1):
        status='done' if t.get('done') else 'not done'
        date=t.get('date','')
        print(f'{i}.{t.get("task")} [{status}] ({date})')
