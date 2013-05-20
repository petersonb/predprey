from predatorprey import *
import pylab as pl

model = PredatorPreyModel()
r = model.addAnimal('Rabbit',50,.1)
f = model.addAnimal('Fox',15,-.05)
w = model.addAnimal('Wolf',8,-.01)
   
model.setPredator(f,r,.001,.01)
model.setPredator(w,f,.001,.01)
data = model.euler(10000,.1)

for d in data[1]:
    pl.plot(data[0],d)
pl.show()

pl.plot(data[1][1],data[1][0])
pl.show()