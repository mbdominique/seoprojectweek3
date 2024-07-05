from unittest.mock import patch
import unittest
from is_weekday import get_famous_birthdays
from requests.exceptions import Timeout

class TestIsWeekday(unittest.TestCase):

    def test_get_famous_birthdays_timeout(self):
        with patch('is_weekday.requests') as mock_requests: #Patch mock with path name as variable_name
            mock_requests.get.side_effect = Timeout #Set the timeout side effect
            with self.assertRaises(Timeout):
                get_famous_birthdays()
            
if __name__ == '__main__':
    unittest.main()