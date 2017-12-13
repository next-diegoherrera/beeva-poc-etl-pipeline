import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "superhero-database", table_name = "superhero_datasets")

def changeType(data):
if "iving" in data["alive"]:
  data["alive"] = True
elif "eceased" in data["alive"]:
  data["alive"] = False

if data["appearances"] is None:
  data["appearances"] = 0

return data

mapped_dyF =  Map.apply(frame = datasource0, f = changeType)

applymapping2 = ApplyMapping.apply(frame = mapped_dyF, mappings = [("name", "string", "name", "string"), ("id", "string", "id", "string"), ("align", "string", "align", "string"), ("eye", "string", "eye", "string"), ("hair", "string", "hair", "string"), ("sex", "string", "sex", "string"), ("alive", "string", "alive", "string"), ("appearances", "string", "appearances", "string"), ("year", "string", "year", "string"), ("page_id", "long", "page_id", "long"), ("urlslug", "string", "urlslug", "string"), ("gsm", "string", "gsm", "string"), ("first_appearance", "string", "first_appearance", "string")], transformation_ctx = "applymapping1")

datasink2 = glueContext.write_dynamic_frame.from_catalog(frame = applymapping2, database = "superhero-data", table_name = "superhero", transformation_ctx = "datasink2")

job.commit()
