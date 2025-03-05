from playwright.sync_api import Page, expect
from playwright.sync_api import BrowserContext


def test_qa_practice_ok(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda dialog: dialog.accept())
    button = page.locator('a.a-button', has_text='Click')
    button.click()
    reqs = page.locator('#result-text')
    expect(reqs).to_be_visible()
    expect(reqs).to_have_text('Ok')


def test_qa_practice_enabled(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.locator('a.a-button', has_text='Click')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value
    reqs = new_page.locator('#result-text')
    expect(reqs).to_be_visible()
    expect(reqs).to_have_text('I am a new page in a new tab')
    button = page.locator('a.a-button', has_text='Click')
    expect(button).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    button.wait_for(state='visible')
    expect(button).to_have_class('mt-4 text-danger btn btn-primary')
    button.click()
