try:
    import requests, re, string, time, random, os, ctypes
    from concurrent.futures import ThreadPoolExecutor, as_completed
except:
    print("Error... Please run Setup.bat!")

ctypes.windll.kernel32.SetConsoleTitleW('RBX Checker | Waiting for input...')
api = 'https://auth.roblox.com/v1/usernames/validate?birthday=2000-04-20T08:00:00.000Z&context=Signup&username='

print('''
██████╗ ██████╗ ██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██████╔╝ ╚███╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██╔══██╗ ██╔██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██████╔╝██╔╝ ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                    ''')

##name gen###
x = 0
c = int(input("How many names do you want to generate? \n"))
print('Generating Names...')
namelist = []
while x != c:
    n = random.randint(5, 5)
    if n == 5:
        namegen = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        namelist += [namegen]      
    x = x + 1
print('Generated Names! Starting Checking Process...')
file_object = open('Generated Names.txt', 'a+')
file_object.write(str(namelist))
file_object.close()
counter = 0
print('Sarting Process...\n')
###name gen###

###checking###
def check(userloop):
    global counter
    r = requests.get(api +userloop) 
    counter += 1
    validstr = 'Number: ' + f'[{str(counter)}]' + ' Valid! ==> ' +userloop
    invalidstr ='Number: ' + f'[{str(counter)}]' + ' Invalid! ==> ' +userloop
    moderatedstr ='Number: ' + f'[{str(counter)}]' + ' Moderated! ==> ' +userloop
    if r.text == '{"code":1,"message":"Username is already in use"}':
        print(invalidstr)
        file_object = open('Invalid Names.txt', 'a+')
        file_object.write(str(userloop))
        file_object.write("\n")
        file_object.close()

    elif r.text == '{"code":2,"message":"Username not appropriate for Roblox"}':
        print(moderatedstr)
        file_object = open('Moderated Names.txt', 'a+')
        file_object.write(str(userloop))
        file_object.write("\n")
        file_object.close()

    else:
        print(validstr)
        file_object = open('Valid Names.txt', 'a+')
        file_object.write(str(userloop))
        file_object.write("\n")
        file_object.close()
    ctypes.windll.kernel32.SetConsoleTitleW('RBX Checker | 'f'{counter}' + ' out of ' + f'{c}' + ' names generated')
###checking###

###threading###
try:
    with ThreadPoolExecutor(max_workers=100) as exe:
        tasks = [exe.submit(check, userloop) for userloop in namelist]
    ctypes.windll.kernel32.SetConsoleTitleW('Completed!')
    print('Done!')
    input("Press enter to exit.")
except:
    print("ERROR: Please restart programme")    
    input("Press enter to exit.")
###threading###