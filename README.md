# AWS-Keyspaces-Cassandra-IOT-Drilling-App

### This repo contains source code for a real-time well data drilling application.
The application can be used to deliver real-time well drilling operation data into Amazon Keyspaces (for Apache Cassandra) for
subsequent use in <strong><font>AIML applications</font></strong>, including:<br>

(1) <strong> Anonamly Detections</strong>. <br>
(2) <strong> Classifications</strong>. <br>

### The drilling operation could be any of the followings: 
 1) <strong>Oil</strong> and <strong>gas</strong> drilling operation (For shale, conventional, and heavy oil/bitumen reservoirs).
 2) <strong>Water</strong> well drilling operation.
 3) <strong>Geothermal</strong> well drilling operation for <strong>renewable energy</strong>.
 
The data can be streamed by the application directly or through an intermediate file (.CSV) that is offloaded to S3 bucket at set intermittent interval.


### The source code files include:
1) <strong>keyspaces_drlling_client.py</strong> - Main Python client application code for: <br>
   a) Connecting to the DBaaS. <br>
   b) Querying (DML, DQL and DDL queries) DBaaS. <br>
   
2) <strong>keyspaces_connection_options.json</strong> - json file for specifying all connection options, which include: <br>
    a) Amazon Keyspaces service-specific credentials. <br>
    b) Connection port. <br>
    c) The DBaaS endpoint. <br>
    d) SSL certificate path. <br>
   
3) <strong>keyspaces_drilling_cfn.yaml</strong> - AWS Cloud Formation IaC stack for: <br>
   a) Creating the NoSQL DBaaS (Amazon Keystore). <br>
   b) Defining (ddl) the Data Model (keyspaces, tables and parametized unique tags). 
   
4) <strong>ddl_timeseries_keyspace.cql</strong> and <strong>ddl_drilling_table.cql</strong> - Cassandra Query Language - CQL's DDL equivalent of of the <strong>keyspaces_drilling_cfn.yaml</strong> file.
   These can be used to define the DBaaS' keyspace and table via:<br>
   a) AWS Management Console's CQL Editor or <br>
   b) CQLSH (CSL Shell) using Amazon Keyspaces service-specific credentials.<br>
   
5) <strong>dml_insert.cql</strong> - sample dml for inserting data into the DBaaS.

6) <strong>dml_update.cql</strong> - sample dml for updating data on the DBaaS.

7) <strong>dml_delete.cql</strong> - sample dml for deleting data on the DBaaS.

8) <strong>dql_select.cql</strong> - sample dql for selecting data from the DBaaS.

9) <strong>ddl_alter.cql</strong> - sample ddl for altering table capacity units on the DBaaS.


### The repo is based on the following languages, frameworks, packages and database servers:
1) Python v3.8 - (https://www.python.org/downloads/release/python-380/)
2) Java 8 - Java-8-openjdk (https://openjdk.java.net/)
3) AWS SDK for Python - Boto3 (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
4) Python Driver for Apache Cassandra  (https://github.com/datastax/python-driver)
5) CQL Language Reference for Amazon Keyspaces (for Apache Cassandra) - (https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.html)
6) Amazon Keyspaces (for Apache Cassandra) - (https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html)
7) Apache Cassandra (includes CQLSH) - (https://cassandra.apache.org/)



# License

Copyright © 2015 - present. MongoExpUser

Licensed under the MIT license.
