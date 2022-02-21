from unittest import skip
from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10

class ItemValidationTest(FunctionalTest):
        
    @skip
    def test_cannot_add_empty_list_items(self):
        # E goes toThe home page and accidentally tries to submit 
        # an empty list item. She hits Enter on the empty input box

        # The homepage refreshes, and there is an error message saying 
        # that the list items cannot be blank

        # she tries again with some text, which now works.

        # Perversely, she now decides to submit another blank item

        # She receives a similar warning on the list page.

        # She can correct it by filling some text in
        self.fail('Write me!')


