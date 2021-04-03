from time import sleep

from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass
import sys

class TestProgress(BaseClass):
    def test_progress_bar(self):
        try:
            self.log=self.getLogger()
            self.adv=po_advancedPage(self.driver,self.log)
            self.adv.advanced()
            self.adv.list_item("JQuery Download Progress bars")
            sleep(2)
            self.driver.find_element_by_xpath('//button[text()="Start Download"]').click()
            sleep(10)
            if self.driver.find_element_by_xpath('//div[@class="progress-label"]').text == "Complete!":
                self.log.info("The download is complete.")
                self.driver.find_element_by_xpath('//button[text()="Close"]').click()
                self.log.info("Clicked on Close button")

            else:
                self.log.error("There was an issue with the download")
                assert False


        except:
            self.log.error(sys.exc_info())
            assert False