import json
from playwright.sync_api import expect, Page, Request, Route


def test_modify_and_check_title(page: Page):
    def handle_request(route: Route, request: Request):
        test_url = 'https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat'
        if test_url in request.url:
            response = route.fetch()
            body = response.json()
            print('body', body['body'])
            body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
            route.fulfill(
                status=response.status,
                headers=response.headers,
                body=json.dumps(body)
            )
        else:
            route.continue_()

    page.route("**/*", handle_request)
    page.goto("https://www.apple.com/shop/buy-iphone", wait_until="load", timeout=60000)
    page.get_by_role("heading", name="iPhone 15 Pro & iPhone 15 Pro").click()
    expect(page.get_by_role("heading", name="яблокофон 15 про", exact=True)).to_be_visible()
