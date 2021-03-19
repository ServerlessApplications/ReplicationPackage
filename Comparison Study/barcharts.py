import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
plt.rcParams.update({'font.size': 22})

#colormap = plt.get_cmap('Greys')
#mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=[colormap(k) for k in np.linspace(0.2, 1, 7)]) 

### Application type ###
labels = ['Us', 'SCS', 'GtST']
ops_means = [0.2, 0.31, 0.34]
batch_means = [0.23, 0.27, 0.68]
stream_means = [0.27, 0.21, 0.3]
API_means = [0.28, 0.46, 0.73]

width = 0.8
comp = 0.7

for i in range(0, len (labels)):
    sum = ops_means[i] + batch_means[i] + stream_means[i] + API_means[i]
    ops_means[i] = ops_means[i]/sum
    batch_means[i] = batch_means[i]/sum
    stream_means[i] = stream_means[i]/sum
    API_means[i] = API_means[i]/sum

height = (1 + 4 * 0.8) * comp + 1
fig, ax = plt.subplots(1, 1, figsize=(12, height))

ax.barh(labels, ops_means, width, label='Operations')
ax.barh(labels, batch_means, width, left=ops_means, label='Batch jobs')
ax.barh(labels, stream_means, width, left=(np.asarray(ops_means) + np.asarray(batch_means)), label='Stream/async')
ax.barh(labels, API_means, width, left=(np.asarray(ops_means) + np.asarray(batch_means) + np.asarray(stream_means)), label='API')


ax.set_xlabel('Relative share of applications/respondents')
ax.legend(ncol=2, loc='lower center', bbox_to_anchor=(0.5, 0.98), fontsize=22)

plt.xlim(0, 1)
plt.tight_layout()
plt.savefig('figures/comparison_application_type.pdf')
plt.close()


### Platform ###
labels = ['Us', 'SCS', 'OSS', 'GtST', 'CNCF']
aws_means = [0.8, 0.945337621, 0.75, 0.59, 0.69]
azure_means = [0.1, 0.138263666, 0.3, 0.25, 0.2]
private_means = [0.08, 0.083601286, 0, 0, 0]
ibm_means = [0.07, 0.009646302, 0.07, 0.05, 0.08]
google_means = [0.03, 0.102893891, 0.19, 0.15, 0.25]

for i in range(0, len (labels)):
    sum = aws_means[i] + azure_means[i] + private_means[i] + ibm_means[i] + google_means[i]
    aws_means[i] = aws_means[i]/sum
    azure_means[i] = azure_means[i]/sum
    private_means[i] = private_means[i]/sum
    ibm_means[i] = ibm_means[i]/sum
    google_means[i] = google_means[i]/sum

height = (1 + 5 * 0.8) * comp + 1
fig, ax = plt.subplots(1, 1, figsize=(12, height))

ax.barh(labels, aws_means, width, label='AWS')
ax.barh(labels, azure_means, width, left=aws_means, label='Azure')
ax.barh(labels, private_means, width, left=(np.asarray(aws_means) + np.asarray(azure_means)), label='Private Cloud')
ax.barh(labels, ibm_means, width, left=(np.asarray(aws_means) + np.asarray(azure_means) + np.asarray(private_means)), label='IBM')
ax.barh(labels, google_means, width, left=(np.asarray(aws_means) + np.asarray(azure_means) + np.asarray(private_means)+ np.asarray(ibm_means)), label='Google')


ax.set_xlabel('Relative share of applications/respondents')
ax.legend(ncol=3, loc='lower center', bbox_to_anchor=(0.5, 0.98), fontsize=22)

plt.xlim(0,1)
plt.tight_layout()
plt.savefig('figures/comparison_platform.pdf')
plt.close()


### Programming Languages ###
labels = ['Us', 'SCS', 'MMS', 'TSoS', 'GtST', 'FtLoS']
js_means = [0.32, 0.74, 0.71, 0.39, 0.62, 0.53]
py_means = [0.32, 0.46, 0.49, 0.47, 0.47, 0.36]
java_means = [0.09, 0.16, 0.30, 0.06, 0.33, 0.06]
c_means = [0.08, 0.02, 0, 0, 0.07, 0]
net_means = [0.06, 0.12, 0.09, 0.04, 0.27, 0.03]
go_means = [0.03, 0.13, 0, 0.005, 0.22, 0.02]
ruby_means = [0.01, 0.03, 0, 0.005, 0, 0]

