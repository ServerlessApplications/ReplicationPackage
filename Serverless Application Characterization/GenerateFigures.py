import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
font_size = 22
plt.rcParams.update({'font.size': font_size})

def analyze_hist(col, title, filename):
    col = col[~col.str.contains('Unknown')]
    col = col.str.replace('\+', "")
    col = col.astype('int32')
    plt.figure(figsize=(12, 4))
    counts, bins, bars = plt.hist(col, bins=np.linspace(0.5, 200.5, 201), density=True, edgecolor='black', color='grey', linewidth=0.5)
    print("--- Comparison to Serverless in the Wild ---")
    print("1 Function", col[col == 1].size/col.size)
    print("<=10 Function", col[col <= 10].size / col.size)
    print(">100 Function", col[col > 100].size / col.size)
    print("--- Comparison to Mixed-Method Study ---")
    print("1-5 Functions", col[col <= 5].size/col.size)
    print("6-10 Functions", col[(col > 5) & (col < 11 )].size / col.size)
    print("11-20 Functions", col[(col > 10) & (col < 21 )].size / col.size)
    print("21+ Functions", col[(col > 20)].size/col.size)
    print("--- Comparison to The New Stack ---")
    print("<1 Functions", col[col < 1].size/col.size)
    print("1 Function", col[col == 1].size/col.size)
    print("2-5 Functions", col[(col > 1) & (col < 6 )].size / col.size)
    print("6-10 Functions", col[(col > 5) & (col < 11 )].size / col.size)
    print("11-25 Functions", col[(col > 10) & (col < 26 )].size / col.size)
    print(">25 Functions", col[(col > 25)].size/col.size)
    plt.ylim([0, 0.4])
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4], fontsize=font_size)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], fontsize=font_size)
    plt.xlim([0.5, 20.5])
    plt.xlabel(title, fontsize=font_size)
    plt.ylabel('Probability density', fontsize=font_size)
    plt.tight_layout()
    plt.savefig('figures/' + filename + '.pdf')
    plt.close()


def analyze_col(col, values, title, filename, alias=False):
    if alias is False:
        alias = values
    col = col[~col.str.contains('Not applicable')]

    results = {}
    for i, value in enumerate(values):
        if value == 'Java':
            obj = col.str.contains(value).value_counts() - col.str.contains('JavaScript').value_counts()
        elif value == 'C/C++':
            obj = col.str.contains('C').value_counts() - col.str.contains('C#').value_counts()
        else:
            obj = col.str.contains(value).value_counts()
        if True in obj.index.tolist():
          results.update({alias[i]: obj[True]})
        else:
          results.update({alias[i]: 0})


    # Generates percentages excluding unknowns
    col = col[~col.str.contains('Unknown')]
    if filename == 'motivation':
        col = col[~col.str.contains('-')]
        if values.__contains__('-'):
            values.remove('-')
    if filename == 'open_source':
        col = col[~col.str.contains('^-')]
        if values.__contains__('-'):
            values.remove('-')
    if values.__contains__("Unknown"):
        values.remove("Unknown")
    if alias.__contains__("Unknown"):
        alias.remove("Unknown")
    results = {}
    for i, value in enumerate(values):
        if value == 'Java':
            obj = col.str.contains(value).value_counts() - col.str.contains('JavaScript').value_counts()
        elif value == 'C/C++':
            obj = col.str.contains('C').value_counts() - col.str.contains('C#').value_counts()
        else:
            obj = col.str.contains(value).value_counts()
        if True in obj.index.tolist():
          results.update({alias[i]: obj[True]})
        else:
          results.update({alias[i]: 0})
    y = [i*100 / len(col) for i in list(results.values())]


    comp = 0.7
    height = (1 + len(results) * 0.8) * comp
    fig, ax1 = plt.subplots(1, 1, figsize=(12, height))
    ax1.barh([x * comp for x in range(len(results))], y, align='center', color='grey', height=0.55)
    for i, v in enumerate(y):
        ax1.text(v + 0.5, i*comp, '{:.0f}'.format(round(v)) + '%', fontsize=font_size, va='center')
    ax1.tick_params(axis='both', which='major', labelsize=font_size)
    ax1.set_yticks([x * comp for x in range(len(results))],)
    ax1.set_yticklabels(list(results.keys()), linespacing=0.6)
    ax1.set_ylim([-0.55* comp, len(results) * comp - 0.45*comp])
    ax1.tick_params(axis='both', length=8, width=1)
    ax1.tick_params(which='minor', axis='both', length=5, width=1)
    from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.xaxis.set_major_formatter(plt.NullFormatter())
    ax1.set_xlim([0, 100])
    ax1.set_xlabel('Proportion of applications [%]', fontsize=font_size)

    plt.tight_layout()
    plt.savefig('figures/' + filename + '.pdf')
    plt.close()



def analyze_is_workflow(df, values, title, filename, alias=False):
    analyze_col((df['Workflow Coordination'].str.contains('applicable')
          & df['Workflow Structure'].str.contains('applicable')
          & df['Workflow Size'].str.contains('applicable')
          & df['Workflow Internal Parallelism'].str.contains('applicable')).astype(str),
                values, title, filename, alias)


print("### Starting Figure Generation ###")
# Create target Directory if don't exist
if not os.path.exists('figures'):
    os.mkdir('figures')
