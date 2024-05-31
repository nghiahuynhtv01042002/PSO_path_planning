import numpy as np
import matplotlib.pyplot as plt  # Fix import statement for pyplot
import math
import random
from tkinter import messagebox

#define objective function
def F1(x):
    return np.sum(x**2)
   
class Particle:
    def __init__(self, position):
        self.position = position
        self.velocity = np.zeros_like(position)
        self.best_position = position
        self.best_fitness = float('inf')
        
def Particle_Swarm_Optimization(objective_func, swarm_size, dimension, iteration_max):
    swarm_best_position = None
    swarm_best_fitness = float('inf')
    particles = []

    # Position initialization
    for _ in range(swarm_size):
        position = np.random.uniform(-0.5, 0.5, dimension)
        particle = Particle(position)
        particles.append(particle)
        # Fitness update
        fitness = objective_func(position)
        if fitness < swarm_best_fitness:
            swarm_best_fitness = fitness
            swarm_best_position = position
            particle.best_position = position
            particle.best_fitness = fitness

    # PSO main loop
    for iteration in range(iteration_max):
        for particle in particles:
            # Update velocity
            w = 0.8
            c1 = 1.2
            c2 = 1.2

            r1 = random.random()
            r2 = random.random()

            # Update position and new velocity
            particle.velocity = (w * particle.velocity 
                                 + c1 * r1 * (particle.best_position - particle.position) 
                                 + c2 * r2 * (swarm_best_position - particle.position))
            particle.position += particle.velocity

            # Evaluate fitness
            fitness = objective_func(particle.position)

            # Update pbest
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

            # Update gbest
            if fitness < swarm_best_fitness:
                swarm_best_fitness = fitness
                swarm_best_position = particle.position

    return swarm_best_position, swarm_best_fitness

# Parameters
swarm_size = 100
iteration_max = 500
dimension = 30
objective_function = {'F1': F1}

print("program on")

# Iteration over objective function using PSO
for fun_name, objective_func in objective_function.items():
    output = "Running function = " + fun_name + "\n"
    best_position, best_fitness = Particle_Swarm_Optimization(objective_func, swarm_size, dimension, iteration_max)
    output += "Best position " + str(best_position) + "\n"
    output += "Best fitness " + str(best_fitness) + "\n"
    output += "\n"
    print(output)
    # messagebox.showinfo("PSO results", output)
    

