import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback14"
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
basicauth = ("cisco", "cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback14",
        "description": "RESTCONF LOOPBACK 14",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "14.1.2.3",
                    "netmask": "255.255.255.0"
                }
            ]    
        },
        "ietf-ip:ipv6": {
            "address": [
                {
                    "ip": "2001:db8:acad:14::14",
                    "prefix-length": "64"
                }
            ]
        }
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message:{}'.format(resp.status_code,resp.json()))