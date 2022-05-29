import os
import json
import requests

path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')

fileStream = open(path_to_json + '/headers.json')
headers = json.load(fileStream)

fileStream = open(path_to_json + '/datasource.json')
dataSourceData = json.load(fileStream)

response = requests.post('http://localhost:3000/api/datasources', headers=headers, json=dataSourceData)

fileStream = open(path_to_json + '/dashboard.json')
dashboardData = json.load(fileStream)
response = requests.post('http://localhost:3000/api/dashboards/db', headers=headers, json=dashboardData)

fileStream.close()