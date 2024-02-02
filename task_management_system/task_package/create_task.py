from.task import Task#task is module and Task is class
def create_task(title,description,category=None):
    new_task=Task(title,description,category)
    return new_task
