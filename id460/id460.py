#!/usr/bin/env python
import math
import sys

#def monotonically_increasing_sequence(maxval, npoints, seqnum):
#    seq = [0]*npoints
#    seq[0] = 1
#    r_maxval = maxval
#    for i in range(1,npoints):
#        if (maxval <= 0):
#            seq[i] = seq[i-1]
#            continue
#        seq[i] = (seqnum % maxval) + seq[i-1]
#        seqnum = seqnum / maxval
#        maxval = r_maxval - seq[i]
#    return seq

def vel(y0, y1):
    if (y0 == y1):
        return y0
    return (y1 - y0)/(math.log(y1) - math.log(y0))

def dist(y0, y1):
    return math.sqrt((y1 - y0) ** 2 + 1)

def travel_time(y0, y1):
    if (y0 == y1):
        return (1 / y0);
    return (math.sqrt((y1 - y0) ** 2 + 1) * (math.log(y1) - math.log(y0)) / (y1 - y0))

def sym_trapz_time_odd(y1, N):
    t = 2*travel_time(y1, 1)
    t += ((N - 2) / float(y1))
    return t

def calc_path_time(path_ys):
    t = 0
    for i,y in enumerate(path_ys):
        if (i > 0):
            t += (dist(path_ys[i-1], y) / vel(path_ys[i-1], y))
    return t


def calc_path_time_ga(path_ys):
    t = 0
    for i,y in enumerate(path_ys):
        if (i > 0):
            t += (dist(path_ys[i-1] + 1, y + 1) / vel(path_ys[i-1] + 1, y + 1))
    return t

def sym_path_time_odd(sym_path_ys):
    t = 2 * calc_path_time(sym_path_ys)
    t += 2 / sym_path_ys[-1]
    return t

def sym_path_time_odd_ga(sym_path_ys):
    sym_path_ys = list(sym_path_ys)
    sym_path_ys.insert(0, 0)
    check = [x >= 0 for x in sym_path_ys]
    if (all(check) != True):
        return 1000000
    t = 2 * calc_path_time_ga(sym_path_ys)
    t += 1 / (sym_path_ys[-1] + 1)
    return t

N = int(sys.argv[1])

#for i in range(0, 100):
#    print monotonically_increasing_sequence(10, 10, i)

##path = [N/2]*(N/2)

##idx = 1
##for i in range(0, int(math.floor(math.log(N, 2)))):
##    path[i] = idx;
##    idx += N / (2 << (i + 1))

##time = sym_path_time_odd(path)
##print path, time

###times = map(lambda x: sym_trapz_time_odd(x, N), range(1, int(math.ceil(N * math.log(N)))))
###min_idx = times.index(min(times))
###print min_idx
###print times[min_idx]

#mintime = 0
#prev_y = 1
#y_stored = []
#for i in range(0,N/2):
#    y_off = range(0,N - prev_y)
#    y_trial = [y + prev_y for y in y_off]
#    dist_trial = map(math.sqrt, map(lambda x: (x ** 2 + 1), y_off))
#    vel_trial = map(lambda ynew: vel(prev_y, ynew), y_trial)
#    time_trial = map(lambda idx: dist_trial[idx] / vel_trial[idx], y_off)
#    min_idx = time_trial.index(min(time_trial))
#    y_stored.append(y_trial[min_idx])
#    mintime += time_trial[min_idx]
#    prev_y = y_trial[min_idx]

#print 2*mintime

import random

from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator
toolbox.register("attr_bool", random.randint, 0, int(math.ceil(N * math.log(N))))
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_bool, (N/2))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return sym_path_time_odd_ga(individual),

# Operator registering
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
#    random.seed(64)
    
    pop = toolbox.population(n=3000)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 100
    
    print("Start of evolution")
    
    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    print("  Evaluated %i individuals" % len(pop))
    
    # Begin the evolution
    for g in range(NGEN):
        print("-- Generation %i --" % g)
        
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
    
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
    
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        print("  Evaluated %i individuals" % len(invalid_ind))
        
        # The population is entirely replaced by the offspring
        pop[:] = offspring
        
        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
    
    print("-- End of (successful) evolution --")
    
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % ([0] + best_ind, best_ind.fitness.values))

#    print sym_path_time_odd_ga([1,1])

if __name__ == "__main__":
    main()
