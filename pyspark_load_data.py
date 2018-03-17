import datetime
import logging

from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType

NUM_DAYS = 1
END_DATE = datetime.date(2017, 10, 1)
DATA_PREFIX = "s3a://247machinelearning-curated/kinesis_analytics/{date.year}/{date.month:02d}/{date.day:02d}/*"


def split_json_lines(bigline):
    split_line = bigline.split('}{')
    all_lines = []
    for s in split_line:
        all_lines.append('{' + s + '}')
    print("Returning {} lines".format(len(all_lines)))
    return all_lines


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    spark = SparkSession \
        .builder \
        .appName("ReadInData") \
        .getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("WARN")
    logger.setLevel(logging.INFO)

    logger.info("Reading in kinesis data")
    schemaString = (
        "pathRoot userAgent referrer timeStamp userStatus"
        " contentKey siteKey authorKey publishedDate userId")
    schema = StructType(
        [StructField(field_name, StringType(), True)
         for field_name in schemaString.split()]
    )
    userdata_df = spark.createDataFrame([], schema)
    for day in range(0, NUM_DAYS):
        logger.info("Reading in data from %d days ago", day)
        date = END_DATE - datetime.timedelta(days=day)
        raw_text_rdd = sc.textFile(DATA_PREFIX.format(date=date))
        raw_text_rdd.coalesce(300)
        split_text_rdd = raw_text_rdd.flatMap(split_json_lines)
        tmp_df = spark\
            .read\
            .json(split_text_rdd)
        userdata_df = userdata_df.union(tmp_df)
        tmp_df.unpersist()
        raw_text_rdd.unpersist()
        split_text_rdd.unpersist()

    userdata_df.repartition(250).alias('userdata')
    userdata_df.cache()
    logger.info("Done reading in data")