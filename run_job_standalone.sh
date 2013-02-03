#!/bin/bash

hadoop jar MyJob.jar MyJob data/cite75_99.txt patout
hadoop jar MyJob.jar CitationHistogram patout/part-00000 histogram
