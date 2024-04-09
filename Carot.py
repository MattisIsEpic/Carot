import socket
import re
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class Server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Just Bind the Server
    def Start(address: str, port: int):
        server.bind((address, port))
        server.listen()
    #accept clients
    def Accept():
        global client
        global address
        client, address = server.accept()
        return [client, address]

class Validate():
    def ValidateTextInput(rule: str, string: str):
        pattern = re.compile(rule)
        if pattern.search(string) is None:
            return True
        else:
            return False
    
    def ValidateURL(rules: list, URL: str):
        r = True
        compiled = []
        for rule in rules:
            compiled.append(re.compile(rule))
        for rule in compiled:
            scan = rule.search(URL)
            if not scan is None:
                r = False
        if r == True:
            return False
        else:
            return True
        
class Encryption():
    def cipher(text, key):
        header = b"header"
        data = b"secret"
        cipher = AES.new(key, AES.MODE_GCM)
        cipher.update(header)
        ciphertext, tag = cipher.encrypt_and_digest(data)

        json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
        json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag) ]
        result = json.dumps(dict(zip(json_k, json_v)))
        return result
    
    def decipher(text, key):
        try:
            b64 = json.loads(text)
            json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
            jv = {k:b64decode(b64[k]) for k in json_k}

            cipher = AES.new(key, AES.MODE_GCM, nonce=jv['nonce'])
            cipher.update(jv['header'])
            plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
            print("The message was: " + plaintext.decode('utf-8'))
        except (ValueError, KeyError):
            print("Incorrect decryption")
    
    def Generate_Key():
        return get_random_bytes(16)
