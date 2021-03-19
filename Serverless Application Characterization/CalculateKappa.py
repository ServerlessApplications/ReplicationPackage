import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.expand_frame_repr', False)
from statsmodels.stats.inter_rater import fleiss_kappa
import re

def calculateFleissKappa(series, characteristics):
    series = series[~(series.str.contains(',') & ~series.str.contains('\)'))]
    series = series.tolist()
    agreement = [[None for i in range(len(characteristics))] for j in range(len(series))]
    for row in range(len(series)):
        i = 0
        for col in range(len(characteristics)):
            if '|' not in series[row]:
                if re.match(characteristics[col], series[row]):
                    agreement[row][col] = 2
                    i = i + 2
                else:
                    agreement[row][col] = 0
            else:
                if re.search(characteristics[col], series[row]):
                    agreement[row][col] = len(re.findall(characteristics[col], series[row]))
                    i = i + len(re.findall(characteristics[col], series[row]))
                else:
                    agreement[row][col] = 0
        if i != 2:
            print("Something went wrong", row, series[row], i)

    return len(series), fleiss_kappa(agreement)


print("### Starting Fleiss Kappa Calculation ###")
data = pd.read_csv('Initial Characterizations.csv')

# Remove characteristics with thematic encoding
del data['Usage of External Services'], data['Motivation']

# Remove characteristics with unbounded numeric values
del data['Number of Distinct Functions']

weights = []
kappas = []
weight, kappa = calculateFleissKappa(data['Platform'], ['Not applicable', 'Unknown', 'Other', 'Google', 'IBM', 'Azure', 'AWS'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['In Production'], ['Not applicable', 'Unknown', 'No', 'Yes'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Execution pattern'], ['Not applicable', 'Unknown', 'Scheduled', 'High-volume on-demand', 'On-demand'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Burstiness'], ['Not applicable', 'Unknown', 'No( |$)', 'Yes'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Trigger types'], ['Not applicable', 'Unknown', 'Manual', 'Scheduled', 'Cloud event', 'HTTP request'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Workflow Coordination'], ['Not applicable', 'Unknown', 'local coordinator', 'Workflow engine', 'Event'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Is Latency Relevant?'], ['Not applicable', 'Unknown', 'For parts of use case', 'For complete use case', 'Real-time', 'Not important'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Data Volume (per execution)'], ['Not applicable', 'Unknown', '> 1 GB', '< 1 GB', '< 100 MB',  '< 10 MB', '< 1 MB'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Workflow Structure'], ['Not applicable', 'Unknown', 'Scatter', 'Gather', 'Dynamic workflow', 'Complex Workflow', 'Loops/Conditional branches', 'Bag of tasks', 'Pipeline', 'Chain'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Workflow Size'], ['Not applicable', 'Unknown', 'Large \(1000\+\)', 'Medium \(10-1000\)', 'Small \(2-10\)'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Cost/Performance Tradeoff'], ['Not applicable', 'Unknown', 'Undefined', 'Performance-focused', 'Cost-focused'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Function Runtime'], ['Not applicable', 'Unknown', 'Long \(min\+\)', 'Short \(ms, s\)'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Resource Bounds'], ['Not applicable', 'Unknown', 'Network', 'External Service', 'Hybrid', 'CPU', 'I/O'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Locality Requirements'], ['Not applicable', 'Unknown', 'Edge', '(Specific region|Regional)', '(Multi-region|Global)', 'None'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Workflow Internal Parallelism'], ['Not applicable', 'Unknown', 'Extreme', 'High', 'Low', 'No( |$)'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Programming Languages'], ['Not applicable', 'Unknown', 'Ruby', 'Go', '(C( |$)|C\+\+)', 'C#', 'Java( |$)', 'Python', '(JavaScript|Javascript|NodeJS|Node.js)'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Function Upgrade Frequency'], ['Not applicable', 'Unknown', 'Rarely', 'Often'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Domain'], ['Not applicable', 'Unknown', 'FinTec', 'Universities', 'Public authority', 'WebServices', 'Scientific computing', 'Entertainment', 'Cross-Domain', 'IoT', 'Other'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Application Type'], ['Not applicable', 'Unknown', 'Business-critical workloads', 'Operations', 'Scientifc Workload', 'Side-task', 'Monitoring', 'Other'])
weights.append(weight)
kappas.append(kappa)
weight, kappa = calculateFleissKappa(data['Open Source'], ['Not applicable', 'Unknown', 'No', '(Yes|http)'])
weights.append(weight)
kappas.append(kappa)

sum = 0
weightsum = 0
for i in range(len(weights)):
    sum = sum + weights[i]*kappas[i]
    weightsum = weightsum + weights[i]
print("Fleiss kappa: ", sum/weightsum)
print("### Finished Fleiss Kappa Calculation ###")