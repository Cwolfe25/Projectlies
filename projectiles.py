import math 
from polynomial import polynomial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
gravity = -9.8
degree = input("what do you want the launch degree to be? ")
psivel = [.1805,7.795]

launchv = input("what do you want the PSI to be? ")
psi = polynomial(psivel)
launchv = float(launchv)
launchv= psi.plugin(launchv)
print(launchv)
displacementy = 0 
degree = float(degree)
launchv = float(launchv)
degree = degree * 3.141592653589793238
degree = degree / 180
#degree = degree * 3.141592653589793238
#degree = degree / 180
yv = math.sin(degree)
yv = abs(yv)
yv = yv * launchv
xv = math.cos(degree)
xv = abs(xv)
xv = xv * launchv
print(xv)
print(yv)
equation = [-5, yv, 0]
eqx = [xv,0]
flightx = polynomial(eqx)
flight = polynomial(equation)
time = yv / 5
#time = -1*yv+sqrt(yv**2-4*-4.9*deltay)
#timet = -4.9*2
#time = time / timet
print(time)
#time = math.sqrt(time)
displacementx = xv * time
print(displacementx)
count = 0

plotint = .01
x = count
y = flight.plugin(count)
"""
x = [count]
y = [flight.plugin(count)]
while count <= time:
    count = count + plotint
        
    x.append(flightx.plugin(count)*1.09361)
    y.append(flight.plugin(count)*1.09361)
plt.plot(x, y)

"""
xdata = []
ydata = []
data = [count,time]
def animate(i):
    #ax.clear()
    count = float(data[0])
    if count <= time:
        x = flightx.plugin(count)*1.09361
        y = flight.plugin(count)*1.09361
        ax.plot(x,y,'-ro')
        xdata.append(x)
        ydata.append(y)

    else:
        x = flightx.plugin(time)*1.09361
        y = 0
        ax.plot(x,y)
    count = count + plotint
    data[0] = count
    ax.set_xlim(-1, 100)                  #sets the veiwing window
    ax.set_ylim(-1, 50)
ax.plot(xdata,ydata)

ani = animation.FuncAnimation(fig, animate, frames=60, interval=plotint)
plt.show()