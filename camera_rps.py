from pkg_resources import run_script
import numpy
from RPS_solution import vision

def get_prediction():
    number = numpy.argmax(vision()) - 1
    return number



# the cv model prints prediction for the last images before you press 'q'
# it's a list of probability values for each of the four options
# take the highest prediction and use it to enter the user_choice