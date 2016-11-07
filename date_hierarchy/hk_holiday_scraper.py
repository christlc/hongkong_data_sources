import pandas as pd
import time
import requests
from StringIO import StringIO
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_year_holiday(year):
    # Sleep to scrape responsibly
    time.sleep(5)
    logger.info("Scraping %i" % year)
    # Link
    url = 'http://www.gov.hk/en/about/abouthk/holiday/%s.htm' % year
    response = requests.get(url, headers=headers)
    df = pd.read_html(StringIO(response.content), 'Every Sunday')[0]
    df.columns = ['Holiday_Description', 'Date', 'Day_of_Week']
    df['Year'] = year
    return df


if __name__=='__main__':
    output = [get_year_holiday(i) for i in range(2007, 2017)]
    df = pd.concat(output)
    # remove 'Every Sunday'
    df = df[df['Holiday_Description']<>'Every Sunday'].copy()
    df['String_Date'] = df['Date'] + df['Year'].map(str)
    df['Date'] = df['String_Date'].map(lambda x: datetime.strptime(x, '%d %B%Y'))
    print(df)
    df.to_csv(os.path.join('output', 'holiday.csv'), encoding='utf8')
