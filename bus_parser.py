import json

import requests

headers = {
	'eurogps.eu.sid': '2fb71a142c5f57ac10d71328a0ae5b312b3e092e21eb2dc5',
    'Origin': 'http://info.skopska.mk',
}

response = requests.get('http://info.skopska.mk:8080/rest-its/scheme/stops', headers=headers)
data = json.loads(response.text)

# data = json.loads(input(''))

output = {
	'type': 'FeatureCollection',
	'features': []
}

for elem in data:
	latitude =  elem['lat']
	longitude = elem['lon']
	name = elem['name'].capitalize()
	idf = elem['id']
	number = elem['number']
	alb_name = elem['translations'].get('al')

	if alb_name is not None:
		alb_name = alb_name.capitalize()


	obj = {
		'type': 'Feature',
		'geometry': {
			'type': 'Point',
			'coordinates': [longitude, latitude]
		},
		'properties': {
	    	'name': name,
	    	'id': idf,
	    	'number': number,
	    	'alb_name': alb_name
	  	}
	}

	output['features'].append(obj)


print(json.dumps(output, ensure_ascii=False))