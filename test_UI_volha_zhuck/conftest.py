import pytest
from pages.sale_page import SalePage
from pages.create_new_customer import CreateNewCustomer
from pages.eco_friendly import EcoFriendlyPage


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def create_new_customer(page):
    return CreateNewCustomer(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendlyPage(page)
