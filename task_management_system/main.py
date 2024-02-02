from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task
#create a task
task1=create_task("Complete Your Assignment","Finish TASK MANAGEMENT SYSTEM")
#display the task
print("Task 1:",task1)
#edit the task
edit_task(task1,new_title="Updated Assignment",new_description="Review and Submit to RASHMI MAM")
#Display the updated task
print("Updated Task 1:",task1)
#categorize the task
categorize_task(task1,"Zappkode Academy")
#Display the categorize task
print("Categorize Task 1:",task1)