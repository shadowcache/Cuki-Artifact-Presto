import json
import requests
import datetime
import pandas as pd
import os
url="http://localhost:9090/api/v1/query_range?query="
presto_url="http://localhost:8080/v1/query/"
step="5"
slaves=["ip_172_31_5_163_ap_east_1_compute_internal"]




# SHADOW
# com_facebook_alluxio_Client_CacheShadowCacheBytesHit_slave017_Count/com_facebook_alluxio_Client_CacheShadowCacheBytesRead_slave017_Count

# LOCAL
# com_facebook_alluxio_Client_CacheBytesReadCache_presto_worker_Count
# com_facebook_alluxio_Client_CacheBytesReadExternal_presto_worker_Count

# dump json
# import json  
# numbers = [2, 3, 5, 7, 11, 13] #存储内容种类多样，可以任意类型
# filename = 'numbers.json'  #文件路径   一般文件对象类型为json文件
# with open(filename, 'w') as f_obj:#打开模式为可写
# 	json.dump(numbers, f_obj)  #存储文件

# com_facebook_alluxio_Client_CacheBytesReadCache_slave017_FiveMinuteRate
# com_facebook_alluxio_Client_CacheShadowCacheBytesHit_slave017_Count/com_facebook_alluxio_Client_CacheShadowCacheBytesRead_slave017_Count&start=1661928731&end=1661932331&step=1
def to_ms(t):
    print(pd.to_timedelta("1ms").total_seconds())


def get_all(start,end,prefix):
    # get throughput
    for slave in slaves:
        read_cache = "com_facebook_alluxio_Client_CacheBytesReadCache_" + slave + "_FiveMinuteRate"
        read_external = "com_facebook_alluxio_Client_CacheBytesReadExternal_"  + slave + "_FiveMinuteRate"
        req = url + read_cache + "+%2B+" + read_external + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/throughput_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)
    
    for slave in slaves:
        read_cache = "com_facebook_alluxio_Client_CacheBytesReadCache_" + slave + "_OneMinuteRate"
        read_external = "com_facebook_alluxio_Client_CacheBytesReadExternal_"  + slave + "_OneMinuteRate"
        req = url + read_cache + "+%2B+" + read_external + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/throughput_oneminute_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)

    # get cache_read_count
    for slave in slaves:
        read_cache = "com_facebook_alluxio_Client_CacheBytesReadCache_" + slave + "_Count"
        req = url + read_cache + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/read_cache_count_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)
    
    for slave in slaves:
        read_external = "com_facebook_alluxio_Client_CacheBytesReadExternal_"  + slave + "_Count"
        req = url + read_external + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/read_external_count_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)

    for slave in slaves:
        hit_rate = "com_facebook_alluxio_Client_CacheHitRate_"  + slave + "_Value"
        req = url + hit_rate + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/hit_rate_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)

    for slave in slaves:
        shadowCacheSpace = "com_facebook_alluxio_Client_CacheShadowCacheBytes_" + slave + "_Count"
        req = url + shadowCacheSpace + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/shadowCacheSpace_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)

    for slave in slaves:
        usedSpace = "com_facebook_alluxio_Client_CacheSpaceUsed_" + slave + "_Value"
        avaSpace = "com_facebook_alluxio_Client_CacheSpaceAvailable_" + slave + "_Value"
        req = url + usedSpace + "+%2B+" + avaSpace + "&start=" + start + "&end=" + end + "&step=" + step
        ret = requests.get(req).json()
        filename = prefix + "/localCacheSpace_" + slave + "_step" + step + ".json"
        with open(filename, 'w') as f_obj:
            json.dump(ret, f_obj)


tpcds_res=pd.read_csv("/home/atc23/presto_cuki/benchmarks/exp_res/tpcds.csv")
for index, row in tpcds_res.iterrows():
    method = row['Method']
    start = str(row['start'])
    end = str(row['end'])
    prefix = "/home/atc23/presto_cuki/benchmarks/exp_res/" + method
    print(prefix)
    if not os.path.exists(prefix):
        os.mkdir(prefix)
    get_all(start,end,prefix)