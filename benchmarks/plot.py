#! python
from re import M, S
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
import sys
import matplotlib.ticker as ticker
import json
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.config as config
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
path="/home/atc23/presto_cuki/benchmarks/exp_res"

workerNum = 1
workers = ['ip_172_31_5_163_ap_east_1_compute_internal']
methods = ['Cuki','FC-512MB','FC-10GB']

# cuki
cuki_cache_file_path = path+"/Cuki/localCacheSpace_"

fig_path = path+"/figs/cache_hit_ratio.pdf"

def get_figsize(w, h, dpi=100):
    return [w * 0.3937008 * dpi / 100, h * 0.3937008 * dpi / 100]


def load_data2(file):
    data = numpy.array(json.load(open(file, 'r'))["data"]["result"][0]['values'])
    return data.astype(np.float_)


def transform_timestamp(data, _start_ts):
    for i in range(len(data)):
        data[i, 0] -= _start_ts
    return data


# load data
cache_data = {}
external_data = {}
for method in methods:
    print(method)
    cache_data[method] = []
    external_data[method] = []
    for worker in workers:
        cache_data[method].append(load_data2(path+"/"+method+"/read_cache_count_"+worker+"_step5.json"))
        external_data[method].append(load_data2(path+"/"+method+"/read_external_count_"+worker+"_step5.json"))


cuki_local_cache_data = []
for worker in workers:
    cuki_local_cache_data.append(load_data2(cuki_cache_file_path+worker+"_step5.json"))


# transform timestamp
for method in methods:
    min_cache_ts = cache_data[method][0][0, 0]
    for i in range(workerNum):
        if min_cache_ts > cache_data[method][i][0,0]:
            min_cache_ts = cache_data[method][i][0,0]
    for i in range(workerNum):
        cache_data[method][i] = transform_timestamp(cache_data[method][i], min_cache_ts)
        external_data[method][i] = transform_timestamp(external_data[method][i], min_cache_ts)

start_list = []
for data in cuki_local_cache_data:
    start_list.append(data[0,0])
start_ts = min(start_list)
for i in range(workerNum):
    cuki_local_cache_data[i] = transform_timestamp(cuki_local_cache_data[i], start_ts)



# dataframe
dataframes = {}
for method in methods:
    dataframes[method] = []
    for i in range(workerNum):
        dataframes[method].append(pd.DataFrame({'cache': cache_data[method][i][:, 1], 'external': external_data[method][i][:, 1]}))

cuki_size_list = []
for data in cuki_local_cache_data:
    df = pd.DataFrame(data, columns=['time', 'size'])
    df.set_index(['time'], inplace=True)
    df['size']= df['size'] / 1024 / 1024
    cuki_size_list.append(df['size'].max())



# normal configuration
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300
plt.rcParams["figure.figsize"] = config.small_figsize2()
plt.rc('axes',lw=config.axes_size)

fig, ax = plt.subplots(1, 1)

# compute cache hit rate
cache_hit_rate = {}
for method in methods:
    cache_hit_rate[method] = []
    for i in range(workerNum):
        cache_hit_rate[method].append(
                (dataframes[method][i]['cache'] / (dataframes[method][i]['cache'] + dataframes[method][i]['external'])).values[-1]
            )

# compute avg. cache hit rate
avg_cache_hit_rate = []
for method in methods:
    avg_cache_hit_rate.append(np.mean(cache_hit_rate[method]))

# comput the sum of cache used
total_cache_size = []
total_cache_size.append(np.sum(cuki_size_list))
total_cache_size.append(512*workerNum)
total_cache_size.append(10240*workerNum)


x = np.array([i for i in range(3)])
xticks_prop={'multialignment':'right'}
plt.xticks(ticks=x, labels=  ['Cuki\n(ours)', 'FC-512MB','FC-10GB'], **xticks_prop,**config.xyticks_dict)

bar_width = 0.65


ax.bar(x,avg_cache_hit_rate,bar_width, color=config.colors[0:4], edgecolor='#000000', linewidth=0.3)
plt.yticks([0.25,0.5,0.75,1],**config.xyticks_dict)
plt.xticks(rotation=16,**config.xyticks_dict)
ax.set_xlabel('Methods', **config.xylabel_fontdict)  
ax.set_ylabel('Avg. CHR', **config.xylabel_fontdict)
ax.set_ylim(0.25,1.2)
plt.grid(True, axis='y',linestyle='--', linewidth=0.5, alpha=0.5)
# 
ax2 = ax.twinx()
legend_properties = {'weight':'bold'}
plt.plot(x,total_cache_size, color='black', marker='o', markersize=5, linewidth=1, label='Cache Size')
ax2.set_ylabel('Cache Size (MB)', **config.xylabel_fontdict)
ax2.set_yscale('log',base=10)
plt.yticks([1,10,100,1000,10000,100000],**config.xyticks_dict)
ax2.legend(prop=legend_properties,framealpha=0.2)
ax2.set_ylim(10,10**5)

plt.savefig(fig_path, dpi=300, bbox_inches='tight')
print(fig_path)
