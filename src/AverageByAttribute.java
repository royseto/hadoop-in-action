import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class AverageByAttribute extends Configured implements Tool {
	
	public static class MapClass extends MapReduceBase
	implements Mapper<LongWritable, Text, Text, Text> {

		public void map(LongWritable key, Text value, 
		OutputCollector<Text, Text> output,
		Reporter reporter) throws IOException {

			String fields[] = value.toString().split(",", -20);
			String country = fields[4];
			String numClaims = fields[8];
			if (numClaims.length() > 0 && !numClaims.startsWith("\"")) {
				output.collect(new Text(country),
				new Text(numClaims + ",1"));
			}
		}
	}

	public static class Reduce extends MapReduceBase
	implements Reducer<Text, Text, Text, DoubleWritable> {

		public void reduce(Text key, Iterator<Text> values, 
		OutputCollector<Text, DoubleWritable> output,
		Reporter reporter) throws IOException {

			double sum = 0;
			int count = 0;

			while (values.hasNext()) {
				String fields[] = values.next().toString().split(",");
				sum += Double.parseDouble(fields[0]);
				count += Integer.parseInt(fields[1]);
			}
			output.collect(key, new DoubleWritable(sum/count));
		}
	}

	public static class Combine extends MapReduceBase
	implements Reducer<Text, Text, Text, Text> {

		public void reduce(Text key, Iterator<Text> values,
		OutputCollector<Text, Text> output,
		Reporter reporter) throws IOException {

			double sum = 0;
			int count = 0;

			while (values.hasNext()) {
				String fields[] = values.next().toString().split(",");
				sum += Double.parseDouble(fields[0]);
				count += Integer.parseInt(fields[1]);
			}
			output.collect(key, new Text(sum + "," + count));
		}
	}

	public int run(String[] args) throws Exception {
		Configuration conf = getConf();
	
		JobConf job = new JobConf(conf, AverageByAttribute.class);
	
		Path in = new Path(args[0]);
		Path out = new Path(args[1]);
		FileInputFormat.setInputPaths(job, in);
		FileOutputFormat.setOutputPath(job, out);
	
		job.setJobName("AverageByAttribute");
		job.setMapperClass(MapClass.class);
		job.setCombinerClass(Combine.class);
		job.setReducerClass(Reduce.class);
    job.setInputFormat(TextInputFormat.class);
    job.setOutputFormat(TextOutputFormat.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);
    
    JobClient.runJob(job);
   
    return 0;
	}

  public static void main(String[] args) throws Exception {
	int res = ToolRunner.run(new Configuration(), new AverageByAttribute(), args);
	
	System.exit(res);
  }
	
}
