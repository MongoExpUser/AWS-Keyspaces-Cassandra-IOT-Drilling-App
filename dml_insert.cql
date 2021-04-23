-- dml sample inserts with batch insert - timeseries.drilling
BEGIN UNLOGGED  BATCH
	INSERT INTO timeseries.drilling (
      id, date_utc, time_utc, -- id, date, time data
      rop_fph, rpm_rpm, spp_psi, dwob_lb, swob_lb, tqr_lbft, bha_type, -- drillstring data
      mud_weight_sg, mud_plastic_visc_cp, mud_yield_point_lb_per_100ft_sq, mud_flow_rate_gpm,  -- mud data
      tvd_ft, md_ft, inc_deg, azim_deg, dogleg_deg_per_100ft, caliper_hole_size_inches, gr_api, deep_resistivity_ohm_m, shock_g,  dtemp_deg_c, -- mwd/lwd data
      is_vibration, is_kick, is_stuckpipe -- event data
  )
	VALUES (
	  	now(), toDate(now()), toTimestamp(now()), -- id, date, time data
      35.01, 65.01, 235.03, 20000.40, 10000.40, 800.40, 'slick', -- drillstring data
      1.18, 18.01, 16, 98.14, -- mud data
      8000, 12000, 67.2, 110.5, 1.1, 6, 20, 303.3, 26, 102.86, -- mwd/lwd data
      false, false, false -- event
  );
APPLY BATCH;
