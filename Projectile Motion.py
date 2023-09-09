import math
import numpy as np

t_max = 5000000
# the maximum number of steps we want it to loop should be very large since we dont know how long each projectile will take

vy = np.zeros(t_max + 1)
sy = np.zeros(t_max + 1)
sx = np.zeros(t_max + 1)
vx = np.zeros(t_max + 1)
# creates empty lists to store the values in, where vy is velocity_y , sy is distance_y etc.

def timeFunction (v_init, angle, sx, sy, vy, vx):
    g = 9.8
    dt = 0.01
    t_max = 5000000
    
    # sets the initial velocities in the x and y direction
    vy_init = v_init * math.sin(angle)
    vx_init = v_init * math.cos(angle)
    print("The initial velocity in the y direction is", round(vy_init,2), "m/s")
    print("The initial velocity in the x direction is", round(vx_init,2), "m/s")
    vx[0] = vx_init
    vy[0] = vy_init
    
    # time taken starts at 0 seconds
    time = 0
    
    # loops a large number of time
    for t in range (0, t_max):
        # uses the equations in the question to simulate the change in v and s for x and y each 0.01 seconds
        vy[t + 1] = vy[t] - dt*g
        sy[t + 1] = sy[t] + dt*vy[t]
        vx[t + 1] = vx[t]
        sx[t + 1] = vx[t] * (t + 1)/100  # t divided by 100 to account for  0.01 seconds
        
        # adds one to the total time taken, represents 0.01 seconds
        time = time + 1
        if sy[t + 1] <= 0:
            timeTaken = time/100
            # time taken divided by 100 because each 1 is 0.01 seconds
            break
    return(timeTaken, sx, sy, vx, vy)

# calculates the initial velocities in the x and y directions
v_init = 100
angle = math.radians(30)


# calls the function and saves the arrays for distance in x, y and time # taken
timeTaken, sx_final, sy_final, vx_final, vy_final = timeFunction(v_init, angle, sx , sy , vy, vx)


print("\nThe maximum height reached is ", round(np.max(sy_final),2), "m")
print("The maximum distance in the x direction before landing is", round(np.max(sx_final), 2), "m")
print("The total time the projectile travels", timeTaken, "s")

########### THIS PART ACTUALLY PLOTS THE GRAPH ##############

import matplotlib.pyplot as plt
plt.plot(sx_final, sy_final, color = 'black')
plt.title("Projectile Motion Simulation")
plt.xlabel("Distance Travelled in x Direction (m)")
plt.ylabel("Distance Travelled in y Direction (m)")


############# 2ND GRAPH TO PLOT POTENTIAL AND KINETIC ENERGIES OF THE OBJECT #####

# initialises values and creates empty arrays to store values for GPE, KE and also time
timeTaken = round(timeTaken)
steps = timeTaken*100
velocity = np.zeros(steps)
KE = np.zeros(steps)
GPE = np.zeros(steps)
time = np.zeros(steps)
time[0] = 0
m = 10

# stores the values of KE and GPE at each time interval using a loop
for i in range (steps):
    velocity[i] = math.sqrt(vx_final[i]**2 + vy_final[i]**2)
    KE[i] = 0.5*m*(velocity[i]**2)
    GPE[i] = m*9.8*sy_final[i]
    time[i] = i * 0.01

# formats and plots the graph
plt.plot(time,KE, label = 'Kinetic Energy', color = 'red')
plt.plot(time, GPE, label = 'Potential Energy', color = 'blue')
plt.plot(time, KE + GPE, label = 'Total Energy', color = 'green')
plt.title("Projectile Motion Simulation")
plt.ylabel("Energy (Joules)")
plt.xlabel("Time (seconds)")
plt.ylim(0, 55000)
plt.legend()
