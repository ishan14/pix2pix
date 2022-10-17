import matplotlib.pyplot as plt
import numpy as np


f = open("results.txt", "r")

ff = f.readlines()

gen_loss = []
disc_loss = []

for values in ff:
    vv = values.split(",")
    gen_loss.append(float(vv[0]))
    disc_loss.append(float(vv[1]))


gen_loss = [float('%.3f'%(round(i, 3)/1000)) for i in gen_loss]
disc_loss = [float('%.3f'%(round(i, 3)/1000)) for i in disc_loss]


fig, ax = plt.subplots(1, 2)

ax[0].plot(gen_loss)
ax[1].plot(disc_loss)
plt.show()