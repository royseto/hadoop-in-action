#!/bin/bash

HADOOP_HOME=/usr/local/Cellar/hadoop/1.0.3
HS_JAR=$HADOOP_HOME/libexec/contrib/streaming/hadoop-streaming-1.0.3.jar

hadoop jar $HS_JAR \
-input logfiles/apache1.splunk.com/access_combined.log \
-output output \
-mapper 'scripts/CountHourlyHits.py' \
-file scripts/CountHourlyHits.py \
-reducer aggregate
