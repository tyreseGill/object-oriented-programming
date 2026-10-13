class Task:
  
  def __init__(self, desc, date, time):
    '''Assigns the parameters to the attributes.'''

    self.desc = desc
    self.date = date
    self.time = time

  
  def get_description(self):
    '''Returns a string of the description belonging to the specified task object.'''
    return self.desc

  
  def __str__(self):
    '''Returns a string used to display the task’s information to the user.'''
    return self.desc + " - Due: " + self.date + " at " + self.time

  
  def __repr__(self):
    '''Returns a string used to write the task to the file.
    Writes each tasks to the file as the task list is iterated.'''
    return self.desc + "," + self.date + "," + self.time + "\n"

  
  def __lt__(self, other):
    '''Returns true if the task for 'self' is less than task for 'other'.
    Compares by year, month, day, and then alphabet'''

    # creates a list consisting of three elements representative of the year, month, and day associated with a task for self and other respectively.
    self_date_list = self.date.split("/")
    other_date_list = other.date.split("/")

    # creates a list consisting of two elements representative of the hours and minutes associated with a task for 'self' and 'other' respectively.
    self_time_list = self.time.split(":")
    other_time_list = other.time.split(":")

    # compares the task for 'self' with some other distinct task by year, month, day, hour, minute, and finally by alphabet
    # should the if-statement be false, then the task object for 'self' must be listed prior to the task object for 'other'
    # ensures that the list for tasks is organized correctly by date, time, and then alphabet
    if self_date_list[0] == other_date_list[0]:
      if self_date_list[1] == other_date_list[1]:
        if self_date_list[2] == self_date_list[2]:
          if self_time_list[0] == other_time_list[0]:
            if self_time_list[1] == other_time_list[1]:
              return self.desc < other.desc
            else:
              return self_time_list[1] < other_time_list[1]
          else:
            return self_time_list[0] < other_time_list[0]
        else:
          return self_date_list[2] < self_date_list[2]
      else:
        return self_date_list[1] < other_date_list[1]
    else:
      return self_date_list[0] < other_date_list[0]
              