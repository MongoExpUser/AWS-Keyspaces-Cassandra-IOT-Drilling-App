--  dml - sample select - timeseries.drilling
SELECT 
  date_utc, tvd_ft, 
  mud_weight_sg, mud_plastic_visc_cp, 
  mud_yield_point_lb_per_100ft_sq, 
  mud_flow_rate_gpm,
  md_ft, inc_deg, azim_deg, 
  dogleg_deg_per_100ft, 
  shock_g, dtemp_deg_c, 
  caliper_hole_size_inches, 
  gr_api, deep_resistivity_ohm_m 
FROM timeseries.drilling
LIMIT 5;
