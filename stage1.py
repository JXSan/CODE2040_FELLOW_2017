import requests
#Jonathan Sanchez - CODE2040 Fellow 2017 Applicant
#Stage 1 - Registration

#API Token in the form of JSON
api_token = '37d4156cbcfc15b43886dbff56d75e9d'

#Registration Endpoint
registration_url = 'http://challenge.code2040.org/api/register'

#GitHub URL
github_url = 'https://github.com/JXSan/CODE2040_FELLOW_2017'

#Create a JSON Dictionary with my Token and GitHub URL
json_token = {'token': api_token, 'github': github_url}

#I will now run the 'send' function to send my GitHub URL to the Registration Endpoint
print(requests.post(registration_url, json_token))
