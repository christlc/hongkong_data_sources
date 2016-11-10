import pandas as pd
import numpy as np
from hk_holiday_scraper import get_years_holiday

START_YEAR = 2007
END_YEAR = pd.datetime.today().year+1

def get_date_hierarchy(start_year=START_YEAR, end_year=END_YEAR):
    """

    :param start_year: cannot be before than 2007, default is 2007
    :param end_year: e.g. default is current year+1
    :return: date hierarchy matrix from start_year to end_year-1
    """
    df = pd.DataFrame()
    df['Day'] = pd.date_range(str(start_year), str(end_year), closed='left')
    df['Month'] = df.Day.map(lambda x: "%d-%02d" % (x.year, x.month))
    df['Quarter'] = df.Day.map(lambda x: "%d Q%d" % (x.year, x.quarter))
    df['Year'] = df.Day.map(lambda x: str(x.year))
    dow_lookup = ['1 Monday', '2 Tuesday', '3 Wednesday', '4 Thursday', '5 Friday', '6 Saturday', '7 Sunday']
    df['Day_of_Week'] = df.Day.map(lambda x: x.dayofweek).map(lambda x: dow_lookup[x])

    # Add Holiday data
    holiday_df = get_years_holiday(start_year, end_year+1) #pd.read_csv('output/holiday.csv', parse_dates=['Date'], infer_datetime_format=True)
    holiday_df['is_HK_Holiday'] = 'Yes'
    df = df.merge(holiday_df[['Date', 'Holiday_Description', 'is_HK_Holiday']], left_on='Day', right_on='Date', how='left')
    df = df.drop('Date', 1)
    df['is_HK_Holiday'] = df['is_HK_Holiday'].fillna('No')
    df['Holiday_Description'] = df['Holiday_Description'].fillna('')
    return df


if __name__ == '__main__':
    df = get_date_hierarchy()
    print(df)
    df.to_csv('output/date_hierarchy.py', encoding='utf8')