import math
import numpy as np
import matplotlib.pyplot as plt

def plot_sieve(all_nmax, all_proportions):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    
def plot_log_sieve(all_nmax, all_proportions):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    plt.xscale("log")
    plt.yscale("log")