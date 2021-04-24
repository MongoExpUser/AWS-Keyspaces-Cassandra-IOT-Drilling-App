--  dml - sample update - timeseries.drilling
UPDATE timeseries.drilling
SET
  bha_type = 'packed'
WHERE
  id = now()
AND
  date_utc = toDate(now());
