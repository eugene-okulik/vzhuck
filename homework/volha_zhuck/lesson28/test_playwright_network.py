from playwright.sync_api import Page, expect, Route
from time import sleep
import re
import json


def test__change_iphone_req(page: Page):

    def change_req(route: Route):
        url = route.request.url
        if "digital-mat" in url:
            response = route.fetch()
            jdata = response.json()
            body = jdata.get('body', {})
            items = body.get('digitalMat', [])
            for item in items:
                if 'productName' in item:
                    item['productName'] = 'яблокофон 16 про'
            for item in jdata["body"]["digitalMat"][0]["familyTypes"]:
                if 'productName' in item:
                    item['productName'] = 'яблокофон 16 про'
            route.fulfill(
                content_type="application/json",
                body=json.dumps(jdata)
            )
        else:
            route.continue_()
    page.route(re.compile(r'/api/digital-mat'), change_req)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone16 = page.locator(
        'h3.rf-hcard-content-title', has_text='iPhone 16 Pro'
    )
    iphone16.click()
    reqs = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(reqs).to_be_visible()
    expect(reqs).to_have_text('яблокофон 16 про')
    sleep(2)
