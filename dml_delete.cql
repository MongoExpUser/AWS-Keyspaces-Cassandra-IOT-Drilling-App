-- dml - sample delete - - timeseries.drilling
DELETE 
  mud_flow_rate_gpm FROM timeseries.drilling
WHERE 
  id = now() 
AND 
  date_utc = toDate(now());
