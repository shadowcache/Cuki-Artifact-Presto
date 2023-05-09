#!/bin/bash
PRESTO_CONFIG_PATH=/home/atc23/presto_cuki/etc
LOG_PATH=/home/atc23/presto_cuki/benchmarks/exp_res
echo "Method,start,end,cost" > ${LOG_PATH}/tpcds.csv
echo "" >  ${LOG_PATH}/tpcds.log

# FC-10GB
echo "[+] FC-10GB" >> ${LOG_PATH}/tpcds.log
MEM="10GB"
sed -i "s#^cache.alluxio.max-cache-size=.*#cache.alluxio.max-cache-size=${MEM}#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
sed -i "s#^cache.alluxio.cache-adaption-enabled=.*#cache.alluxio.cache-adaption-enabled=false#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
bash /home/atc23/presto_cuki/benchmarks/tpcds_s3_once.sh >> ${LOG_PATH}/tpcds.log
RES=$(tail -1 ${LOG_PATH}/tpcds.log)
echo -e "FC-10GB,${RES}" >> ${LOG_PATH}/tpcds.csv


# FC-512mb
echo "[+] FC-512MB" >> ${LOG_PATH}/tpcds.log
MEM="512MB"
sed -i "s#^cache.alluxio.max-cache-size=.*#cache.alluxio.max-cache-size=${MEM}#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
sed -i "s#^cache.alluxio.cache-adaption-enabled=.*#cache.alluxio.cache-adaption-enabled=false#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
bash /home/atc23/presto_cuki/benchmarks/tpcds_s3_once.sh >> ${LOG_PATH}/tpcds.log
RES=$(tail -1 ${LOG_PATH}/tpcds.log)
echo -e "FC-512MB,${RES}" >> ${LOG_PATH}/tpcds.csv

# CUKI
echo "[+] Cuki" >> ${LOG_PATH}/tpcds.log
sed -i "s#^cache.alluxio.shadow-cache-type=.*#cache.alluxio.shadow-cache-type=CLOCK_CUCKOO_FILTER#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
sed -i "s#^cache.alluxio.cache-adaption-enabled=.*#cache.alluxio.cache-adaption-enabled=true#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
sed -i "s#^cache.alluxio.shadow-cache-enabled=.*#cache.alluxio.shadow-cache-enabled=true#g"  ${PRESTO_CONFIG_PATH}/catalog/hive.properties
bash /home/atc23/presto_cuki/benchmarks/tpcds_s3_once.sh >> ${LOG_PATH}/tpcds.log
RES=$(tail -1 ${LOG_PATH}/tpcds.log)
echo -e "Cuki,${RES}" >> ${LOG_PATH}/tpcds.csv
