from datetime import datetime
from colorama import init,Fore,Style # type: ignore
from prettytable import PrettyTable,ALL,FRAME,HEADER
import json
total_task=[]
init()
italic= "\033[3m"
nomal="\033[0m"
bold_underline_text = "\033[1m\033[4m"
def color_it(str,color):
    return getattr(Fore,color.upper())+str+Style.RESET_ALL
def fetchtasks():
    try:
        with open('tasks.json','r') as f:
            total_task=json.load(f)
        return total_task
    except FileNotFoundError:
        return []
total_task=fetchtasks()
print(color_it('TODO-LIST','BLUE'))
def savejson(total):
    with open('tasks.json','w')  as f:
        json.dump(total,f,indent=4   )
    f.close()
def prettify_table(tasks):
    table=PrettyTable()
    table.hrules=ALL
    table.title=color_it('TODO LIST','Green')
    table.field_names=[Fore.LIGHTMAGENTA_EX+'S.no','Tile',"Description","Created","Status"+Style.RESET_ALL]
    table.max_width=25
    for index,task in enumerate(tasks):
        task_status_color=''
        if(task['task_status']=='pending'):
            task_status_color=color_it(task['task_status'],'red')
        else:
            task_status_color=color_it(task['task_status'],'green')
        table.add_row([index+1,task['task_title'],task['task_desc'],task['task_created'],task_status_color])
    print(table)
def update_prop(chosen):
    prop_dict={
                'title':'task_title',
                'description':'task_desc',
                'created':'task_created',
                'status':'task_status'
            }
    prop_choice=input(color_it('Enter property name to update:','green')).lower()
    value=input(color_it('Enter value for that property:','green'))
    if prop_choice in prop_dict:
        prop_choose=prop_dict[prop_choice]
        chosen[prop_choose]=value
    return chosen
while(True):
    print('1.Add a task')
    print('2.delete a task')
    print('3.Update a task')
    print('4.Display task')
    while(True):
        n=int(input('Choose an option:'))
        if n!=0 and n<=4:
            break
        else:
            print(color_it('please enter valid number','red'))
            continue
    if(n==1):
        print(bold_underline_text+color_it('Enter task Details','red')+nomal)
        task_title=input(italic+color_it('Enter task title:','green'))
        task_des=input(italic+color_it('Enter task description:','green'))
        task_created=datetime.now()
        formated_created=task_created.strftime("%A,%d-%m-%y,%H:%M:%S")
        task={
            "task_title":task_title,
            "task_desc":task_des,
            "task_created":formated_created,
            "task_status":"pending",
        }
        total_task.append(task)
        savejson(total_task)
        print(color_it(italic+"Task is added successfully with an index {}".format((total_task.index(task)+1)),'blue'))
        prettify_table(total_task)
        choice=input('Do you want to continue(y/n):')
        if(choice=='y'):
            continue
        else:
            break
    if(n==2):
        prettify_table(total_task)
        index=int(input(color_it('Enter the serial number of the task to delete:','green')))
        if index!=0 and index<=len(total_task):
                chosen=total_task[(index-1)]
                total_task.remove(chosen)
                print(color_it('Task sucessfully deleted','Green'))
                savejson(total_task)
                if(len(total_task)==0):
                    print(color_it('There is no task available to shoe','Red'))
                else:
                    prettify_table(total_task)
        else:
            print(bold_underline_text+color_it('Task not existed','red'))
        choice=input('Do you want to continue(y/n):')
        if(choice=='y'):
            continue
        else:
            break
    if(n==3):
        prettify_table(total_task)
        index=int(input(color_it('Enter the serial number of the task to Update:','green')))
        while(True):
            change_choice=input(color_it('Do you want to change single or multiple propeties of task(S/M):','green')).lower()
            if(change_choice=='s' or change_choice=='m'):
                break;
            else:
                print(color_it('Plsease enter either S or M ','red'))
                continue
        if index!=0 and index<=len(total_task):
            chosen=total_task[(index-1)]
            later=chosen.copy()
        else:
            print(bold_underline_text+color_it('Task not existed','red'))
        if(change_choice.lower()=='s'):
            chosen=update_prop(chosen)
            savejson(total_task)
            print(italic+color_it('Before update:','Blue'))
            prettify_table([later])
            print(italic+color_it('After update:','Blue'))
            prettify_table([chosen])
            choice=input('Do you want to continue(y/n):')
            if(choice=='y'):
                continue
            else:
                break
        else:
            n=int(input(color_it('How many properties do you want to change:','green')))
            for i in range(1,n+1):
                chosen=update_prop(chosen)
            savejson(total_task)
            print(italic+color_it('Before update:','Blue'))
            prettify_table([later])
            print(italic+color_it('After update:','Blue'))
            prettify_table([chosen])
            choice=input('Do you want to continue(y/n):')
            if(choice=='y'):
                continue
            else:
                break
    if(n==4):
        if(len(total_task)==0):
            print(bold_underline_text+color_it('There is no tasks available','red'))
        else:
            prettify_table(total_task)
        choice=input('Do you want to continue(y/n):')
        if(choice=='y'):
            continue
        else:
            break


