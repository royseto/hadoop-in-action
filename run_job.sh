#!/bin/bash

hadoop jar MyJob.jar MyJob patent/cite75_99.txt patout
hadoop jar MyJob.jar CitationHistogram patout/part-00000 histogram
