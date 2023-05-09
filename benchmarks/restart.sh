#!/bin/bash
set +ex

PRESTO_SERVER="/home/atc23/presto_cuki/presto-server/target/presto-server-0.266-SNAPSHOT/presto-server-0.266-SNAPSHOT/bin/launcher"
PRESTO_CONFIG_PATH=/home/atc23/presto_cuki/etc

#stop
${PRESTO_SERVER} --etc-dir=${PRESTO_CONFIG_PATH}  stop
sleep 10s


# clear cache
rm -rf /dev/shm/alluxioclient/LOCAL



#start
${PRESTO_SERVER} --etc-dir=${PRESTO_CONFIG_PATH}  start
#ssh  lisimian@slave026 "${PRESTO_SERVER} --etc-dir=${PRESTO_CONFIG_PATH} start"
#ssh  lisimian@slave028 "${PRESTO_SERVER} --etc-dir=${PRESTO_CONFIG_PATH} start"
