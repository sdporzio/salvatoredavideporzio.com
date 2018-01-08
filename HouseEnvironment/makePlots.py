import os, sys, json, pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict as OD
from NotebookUtils.ProgressBar import LogProgress as LP
from skhep.simulation import pdgid
plt.rcParams['font.family']='serif'
plt.rcParams['font.weight']='light'
plt.rcParams['font.size']=14
figsize = (12,8)

import datetime;
now = datetime.datetime.now()

time = []
temp = []
last = now
for i in range(50):
    last = last + datetime.timedelta(seconds=60)
    time.append(last)
    temp.append(np.random.rand()*2. + 20)

fig = plt.figure(figsize=figsize)
plt.plot(time,temp)
plt.savefig('HouseEnvironment/Plots/temperature.jpg')