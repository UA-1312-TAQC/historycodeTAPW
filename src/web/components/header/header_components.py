from playwright.sync_api import Locator

from src.web.base import BaseComponent


class HeaderComponents(BaseComponent):
    def __init__(self, locator):
        super().__init__(locator)
        self._logo = None

    def get_logo(self)->Locator:
        if self._logo is None:
            self._logo = self.locator.locator('div.logoContainer')
        return self._logo
