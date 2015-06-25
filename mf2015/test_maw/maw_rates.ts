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
  METHODS  linear   linear
END ATTRIBUTES
#   time   mawq1   mawq2
     0.0  -1737.  -2767.
     1.0  -1735.  -2766.
     2.0  -1734.  -2764.
     3.0  -1733.  -2762.
     4.0  -1732.  -2760.
     5.0  -1731.  -2758.
     6.0  -1730.  -2756.
     7.0  -1729.  -2754.
     8.0  -1728.  -2752.
     9.0  -1727.  -2750.
    10.0  -1726.  -2748.
    11.0  -1725.  -2746.
    30.0  -1707.  -2737.
