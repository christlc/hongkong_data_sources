import pandas as pd
import time
import requests
from StringIO import StringIO
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_year_holiday(year, sleep_seconds=5):
    # Sleep to scrape responsibly
    time.sleep(sleep_seconds)
    logger.info("Scraping %i" % year)
    # Link
    url = 'http://www.gov.hk/en/about/abouthk/holiday/%s.htm' % year
    response = requests.get(url, headers=headers)
    df = pd.read_html(StringIO(response.content), 'Every Sunday')[0]
    df.columns = ['Holiday_Description', 'Date', 'Day_of_Week']
    df['Year'] = year
    # remove 'Every Sunday'
    df = df[df['Holiday_Description']<>'Every Sunday'].copy()
    df['String_Date'] = df['Date'] + df['Year'].map(str)
    df['Date'] = df['String_Date'].map(lambda x: datetime.strptime(x, '%d %B%Y'))
    return df


def get_years_holiday(from_year, to_year):
    output = [get_year_holiday(i) for i in range(from_year, to_year)]
    df = pd.concat(output)
    return df


if __name__=='__main__':
    df = get_years_holiday(2007, 2017)
    print(df)
    df.to_csv(os.path.join('output', 'holiday.csv'), encoding='utf8')
