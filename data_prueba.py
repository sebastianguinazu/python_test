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
    
  df.loc[df['color_intensity']<=4, 'color_intensity_cat'] = 'little intense'
  df.loc[((df['color_intensity']>4) & (df['color_intensity']<=8)), 'color_intensity_cat'] = 'medium intensity'
  df.loc[df['color_intensity']>8, 'color_intensity_cat'] = 'very intense'
  df = df.drop('color_intensity', axis=1)  
    
  df.loc[(df.target == 1),'target'] = 0
  df.loc[(df.target == 2),'target'] = 1
  
  idx_tochange = rng.choice(np.argwhere(list(df['target'] == 0)).ravel()
                        ,size=10,replace=False)
  df.loc[idx_tochange, 'target'] = 1
  
  return df
