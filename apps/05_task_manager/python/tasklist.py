import task_class


class Tasklist:

  def __init__(self):
    temporary_list = []
    task_list = []
    # opens the fie, reads it, and develops a list consisting of each individual line with a task listed in the file
    file = open('../txt/tasklist.txt')
    filledList = file.read().split("\n")

    # for each task in the now filled in list, task description, date, and time respectively are grouped together as
    #   elements of a sublist which is then appended to the temporary list
    for tasks in filledList:
      temporary_list.append(tasks.split(","))

    # for the sublist of each task in the temporary list, the description, date, and time associated with each task is
    #   appended to the permanent list as an object
    # should there be only one task left, the program breaks out of the loop to avoid a crash
    for tasks in temporary_list:
      if len(tasks) == 1:
        break
      task_elem = task_class.Task(tasks[0], tasks[1], tasks[2])
      task_list.append(task_elem)

    # resorts the list after the new task has been added to it
    for i in range(len(task_list) - 1):
      for j in range(i + 1, len(task_list)):
        if task_list[j].__lt__(task_list[i]):
          temp = task_list[i]
          task_list[i] = task_list[j]
          task_list[j] = temp
    self._tasklist = task_list

  
  def add_task(self, desc, date, time):
    self._tasklist.append(task_class.Task(desc, date, time))
    for i in range(len(self._tasklist) - 1):
        for j in range(i + 1, len(self._tasklist)):
          if self._tasklist[j].__lt__(self._tasklist[i]):
            temp = self._tasklist[i]
            self._tasklist[i] = self._tasklist[j]
            self._tasklist[j] = temp

  def get_current_task(self):
    return self._tasklist[0]

  def mark_complete(self):  ### ????
    return self._tasklist.pop(0)

  def postpone_task(self, date, time):
    if len(self._tasklist) != 0:
      self._tasklist[0].date = date
      self._tasklist[0].time = time
      for i in range(len(self._tasklist) - 1):
        for j in range(i + 1, len(self._tasklist)):
          if self._tasklist[j].__lt__(self._tasklist[i]):
            temp = self._tasklist[i]
            self._tasklist[i] = self._tasklist[j]
            self._tasklist[j] = temp


  """Writes the newly updated content to the file"""
  def save_file(self):
    temp = ""
    f = open('../txt/tasklist.txt', "w")
    for task in self._tasklist:
      if self._tasklist.index(task) != len(self._tasklist):
        temp += task.__repr__()
        print(temp)
    f.write(temp)
    f.close()

  
  """Returns the number of tasks in the list."""
  def __len__(self):
    return len(self._tasklist)

  def __iter__(self):
    self._i = -1
    return self

  def __next__(self):
    self._i += 1
    # stops iterating when the program reaches the end of the task list
    if self._i >= len(self._tasklist):
      raise StopIteration
    else:
      return self._tasklist[self._i]
      