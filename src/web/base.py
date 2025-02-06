from playwright.sync_api import (expect, Locator, Page)


class BasePage:
    def __init__(self, page: Page):
        self.page = page


class BaseComponent:
    def __init__(self, locator: Locator):
        self.locator = locator

    def wait_to_be_visible(self, element: Locator) -> Locator:
        element.scroll_into_view_if_needed()
        expect(element).to_be_visible()
        return element


class BaseElement(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
