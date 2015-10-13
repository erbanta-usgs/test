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
 0.0    108.1  113.0  
 1.0    108.2  113.5 
 2.0    109.5  114.0 
 3.0    111.4  114.8 
 4.0    110.3  115.0  
 6.0    109.2  115.1 
 9.0    108.2  114.4  
11.0    108.1  113.5  
366.0   108.1  113.5
