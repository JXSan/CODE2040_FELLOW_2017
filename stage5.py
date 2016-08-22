import requests, datetime
#Jonathan Sanchez - CODE2040 Fellow 2017 Applicant
#Stage 5 - The Dating Game

#API Token in the form of JSON
api_token = '37d4156cbcfc15b43886dbff56d75e9d'

#CODE2040 Endpoint
endpoint = 'http://challenge.code2040.org/api/dating'

#CODE2040 Validate Endpoint
v_endpoint = 'http://challenge.code2040.org/api/dating/validate'

#Create a JSON Dictionary with my Token
json_token = {'token': api_token}

#I will now run the 'send' function to send my Token to the Endpoint
json_dictionary = requests.post(endpoint, json_token)

datestamp = json_dictionary.json()['datestamp']

interval = json_dictionary.json()['interval']

print(datestamp)

#split the datestamp into serperate variables corresponding to the datestamp format
year = datestamp[0:4]
month = datestamp[5:7]
day = datestamp[8:10]
hour = datestamp[11:13]
minute = datestamp[14:16]
second = datestamp[17:19]

#Create a datetime object
date = datetime.datetime(int(year), int(month),  int(day),  int(hour),  int(minute),  int(second))

#Create the new time with the updated number of seconds
new_time = date + datetime.timedelta(seconds=interval)

#Turn the new time into an ISO format
time = new_time.isoformat() + "Z"

returning_token = {
    'token': api_token,
    'datestamp': time
}

#Post back to HQ ;D
final = requests.post(v_endpoint, json=returning_token)

#Did I get it right? HECK YEAH!
print(final.text)
