#!/bin/bash

HADOOP_HOME=/usr/local/Cellar/hadoop/1.0.3
HS_JAR=$HADOOP_HOME/libexec/contrib/streaming/hadoop-streaming-1.0.3.jar

hadoop jar $HS_JAR \
-input patent/apat63_99.txt \
-output output \
-mapper 'scripts/AttributeCount.py 1' \
-file 'scripts/AttributeCount.py' \
-reducer aggregate
