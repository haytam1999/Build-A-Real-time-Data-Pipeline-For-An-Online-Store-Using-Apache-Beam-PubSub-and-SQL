# Build-A-Real-time-Data-Pipeline-For-An-Online-Store-Using-Apache-Beam-PubSub-and-SQL

This project uses GCP pub/sub and dataflow to create a realtime data pipeline which ingest data from an online store created using dash. 

1) Tools used: 

	-GCP Pub/Sub- is a messaging service provided by Google Cloud Platform that enables 
				  asynchronous communication between different applications and services. 
	
	-GCP Dataflow- is a fully-managed cloud service provided by Google Cloud Platform for building data processing pipelines. 
	
	-Apache Beam- is an open-source, programming model for batch and streaming data processing. 
				  It provides a way to write data processing pipelines.
				  
	-GCP Cloud SQL- is a fully-managed relational database service. 
				    It allows users to create, manage, and scale relational databases in the cloud with ease.
					
	-Data Studio- is a free web-based data visualization and reporting tool provided by Google.
	
	
2) Data Source:

The data will be uploaded from an online store.

3) Schema:

Here is the schema I followed to build the pipeline:

![alt text](https://github.com/haytam1999/Build-A-Real-time-Data-Pipeline-For-An-Online-Store-Using-Apache-Beam-PubSub-and-SQL/blob/master/Schema.png?raw=true)

4) Scripts:

*online_store_app.py: dash script to create the online store application.
	-dash is a tool created by Plotly to quickly build a web application using different prebuild UI components.

*publish_data_to_pubsub_topic.py: publishes data from the online store into the Pub/Sub topic.

*pipeline_config.py: this file contains all the configuration like Pub/Sub subscriber details, service account key path, 
					 MySQL DB connection details, and table details.
					 
*mainPipeline.py: In this pipeline script, we are reading data from the Pub/Sub, unnesting the data, 
				  and storing the final data in a relational database.
