'''
Caesar/ROT Cipher Brute-Forcer
Auther: nour
'''

import sys 
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = ''
for arg in '\n'.join(sys.argv[1:28:8]): 
    ciphertext += arg 
       
def Caeser_decrypt(ciphertext, key):  
   assert key > 0
   
   ciphertext = ciphertext.upper()
   plaintext = '' 

   for state in ciphertext:  
        if state not in alphabet:
           plaintext += state
        else:
            plaintext += alphabet[(alphabet.index(state) - key) % 25] 
        
   return plaintext

def bruteforce(ciphertext):
    for i in range(1, 25):
        print(f"{i}: {Caeser_decrypt(ciphertext, i)}")

bruteforce(ciphertext)
