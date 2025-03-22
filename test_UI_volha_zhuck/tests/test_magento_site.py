# create account tests
def test_create_account_with_invalid_email(create_new_customer):
    create_new_customer.open_page()
    create_new_customer.fill_create_account_form(
        "Bob", "Marley", "bob", "1234567890Qw!", "1234567890Qw!"
    )
    create_new_customer.check_error_alert_invalid_email(
        'Please enter a valid email address (Ex: johndoe@domain.com).'
    )


def test_header_title_text(create_new_customer):
    create_new_customer.open_page()
    create_new_customer.check_page_header_is('Create New Customer Account')


def test_wrong_confirm_password(create_new_customer):
    create_new_customer.open_page()
    create_new_customer.fill_create_account_form(
        "Bob", "Marley", "bob@hj.vh", "1234567890Qw!", "1234567890Qw"
    )
    create_new_customer.check_error_alert_wrong_confirm_password(
        'Please enter the same value again.'
    )


def test_validation_messages_empty_fields(create_new_customer):
    validation_text = 'This is a required field.'
    create_new_customer.open_page()
    create_new_customer.fill_create_account_form(
        "", "", "", "", ""
    )
    create_new_customer.check_first_name_empty_validation_text(validation_text)
    create_new_customer.check_last_name_empty_validation_text(validation_text)
    create_new_customer.check_email_empty_validation_text(validation_text)
    create_new_customer.check_password_validation_text(validation_text)
    create_new_customer.check_confirm_password_validation_text(validation_text)


# Sales page tests
def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_women_deals("Women's Deals")
    sale_page.check_men_deals("Mens's Deals")
    sale_page.check_gear_deals("Gear Deals")


def test_women_menu_items(sale_page):
    sale_page.open_page()
    sale_page.check_women_menu_sweaters("Hoodies and Sweatshirts")
    sale_page.check_women_menu_jackets("Jackets")
    sale_page.check_women_menu_pants("Pants")
    sale_page.check_women_menu_shorts("Shorts")


def test_hoodies_deal(sale_page):
    sale_page.open_page()
    sale_page.check_hoodies_deal("Hoodies & Sweatshirts")


# eco friendly tests
def test_add_to_cart(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_to_cart_eco('Ana Running Short')


def test_product_page_opened(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.check_material_eco('Fiona Fitness Short')


def test_add_to_wish_list(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.wish_list('Customer Login')
