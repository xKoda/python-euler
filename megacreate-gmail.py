from apiclient.discovery import build
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
from bs4 import BeautifulSoup
from random import choice
from stem import Signal
from stem.control import Controller
import time
import base64
import subprocess
import atexit

#Accounts get saved here in mail:pass format
output_file_dir = "/root/megacreate/OUTPET.txt"

#Command/absolute path to call megareg over torsocks (or without it if not using tor)
torsocks_megareg_dir = "torsocks megareg"

#gmail account name (without @gmail.com)
gmail_acc="apitestingtopkek"

#Whether to use tor
useTor=True

#Chunk size
n=10
j=n


# Setup the Gmail API
SCOPES = 'https://mail.google.com/'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = build('gmail', 'v1', http=creds.authorize(Http()))

def list_mail():
    try:
        return [dic["id"] for dic in GMAIL.users().messages().list(userId="me", q="from:welcome@mega.nz").execute()['messages']]
    except KeyError:
        return []

def delete_mail():
    print("Cleaning up rest mail")
    msg_list_ids = list_mail()
    if msg_list_ids:
        GMAIL.users().messages().batchDelete(userId="me", body={"ids": msg_list_ids}).execute()

def wait_for_mail(number):
    waittime=0
    while True:
        if waittime>120:
            print("Ive been waiting 2 minutes for the damn mail. I'll give up and restart")
            return []
        time.sleep(1)
        msg_list_ids = list_mail()
        if len(msg_list_ids)==number:
            return msg_list_ids
        waittime+=1

def random_text():
    return ''.join([choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(21)])

def random_mail():
    return ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(30)])

def extract_url(mail_str):
    soup = BeautifulSoup(mail_str, "lxml")
    for link in soup.findAll("a"):
        if link.get("href") is not None and "#confirm" in link.get("href"):
            url = link.get("href").replace('3D"', "").replace('"', "")    
    return url

def refresh_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

atexit.register(delete_mail)
c=0
deleted_mail=False
while True:
    while True:
        start = time.time()
        print("Starting a new bulk")
        email_code_pairs = {}
        email_pass_pairs = {}
        confirm_commands = []
        n=j
        if not deleted_mail:
            delete_mail()
        if useTor:
            if c%20==0:
                refresh_ip()
            if c%100==0: #Sometimes tor hangs, preventing it here
                subprocess.check_output("systemctl restart tor", shell=True)
                time.sleep(1)

        #Register a bulk of size n
        print("Registering accounts")
        while n > 0:
            email = gmail_acc + "+" + random_mail() + "@gmail.com"
            email_password = random_text()
            confirm_text = str(subprocess.check_output(torsocks_megareg_dir +" -n johncena -e " + email + " -p " + email_password + " --register",  shell=True))
            confirm_text = confirm_text[confirm_text.find("megareg"):confirm_text.find("@LINK@")+6]
            email_code_pairs[email]=confirm_text
            email_pass_pairs[email]=email_password
            n-=1
        print("Done registering")
        
        #Wait for mail and read it
        msg_list_ids = wait_for_mail(j)
        if not msg_list_ids:
            break
        for i in msg_list_ids:
            mail_str=str(base64.urlsafe_b64decode(GMAIL.users().messages().get(id=i, userId="me", format="raw").execute()["raw"]))
            current_link = extract_url(mail_str).replace("=\\r\\n", "")
            current_email = mail_str[16:73]
            current_command = email_code_pairs[current_email].replace("@LINK@", current_link)
            confirm_commands.append(current_command)

        #Confirm accounts
        print("Confirming accounts")
        for command in confirm_commands:
            subprocess.check_output(command,shell=True)

        #Write to file
        with open(output_file_dir, "a+") as f:
            for m in email_pass_pairs:
                f.write(m+":"+email_pass_pairs[m]+"\n")
        
        #Wait for rest mail and delete it
        if wait_for_mail(2*j):
            delete_mail()
            deleted_mail=True

        c+=j
        print("Bulk done. Generated "+str(j)+" accounts in "+str(round(time.time()-start,1))+"s"+". Currently: "+str(c))
