from unittest import TestCase
from unittest.mock import patch

from lesson11.some import (
    external_function,
    some_important_fn,
)


class OurMockTestCase(TestCase):

    def test_some_important_fn(self):

        with patch('lesson11.some.external_function') as mock:
            mock.return_value = 7
            result = some_important_fn(10, 25)
            mock.assert_called_once_with(30)
            self.assertEqual(result, 7)
