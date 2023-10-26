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

def record_matches_fips(record, areas):
    """
    Predicate that takes a QCEW record and dictionary of FIPS areas and
    decides whether the record contains information about a FIPS area in
    the dictionary
    """
    if get_fips(record) in areas:
        return True


def record_is_all_industries(record):
    """
    Predicate that takes a QCEW record and decides whether the record
    contains information about all industries under all types of
    ownership throughout the entire economy
    """
    if record[2].strip("\"") == "10" and record[1].strip("\"") == "0":
        return True


def record_is_software_industry(record):
    """
    Predicate that takes a QCEW record and decides whether the record
    contains information about privately owned software publishing firms
    """
    if record[2].strip("\"") == "513210" and record[1].strip("\"") == "5":
        return True


def get_fips(record):
    """
    Extracts a FIPS area code from a QCEW record
    """
    return record[0].strip("\"")


def get_estabs(record):
    """
    Extracts the annual average of quarterly establishment counts for a
    given year from a QCEW record
    """
    return int(record[8].strip("\""))

def get_emplvl(record):
    """
    Extracts the annual average of monthly employment levels for a given
    year from a QCEW record
    """
    return int(record[9].strip("\""))


def get_wages(record):
    """
    Extracts the sum of the four quarterly total wage levels for a given
    year from a QCEW record
    """
    return int(record[10].strip("\""))

