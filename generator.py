import secrets

def generate_private_key():
    numbers = input("How many words in your final mnemonic? (12, 15, 18, 21, 24): ")
    if numbers=="12":byte=16
    elif numbers=="15":byte=20
    elif numbers=="18":byte=24
    elif numbers=="21":byte=28
    elif numbers=="24":byte=32
    else : 
        print("Not a valid input!")
        quit()
    private_key = secrets.token_bytes(byte)
    return private_key

private_key = generate_private_key()
print("Generated Private Key:", private_key)
print("Presented in HEX form:", private_key.hex())

import base58
import hashlib

def hex_to_wif(hex_private_key):
    extended_key = '80' + hex_private_key
    first_hash = hashlib.sha256(bytes.fromhex(extended_key)).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    checksum = second_hash[:4]
    extended_key += checksum.hex()
    wif = base58.b58encode(bytes.fromhex(extended_key)).decode()
    return wif

wif = hex_to_wif(private_key.hex())
print("Converted HEX to WIF:", wif)

import mnemonic

language = 'english'  
mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(private_key)
mnemonic_word_list = " ".join(mnemonic_words.split())
print("Converted Private Key to Mnemonic:", mnemonic_word_list)
