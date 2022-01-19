import requests
import json

app_info = {
    'name': 'Takuro Hozumi',
    'preferred name': 'Tak Hozumi',
    'resume': 'https://www.dropbox.com/s/ukmliso3tlrmcbm/Resume_Dec2021v1.pdf?dl=0',
    'linkedin': 'https://www.linkedin.com/in/tak-hozumi-13581714/',
    'location': 'Lewis Center, Ohio',
    'favorite candy': 'Kit Kat',
    'superpower': 'FinTech Fan / Credit Card Maestro'
}
json_data = json.dumps(app_info)
submit = requests.post(url='https://contact.plaid.com/jobs', data=json_data, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
print(submit.text)
