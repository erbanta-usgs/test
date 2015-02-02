# The ATTRIBUTES block is required.
# Number of names on NAME line indicates number of time series to be created.
# NAMES is synonymous with NAME
# Either METHOD or METHODS must be specified, but not both.
# If METHOD is specified, all time series in file share the same method (either LINEAR or STEPWISE).
# IF METHODS is specified, a method is specified for each time series.
BEGIN ATTRIBUTES
  NAME river_stage_4 river_stage_5
  METHODS linear stepwise
END ATTRIBUTES
 0.0    104.0  113.0  
 1.0    104.1  113.5 
 2.0    105.5  114.0 
 3.0    107.4  114.8 
 4.0    106.3  115.0  
 6.0    105.2  115.1 
 9.0    104.1  114.4  
11.0    104.0  113.5  
366.0   104.0  113.5
