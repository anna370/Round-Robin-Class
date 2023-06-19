class RoundRobin:
  """
  Class representing a round robin tournament schedule.
  """
  def __init__(self, name_list):
    """
    Initializes a round robin schedule for a list of names. 
    Makes a copy of the second parameter and initializes the names attribute.
    
    parameters:
      name_list: a list of strings, each of which is a name
    """
    self.names = list(name_list)
  
  def generate_round(self):
    """
    Generates and returns one round of the schedule.
    
    parameters:
      None
    return value:
      A list of tuples, where each tuple is a pair of names
    """
    list_copy = list(self.names)

    if len(list_copy) % 2 == 1:
      list_copy.append("bye")

    pairs = []

    for i in range(len(list_copy) // 2):
      pairs.append((list_copy[i], list_copy[-i - 1]))
    
    self.names = [list_copy[0]] + list_copy[-1:] + list_copy[1:-1]

    return pairs

rr = RoundRobin(['A', 'B', 'C'])
print(rr.generate_round()) # [('A', 'bye'), ('B', 'C'), ('A', 'C'), ('bye', 'B'), ('A', 'B'), ('C', 'bye')]
print(rr.generate_round()) # Next round
