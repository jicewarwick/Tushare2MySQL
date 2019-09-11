import logging
import unittest

from AShareData.WindData import WindData
from AShareData.utils import prepare_engine

logging.basicConfig(format='%(asctime)s  %(name)s  %(levelname)s: %(message)s', level=logging.DEBUG)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        config_loc = 'config.json'
        self.wind_data = WindData(prepare_engine(config_loc))

    def test_get_industry_func(self):
        wind_code = '000019.SZ'
        start_date = '20161212'
        end_date = '20190905'
        provider = '中证'
        start_data = '软饮料'
        end_data = '食品经销商'
        print(self.wind_data._find_industry(wind_code, provider, start_date, start_data, end_date, end_data))

    def test_update_zz_industry(self):
        self.wind_data.update_industry('中证')

    def test_update_sw_industry(self):
        self.wind_data.update_industry('申万')

    def test_update_wind_industry(self):
        self.wind_data.update_industry('Wind')


if __name__ == '__main__':
    unittest.main()