import requests
#Jonathan Sanchez - CODE2040 Fellow 2017 Applicant
#Stage 4 - Prefix

#API Token in the form of JSON
api_token = '37d4156cbcfc15b43886dbff56d75e9d'

#CODE2040 Endpoint
endpoint = 'http://challenge.code2040.org/api/prefix'

#CODE2040 Validate Endpoint
v_endpoint = 'http://challenge.code2040.org/api/prefix/validate'

#Create a JSON Dictionary with my Token
json_token = {'token': api_token}

#I will now run the 'send' function to send my Token to the Endpoint
json_dictionary = requests.post(endpoint, json_token)

#Extract the prefix and array from the JSON
prefix = dict(json_dictionary.json())["prefix"]
array = dict(json_dictionary.json())["array"]

result = []

for i in range(0, len(array)):
	if(array[i][0:len(prefix)] != prefix):
		result.append(str(array[i]))

#Token to return to the server
returning_token = {'token': api_token, 'array': result}

finish = requests.post(v_endpoint, returning_token)

print(finish.text)
