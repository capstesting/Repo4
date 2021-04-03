from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass
import sys
from time import sleep

class TestDynamicData(BaseClass):
    def test_dynamicData(self):
        try:
            self.log=self.getLogger()
            self.adv=po_advancedPage(self.driver,self.log)
            self.adv.advanced()
            self.adv.list_item("Dynamic Data Loading")
            sleep(2)
            for i in range(5):
                self.driver.find_element_by_xpath('//button[@id="save"]').click()
                sleep(5)
                self.log.info(self.driver.find_element_by_xpath('//div[@id="loading"]').text)

        except:
            self.log.error(sys.exc_info())
            assert False