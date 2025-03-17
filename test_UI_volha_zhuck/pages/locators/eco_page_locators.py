ana_shorts_locator = """
(//div[@class='product-item-info'])[1]
"""
add_to_cart_locator = """
//button[
    @type='submit' and
    @title='Add to Cart' and
    contains(@class, 'tocart')
]
"""
ana_short_product_title_locator = """
//span[
    @class='base' and
    @data-ui-id='page-title-wrapper' and
    @itemprop='name'
]
"""
material_menu_locator = """
//div[@data-role='title' and contains(., 'Material')]
"""
spandex_locator = """
//li[@class='item']/a[text()[normalize-space()='Spandex']]
"""
fiona_shorts_locator = """
//a[
    @class='product-item-link' and
    normalize-space()='Fiona Fitness Short'
]
"""
add_to_wish_list = """
//a[@class='action towishlist' and @title='Add to Wish List']
"""
customer_login_locator = """
//span[@class='base' and contains(text(), 'Customer Login')]
"""
