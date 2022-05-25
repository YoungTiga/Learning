from project.task import Task


class Section:

    def __init__(self,name):
        self.name = name
        self.tasks = []
    def  add_task(self,new_task: Task):
        if any([x.name==new_task.name for x in self.tasks]):
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return  f"Task {new_task.details()} is added to the section"

    def complete_task(self,task_name):
        if not any([x.name==task_name for x in self.tasks]):
            return f"Could not find task with the name {task_name}"
        curr_task = [x for x in self.tasks if x.name == task_name][0]
        curr_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        tasks_to_remove = [x for x in self.tasks if x.completed == True]
        for task in tasks_to_remove:
            self.tasks.remove(task)
        return f"Cleared {len(tasks_to_remove)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details()+"\n"
        return  result