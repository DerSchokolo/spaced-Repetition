from classes import *
import json

json_data_deck = '''
[
    {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com"
    },
    {
        "name": "Jane Smith",
        "age": 25,
        "email": "jane@example.com"
    },
    {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice@example.com"
    }
]
'''

# Parse the JSON data into a list
data_list = json.loads(json_data)

# Create a list of Person objects
people = [Person(**data) for data in data_list]