data = pd.read_csv('Dataset.csv')
analyze_is_workflow(data, ['True', 'False'], 'Is it a workflow?', 'is_workflow', ['Yes', 'No'])
print("Generated Figure: Is it a workflow?")
analyze_hist(data['Number of Distinct Functions'], 'Number of distinct functions', 'number_of_functions')
print("Generated Figure: Number of distinct functions")
analyze_col(data['In Production'], ['No', 'Yes'], 'Is the use case deployed in production?', 'production')
print("Generated Figure: Is the use case deployed in production?")
analyze_col(data['Platform'], ['Google', 'IBM', 'Private Cloud', 'Azure', 'AWS'], 'Deployment platform', 'platform', ['Google Cloud', 'IBM Cloud', 'Private Cloud', 'Azure', 'AWS'])
print("Generated Figure: Deployment platform")
analyze_col(data['Execution pattern'], ['Scheduled', 'High-volume On-demand', '(?<! )On-demand'], 'Execution pattern', 'execution_pattern', ['Scheduled', 'High-volume\non-demand', 'On-demand'])
print("Generated Figure: Execution pattern")
analyze_col(data['Burstiness'], ['No', 'Yes'], 'Is the workload bursty?', 'bursty', ['Not Bursty', 'Bursty'])
print("Generated Figure: Is the workload bursty?")
analyze_col(data['Trigger types'], ['Manual', 'Scheduled', 'Cloud event', 'HTTP request'], 'How are workflow executions triggered?', 'trigger')
print("Generated Figure: How are workflow executions triggered?")
analyze_col(data['Workflow Coordination'], ['local coordinator', 'Workflow engine', 'Event'], 'How are workflows coordinated?', 'coordination', ['Local coordinator', 'Workflow engine', 'Event'])
print("Generated Figure: How are workflows coordinated?")
analyze_col(data['Is Latency Relevant?'], ['Real-time', 'For parts of use case', 'For complete use case', 'Not important'], 'Is latency relevant?', 'latency_relevant', ['Real-time', 'Parts of application', 'Complete application', 'Not important'])
print("Generated Figure: Is latency relevant?")
analyze_col(data['Data Volume (per workflow execution)'], ['> 1 GB', '< 1 GB', '< 100 MB',  '< 10 MB', '< 1 MB'], 'Data volume per workflow execution', 'data_volume')
print("Generated Figure: Data volume per workflow execution?")
analyze_col(data['Workflow Structure'], ['Bag of tasks', '(Complex Workflow|Dynamic workflow|Loops/Conditional branches)', '(Chain|Pipeline)'], 'Workflow structure', 'workflow_structure', ['Bag of tasks', 'Complex Workflow', 'Sequential Workflow'])
print("Generated Figure: Workflow structure?")
analyze_col(data['Workflow Size'], ['Large \(1000\+\)', 'Medium \(10-1000\)', 'Small \(2-10\)'], 'Workflow size', 'workflow_size', ['Large (1000+)', 'Medium (10-1000)', 'Small (2-10)'])
print("Generated Figure: Workflow size")
analyze_col(data['Cost/Performance Tradeoff'], ['Undefined', 'Performance-focused', 'Cost-focused'], 'Cost/performance tradeoff', 'tradeoff')
print("Generated Figure: Cost/performance tradeoff")
analyze_col(data['Function Runtime'], ['Long', 'Short'], 'Function runtime', 'function_runtime', ['Long (min+)', 'Short (ms, s)'])
print("Generated Figure: Function runtime")
analyze_col(data['Resource Bounds'], ['Network', 'External Service', 'Hybrid', 'CPU', 'I/O'], 'Resource bounds', 'resource_bounds')
print("Generated Figure: Resource bounds")
analyze_col(data['Locality Requirements'], ['Edge', 'Multi-region', 'Specific region', 'None'], 'Locality requirements', 'locality_requirement')
print("Generated Figure: Locality requirements")
analyze_col(data['Workflow Internal Parallelism'], ['No', '(Extreme|High|Low)'], 'Workflow internal parallelism', 'parallelism', ['No', 'Yes'])
print("Generated Figure: Workflow internal parallelism")
analyze_col(data['Programming Languages'], ['Ruby', 'Go', 'C#', 'C/C++', 'Java', 'Python', 'JavaScript'], 'Programming languages', 'languages')
print("Generated Figure: Programming languages")
analyze_col(data['Function Upgrade Frequency'], ['Often', 'Rarely'], 'Function upgrade frequency', 'upgrade')
print("Generated Figure: Function upgrade frequency")
analyze_col(data['Usage of External Services'], ['Cloud ML', 'Cloud Streaming', 'Cloud Queue', 'Cloud Logging/Monitoring', '-', 'Cloud Pub/Sub', 'Cloud API Gateway', 'Cloud Database', 'Cloud Storage'], 'Use of external services', 'external_services', ['ML', 'Queue', 'Streaming', 'Monitoring', 'None', 'Pub/Sub', 'API Gateway', 'Database', 'Storage'])
print("Generated Figure: Use of external services")
analyze_col(data['Domain'], ['Public authority', 'FinTec', 'Other', 'Entertainment', 'IoT', 'Scientific computing', 'Cross-Domain', 'WebServices'], 'Domain', 'domain')
print("Generated Figure: Domain")
analyze_col(data['Application Type'], ['Operations & Monitoring', 'Batch Tasks', 'Stream/async Processing', 'API'], 'Application type', 'application_type', ['Ops & Monitoring', 'Batch Tasks', 'Stream/async', 'API'])
print("Generated Figure: Application type")
analyze_col(data['Motivation'], ['Maintainability', 'Performance', 'Simplify Development', 'Scalability', 'NoOps', 'Cost'], 'Motivation', 'motivation', ['Maintainability', 'Simplify Development', 'Performance', 'Scalability', 'NoOps', 'Cost'])
print("Generated Figure: Motivation")
analyze_col(data['Open Source'], ['^No', 'http'], 'Open Source', 'open_source', ['No', 'Yes'])
print("Generated Figure: Open Source")
print("### Finished Figure Generation ###")