import sys
from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass
from time import sleep


class TestTableFilter(BaseClass):
    def test_table_filter(self):
        try:
            self.log = self.getLogger()
            self.adv = po_advancedPage(self.driver, self.log)
            self.adv.advanced()
            self.adv.list_item("Table Filter ")
            sleep(2)
            self.driver.find_element_by_xpath('//button[@class="btn btn-success btn-filter"]').click()
            sleep(2)

            self.record = self.driver.find_elements_by_xpath('//table[@class="table table-filter"]/tbody/tr[@data-status="pagado"]')
            self.log.info(str(len(self.record)) + " record(s) found")
            for i in self.record:
                self.row = i.find_element_by_xpath('td[3]/div/div/h4[@class="title"]/span')
                if self.row.text != "(Green)":
                    self.log.critical(
                        "The filter is not working as the record for " + self.row.text + " is also present")
                    assert False
                else:
                    self.log.info("This record is fine")

        except:
            self.log.error(sys.exc_info())
            assert False
