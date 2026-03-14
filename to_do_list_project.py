print("       -------IT IS A CLI BASED TO-DO-LIST PROJECT--------     ")
Menu_list=["1.Add a task","2.View task","3.Remove task","4.Exit"]
def menu():
 print("---welcome to your task----")
 for item in Menu_list:
    print(item)

menu()
user_choice=int(input("enter choice number:"))
add_task=[]
if user_choice not in [1,2,3,4]:
     print("please enter valid number") 
     menu()
     user_choice=int(input("enter choice number:"))


while user_choice in [1,2,3,4]:
  if user_choice==4:
    print(" -----you are exit successfully-----")
    break
 
  elif user_choice==1:
    print("----Task add section----")
    task=input(f"enter task: ")
    add_task.append(task)
    print("task added sucessfuly")
    menu()
    user_choice=int(input("enter choice number:"))
  elif user_choice==2:
     if not add_task:
         print("you have no task")
         menu()
         user_choice=int(input("enter choice number:")) 
     else:
         print("---view task----")
         i=0
         for item in add_task:
             i+=1
             print(i,".",item)
         menu()        
         user_choice=int(input("enter choice number:"))     
  elif user_choice==3:
     print("---Task remove section-----")
     if not add_task:
      print("you have no task")
      menu()
      user_choice=int(input("enter choice number:")) 

     elif add_task:
         task_remove=int(input("select  task number to remove task:"))
         task_remove-=1
         if task_remove>(len(add_task)-1) or task_remove<0:
             print("you choose wrong task number")
         else:
             add_task.pop(task_remove)
             print("task removed sucessfully")
             menu()
             user_choice=int(input("enter choice number:")) 
  elif user_choice not in [1,2,3,4]:
    print("please enter valid number") 
    menu()
    user_choice=int(input("enter choice number:"))
   
   
     
 
     
    
   
 
       
