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

from util import *


class IndustryData:
    """
    Contains statistics for a single industry.
    """
    def __init__(self):
        # Study the instructions and the unit tests to discover
        # the names and types of the attributes
        pass

    def add_record(self, record, areas):
        """
        Adds a record's data to the summary statistics.

        This method does not need to validate it its input;
        the record must be validated before this method is called.

        Parameters:
         - record: A record containing employment and wage data.
         - areas: A dictionary mapping FIPS area codes to human-friendly area titles.

        This method updates the following summary statistics:
         - Adds one to the total number of areas processed.
         - Calculates and accumulates the total annual wages.
         - Keeps track of the area with the maximum annual wages.
         - Calculates and accumulates the total number of establishments.
         - Keeps track of the area with the maximum number of establishments.
         - Calculates and accumulates the total employment level.
         - Keeps track of the area with the maximum employment level.
        """
        pass
