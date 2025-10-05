from functions.files_ops import  welcome , add_task , show_tasks


while True:
    welcome()
    user_input=input('انتحاب کنید: ').strip()
    if user_input=='1':
        title=input('عنوان کار را وارد کنید:  ').strip()
        add_task(title)
    elif user_input=="2":
        show_tasks()  



