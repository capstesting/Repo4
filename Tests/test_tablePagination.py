import sys
from time import sleep
from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass


class TestTablePagination(BaseClass):
    def test_table_pagination(self):
        try:
            self.log = self.getLogger()
            self.adv = po_advancedPage(self.driver, self.log)
            self.log.info("Advanced object is created")
            self.adv.advanced()
            self.adv.list_item("Table Pagination")
            self.count = 0
            while True:
                self.count += 1
                sleep(1)
                self.table = self.driver.find_elements_by_xpath(
                    '//tbody[@id="myTable"]/tr[@style="display: table-row;"]')
                self.length = len(self.table)
                if self.length <= 5:
                    self.log.info(self.length)
                    if self.driver.find_element_by_xpath('//a[@class="next_link"]').is_displayed():
                        self.driver.find_element_by_xpath('//a[@class="next_link"]').click()
                        self.log.info("Next button clicked.")
                    else:
                        self.log.info("Next button is not available and hence breaking the loop")
                        break

                else:
                    self.log.critical("There are more than 5 items: " + str(self.length))

        except:
            self.log.error(sys.exc_info())
            assert False
