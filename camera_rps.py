from RPS_solution import prediction

def get_prediction():
    for n in range(1,3):
        if prediction[n]>prediction[n+1]:
            user_choice = prediction[n]
        else:
            user_choice = prediction[n+1]
    return user_choice

# the cv model prints prediction for the last images before you press 'q'
# it's a list of probability values for each of the four options
# take the highest prediction and use it to enter the user_choice