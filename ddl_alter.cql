-- dql - sample alter - timeseries.drilling
ALTER TABLE timeseries.drilling  
WITH custom_properties = {
  'capacity_mode': {
    'throughput_mode': 'PROVISIONED', 
    'read_capacity_units': 5, 
    'write_capacity_units': 5}
};
