# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:04:40 2015

@author: erbanta
"""

import os
import numpy as np
import sys

# Generate mf6 well input for a rectangular well field using a time series.
# Need to generate input for well package, one entry for each well.
# Also generate a separate time-series file (copy of an original file)
# for each well.

startrow = 101
#endrow = 400
endrow = 105
startcol = 101
#endcol = 400
endcol = 105

numrows = endrow - startrow + 1
numcols = endcol - startcol + 1
maxbound = numrows * numcols

# make a time series list of pairs of time and rate.
ts = [("0.0", "0.0"), ("1.0", "0.0"), ("1001.0", "10000.0")]
welfil = open("test_ts_many_inject.well", "w")

# write initial lines of well file

# make a list of row numbers
rows = range(startrow, endrow + 1)
print "rows = ", rows

# make a list of column numbers
cols = range(startcol, endcol + 1)
print "cols = ", cols

basename = "rate"


# Make TS file and write line to well file for each well location
for row in rows:
    rowstr = "r" + str(row)
    for col in cols:
        colstr = "c" + str(col)
        tsname = basename + "_" + rowstr + "_" + colstr
        fname = tsname + ".ts"
        print "fname = ", fname
        #
        # open and build a time-series file
        tsfil = open(fname, "w")
        tsfil.write("BEGIN ATTRIBUTES\n")
        strg = "  NAME " + tsname + "\n"
        tsfil.write(strg)
        tsfil.write("  METHOD linear\n")
        tsfil.write("END ATTRIBUTES\n")
        tsfil.write("# time  rate\n")
        for tsr in ts:
            strg = tsr[0] + "  " + tsr[1] + "\n"
            tsfil.write(strg)
        tsfil.close()
        #
        # Write line to well input
        
#
# write final line of well file and close it
welfil.write("END PERIOD")
welfil.close()
   