import requests  # This will be patched in the test files
from datetime import datetime

def is_weekday():
    today = datetime.today()
    return(0 <= today.weekday() < 5)
    
def get_famous_birthdays():
    req = requests.get('http://localhost/api/famous_birthdays')
    if req.status_code == 200:
        return req.json()
    return None