from pwn import *
import sys
import hashlib

# Check for valid arguments
if len(sys.argv) != 2:
    print("Invalid Argument")
    print("Usage: {} <sha256sum>".format(sys.argv[0]))
    exit()

wanted_hash = sys.argv[1]
password_file = "/usr/share/wordlists/rockyou.txt"  # Adjust based on your location
attempts = 0

# Log the attempt
with log.process("Attempting to crack: {}!\n".format(wanted_hash)) as p:
    # Handling the password file
    with open(password_file, "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = hashlib.sha256(password).hexdigest()  # Hash the password
            p.status("[{}] Trying: {}".format(attempts, password.decode('latin-1')))
            
            # Check if the hashed password matches the wanted hash
            if password_hash == wanted_hash:
                p.success("Password found after {} attempts: '{}' hashes to '{}'".format(attempts, password.decode('latin-1'), password_hash))
                exit()

            attempts += 1
            
    p.failure("Password hash not found after {} attempts!".format(attempts))


