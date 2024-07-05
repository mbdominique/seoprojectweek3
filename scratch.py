from unittest.mock import Mock

newMockObject = Mock()

newMockObject.return_value = False
newMockObject.side_effect = KeyError
newMockObject.call_count = 3

newMockObject()