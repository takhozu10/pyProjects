import requests
import json

app_info = {
    'name': 'Takuro Hozumi',
    'preferred name': 'Tak Hozumi',
    'email': 'thozumi.10@gmail.com',
    'resume': 'https://www.dropbox.com/s/ukmliso3tlrmcbm/Resume_Dec2021v1.pdf?dl=0',
    'phone': '614-352-1138',
    'job_id': 'b2d47344-cf07-476d-a16a-7674bcf60cb0',
    'github': 'https://github.com/takhozu10',
    'linkedin': 'https://www.linkedin.com/in/tak-hozumi-13581714/',
    'location': 'Lewis Center, Ohio',
    'favorite_candy': 'Kit Kat',
    'superpower': 'FinTech Fan / Credit Card Maestro'
}
json_data = json.dumps(app_info)
submit = requests.post(url='https://contact.plaid.com/jobs', data=json_data, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
print(submit.text)
