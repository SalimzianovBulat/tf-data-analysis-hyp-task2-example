import pandas as pd
import numpy as np


chat_id = 469801461 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    import scipy.stats as sps
    alpha = 0.05
    return sps.kstest(x, y)[1] <= alpha # Ваш ответ, True или False
