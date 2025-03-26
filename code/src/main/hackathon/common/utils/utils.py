import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
from matplotlib import pyplot as plt

def convert_datetime_features(df,datetime_cols):
    for feature in datetime_cols:

        df[feature].fillna(method='ffill', inplace=True)
        # Convert to datetime objects
        df[feature] = pd.to_datetime(df[feature])

        # Extract features
        df[feature + '_year'] = df[feature].dt.year
        df[feature + '_month'] = df[feature].dt.month
        df[feature + '_day'] = df[feature].dt.day
        df[feature + '_dayofweek'] = df[feature].dt.dayofweek
        df[feature + '_quarter'] = df[feature].dt.quarter
        df[feature + '_is_weekend'] = (df[feature].dt.dayofweek // 5 == 1).astype(int)
        df.drop([feature],axis=1,inplcae=True)
    return df

# write a fucntion for one hot encoding
def one_hot_encode(df, columns):
  for column in columns:
    dummies = pd.get_dummies(df[column], prefix=column)
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
  return df

# write a fucntion for frequency encoding
def frequency_encode(df, columns):
  for column in columns:
    frequencies = df[column].value_counts(normalize=True)/(len(df)*0.01)
    df[column + '_freq'] = df[column].map(frequencies)
    df = df.drop(column, axis=1)
  return df

#write a function to rank categories based on frequency, highest frequency get 1, followed by 2,3,4
def frequency_ranking_encode(df, columns):
  for column in columns:
    frequencies = df[column].value_counts(normalize=True)
    frequencies={category: rank+1 for rank, category in enumerate(frequencies.index)}
    df[column + '_freq'] = df[column].map(frequencies)
    df = df.drop(column, axis=1)
  return df