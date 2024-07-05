from unittest.mock import Mock
import requests


requests = Mock()
requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

print(dir(requests))  # This shows us available methods to use with an object.
print(requests.get.assert_called())
print(requests.get.return_value())
print(requests.get.assert_called_with('https://pokeapi.co/api/v2/pokemon/pikachu'))
print(requests.method_calls)