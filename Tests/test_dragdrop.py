from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from PageObject.po_advancedPage import po_advancedPage
from Utitlities.BaseClass import BaseClass
import sys


class TestDragDrop(BaseClass):
    def test_dragdrop(self):
        try:
            self.log = self.getLogger()
            self.adv = po_advancedPage(self.driver, self.log)
            self.adv.advanced()
            self.adv.list_item("Drag and Drop")
            sleep(2)
            self.action = ActionChains(self.driver)
            self.drag1 = self.driver.find_element_by_xpath('//*[@id="todrag"]/span[1]')
            self.drag2 = self.driver.find_element_by_xpath('//*[@id="todrag"]/span[2]')
            self.destination = self.driver.find_element_by_xpath('//div[@class="w50 moveleft"]/div[@id="mydropzone"]')
            self.action.drag_and_drop(self.drag1, self.destination).perform()
            self.action.drag_and_drop(self.drag2, self.destination).perform()

            self.dropped = self.driver.find_elements_by_xpath('div[@id="droppedlist"]/span')
            self.log.info(len(self.dropped))
            for i in self.dropped:
                self.name = self.dropped.text
                if self.name == "Draggable 1":
                    self.log.info("Draggable 1 is dropped correctly")
                elif self.name == "Draggable 2":
                    self.log.info("Draggable 2 is dropped correctly")
                else:
                    self.log.error("Not working")
                    assert False

        except:
            self.log.error(sys.exc_info())
            assert False
