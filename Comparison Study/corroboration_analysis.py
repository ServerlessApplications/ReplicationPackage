import pandas as pd
import numpy as np
from scipy import stats


def rel_to_score(rel):
    if rel < 0.2:
        return "No"
    if rel < 0.4:
        return "Low"
    if rel < 0.6:
        return "Medium"
    if rel < 0.8:
        return "High"
    return "Very High"


sheet_to_df_map = pd.read_excel('Corroboration Mapping.xls', sheet_name=None)

for item in sheet_to_df_map.items():
     # extract caracteristic and comparison survey names
     characteristic = item[0].split(' -')[0]
     results = item[1]
     survey = results.columns[2]

     # clean up excess columns
     #results = results.drop(results.columns[5], axis=1)
     #results = results.drop(results.columns[4], axis=1)
     #results = results.drop(results.columns[3], axis=1)

     # extract overlapping data
     overlapping = results[results[results.columns[0]] == 'Overlapping?']

     # clean up excess rows
     results = results[results.index < overlapping.index[0]-1]

     # remove other field
     results = results[results.index != overlapping.index[0]-3]

     # unknown correction
     unknown = results[results.index == overlapping.index[0]-2]
     results = results[results.index != overlapping.index[0]-2]
     results['Our Study'] = results['Our Study'] / (1 - unknown['Our Study'][overlapping.index[0]-2]) * 100
     results[survey] = results[survey] / (1 - unknown[survey][overlapping.index[0]-2]) * 100

     # overlapping correction
     overlapping_us = overlapping['Our Study'][overlapping.index[0]]
     overlapping_them = overlapping[survey][overlapping.index[0]]
     if (overlapping_us == 1.0) & (overlapping_them != 1.0):
         our_max = results['Our Study'].max()
         their_max = results[survey].max()
         scaling = their_max/our_max
         results['Our Study'] = results['Our Study'] * scaling
     if (overlapping_us != 1.0) & (overlapping_them == 1.0):
         our_max = results['Our Study'].max()
         their_max = results[survey].max()
         scaling = our_max/their_max
         results[survey] = results[survey] * scaling

     # calculate Spearman correlation coefficient
     order1 = results.sort_values(by=['Our Study'])[results.columns[0]]
     order2 = results.sort_values(by=[survey])[results.columns[0]]
     correlation, p = stats.spearmanr(order1, order2)
     scaled_correlation = (correlation + 1) / 2

     # calculate weighted percentage error
     error = 0
     for index, row in results.iterrows():
         if row['Our Study'] != 0.0:
             percentage_error = abs(row[survey] - row['Our Study'])/row['Our Study']
             error = error + min(percentage_error, 1) * row['Our Study']/results['Our Study'].sum()
     accuracy = 1 - error

     total_rel = round((accuracy + scaled_correlation)/ 2, 2)
     print(characteristic, "-", survey, "\t1 - Weighted Mape:", round(accuracy, 3), "\tSPEARMAN:", round(scaled_correlation, 3), "\tTOTAL SCORE:", total_rel, "RATING:", rel_to_score(total_rel))