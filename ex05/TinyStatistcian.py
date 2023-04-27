# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/30 23:33:21 by archid-           #+#    #+#              #
#    Updated: 2023/03/31 12:32:26 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import numpy as np
from math import sqrt

class TinyStatistician(object):
    def mean(X):
        return None if type(X) != list or len(X) == 0 else sum(X) / len(X)

    def percentile(X, p):
        if len(X) == 0:
            return None
        X = sorted(X) # sort the range
        i = int((p / 100) * len(X)) # find the percentile index
        val = X[i] # get value of the percentile
        if len(X) % 2 == 0: #take the mid value in case the precentile is even 
            val += X[i - 1]
            val /= 2
        return float(val)

    def median(X):
        return TinyStatistician.percentile(X, 50)

    def quartile(X):
        if type(X) != list or len(X) == 0:
            return None
        else:
            return [TinyStatistician.percentile(X, 25), TinyStatistician.percentile(X, 75)]
    
    def var(X):
        mean = TinyStatistician.mean(X)
        return None if mean is None else sum([float(x - mean) ** 2 for x in X]) / len(X)

    def std(X):
        var = TinyStatistician.var(X)
        return None if var is None else float(sqrt(var))

if __name__ == '__main__':
    A = [1, 42, 300, 10, 59]
    print(TinyStatistician.mean(A))
    print(TinyStatistician.median(A))
    print(TinyStatistician.quartile(A))
    print(TinyStatistician.var(A))
    print(TinyStatistician.std(A))