for i in range(0, len (labels)):
    sum = js_means[i] + py_means[i] + java_means[i] + c_means[i] + net_means[i] + go_means[i] + ruby_means[i]
    js_means[i] = js_means[i]/sum
    py_means[i] = py_means[i]/sum
    java_means[i] = java_means[i]/sum
    c_means[i] = c_means[i]/sum
    net_means[i] = net_means[i]/sum
    go_means[i] = go_means[i]/sum
    ruby_means[i] = ruby_means[i]/sum

height = (1 + 6 * 0.8) * comp + 1
fig, ax = plt.subplots(1, 1, figsize=(12, height))

ax.barh(labels, js_means, width, label='JavaScript')
ax.barh(labels, py_means, width, left=js_means, label='Python')
ax.barh(labels, java_means, width, left=(np.asarray(js_means) + np.asarray(py_means)), label='Java')
ax.barh(labels, c_means, width, left=(np.asarray(js_means) + np.asarray(py_means) + np.asarray(java_means)), label='C/C++')
ax.barh(labels, net_means, width, left=(np.asarray(js_means) + np.asarray(py_means) + np.asarray(java_means)+ np.asarray(c_means)), label='C# / .NET')
ax.barh(labels, go_means, width, left=(np.asarray(js_means) + np.asarray(py_means) + np.asarray(java_means)+ np.asarray(c_means) + np.asarray(net_means)), label='Go')
ax.barh(labels, ruby_means, width, left=(np.asarray(js_means) + np.asarray(py_means) + np.asarray(java_means)+ np.asarray(c_means) + np.asarray(net_means) + np.asarray(go_means)), label='Ruby')


ax.set_xlabel('Relative share of applications/respondents')
ax.legend(ncol=4, loc='lower center', bbox_to_anchor=(0.5, 0.98), fontsize=22)

plt.xlim(0,1)
plt.tight_layout()
plt.savefig('figures/comparison_language.pdf')
plt.close()


### Motivation ###
labels = ['Us', 'SCS', 'MMS', 'OSS', 'GtST']
cost_means = [0.33, 0.357827476, 0.29, 0.59, 0.4]
scalability_means = [0.24, 0.364217252, 0.31, 0.57, 0.47]
performance_means = [0.13, 0.201277955, 0, 0, 0.18]
development_means = [0.09, 0.309904153, 0, 0.3, 0.41]
noops_means = [0.24, 0, 0.28, 0.56, 0]

for i in range(0, len (labels)):
    sum = cost_means[i] + scalability_means[i] + performance_means[i] + development_means[i] + noops_means[i]
    cost_means[i] = cost_means[i]/sum
    scalability_means[i] = scalability_means[i]/sum
    performance_means[i] = performance_means[i]/sum
    development_means[i] = development_means[i]/sum
    noops_means[i] = noops_means[i]/sum

height = (1 + 5 * 0.8) * comp + 1
fig, ax = plt.subplots(1, 1, figsize=(12, height))

ax.barh(labels, cost_means, width, label='Cost')
ax.barh(labels, scalability_means, width, left=cost_means, label='Scalability')
ax.barh(labels, performance_means, width, left=(np.asarray(cost_means) + np.asarray(scalability_means)), label='Performance')
ax.barh(labels, development_means, width, left=(np.asarray(cost_means) + np.asarray(scalability_means) + np.asarray(performance_means)), label='DevSpeed')
ax.barh(labels, noops_means, width, left=(np.asarray(cost_means) + np.asarray(scalability_means) + np.asarray(performance_means)+ np.asarray(development_means)), label='NoOps')


ax.set_xlabel('Relative share of applications/respondents')
ax.legend(ncol=3, loc='lower center', bbox_to_anchor=(0.5, 0.98), fontsize=22)

