from .. hk_data_sources.date_hierarchy import generate_date_hierarchy as gen_date_hier
from .. hk_data_sources.date_hierarchy import hk_holiday_scraper as holiday_scraper


def test_get_years_holidays():
    # TODO better tests
    df = holiday_scraper.get_years_holiday(2007, 2008)
    assert df.shape == (17, 5)


def test_get_date_hierarchy():
    df = gen_date_hier.get_date_hierarchy(start_year=2007, end_year=2008)
    #print df
    assert df.shape == (365, 7)
