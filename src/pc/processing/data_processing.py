import numpy
from scipy.optimize import curve_fit
from math import log

SAMPLE_PERIOD_S = 1.0
_BETA = 0
_VREF = 3.3
_U16 = 65535
_PULL_UP_RES = 1000
_VOLTAGE_FACTOR = _VREF / _U16
_B_OVER_298 = _BETA / 298

def _convert_temp_c(adc_u16: int) -> float:
    volt = adc_u16 * _VOLTAGE_FACTOR
    res = (volt / (_VREF - volt)) * _PULL_UP_RES
    temp_c = (_BETA / (log(res / _PULL_UP_RES) + (_B_OVER_298))) - 273

    return temp_c

def _decay_func(t, a, b, amb_temp):
    return a * numpy.exp(-b * t) + amb_temp

def get_decay_params(data: list[int]) -> tuple[float, float, float]:
    time = numpy.array([float(t*SAMPLE_PERIOD_S) for t in range(0, len(data))])
    temp = numpy.array(data)

    params, _ = curve_fit(_decay_func, time, temp)
    a, b, amb_temp = params
    
    return a, b, amb_temp