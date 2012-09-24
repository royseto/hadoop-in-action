#!/bin/bash

HADOOP_HOME=/usr/local/Cellar/hadoop/1.0.3
HS_JAR=$HADOOP_HOME/libexec/contrib/streaming/hadoop-streaming-1.0.3.jar

hadoop jar $HS_JAR \
-input input/InnerProduct/two_vectors3.txt \
-output output \
-mapper 'scripts/IdentityMapper.py' \
-reducer 'scripts/SparseVectorInnerProdReducer.py' \
-file 'scripts/IdentityMapper.py' \
-file 'scripts/SparseVectorInnerProdReducer.py' \
-jobconf mapred.reduce.tasks=1 \