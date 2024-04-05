import numpy as np
import matplotlib.pyplot as plt
from local.lib import timeseries as ts
import pandas as pd
import os
from IPython.display import Image
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
%matplotlib inline

date_split = "2018-03-01"

idx = pd.date_range("2018-01-01", "2018-03-31", freq="6h")
i = np.linspace(-5,4,len(idx))
i = np.linspace(np.random.random()*5-5,np.random.random()*5+2,len(idx))
t = np.log(i**2+.3)*np.cos(4*i)
t += (np.random.normal(size=len(idx))*.4)
t = np.round(t*3+30,3)
d = pd.DataFrame(np.r_[[t]].T, columns=["signal"], index=idx)
d.index.name="date"

plt.figure(figsize=(15,3))
plt.plot(d[:date_split].index, d[:date_split].signal, color="black", lw="2", label="train");
plt.plot(d[date_split:].index, d[date_split:].signal, color="red", lw="2", label="test");
plt.axvline(date_split, color="grey"); plt.legend();plt.grid();
signal = d


def make_timeseries_dataset(d, n_timesteps_lookback):
    import pandas as pd
    
    columnasDespl = []
    colPred = pd.DataFrame()
    for i in range(n_timesteps_lookback, -1, -1): # Num desplazamiento, Parada, Salto
      columna = d.shift(-i)
      columnasDespl.append(columna)


    #colPredict = d.shift(1)
    df = pd.concat(columnasDespl, axis=1)
    colPred["signal+1"] = d.shift(- n_timesteps_lookback - 1)
    df = pd.concat([df, colPred], axis=1)

    colPred

    df = df.dropna()

    for i in range (n_timesteps_lookback, -1, -1):

      df = df.rename(columns={df.columns[i]:'singal-' + str(i)})
    
    #nombresCol = ['signal-' +str(i) for i in range(n_timesteps_lookback,-1,-1)]
    #df.columns = nombresCol

    #df
    return df
#d.dropna()
make_timeseries_dataset(d, 3)