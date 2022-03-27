import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth


USERNAME = input("Please enter your username: ")
PASSWORD = getpass("Please enter your password ")


MainUrl = "https://sandboxdnac.cisco.com"
authToken = "/dna/system/api/v1/auth/token"
VlanApi = "/dna/intent/api/v1/topology/vlan/vlan-names"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

DNACAuth = MainUrl + authToken

response = requests.post(DNACAuth, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=headers, data=payload)

JSONToken = response.json()

TOKEN = JSONToken['Token']

dnaVLANS = MainUrl + VlanApi

getPayload={}
getHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Auth-Token': TOKEN
}

getResponse = requests.get(dnaVLANS, headers=getHeaders, data=getPayload)

getJSON = getResponse.json()

print(getJSON)
