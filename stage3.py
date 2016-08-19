import requests
#Jonathan Sanchez - CODE2040 Fellow 2017 Applicant
#Stage 3 - Needle in a haystack

#API Token in the form of JSON
api_token = '37d4156cbcfc15b43886dbff56d75e9d'

#CODE2040 Endpoint
endpoint = 'http://challenge.code2040.org/api/haystack'

#CODE2040 Validate Endpoint
v_endpoint = 'http://challenge.code2040.org/api/haystack/validate'

#Create a JSON Dictionary with my Token
json_token = {'token': api_token}

#I will now run the 'send' function to send my Token to the Endpoint
json_dictionary = requests.post(endpoint, json_token)

#Parse JSON
data = json_dictionary.json()

#Extract the haystack and needle from the JSON
haystack = data['haystack']
needle = data['needle']

#Single out the index (needle)
index = haystack.index(needle)

#Token to return to the server
returning_token = {'token': api_token, 'needle': index}
