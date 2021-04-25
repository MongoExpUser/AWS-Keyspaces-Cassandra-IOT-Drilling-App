--  ddl - create timeseries keyspace
CREATE KEYSPACE IF NOT EXISTS timeseriesTwo
  WITH REPLICATION = {'class': 'SingleRegionStrategy'}
    AND TAGS = {'Creator': 'creator@domain.com', 'Name': 'org-iot-prod-us-east-1-timeseries'};
