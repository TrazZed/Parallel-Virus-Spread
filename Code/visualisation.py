import numpy as np
import imageio as io
import matplotlib.pyplot as plt

count = 0
data = open("OutputData.txt")
for line in data:
    count += 1
    if (count % 5 == 0):
        print(count)
        fig, ax = plt.subplots()
        ax.axis([0, 500, 0, 500])
        people = line.split(",")
        for person in people:
            if (person == "\n"):
                break
            personInfo = person.split(" ")
            if (int(personInfo[4]) == 0):
                pass
            elif (int(personInfo[2]) == 1):
                ax.scatter(int(personInfo[0]), int(personInfo[1]), c='grey')
            elif (int(personInfo[3]) == 1):
                ax.scatter(int(personInfo[0]), int(personInfo[1]), c='red')
            else:
                ax.scatter(int(personInfo[0]), int(personInfo[1]), c='green')
            
        fig.savefig(r"Images\num" + str(count) + ".png")
        plt.close()

data.close()

names = np.arange(5, count, 5)
listOfImagePaths = []
for name in names:
    listOfImagePaths.append(r"Images\num" + str(name) + ".png")
ims = [io.imread(f) for f in listOfImagePaths]
io.mimwrite("animation.gif", ims)