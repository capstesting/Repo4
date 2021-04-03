from time import sleep
import sys
from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass


class TestBootstrapProgress(BaseClass):
    def test_bootstrap_progress(self):
        try:
            self.log = self.getLogger()
            self.adv = po_advancedPage(self.driver,self.log)
            self.adv.advanced()
            self.adv.list_item("Bootstrap Download Progress bar")
            sleep(3)
            self.driver.find_element_by_xpath('//button[@id="cricle-btn"]').click()
            self.log.info("Started the download")
            self.status = 0
            for i in range(25):
                self.progress = self.driver.find_element_by_xpath('//*[@id="circle"]/div/div[1]').text
                if self.progress == "100%":
                    self.status = 1
                    self.log.info("Download is complete")
                    break
                else:
                    self.log.info("Download progress: " + self.progress)
                    sleep(1)

            if self.status == 1:
                self.log.info("Closing program")
            else:
                self.log.error("Download incomplete")
                self.log.error(self.driver.find_element_by_xpath('//*[@id="circle"]/div/div[1]').text)
                assert False

        except:
            self.log.error(sys.exc_info())
            assert False