plt.xlim(0,1)
plt.tight_layout()
plt.savefig('figures/comparison_motivation.pdf')
plt.close()


### External Services ###
labels = ['API Routing', 'Database', 'Storage', 'Messaging', 'ML']
our_means = [0.18/0.99, 0.47/0.99, 0.61/0.99, 0.27/0.99, 0.04/0.99]
community_means = [0.3340356762, 0.47, 0.4162857741, 0.3407499612, 0.1023928457]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 4))
rects1 = ax.bar(x - width/2, our_means, width, label='Us', color='darkgrey')
rects2 = ax.bar(x + width/2, community_means, width, label='SCS', color='grey')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('applications/respondents [%]')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.tight_layout()
plt.savefig('figures/comparison_services.pdf')
plt.close()


### Trigger Types ###
labels = ['HTTP request', 'Cloud event', 'Scheduled']
our_means = [0.46/0.97, 0.39/0.97, 0.12/0.97]
wild_means = [0.6407, 0.3632, 0.2915]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 5))
rects1 = ax.bar(x - width/2, our_means, width, label='Us')
rects2 = ax.bar(x + width/2, wild_means, width, label='SitW')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('applications/respondents [%]')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.tight_layout()
plt.savefig('figures/comparison_triggers.pdf')
plt.close()



### Number of Functions ###
our_study = [1, 4, 1, 1, 2, 1, 7, 3, 1, 3, 2, 1, 1, 1, 2, 4, 4, 2, 3, 8, 2, 4, 9, 1, 1, 1, 5, 5, 1, 2, 24, 1, 1, 1, 3, 6, 3, 1, 2, 3, 2, 1, 1, 4, 3, 13, 5, 2, 1, 9, 1, 4, 8, 4, 4, 1, 3, 2, 2, 5, 2, 1, 2, 1, 170, 2, 3, 16, 10, 15, 10, 2]
fig, ax = plt.subplots(figsize=(12,5))
plt.hist(our_study, label="Us", bins=np.linspace(0.5, 200.5, 201), density=True, alpha = 0.5, linewidth=2, histtype='step', zorder=2)

mixed_method = []
for i in range(0, 35): 
    mixed_method.append(3)
for i in range(0, 29): 
    mixed_method.append(7)
for i in range(0, 20): 
    mixed_method.append(12)
plt.hist(mixed_method, label="MMS", bins=[0.5, 5.5, 10.5, 20.5], density=True, alpha=0.5, histtype='step', linewidth=2.5, zorder=1)

new_stack = []
for i in range(0, 103): 
    new_stack.append(1)
for i in range(0, 283): 
    new_stack.append(3)
for i in range(0, 217): 
    new_stack.append(7)
for i in range(0, 119): 
    new_stack.append(12)
plt.hist(new_stack, label="GtST", bins=[0.5, 1.5, 5.5, 10.5, 25.5], density=True, alpha=0.5, histtype='step', linewidth=2.5, zorder=1)

counts = [13094, 4197, 2143, 1248, 831, 557, 402, 294, 247, 186, 135, 116, 109, 88, 47, 59, 43, 61, 36, 33, 61]
sitw = []
for i in range (1, 22):
    for j in range(0, counts[i-1]):  
        sitw.append(i)
plt.hist(sitw, label="SitW", bins=np.linspace(0.5, 200.5, 201), density=True, alpha=0.5, histtype='step', linewidth=2.5, zorder=1)

handles, labels = ax.get_legend_handles_labels()
leg_entries = {}
for h, label in zip(handles, labels):
    leg_entries[label] = mpl.lines.Line2D([0], [0], color=h.get_facecolor()[:-1],
                                alpha=h.get_alpha(), lw=h.get_linewidth())
labels_sorted, lines = zip(*sorted(leg_entries.items()))
ax.legend(lines, labels_sorted, frameon=False)
plt.ylim([0, 0.55])
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=22)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], fontsize=22)
plt.xlim([0.5, 20.5])
plt.xlabel('Number of distinct functions', fontsize=22)
plt.ylabel('Probability density', fontsize=22)
plt.tight_layout()
plt.savefig('figures/comparison_number.pdf')
plt.close()
