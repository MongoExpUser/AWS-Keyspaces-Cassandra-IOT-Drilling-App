# ****************************************************************************************************************
# *                                                                                                              *
# *  Project:  IOT Drilling App                                                                                  *
# *                                                                                                              *
# *  Copyright © MongoExpUser. All Rights Reserved.                                                              *
# *                                                                                                              *
# *  1) The module implements DBClient() class for:                                                              *
# *     a) Connecting/disconnecting to Cassandra or Amazon Keyspaces service (DBaaS) using:                      *
# *        - Python driver for Apache Cassandra and service-specific credentials                                 *
# *      b) Running queries against Amazon Keyspaces service (DBaaS)                                             *
# *                                                                                                              *
# *  2) Note:                                                                                                    *
# *     a) Os:Ubuntu 20.04 LTS                                                                                   *
# *     b) Install Python version 3.8 as: sudo apt-get install python3.8                                         *
# *     c) Install dependent module, boto3 as: sudo python3.8 -m pip install boto3                               *
# *     d) Install python cassandra-driver as: sudo python3.8 -m pip install cassandra-driver                    *
# *                                                                                                              *     
# *  3) AWS documentation link: https://docs.aws.amazon.com/keyspaces/latest/devguide/using_python_driver.html   *
# *                                                                                                              *
# ****************************************************************************************************************

import sys
from os import getcwd
from json import load
from os.path import join
from pprint import pprint
from json import dumps, loads
from datetime import datetime
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
from random import random, randint, uniform
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster, BatchStatement
from logging import getLogger, StreamHandler, Formatter
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED


class DBClient():
    """
    A class for connecting to and quering databses:
    """
  
    def __init__(self):
        print()
        print("Initiating Query Engine.")

    def separator(self):
        print("------------------------------------------------------------------")
        
    def log_messages(self):
        log = getLogger()
        log.setLevel('INFO')
        stream_handler = StreamHandler()
        stream_handler.setFormatter(Formatter("{}{}{}{}".format("%(asctime)s ", "[%(levelname)s] ",  "%(name)s : ", "%(message)s") ))
        log.addHandler(stream_handler)
        return log

    def connect_db(self, connection_options=None):
        port = connection_options.get("port")
        endpoint = connection_options.get("endpoint")
        username = connection_options.get("credentials").get("username")
        password = connection_options.get("credentials").get("password")
        ssl_certificate_path = connection_options.get("ssl_certificate_path")
    
        if connection_options:
            try:
                ssl_context = SSLContext(PROTOCOL_TLSv1_2)
                ssl_context.load_verify_locations(ssl_certificate_path)
                ssl_context.verify_mode = CERT_REQUIRED
                auth_provider = PlainTextAuthProvider(username=username, password=password)
                cluster = Cluster([endpoint], ssl_context=ssl_context, auth_provider=auth_provider, port=port)
                connection = cluster.connect()
                print()
                print("Connected to Amazon Keyspaces at ", connection_options.get("endpoint"))
                return connection
            except(Exception) as connection_error:
              print(connection_error)
              
    def load_json_file_to_dict(self, file_path=None):
        if file_path:
            with open(join(getcwd(), file_path)) as file:
                return load(file)

    def load_cql_file_to_string(self, file_path=None):
        if file_path:
            with open(file_path, 'r') as file:
                return file.read()
    
    def connection_options(self, options_file_path=None):
        conn_options = self.load_json_file_to_dict(file_path=options_file_path)
        return {
            "port" : conn_options.get('port'),
            "endpoint" : conn_options.get('endpoint'),
            "credentials" : conn_options.get("credentials"),
            "ssl_certificate_path" : conn_options.get('ssl_certificate_path'),
        }
                
    def list_of_queries(self, list_of_query_files_path=None):
        query_list = []
        if list_of_query_files_path:
            for file_path in list_of_query_files_path:
                query = self.load_cql_file_to_string(file_path=file_path)
                query_list.append(SimpleStatement(query , consistency_level=ConsistencyLevel.LOCAL_QUORUM))
            return query_list

    def view_query_result(self, query_result=None, view=None):
        for index, row in enumerate(query_result):
            self.separator()
            print("Item/Row -", index+1, ":")
            self.separator()
            pprint(list(row))
            
    def run_query(self, connect_db=None, list_of_queries=None, view_query=None, view_result=None):
        try:
            count = 0
            for query in list_of_queries:
                count = count + 1
                query_result = connect_db.execute(query)
                if view_query:
                    print()
                    print("-------------- Query No. ", count, " starts. --------------")
                    print(query)
                    print()
                    print("-------------- Query No. ", count, " ends.   --------------")
                    print()
                if query_result and view_result:
                    self.view_query_result(query_result=query_result)
        except(Exception) as query_error:
            print(query_error)
            return
        finally:
            self.log_messages().info("{}{}{}".format("A total number of ", count, " queries successfully executed."))
        
def main():
    # 0. define common variables
    view_query = True
    view_result = True
    redirect_stdout_to_file = False
    db_client = DBClient()
    output_file_path = "db_output_details.json"
    options_file_path = "keyspaces_connection_options.json"
    if redirect_stdout_to_file:
        #print to console or to output_filename, in append ('a') mode
        print("Writing output to file in the CWD")
        sys.stdout = open(output_file_path , 'a')
    # 2. connect and run query/queries
    db_client.separator()
    file_path_one = 'dml_insert.cql'
    file_path_two = 'dml_select.cql'
    list_of_query_files_path = [file_path_one, file_path_two]
    connection_options = db_client.connection_options(options_file_path=options_file_path)
    connect_db = db_client.connect_db(connection_options=connection_options)
    list_of_queries = db_client.list_of_queries(list_of_query_files_path=list_of_query_files_path)
    db_client.run_query(connect_db=connect_db, list_of_queries=list_of_queries, view_query=view_query, view_result=view_result)

if __name__ in ['__main__']:
    main()
