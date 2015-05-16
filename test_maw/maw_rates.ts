# The ATTRIBUTES block is required.
# Number of names on NAME line indicates 
#     number of time series to be created.
# NAME must precede METHOD (or METHODS).
# Either METHOD or METHODS must be specified, but not both.
# If METHOD is specified, all time series in file
#     share the same method (either LINEAR or STEPWISE).
# IF METHODS is specified, a method is specified for each time series.
#
BEGIN ATTRIBUTES
  NAME     mawq1    mawq2
  METHODS  linear   stepwise
END ATTRIBUTES
#   time   mawq1   mawq2
     0.0  -1707.  -2767.
    30.0  -1707.  -2737.
