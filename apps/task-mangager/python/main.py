import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import task


def main_menu():
  '''Prompts the user to input a value between 1 and 5 in order to manage the list of tasks provided from the separate file
  Returns: The integer inputted by the user representative of the action they wish to take with regards to managing the task list
  '''

  # gathers the user's data pertaining to the choice that they wish to choose from the list of options from the main menu within the range 1-5
  selection = get_int_range(
    "1. Display current task\n2. Mark current task complete\n3."
    " Postpone current task\n4. Add new task\n5. Save and quit\nEnter Choice: ",
    1, 5)
  
  return selection


def read_file(filename):
  '''Passes in the name of the file and initializes the list for the file to be read from.
  Args:
    filename: A string representative of the file to be read from.
  Returns:
    task_list: A sorted list consisting of the tasks to be completed
  '''

  temporary_list = []
  task_list = []

  # opens the fie, reads it, and develops a list consisting of each individual line with a task listed in the file
  file = open(filename)
  filledList = file.read().split("\n")

  # for each task in the now filled in list, task description, date, and time respectively are grouped together as elements of a sublist which is then appended to the temporary list
  for tasks in filledList:
    temporary_list.append(tasks.split(","))
    
  # for the sublist of each task in the tempoary list, the description, date, and time associated with each task is appended to the permanent list as an object
  # should there be only one task left, the program breaks out of the loop to avoid a crash
  for tasks in temporary_list:
    if len(tasks) == 1:
      break
    task_elem = task.Task(tasks[0], tasks[1], tasks[2])
    task_list.append(task_elem)
        
  # resorts the list after the new task has been added to it
  for i in range(len(task_list) - 1):
    for j in range(i + 1, len(task_list)):
      if task_list[j].__lt__(task_list[i]):
        temp = task_list[i]
        task_list[i] = task_list[j]
        task_list[j] = temp

  return task_list


def write_file(filename, tasklist):
  '''Iterates through the task list and writes each task within the task list to the file to be written to. 
  Args:
    filename: A string symbolic of the name of the file to be written to
    tasklist: A list consisting of the tasks to be completed
  '''

  # opens the file to be written into and adds each task to the temporary variable as a string until all tasks have been accounted for and writes the resulting string stored to the file
  temp = ""
  f = open(filename, "w")
  for task in tasklist:
    if tasklist.index(task) != len(tasklist):
      temp += task.__repr__()
      print(temp)
  f.write(temp)
  f.close()

def get_date():
  '''Prompts the user to input the year, month, and day for a task when the user indicates that they wish to add to the task list or postpone their current task
  Returns: The date inputted by the user in the format "YYYY/MM/DD"
  '''
  
  print("Enter new due date:")

  # collects the user's input related to the new year, month, and day associated with a specified task and checks to make sure it is within the appropriate range.
  year = get_int_range("Enter year: ", 2000, 3000)
  month = get_int_range("Enter month: ", 1, 12)
  day = get_int_range("Enter day: ", 1, 31)

  # ensures that the inputted date values follow the "YYYY/MM/DD" format by accounting for any missing 0s when the month/day < 10
  if int(month) < 10:
    month = "0" + str(month)
  if int(day) < 10:
    day = "0" + str(day)

  # returns the date in the "YYYY/MM/DD" format
  return str(year) + "/" + str(month) + "/" + str(day)


def get_time():
  '''Prompts the user to input the hours and minutes for a task when the user indicates that they wish to add to the task list or postpone their current task
  Returns: The time inputted by the user in the format "HH:MM"
  '''
  
  print("Enter new time:")

  # collects the user's input related to the hours and minutes associated with a specified task and checks to make sure it is within the appropriate range.
  hour = get_int_range("Enter hour: ", 0, 23)
  minute = get_int_range("Enter minute: ", 0, 59)

  # ensures that the inputted time values follow the "HH:MM" format by accounting for any missing 0s when the hour/minute < 10
  if hour < 10:
    hour = "0" + str(hour)
  if minute < 10:
    minute = "0" + str(minute)

  # returns the time in the "HH:MM" format
  return str(hour) + ":" + str(minute)


def main():
  task_list = read_file("../txt/tasklist.txt")

  # runs until the user inputs 5 and exits the program
  while True:
    
    print("\n-Tasklist-")
    tasks_left = len(task_list)
    print("Tasks to Complete:", tasks_left)
    user_input = int(main_menu())    
    
    if user_input == 1:
      # user indicates that they want to display their current task
    
      if tasks_left == 0:
        # if the user inputs 1 and there are no tasks left, the program outputs a print statement declaring that all the user's tasks have been completed
        print("All tasks are complete")
      else:
        # else, there must still be at least one task left. In this case, the first element in the task list is displayed
        print("Current task is:", task_list[0].__str__())

    elif user_input == 2:
      # user indicates that they want to mark the current task as complete
      
      if tasks_left == 0:
        # if the user inputs 2 and there are no tasks left, the program outputs a print statement declaring that all the user's tasks have been completed
        print("All tasks are complete")
      else:
        # else, there must still be at least one task left. In this case, the first element in the task list is removed from the task list
        print("Marking Current Task Complete:\n", task_list[0].__str__())
        task_list.remove(task_list[0])
        if len(task_list) != 0:
          # if the length of the task list isn't 0, then there must still exist a task to complete
          # outputs the next task listed within the list that is still in need of completion
          print("New Current Task is Now:\n", task_list[0].__str__())

    elif user_input == 3:
      # user indicates that they want to postpone the current task
      
      if len(task_list) != 0:
        # if the length of the task list isn't 0, then there must still exist a task to complete
        # outputs a print statement displaying the task being postponed
        # collects the user's input pertaining to the new date and time to which the task will be postponed to
        print("Postponing Task:\n", task_list[0].__str__())
        task_list[0].date = get_date()
        task_list[0].time = get_time()

        # resorts the list after the new task has been added to it
        for i in range(len(task_list) - 1):
          for j in range(i + 1, len(task_list)):
            if task_list[j].__lt__(task_list[i]):
              temp = task_list[i]
              task_list[i] = task_list[j]
              task_list[j] = temp
      else:
        # if the first if-statement fails, then there must be no more tasks left to complete
        print("All tasks are complete")

    elif user_input == 4:
      # user indicates that they want to add onto their list of tasks

      # collects data related to the description, date, and time to the task they want to add and assigns these attributes to a new object representative of this new task and adds it to the task list
      desc = input("Enter a task: ")
      date = get_date()
      time = get_time()
      new_task = task.Task(desc, date, time)
      task_list.append(new_task)

      # resorts the list after the new task has been added to it
      for i in range(len(task_list) - 1):
        for j in range(i + 1, len(task_list)):
          if task_list[j].__lt__(task_list[i]):
            temp = task_list[i]
            task_list[i] = task_list[j]
            task_list[j] = temp

    elif user_input == 5:
      # user indicates that they want to save their new task list, overwrites the previous task list, and exits the program
      write_file("../txt/tasklist.txt",task_list)
      print("Goodbye.")
      exit()

main()