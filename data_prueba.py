def load_data():
  import pandas as pd
  import numpy as np
  import warnings
  from pandas.core.common import SettingWithCopyWarning

  warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
  
  from sklearn.datasets import load_wine

  wine = load_wine()
  df = pd.DataFrame(data=wine['data'], columns = wine['feature_names'])
  df['target'] = wine['target']

  for var in ['alcohol', 'magnesium', 'proline']:
    df[var][np.random.choice([True, False], size=df.shape[0], p=[.2,.8])] = np.NaN
    
  df.loc[(df.target == 1),'target'] = 0
  df.loc[(df.target == 2),'target'] = 1
  
  return df
