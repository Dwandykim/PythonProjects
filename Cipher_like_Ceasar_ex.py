# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:29:21 2022

@author: dwand
"""
"""str2 = book, plain_text = str1
Goal: P1 is trying to send a encrypted messsage to P2 
Assumptions: P1 and P2 both have the secret_book"""
message = 'paris'
secret_book = 'tpkaryois'

gen_code_keys = (lambda book, plain_text:(
 {c: str(book.find(c)) for c in plain_text}))

encoder = (lambda code_keys, plain_text:
 ''.join(['*' + code_keys[c] for c in plain_text])[1:])
          
encrypt = (lambda book, plain_text:
 encoder(gen_code_keys(book, plain_text), plain_text))
    
secret_msg = encrypt(secret_book,message)
print(secret_msg)



gen_decode_keys = (lambda book, cipher_text:
 {s: book[int(s)] for s in cipher_text.split('*')})

secret_dict = gen_decode_keys(secret_book, secret_msg)
    
def decoder(decoded_keys, secret_msg):
    msg = '' 
    for number in secret_msg:
         if number != '*':
             msg += decoded_keys[number]
    return msg                             
         
print(decoder(secret_dict, secret_msg))
                     
    
    
    
# decoder = (lambda decoded_keys, secret_msg:
#  ''.split(['*' + decoded_keys[c] for c in secret_msg])[1:])
          
# encrypt = (lambda book, plain_text:
#  encoder(gen_code_keys(book, plain_text), plain_text))
    
# print(gen_decode_keys(str2, secret_msg))