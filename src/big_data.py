#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

import sys
import time

from area_titles import area_titles_to_dict
from report import Report
from util import record_matches_fips, record_is_all_industries, record_is_software_industry


if len(sys.argv) == 1:
    print("Error: too few arguments. Directory name is required.")
    sys.exit(2)

print("Reading the databases...", file=sys.stderr)
before = time.time()

areas = area_titles_to_dict(sys.argv[1])
rpt = Report(2022)

file = open(sys.argv[1]+"/2022.annual.singlefile.csv")
file.readline()
for line in file:
    if record_matches_fips(line.split(","), areas):
        if record_is_all_industries(line.split(",")):
            rpt.all.add_record(line.split(","), areas)
        elif record_is_software_industry(line.split(",")):
            rpt.soft.add_record(line.split(","), areas)

file.close()





after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)


