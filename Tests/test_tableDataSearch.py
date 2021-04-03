import sys
from time import sleep

from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass


class TestTableDataSearch(BaseClass):
    def test_table_data_search(self):
        try:
            self.log = self.getLogger()
            self.adv = po_advancedPage(self.driver, self.log)
            self.adv.advanced()
            self.adv.list_item("Table Data Search")

            # Test the task
            sleep(3)
            self.driver.find_element_by_xpath('//input[@id="task-table-filter"]').send_keys("Bug Fixing")
            self.log.info("Values sent to the input")
            self.result_items = self.driver.find_elements_by_xpath('//table[@id="task-table"]/tbody/tr')
            self.log.info(len(self.result_items))
            self.count=0
            for i in self.result_items:

                self.td = i.find_elements_by_xpath('td')
                if self.td[1].text == "Bug fixing" and i.is_displayed():
                    self.count+=1
                    self.log.info("The search is working fine.")
                    self.log.info("Details are: " + self.td[1].text + ", " + self.td[2].text)
            if self.count == 0:
                self.log.warning("No value found")
            else:
                self.log.info(str(self.count) + " value(s) found!")
        except:
            self.log.error(sys.exc_info())
            assert False
