import requests
#Jonathan Sanchez - CODE2040 Fellow 2017 Applicant
#Stage 2 - Reverse a string

#API Token in the form of JSON
api_token = '37d4156cbcfc15b43886dbff56d75e9d'

#CODE2040 Endpoint
endpoint = 'http://challenge.code2040.org/api/reverse'

#CODE2040 Validate Endpoint
v_endpoint = 'http://challenge.code2040.org/api/reverse/validate'

#Create a JSON Dictionary with my Token
json_token = {'token': api_token}

#I will now run the 'send' function to send my Token to the Endpoint
string = requests.post(endpoint, json_token)

#Reverse the string
new_string = str(string.text[::-1])

#Create a returning JSON Dictionary
returning_token = {'token': api_token, 'string': new_string}

#I will now POST my JSON to the VALIDATE server
print(requests.post(v_endpoint, returning_token))
