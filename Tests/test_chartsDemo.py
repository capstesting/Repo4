from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass
import sys
from time import sleep

class TestChartsDemo(BaseClass):
    def test_chart_demo(self):
        try:
            self.log=self.getLogger()
            self.adv = po_advancedPage(self.driver,self.log)
            self.adv.advanced()
            self.adv.list_item("Charts Demo")
            sleep(2)
            self.li=self.driver.find_elements_by_xpath('//*[@id="pie-chart-widget"]/div[3]/div[1]/ul/li')
            for i in self.li:
                self.log.info(i.text)

        except:
            self.log.error(sys.exc_info())
            assert False