from pages.base_page import BasePage
from pages.locators import sale_page_locators as sale
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_menu(self, text, locator):
        header_title = self.page.locator(locator).first
        expect(header_title).to_have_text(text)

    def check_women_deals(self, text):
        women_deal_title = self.page.locator(sale.women_deals_locator)
        expect(women_deal_title).to_have_text(text)

    def check_men_deals(self, text):
        men_deal_title = self.page.locator(sale.men_deals_locator)
        expect(men_deal_title).to_have_text(text)

    def check_gear_deals(self, text):
        gear_deal_title = self.page.locator(sale.gear_deals_locator)
        expect(gear_deal_title).to_have_text(text)

    def check_women_menu_sweaters(self, text):
        self.check_menu(text, sale.women_hoodies_locator)

    def check_women_menu_jackets(self, text):
        self.check_menu(text, sale.women_jackets_locator)

    def check_women_menu_pants(self, text):
        self.check_menu(text, sale.women_pants_locator)

    def check_women_menu_shorts(self, text):
        self.check_menu(text, sale.women_shorts_locator)

    def check_hoodies_deal(self, text):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator(sale.women_hoodies_locator).first.click()
        header_text = self.page.locator(sale.h1_locator)
        expect(header_text).to_have_text(text)
