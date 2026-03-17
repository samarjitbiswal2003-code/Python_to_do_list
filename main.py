print("       -------IT IS A CLI BASED TO-DO-LIST PROJECT--------     ")
Menu_list=["Add a task","View task","Remove task","Complete task","Exit"]
def menu():
 print("---welcome to your task----")
 for index, item in enumerate(Menu_list,start=1):
    print(index,".",item)

add_task=[]
while True:
    menu()
    try:
     user_choice=int(input("enter choice number:"))
     if user_choice==5:
      print(" -----you are exit successfully-----")
      break
 
    except  ValueError:
       print("Invalid input")
       continue

    
    if user_choice not in [1,2,3,4]:
        print("please enter valid number") 
        
    elif user_choice==1:
            print("----Task add section----")
            task=input("enter task: ")
            add_task.append(task)
            print("task added successfuly")
            
    elif user_choice==2:
         if not add_task:
              print("you have no task")
             
         else:
              print("---view task----")
        
              for si_no , task in enumerate(add_task,start=1):
            
                  print(si_no,".",task)
              
    elif user_choice==3:
         print("---Task remove section-----")
         if not add_task:
             print("you have no task")
             
         elif add_task:
                for si_no , task in enumerate(add_task,start=1):
                        print(si_no,".",task)
                    
                try:
                    task_remove=int(input("select  task number to remove task:"))
                    task_remove-=1
                    if task_remove>(len(add_task)-1) or task_remove<0:
                        print("you choose wrong task number")
                    else:
                        add_task.pop(task_remove)
                        print("task removed sucessfully")
                except ValueError:
                    print("Invalid task number")
    elif user_choice==4:
        print("-----Task Complete Section-----")
        if not add_task:
            print("You have no task to complete")
        else:
            for si_no,item in enumerate(add_task,start=1):
                print(si_no,".",item)    
            try:
                complete_task= int(input("select your completed task: ")) 
                complete_task-=1
                if " ✔" in add_task[complete_task]:
                    print("task already completed")
                else:    
                 add_task[complete_task]= add_task[complete_task]+ " ✔"
                 print("task completed successfully!")      
            except ValueError:
                print("Invalid input! Please enter a number.")
            except IndexError:
                print("Invalid task number!")                

   
   
     
 
     
    
   
 
       
