import org.apache.spark.{SparkContext, SparkConf}

/**
  * Created by Shah Rukh Khan on 31-Jan-2019.
  */
object Segmentation_ICP2 {

  def main(args: Array[String]) {

    System.setProperty("hadoop.home.dir","D:\\winutils");

    val sparkConf = new SparkConf().setAppName("SparkFirstChar").setMaster("local[*]")

    val sc=new SparkContext(sparkConf)
    val input=sc.textFile("input.txt")
    val splitted=input.flatMap(line=>{line.split(" ")}).groupBy(word=>word.charAt(0))
    splitted.foreach(println(_))

  }
}