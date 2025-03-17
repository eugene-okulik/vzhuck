from pages.locators import create_acc_locators as loc
from pages.base_page import BasePage
from playwright.sync_api import expect


class CreateNewCustomer(BasePage):

    def open_page(self):
        self.page.goto(
            'https://magento.softwaretestingboard.com/customer/account/create/'
            )

    def fill_create_account_form(
            self, firstname, lastname, email, password, password_confirmation
            ):
        firstname_field = self.page.locator(loc.firstname_field_loc)
        lastname_field = self.page.locator(loc.lastname_field_loc)
        email_field = self.page.locator(loc.email_field_loc)
        password_field = self.page.locator(loc.password_field_loc)
        password_confirmation_field = self.page.locator(
            loc.password_confirmation_field_loc
        )
        firstname_field.fill(firstname)
        lastname_field.fill(lastname)
        email_field.fill(email)
        password_field.fill(password)
        password_confirmation_field.fill(password_confirmation)
        button_create_acc = self.page.locator(
            loc.buttom_create_acc_loc
        )
        button_create_acc.click()

    def check_error_alert_invalid_email(self, text):
        error_locator = (
            loc.error_locator_loc
        )
        error_message = self.page.locator(error_locator)
        expect(error_message).to_have_text(text)

    def check_error_alert_wrong_confirm_password(self, text):
        error_locator = (
            loc.confirm_password_locator
        )
        error_message = self.page.locator(error_locator)
        expect(error_message).to_have_text(text)

    def check_page_header_is(self, text):
        header_title = self.page.locator(loc.header_loc)
        expect(header_title).to_have_text(text)

    def check_empty_field_firstname(self, text):
        error_locator = (
            loc.first_name_error_locator
        )
        error_message = self.page.locator(error_locator)
        expect(error_message).to_have_text(text)

    def check_empty_field_lasttname(self, text):
        error_locator = (
            loc.first_name_error_locator
        )
        error_message = self.page.locator(error_locator)
        expect(error_message).to_have_text(text)

    def check_required_empty_fields(self, validation_text, locator):
        error_message = self.page.locator(locator)
        expect(error_message).to_have_text(validation_text)

    def check_first_name_empty_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.first_name_error_locator
        )

    def check_last_name_empty_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.last_name_error_locator
        )

    def check_email_empty_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.email_error_locator
        )

    def check_password_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.password_error_locator
        )

    def check_confirm_password_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.confirm_password_error_locator
        )
