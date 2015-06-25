# The ATTRIBUTES block is required.
# Number of names on NAME line indicates 
#     number of time series to be created.
# NAME must precede METHOD (or METHODS).
# Either METHOD or METHODS must be specified, but not both.
# If METHOD is specified, all time series in file
#     share the same method (either LINEAR or STEPWISE).
# IF METHODS is specified, a method is specified for each time series.
BEGIN ATTRIBUTES
  NAME river_stage_1 river_stage_2 river_stage_3
  METHOD linear
# or maybe: METHODS linear linear stepwise  
END ATTRIBUTES
# time  riv_1  riv_2  riv_3
 0.0    101.0  111.0  115.1
 1.0    101.0  111.5  115.6
 2.0    103.0  112.0  116.4
 3.0    105.0  112.8  116.5
 4.0    104.0  113.0  115.9
 6.0    103.0  113.1  115.7
 9.0    102.0  112.4  115.2
11.0    101.0  111.5  115.1
