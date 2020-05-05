#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

import signal

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

import pyfiglet 
  
result = pyfiglet.figlet_format("Anonymouse") 
print(result)

import requests

print("Anonymous-Mail ანონიმური მეილი")
print("------------------------------------------------------")
print("https://github.com/AnonymousFromGeorgia/Anonymous-Mail")
print("------------------------------------------------------")
to = raw_input('შეიყვანეთ ადრესატი (example@gmail.com): ')
subject = raw_input('შეიყვანეთ წერილის თემა (Subject): ')
message = raw_input('დაწერეთ წერილი (Message): ')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})

if 'The e-mail has been sent' in email_req.text:
    print("---------------------------------------------------------------------------------------------")
    print("მეილი წარმატებით გაიგზავნა!")
    print("---------------------------------------------------------------------------------------------")
    print("მეტი ანონიმურობისთვის, მეილი 12 საათის განმავლობაში მივა ადრესატთან შემთხვევითობის პრინციპით.")
    print("---------------------------------------------------------------------------------------------")

print("--------------------------------------------------")
print("პროგრამის ავტორი: გიო რგი")
print("--------------------------------------------------")
print("YouTube - https://youtube.com/AnonymousFromGeorgia")
print("--------------------------------------------------")
print("Github - https://github.com/AnonymousFromGeorgia")
print("--------------------------------------------------")
print("Facebook - https://facebook.com/anonimaluri")
print("--------------------------------------------------")
print("Twitter - https://twitter.com/anonimaluri")
print("--------------------------------------------------")
print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
print("--------------------------------------------------")
