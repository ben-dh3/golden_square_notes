class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.task = task

    def format(self):
        if self.task.complete == False:
            return '- [ ] ' + self.task.title
        if self.task.complete == True:
            return '- [x] ' + self.task.title
