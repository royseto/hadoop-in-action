import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class CitationHistogram extends Configured implements Tool {
	
	public static class MapClass extends MapReduceBase
	implements Mapper<Text, Text, IntWritable, IntWritable> {
		
		private final static IntWritable uno = new IntWritable(1);
		private IntWritable citationCount = new IntWritable();
		
		public void map(Text key, Text value, 
		OutputCollector<IntWritable, IntWritable> output, 
		Reporter reporter) throws IOException {
		  citationCount.set(Integer.parseInt(value.toString()));
			output.collect(citationCount, uno);
		}
	}
	
	public static class Reduce extends MapReduceBase
	implements Reducer<IntWritable, IntWritable, IntWritable, IntWritable> {
		
		public void reduce(IntWritable key, Iterator<IntWritable> values,
		OutputCollector<IntWritable, IntWritable> output,
		Reporter reporter) throws IOException {
			int count = 0;
			while (values.hasNext()) {
				count += values.next().get();
			}
			output.collect(key, new IntWritable(count));
		}
	}
	
	public int run(String[] args) throws Exception {
		Configuration conf = getConf();
	
		JobConf job = new JobConf(conf, CitationHistogram.class);
	
		Path in = new Path(args[0]);
		Path out = new Path(args[1]);
		FileInputFormat.setInputPaths(job, in);
		FileOutputFormat.setOutputPath(job, out);
	
		job.setJobName("CitationHistogram");
		job.setMapperClass(MapClass.class);
    job.setReducerClass(Reduce.class);
    job.setInputFormat(KeyValueTextInputFormat.class);
    job.setOutputFormat(TextOutputFormat.class);
    job.setOutputKeyClass(IntWritable.class);
    job.setOutputValueClass(IntWritable.class);
    
    JobClient.runJob(job);
   
    return 0;
	}

  public static void main(String[] args) throws Exception {
	int res = ToolRunner.run(new Configuration(), new CitationHistogram(), args);
	
	System.exit(res);
  }
}
