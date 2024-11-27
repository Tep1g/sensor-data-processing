import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def _decay_func(t, a, b, amb_temp):
    return a * np.exp(-b * t) + amb_temp

def _get_decay_params(data: list[float], sample_period_s) -> tuple[float, float, float]:
    time = np.array([float(t*sample_period_s) for t in range(0, len(data))])
    temp = np.array(data)

    params, _ = curve_fit(_decay_func, time, temp)
    a, b, amb_temp = params
    
    return a, b, amb_temp

def plot_temp_log_func(data: list[float], duration_s: int, sample_period_s: int):
    a, b, amb_temp = _get_decay_params(data, sample_period_s)
    t = np.linspace(0, duration_s, duration_s * 10)
    temp = a*np.exp(-b*t) + amb_temp

    plt.plot(t, temp)
    plt.xlabel('time')
    plt.ylabel('temperature')
    plt.title('Logarithmic Curve Fit Function')
    plt.grid(True)
    plt.show()

def plot_temps(data: list[float], sample_period_s: int):
    time = np.array([float(t*sample_period_s) for t in range(0, len(data))])
    temp = np.array(data)

    plt.plot(time, temp)
    plt.xlabel('time')
    plt.ylabel('temperature')
    plt.title('Temperature points')
    plt.grid(True)
    plt.show()