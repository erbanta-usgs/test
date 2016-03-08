# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:04:40 2015

@author: erbanta
"""

#import os
#import numpy as np
import sys

args = sys.argv
numargs = len(args) - 1
if numargs < 5:
    print "Error: Need args (startrow endrow startcol endcol Q)"
    exit()
#
startrow = int(args[1])
endrow = int(args[2])
startcol = int(args[3])
endcol = int(args[4])
Q = float(args[5])

# Generate mf6 well input for a rectangular well field using a time series.
# Need to generate input for well package, one entry for each well.
# Also generate a separate time-series file (copy of an original file)
# for each well.

if Q < 0.0:
    mode = "pump"
else:
    mode = "inject"

numrows = endrow - startrow + 1
numcols = endcol - startcol + 1
maxbound = numrows * numcols

# make a time series list of pairs of time and rate.
Qd3 = Q / 3.0
ts = [(0.0, 0.0), (1.0, 0.0), (500.0, Qd3), (1001.0, Q)]

# write initial lines of well file

# make a list of row numbers
rows = range(startrow, endrow + 1)
#print "rows = ", rows

# make a list of column numbers
cols = range(startcol, endcol + 1)
#print "cols = ", cols

basename = mode + "_Q"

# make an empty list of time-series file names, and one of time-series names
tsfiles = []
tsnames = []

# populate the lists and write the time-series files.
for row in rows:
    rowstr = "r" + str(row)
    for col in cols:
        colstr = "c" + str(col)
        tsname = basename + "_" + rowstr + "_" + colstr
        print "time series: " + tsname
        # add tsname to list of time series
        tsnames.append(tsname)
        #
        # open and build a time-series file
        fname = tsname + ".ts"
        tsfile = open(fname, "w")
        tsfile.write("BEGIN ATTRIBUTES\n")
        strg = "  NAME " + tsname + "\n"
        tsfile.write(strg)
        tsfile.write("  METHOD linear\n")
        tsfile.write("END ATTRIBUTES\n")
        tsfile.write("# time  rate\n")
        for tsr in ts:
            strg = str(tsr[0]) + "  " + str(tsr[1]) + "\n"
            tsfile.write(strg)
        # add ts file name to list of ts files then close the file
        tsfiles.append(tsfile.name)
        tsfile.close()
#
# write the well file
name = "test_ts_many_" + mode + ".wel"
welfil = open(name, "w")
#
# write OPTIONS block
welfil.write("BEGIN OPTIONS\n")
strg = "  PACKAGENAME '" + mode + " Wells'\n"
welfil.write(strg)
for fn in tsfiles:
    strg = "  TimeSeriesFile " + fn + "\n"
    welfil.write(strg)
welfil.write("END OPTIONS\n\n")
#
# write DIMENSIONS block
welfil.write("BEGIN DIMENSIONS\n")
strg = "  MAXBOUND " + str(maxbound) + "\n"
welfil.write(strg)
welfil.write("END DIMENSIONS\n\n")
#
# write PERIOD block
welfil.write("BEGIN PERIOD 2\n")
#
# write line to well file for each well location
i = 0
for row in rows:
    for col in cols:
        strg = "  1  " + str(row) + "  " + str(col) + "  " + tsnames[i] + "\n"
        welfil.write(strg)
        i = i + 1
#
# write final line of well file and close it
welfil.write("END PERIOD\n")
welfil.close()

print "\nWrote file: " + welfil.name
print "Normal termination of " + args[0] + "\n"
   