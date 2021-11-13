from crypt import crypt
import sys

if (len(sys.argv) != 2) :
    print ('Usage : python3 descrack.py <WORDLIST>')
    sys.exit(1)

filename    = sys.argv[1]
target      = "42hDRfypTqqnw"

with open(filename, 'r', errors='replace') as wordlist :
    passwords = wordlist.readlines()

for password in passwords :
    password = password.rstrip()
    print("[*] Trying " + password)
    guess = crypt(password, '42')
    print("[DEBUG] Got " + guess)
    if (guess == target) :
        print("[+] Cracked DES hash : " + password)
        exit(0)
