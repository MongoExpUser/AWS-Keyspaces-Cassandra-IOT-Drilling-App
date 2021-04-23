-- drilling table
CREATE TABLE IF NOT EXISTS timeseries.drilling (
  -- id, date, time data
  id TIMEUUID,
  date_utc DATE,
  time_utc TIMESTAMP,
  -- drill string data from regular drilling operation (drill string-related)
  rop_fph DECIMAL,
  rpm_rpm DECIMAL,
  spp_psi DECIMAL,
  dwob_lb DECIMAL,
  swob_lb DECIMAL,
  tqr_lbft DECIMAL,
  bha_type TEXT,
  -- mud data from regular drilling operation (mud-related)
  mud_weight_sg DECIMAL,
  mud_plastic_visc_cp DECIMAL,
  mud_yield_point_lb_per_100ft_sq DECIMAL,
  mud_flow_rate_gpm DECIMAL,
  -- mwd/lwd data (measured or calculated) from downhole mwd/lwd tool measurements
  tvd_ft DECIMAL,
  md_ft DECIMAL,
  inc_deg DECIMAL,
  azim_deg DECIMAL,
  dogleg_deg_per_100ft DECIMAL,
  caliper_hole_size_inches DECIMAL,
  gr_api DECIMAL,
  deep_resistivity_ohm_m DECIMAL,
  shock_g DECIMAL,
  dtemp_deg_c DECIMAL,
  --  event data from mwd/lwd tool measurements and other sources
  is_vibration BOOLEAN,
  is_kick BOOLEAN,
  is_stuckpipe BOOLEAN,
  PRIMARY KEY (date_utc, id)
) WITH CUSTOM_PROPERTIES={'point_in_time_recovery': {'status': 'disabled'}}
  AND CLUSTERING ORDER BY (id DESC)
  AND TAGS = {'Creator': 'creator@domain.com', 'Name': 'org-iot-prod-us-east-1-drilling'};
  
