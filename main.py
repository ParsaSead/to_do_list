from functions.files_ops import  welcome


while True:
    welcome()
    user_input=input('انتحاب کنید: ').strip()
    if user_input=='1':
        title=input('عنوان کار را وارد کنید:  ').strip()
        add_task(title)



