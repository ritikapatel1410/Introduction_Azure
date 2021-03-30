'''
    @Author: Ritika Patidar
    @Date: 2021-03-28 12:15:10
    @Last Modified by: Ritika Patidar
    @Last Modified time: 2021-03-28 12:15:38  
    @Title : spark word count problem
'''
import sys
from pyspark import SparkContext, SparkConf

def main():
    """
        Description:
            this is define for word count problem
        Parameter:
            None
        Return:
            None
    """
    # create Spark context with necessary configuration
    sc = SparkContext("local","PySpark Word Count Exmaple")

    # read data from text file and split each line into words
    words = sc.textFile("sparktext.txt").flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

    # save the counts to output
    wordCounts.saveAsTextFile("/home/patidar/Desktop/spark/output/")

main()