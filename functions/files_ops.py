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
    save_tasks(tasks):
    print(f"کار{title}اضافه شد")   
