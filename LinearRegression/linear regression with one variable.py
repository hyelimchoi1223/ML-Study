from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def hypothesis(seta0, seta1, value_x):    
    return seta0+(seta1*value_x)

lineardata = {'x':[],'y':[]}
for x in np.arange(0,10,1):
    lineardata['x'].append(x)
    lineardata['y'].append(hypothesis(-569.6, -530.9, x))

lineardata_df = pd.DataFrame(lineardata)
testdata = {'x':[1,2,2,3,3,4,5,6,6,6,8,10],
           'y':[-890, -1411,-1560,-2220, -2091, -2878, -3537, -3268, -3920, -4163, -5471, -5157] }
test_df = pd.DataFrame(testdata, index=['methane', 'ethene', 'ethene', 'propane', 'cyclopropane', 'butan', 'pentane', 'benzene', 'cycloexane', 'hexane', 'octane', 'napthalene'])
plt.plot(testdata['x'], testdata['y'])
plt.plot(lineardata_df['x'], lineardata_df['y'])
plt.show()