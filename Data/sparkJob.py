from __future__ import print_function
import sys
import findspark
findspark.init("/home/ubuntu/spark-2.1.1-bin-hadoop2.7")
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SparkSession


def getSparkSessionInstance(sparkConf):
    if ('sparkSessionSingletonInstance' not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession\
            .builder\
            .config(conf=sparkConf)\
            .getOrCreate()
    return globals()['sparkSessionSingletonInstance']


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sparkJob.py <hostname> <port> ", file=sys.stderr)
        sys.exit(-1)
    host, port = sys.argv[1:]
    sc = SparkContext("local[2]","Popular Word Finder")
    ssc = StreamingContext(sc, 30)
    lines = ssc.socketTextStream(host, int(port))
    words = lines.flatMap(lambda line: line.split(" "))
    def process(time, rdd):
        print("========= %s =========" % str(time))
        try:
            spark = getSparkSessionInstance(rdd.context.getConf())

            rowRdd = rdd.map(lambda w: Row(word=w))
            wordsDataFrame = spark.createDataFrame(rowRdd)
            wordsDataFrame.createOrReplaceTempView("words")
            wordCountsDataFrame = \
                spark.sql("select word, count(*) as total from words group by word")
            wordCountsDataFrame.show()
            wordCountsDataFrame.write.csv('./csvs/')
        except:
            pass

    words.foreachRDD(process)
    ssc.start()
    ssc.awaitTermination()
