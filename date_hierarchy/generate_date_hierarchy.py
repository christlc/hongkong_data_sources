import pandas as pd
import numpy as np

START_YEAR = 2007
END_YEAR = pd.datetime.today()

def main():
    df = pd.DataFrame()
    df['Day'] = pd.date_range(str(START_YEAR), str(END_YEAR))
    df['Month'] = df.Day.map(lambda x: "%d-%02d" % (x.year, x.month))
    df['Quarter'] = df.Day.map(lambda x: "%d Q%d" % (x.year, x.quarter))
    df['Year'] = df.Day.map(lambda x: str(x.year))
    dow_lookup = ['1 Monday', '2 Tuesday', '3 Wednesday', '4 Thursday', '5 Friday', '6 Saturday', '7 Sunday']
    df['Day_of_Week'] = df.Day.map(lambda x: x.dayofweek).map(lambda x: dow_lookup[x])
    return df

    # Add Holiday data
    holiday_df = pd.read_csv('output/holiday.csv', parse_dates=['Date'], infer_datetime_format=True)
    holiday_df['is_HK_Holiday'] = 'Yes'
    df = df.merge(holiday_df[['Date', 'Holiday_Description', 'is_HK_Holiday']], left_on='Day', right_on='Date', how='left')
    df = df.drop('Date', 1)
    df['is_HK_Holiday'] = df['is_HK_Holiday'].fillna('No')
    df['Holiday_Description'] = df['Holiday_Description'].fillna('')
    df.to_csv('output/date_hierarchy.py')


if __name__ == '__main__':
    main()
