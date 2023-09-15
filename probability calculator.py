import copy
import random

class Hat:
  def __init__(self,**argv):
    self.contents = []
    for k,v in argv.items():
      for itr in range(v):
        self.contents.append(k)
    
  def draw(self, draws):
    draw_list = []
    if draws >= len(self.contents):
      return self.contents
    for i in range(draws):
      n = self.contents.pop(random.randrange(len(self.contents)))
      draw_list.append(n)
    return draw_list
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  final_count=0
  for _ in range(num_experiments):
    copyhat = copy.deepcopy(hat)
    temp_list = copyhat.draw(num_balls_drawn)
    success=True
    for key,value in expected_balls.items():
      if temp_list.count(key) < value:
        success=False
        break
    if success:
      final_count+=1
  return final_count/num_experiments
