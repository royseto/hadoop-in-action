#!/bin/bash

javac -classpath /usr/local/Cellar/hadoop/1.0.3/libexec/hadoop-core-1.0.3.jar -d classes \
src/MyJob.java
jar -cvf MyJob.jar -C classes/ .
