import requests
import json

app_info = {
    'name': '',
    'email': '',
    'resume': '',
    'phone': '',
    'job_id': '',
    'github': 'https://github.com/takhozu10',
    'twitter': 'N/A',
    'website': 'N/A',
    'location': '',
    'favorite_candy': '',
    'superpower': ''
}
json_data = json.dumps(app_info)
submit = requests.post(url='https://contact.plaid.com/jobs', data=json_data, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
print(submit.text)
