import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'aminaflow':556.9075,'flotation1':250.3695,'flotation2':249.472,'flotation3':250.472,'flotation4':405.9865,'flotation5':408.896,'flotation7':406.447,"%iron"=66.07,})
print(r.json())
