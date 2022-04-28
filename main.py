# system module
from asyncio.windows_events import NULL
import sys
from helpers import getCommandType
from prosess import	check
from functions import commandsPrint,openBrowser

def main():
    args = sys.argv

    if len(args) > 1:    
        command = getCommandType(args[1])
        check(command)
    
    
    user_input = input('Type command: ')
    if user_input == '0':
        sys.exit()
    elif user_input == '1':
        commandsPrint()
    elif user_input == '2':
        url = input()
        openBrowser(url)


if __name__ == "__main__":
    main()