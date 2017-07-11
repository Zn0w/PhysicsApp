from math import *

class MathHandler:
    def __init__(self, angle, speed):
        self.angle = radians(float(angle))
        self.speed = float(speed)

        print("angle: " + str(self.angle) + "||||speed: " + str(self.speed))

        '''try:
            self.angle = float(angle)
            self.speed = float(speed)
        except ValueError:
            pass'''

        self.g = 9.8

        self.flyTime = 2 * self.speed * sin(self.angle) / self.g
        self.flyDistance = self.speed * self.speed * sin(2 * self.angle) / self.g
        self.maxHeight = (self.speed * self.speed * sin(self.angle) * sin(self.angle)) / (2 * self.g)

    def getXPosition(self, time):
        x = self.speed * time * cos(self.angle)
        return x

    def getYPosition(self, time):
        y = (self.speed * time * sin(self.angle)) - (self.g * time * time / 2)
        return y