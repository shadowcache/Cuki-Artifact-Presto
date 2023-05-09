#!/bin/bash
set +ex
PRESTO_HOME="/home/atc23/presto_cuki/presto"
PRESTO="/home/atc23/presto_cuki/presto-cli/target/presto-cli-0.266-SNAPSHOT-executable.jar"
PRESTO_SERVER="/home/atc23/presto_cuki/presto-server/target/presto-server-0.266-SNAPSHOT/presto-server-0.266-SNAPSHOT/bin/launcher"
SQL_PATH="/home/atc23/presto_cuki/benchmarks/sql_scripts/tpcds-sqls"
PRESTO_CONFIG_PATH=/home/atc23/presto_cuki/etc

MAX_SQL_NUM=5
OPS=1

# ${PRESTO}  --server localhost:8881 --catalog hive --schema tpcds10 -f sigmod21-queries/query_99.sql > /dev/null
bash /home/atc23/presto_cuki/benchmarks/restart.sh
# wait for server start
sleep 30s

start_tick=$(date +%s)
echo -e "start timestamp ${start_tick}"

for (( i=0; i < $MAX_SQL_NUM; i++ )); do
  echo "ops ${i}"
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_7.sql > /dev/null &
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_53.sql > /dev/null &
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_68.sql > /dev/null &
  wait
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_30.sql > /dev/null &
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_73.sql > /dev/null & 
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_57.sql > /dev/null & 
  wait 
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_22.sql > /dev/null & 
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_46.sql > /dev/null & 
  ${PRESTO} --server localhost:8080 --catalog hive --schema s3tpcds10 -f ${SQL_PATH}/query_25.sql > /dev/null & 
  wait
done
 
end_tick=$(date +%s)

echo -e "${start_tick},${end_tick}"