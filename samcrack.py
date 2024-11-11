import os, sys
from passlib.hash import lmhash, nthash

def main():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    
    if len(sys.argv) != 3:
        sys.exit('\r\nUsage: <wordlist> <sam-file>\r\n')
    
    wordlist = []
    sam_hashes = []
    
    print('Importing wordlist...')
    try:
        with open(sys.argv[1], 'r') as f:
            wordlist = f.read().splitlines()
    except Exception as ex:
        sys.exit(f"Error: {ex}")
    
    print('Importing SAM file...')
    try:
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            sam_hashes = f.read().splitlines()
    except Exception as ex:
        sys.exit(f"Error: {ex}")
        
    print('Extracting SAM hashes...')
    hashes = {}
    for line in sam_hashes:
        if ':' in line:
            username, hash_value = line.split(':', 1)
            hashes[username] = hash_value.strip()
        
    print('\r\nCracking! Please be patient...\r\n')
    for username, hash_value in hashes.items():
        for password in wordlist:
            
            # use UTF-16 when generating hash
            try:
                ntlm_hash = nthash.hash(password)
            except Exception as ex:
                print(f"Error: {ex}")
                continue

            if ntlm_hash == hash_value.lower():
                print(f'Password "{password}" found for user "{username}"')
                break
    
    print('\r\nDone.\r\n')

if __name__ == "__main__":
    main()
