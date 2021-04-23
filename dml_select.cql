-- dml - selecting/reading timeseries.drilling data
SELECT  tvd_ft, md_ft, inc_deg, azim_deg,
        dogleg_deg_per_100ft, dtemp_deg_c, shock_g,
        caliper_hole_size_inches, gr_api, deep_resistivity_ohm_m
FROM timeseries.drilling
LIMIT 10;
