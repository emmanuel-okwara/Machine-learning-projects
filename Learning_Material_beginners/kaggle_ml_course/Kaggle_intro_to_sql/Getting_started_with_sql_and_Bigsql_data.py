# import google.cloud
from google.cloud import bigquery as bg

# Introduction 
    # Structured Query Language , or SQL, is the programming language used with databases, 
    # and it is an important skill for any data scientist
    # To use Bigquery we will import the python package below
    
        # The first step in the workflow is to create a Client object 
        # This is what we will use for retreving data from  the BigQuery Database
client = bg.Client()
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

