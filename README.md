# AWS-Keyspaces-Cassandra-IOT-Drilling-App


### This repo contains source code for a real-time well data drilling application.
The application can be used to deliver real-time well drilling operation data into Amazon Keyspaces (for Apache Cassandra) for
subsequent use in AIML applications including (1) Anonamly Detections and (2) Classifications.


### The drilling operation could be any of the followings: </strong>
 1) Oil and gas drilling operation (For Shale, conventional, and heavy oil/bitumen reservoir)
 2) Water well drilling operation.
 3) Geothermal well drilling operation.
 
The data can be streamed by the application directly or through an intermediate file (.CSV) that is offloaded to S3 bucket at set intermittent interval.


### The source code files include:
1) <strong>keyspaces_drilling_cfn.yaml</strong> - AWS Cloud Formation IaC stack for: <br>
   a) Creating the NoSQL DBaaS (Amazon Keystore) and <br>
   b) Defining (ddl) the Data Model (keyspaces, tables and parametized unique tags) 
   
2) <strong>keyspaces_drilling.cql</strong> - Cassandra Query Language - CQL's DDL equivalent of of the keyspaces_drilling_cfn.yaml file.
   This can be used to define DBaaS via:<br>
   a) AWS Management Console's CQL Editor or <br>
   b) CQLSH (CSL Shell) using Amazon Keyspaces service-specific credentials.<br>
   
3) <strong>keyspaces_drlling_client.py</strong> - Main Python client application code for: <br>
   a) Connecting to the DBaaS <br>
   b) Quering (DML and DDL queries) DBaaS <br>
   
4) <strong>keyspaces_connection_options.json</strong> - json file for specifying all connection options, which include: <br>
    a) Amazon Keyspaces service-specific credentials <br>
    b) Connection port <br>
    c) The DBaaS endpoint <br>
    d) SSL certificate path <br>
   
5) <strong>dml_insert.cql</strong> - sample dml query for inserting data into the DBaaS.

6) <strong>dml_update.cql</strong> - sample dml query for updating data into the DBaaS.

7) <strong>dml_select.cql</strong> - sample dql query for selecting/reading data from the DBaaS.

 

### The repo is based on the following languages, frameworks, packages and database servers:
1) Python v3.8 - (https://www.python.org/downloads/release/python-380/)
2) Java 8 - Java-8-openjdk (https://openjdk.java.net/)
3) AWS SDK for Python - Boto3 (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
4) Python Driver for Apache Cassandra  (https://github.com/datastax/python-driver)
5) CQL Language Reference for Amazon Keyspaces (for Apache Cassandra) - (https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.html)
6) Amazon Keyspaces (for Apache Cassandra) - (https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html)
7) Apache Cassandra (includes CQLSH) - (https://cassandra.apache.org/)
<br> 

# License

Copyright © 2021 - present. MongoExpUser

Licensed under the MIT license.
