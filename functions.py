import env
import webbrowser
import os
from env import info

def get_version():
    return env.info['version']


def openBrowser(url):

    url = 'https:' + url
    
    chrome_path = ''
    os_name = info['os']

    if os_name == 'Windows':
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    if os_name == "":
         # MacOS
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
 
    if os.name == "":
        # Linux
        chrome_path = '/usr/bin/google-chrome %s'

 

    webbrowser.get(chrome_path).open(url)

def commandsPrint():
    print('''
        0 - exit \n
        1 - help \n
        2 - open chrome \n   
    
    ''')