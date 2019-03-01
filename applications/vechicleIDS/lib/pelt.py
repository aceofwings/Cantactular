from lib import pelt
from changepy.costs import normal_mean, normal_var, normal_meanvar
import numpy as np
size = 100

mean_a = 5.0
mean_b = 10.0
var = 0.1

data_a = np.random.normal(mean_a, var, size)
data_b = np.random.normal(mean_b, var, size)
data = np.append(data_a, data_b)

cp = pelt(normal_var(data, var), 104)
 # since data is random, sometimes it might be different, but most of the time there will be at most a couple more values around 100
print(cp)
