import math

def radiusCircumferenceCircle(name,c):
    radius = c/2 * math.pi
    return "The radius in terms of circumference of {} is {}".format(name, radius)

print(radiusCircumferenceCircle('A Jets Large Pizza', 15))