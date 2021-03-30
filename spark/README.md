# Spark framwork
* word count problem

* install spark on ubuntu
 * Install Packages Required for Spark
   * Before downloading and setting up Spark, you need to install necessary dependencies. This step includes installing the following packages:
     * JDK
     * Scala
     * Git
   * Open a terminal window and run the following command to install all three packages at once:
     * sudo apt install default-jdk scala git -y
 * Download and Set Up Spark on Ubuntu   
   * Download Spark Archive and extract by following command 
     * wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
     * tar xvf spark-*
  
   * Finally, move the unpacked directory spark-3.0.1-bin-hadoop2.7 to the opt/spark directory
     * sudo mv spark-3.0.1-bin-hadoop2.7 /opt/spark
   
 * Configure Spark Environment
   * add these three lines to .profile
     * echo "export SPARK_HOME=/opt/spark" >> ~/.profile
     * echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
     * echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile
     
   * open file .profile file then add these three lines
     * export SPARK_HOME=/opt/spark
     * export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
     * export PYSPARK_PYTHON=/usr/bin/python3
   * finish adding the paths, load the .profile file in the command line by typing
     * source ~/.profile
     
 * Start Standalone Spark Master Server
   * Now that you have completed configuring your environment for Spark, you can start a master server
     * start-master.sh
   * To view the Spark Web user interface, open a web browser and enter the localhost IP address on port 8080.
     * http://127.0.0.1:8080/
     
 * Start Spark Slave Server (Start a Worker Process)
   * In this single-server, standalone setup, we will start one slave server along with the master server.To do so, run the following command in this format:
     * start-slave.sh spark://master:port
       The master in the command can be an IP or hostname
       
 * Test Python in Spark
   * pyspark
 
In the terminal, type
* Reference:
 * https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/
 * https://pythonexamples.org/pyspark-word-count-example/ 
