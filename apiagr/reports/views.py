from django.shortcuts import render
# noinspection PyUnresolvedReferences
import xml.etree.ElementTree as ET
import requests

# Create your views here.


def index(request):

    url = "http://tcbuild1dk1.dk.sitecore.net/app/rest/agents"

    headers = {
        'Authorization': "Basic dnY6U2NwdzIwMzg=",
        'Cache-Control': "no-cache",
        'Postman-Token': "8a98c596-f647-46d6-8e82-24b3bb061938"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    root = ET.fromstring(response.text)
    param = []
    for child in root:
        mas = []
        print(child.get('id'))
        print(child.get('name'))
        print(child.get('webUrl'))
        mas.append(child.get('id'))
        mas.append(child.get('name'))
        mas.append(child.get('webUrl'))
        param.append(mas)

    return render(request, 'reports/index.html', {'list': param})

