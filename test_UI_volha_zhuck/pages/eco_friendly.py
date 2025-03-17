from pages.base_page import BasePage
from pages.locators import eco_page_locators as loc
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def add_to_cart_eco(self, text):
        self.page.reload()
        self.page.wait_for_load_state("domcontentloaded")
        item = self.page.locator(loc.ana_shorts_locator)
        expect(item).to_be_visible(timeout=10000)
        add_to_cart = self.page.locator(loc.add_to_cart_locator).first
        item.hover()
        add_to_cart.click()
        product_title_locator = loc.ana_short_product_title_locator
        element = self.page.locator(product_title_locator)
        expect(element).to_have_text(text)

    def check_material_eco(self, text):
        self.page.reload()
        self.page.wait_for_load_state("domcontentloaded")
        option = self.page.locator(loc.material_menu_locator)
        option.click()
        spandex_option = loc.spandex_locator
        menu_element = self.page.locator(spandex_option)
        menu_element.click()
        product_element_locator = loc.fiona_shorts_locator
        element = self.page.locator(product_element_locator)
        expect(element).to_have_text(text)

    def wish_list(self, text):
        self.page.reload()
        self.page.wait_for_load_state("domcontentloaded")
        item = self.page.locator(loc.ana_shorts_locator)
        add_to_wish_list = self.page.locator(loc.add_to_wish_list).first
        item.hover()
        add_to_wish_list.click()
        customer_login = loc.customer_login_locator
        element = self.page.locator(customer_login)
        expect(element).to_have_text(text)
