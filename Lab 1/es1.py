# dice rolling simulator
import random

class Dice:
    def __init__(self, num_faces):
        self.num_faces = num_faces

    def __str__(self):
        return "The dice have " + str(self.num_faces) + " faces"
    
    def launch_dice(self):
        return random.randint(1, self.num_faces)


if __name__ == "__main__":
    a = Dice(6)
    print(a)
    for i in range(1, 10):
        print("launch result: ", a.launch_dice())
