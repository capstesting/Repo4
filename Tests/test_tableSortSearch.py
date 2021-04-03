import sys

from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass
from time import sleep

class TestTableSort(BaseClass):
    def test_table_sort(self):
         try:
            self.log=self.getLogger()
            self.adv=po_advancedPage(self.driver,self.log)
            self.adv.advanced()
            self.adv.list_item("Table Sort & Search")
            sleep(3)
            self.driver.find_element_by_xpath('//select[@name="example_length"]/option[@value="100"]').click()
            sleep(2)
            self.sort = self.driver.find_element_by_xpath('//*[@id="example"]/thead/tr/th[1]')
            self.sort.click()
            self.log.info("Clicked on Sort")
            self.row=self.driver.find_elements_by_xpath('//table[@id="example"]/tbody/tr[@role="row"]')
            self.prev = 'Z'
            for i in self.row:
                self.name = i.find_element_by_xpath('td[1]').text
                if self.name[0]<=self.prev[0]:
                    self.log.info("Working fine. This name is: "+ self.name + " and previous name was: "+self.prev)
                    self.prev=self.name
                else:
                    self.log.error("Not working fine. This name is: "+ self.name + " and previous name was: "+self.prev)
                    assert False

         except:
             self.log.error(sys.exc_info())
             assert False