[![Build Status](https://travis-ci.org/christlc/hongkong_data_sources.svg?branch=master)](https://travis-ci.org/christlc/hongkong_data_sources)
[![codecov](https://codecov.io/gh/christlc/hongkong_data_sources/branch/master/graph/badge.svg)](https://codecov.io/gh/christlc/hongkong_data_sources)
[![Readthedocs](https://readthedocs.org/projects/hongkong-data-sources/badge/?version=latest)](http://hongkong-data-sources.readthedocs.io/)

# A set of HK data available for use immediately

## Date hierarchy with holidays

The HK holiday is scraped from government website.

Get the Pandas dataframe via:

    df = date_hierarchy.get_date_hierarchy(start_year=START_YEAR, end_year=END_YEAR)

