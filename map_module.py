from tabulate import tabulate
# This imports the tabulate Library so that i can display a table like map to the user

class FarmMap:
  def __init__(self):
    self.section = [
      ["Farm House", "Barn", "Field"],
      ["Field", "Field", "Field"],
      ["Field", "Field", "Field"]   
    ]
    # A 3 by 3 grid representing the map 

    self.fields_data = {
      (0, 2): {"type" : None, "count" : 0},
      (1, 0): {"type" : None, "count" : 0},
      (1, 1): {"type" : None, "count" : 0}, 
      (1, 2): {"type" : None, "count" : 0},
      (2, 0): {"type" : None, "count" : 0},
      (2, 1): {"type" : None, "count" : 0},
      (2, 2): {"type" : None, "count" : 0},  
    }
    #This is the dictionary that stores the type and count of items in each field
    # the keys represent the coordinates on the map and are tuples 

  def display_map(self):
    for (row, col), data in self.fields_data.items():
      if data["type"] is not None:
        self.sections[row][col] = f"{data['count']} {data['type']}"
    print(tabulate(self.sections, tablefmt="grid"))
# The code loops over field_data to update self.sections with the type and count of items in each field
# Uses tabulate to print the map in grid form 