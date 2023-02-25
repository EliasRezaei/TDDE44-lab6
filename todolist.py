class TaskList(object):
    """Klassen taskList."""

    def __init__(self):
        """Tillhörande instansvaribler till klassen TaskList defineras."""
        self.task_list = []
        self.task_counter = 0

    def create_task(self, description):
        """Ett id ges till det uppgift som skapas av användaren."""
        task_id = self.task_counter
        task = Task(task_id, description)
        self.task_list.append(task)
        self.task_counter += 1

    def mark_done(self, task_id):
        """Om uppgiften ska markeras som färdigt."""
        self.task_list[task_id].mark_done2()

    def __str__(self):
        """Utskrivning med markering av oklara och klara uppgifter."""
        if len(self.task_list) == 0:
            print("listan är tom")

        for task in self.task_list:
            if task.done:
                print(task.task_id, "[X]", task.description)
            else:
                print(task.task_id, "[ ]", task.description)


class Task(object):
    """Klass Task."""

    def __init__(self, task_id, description):
        """Definera task klassen och skicka in namnet och dess ID."""
        self.task_id = task_id
        self.description = description
        self.done = False

    def mark_done2(self):
        """Ändra instansvariabeln done till True."""
        self.done = True

