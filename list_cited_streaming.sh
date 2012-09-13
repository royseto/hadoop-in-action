#!/bin/bash

hadoop jar /usr/local/Cellar/hadoop/1.0.3/libexec/contrib/streaming/hadoop-streaming-1.0.3.jar \
-input patent/cite75_99.txt \
-output output \
-mapper 'cut -f 2 -d ,' \
-reducer 'uniq'
