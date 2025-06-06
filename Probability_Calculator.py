import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = [color for color, count in self.kwargs.items() for _ in range(count)]

    def __repr__(self):
        value_str = ', '.join(f'{color}={count}' for color, count in self.kwargs.items())
        hat_str = 'Hat(' + value_str + ')'

        return hat_str

    def draw(self, draws):
        num_of_balls = len(self.contents)

        if draws >= num_of_balls:
            balls_drawn = self.contents.copy()
            sorted_draws = sorted(balls_drawn)
            for color in sorted_draws:
                if color in self.contents:
                    self.contents.remove(color)
            return sorted_draws
        else:
            balls_drawn = random.sample(self.contents, draws)
            sorted_draws = sorted(balls_drawn)
            for color in sorted_draws:
                if color in self.contents:
                    self.contents.remove(color)
            return sorted_draws

        for color in sampled_colors:
            if color in colors:
                colors.remove(color)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #Base values
    N = num_experiments
    #M = Number of matches
    M = 0
    expected_list = [color for color, count in expected_balls.items() for _ in range(count)]
    sorted_expected = sorted(expected_list)

    for i in range(num_experiments):
        #Reset hat as experiment_hat
        experiment_hat = eval(repr(hat))
        balls_drawn = experiment_hat.draw(num_balls_drawn)    

        #Compare balls_drawn to expected_balls
        drawn_dict = {color: balls_drawn.count(color) for color in set(balls_drawn)}
        if all(drawn_dict.get(color, 0) >= count for color, count in expected_balls.items()):
            M += 1         

    probability = M/N
    return probability


#Example
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)


"""       
Experiment function determines probability of drawing the expected_balls
from a Hat object in the number of draws in num_balls_drawn.
The probability is determined using the amount of experiments ran using the num_experiments argument.

Above is an example of using the program
"""


