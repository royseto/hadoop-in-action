#!/bin/bash

HADOOP_HOME=/usr/local/Cellar/hadoop/1.0.3
HS_JAR=$HADOOP_HOME/libexec/contrib/streaming/hadoop-streaming-1.0.3.jar

hadoop jar $HS_JAR \
-input patent/cite75_99.txt \
-output output \
-mapper 'scripts/RandomSample.py 10' \
-file scripts/RandomSample.py 
-D mapred.reduce.tasks=1
