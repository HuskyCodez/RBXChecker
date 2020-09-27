try:
    import requests, re, string, time, random, os, ctypes
    from concurrent.futures import ThreadPoolExecutor, as_completed
except:
    print("Error... Please run Setup.bat!")

ctypes.windll.kernel32.SetConsoleTitleW('Waiting for input...')
api = 'http://api.roblox.com/users/get-by-username?username='

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

def check(userloop):
    global counter
    r = requests.get(api +userloop) 
    counter += 1
    validstr = 'Number: ' + str(counter) + ' Valid! ==> ' +userloop
    invalidstr ='Number: ' + str(counter) + ' Invalid! ==> ' +userloop
    if r.text == "{\"success\":false,\"errorMessage\":\"User not found\"}":
        print(validstr)
        file_object = open('Valid Names.txt', 'a+')
        file_object.write(str(userloop))
        file_object.write("\n")
        file_object.close()
    else:
        print(invalidstr)
        file_object = open('Invalid Names.txt', 'a+')
        file_object.write(str(userloop))
        file_object.write("\n")
        file_object.close()
    ctypes.windll.kernel32.SetConsoleTitleW(f'{counter}' + ' out of ' + f'{c}' + ' names generated')
    
try:
    with ThreadPoolExecutor(max_workers=100) as exe:
        tasks = [exe.submit(check, userloop) for userloop in namelist]
    ctypes.windll.kernel32.SetConsoleTitleW('Completed!')
    print('Done!')
    input("Press enter to exit.")
except:
    print("ERROR: Please restart programme")    
    input("Press enter to exit.")