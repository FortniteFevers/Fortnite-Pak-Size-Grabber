import os
import requests
from colorama import *
init()
import time

#---------------#

FortniteGamePath = 'C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\'
# ^  Make sure to include a '\\' at the end!  ^ #

FileFormat = '.ucas'
# ^ The file format you want to choose to grab. #

#---------------#


print('')
print('----------------------------')
print(Fore.GREEN + f'Loaded file path as {FortniteGamePath}')
print(f'\nLoaded FileFormat as {FileFormat}')
print(Fore.WHITE + '----------------------------')
thing = FileFormat.replace('.', '')
print(Fore.GREEN + f'\nGrabbing current {thing} files...')
time.sleep(0.5)

print(Fore.YELLOW + '\nDo you want to grab all files or leaked files?')
o = input('>> ')
counter = 1

if o == 'all':
    try:
        for file in os.listdir(FortniteGamePath): # For every single file in the paks folder, do this
            try:
                if file.endswith(FileFormat): # IF the file is a ucas file, do this!
                    filesingle = (f'{FortniteGamePath}{file}') # Grabs File
                    file = os.path.join(file) # Grabs the file and joins it
                    lol = os.path.getsize(filesingle) # Grabs the size of the current file in kb
                    lol = lol/1024 # Convertes the bytes to kb
                    lol = lol/1000 # Converts the kb to mb
                    lol = round(lol, 1) # Rounds it up so theres no ugly decimals
                    file = file.replace(FileFormat, '')
                    uh = len(FortniteGamePath)
                    print(f'\n'+Fore.GREEN+f'{file} - '+Fore.YELLOW+f'{lol}mb')
                    counter = counter + 1
                    time.sleep(0.05)
            except:
                print (Fore.RED+'\nAn error has been found. You most likely have put in the wrong file path, try again!')
                time.sleep(3)
                exit()
    except:
        print (Fore.RED+'\nAn error has been found. You most likely have put in the wrong file path, try again!')
        time.sleep(3)
        exit()
else:
    o = 'xxx'
    try:
        for file in os.listdir(FortniteGamePath): # For every single file in the paks folder, do this
            try:
                if file.endswith(FileFormat): # IF the file is a ucas file, do this!
                    filesingle = (f'{FortniteGamePath}{file}') # Grabs File
                    file = os.path.join(file) # Grabs the file and joins it
                    lol = os.path.getsize(filesingle) # Grabs the size of the current file in kb
                    lol = lol/1024 # Convertes the bytes to kb
                    lol = lol/1000 # Converts the kb to mb
                    lol = round(lol, 1) # Rounds it up so theres no ugly decimals
                    file = file.replace(FileFormat, '')
                    uh = len(FortniteGamePath)

                    response = requests.get('https://pastebin.com/raw/Aiy0yHVK')

                    for i in response.json():
                        pak = response.json()[i]
                        if pak in file:
                            print(f'\n'+Fore.GREEN+f'{file} - '+Fore.YELLOW+f'{lol}mb')

                    counter = counter + 1
            except:
                print (Fore.RED+'\nAn error has been found. You most likely have put in the wrong file path, try again!')
                time.sleep(3)
                exit()
    except:
        print (Fore.RED+'\nAn error has been found. You most likely have put in the wrong file path, try again!')
        time.sleep(3)
        exit()


x = counter-1
if o != 'xxx':
    print(f'\n\nFound {x} "{thing}" files.')
else:
    response = requests.get('https://pastebin.com/raw/Aiy0yHVK')
    x = len(response.json()) * 2
    print(f'\n\nFound {x} leaked "{thing}" files.')
print(Fore.CYAN + '\nSuccesfully Grabbed File Sizes!' + Fore.RESET)
time.sleep(500)
