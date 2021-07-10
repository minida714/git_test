# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:34:01 2021

@author: origi
"""
from cryptography.fernet import Fernet # symmetric encryption


class SimpleEnDecrypt:
    def __init__(self, key=None):
        if key is None: # 키가 없다면
            key = Fernet.generate_key() # 키를 생성한다
        self.key = key
        self.f   = Fernet(self.key)
    
    def encrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.encrypt(data) # 바이트형태이면 바로 암호화
        else:
            ou = self.f.encrypt(data.encode('utf-8')) # 인코딩 후 암호화
        if is_out_string is True:
            return ou.decode('utf-8') # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou
        
    def decrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.decrypt(data) # 바이트형태이면 바로 복호화
        else:
            ou = self.f.decrypt(data.encode('utf-8')) # 인코딩 후 복호화
        if is_out_string is True:
            return ou.decode('utf-8') # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou


if __name__=='__main__':
    # instance 생성
    simpleEnDecrypt = SimpleEnDecrypt()
    # key 저장
    key = simpleEnDecrypt.key

    plain_text = '한글 암호'
    print(plain_text)

    # 암호화
    encrypt_text = simpleEnDecrypt.encrypt(plain_text)
    print(encrypt_text)

    # 복호화 동일 instance로 내재된 key로 복호화
    decrypt_text = simpleEnDecrypt.decrypt(encrypt_text)
    print(decrypt_text)

    # 다른 instance로 key 적용 복호화
    test_decrypt = SimpleEnDecrypt(key=key)
    decrypt_text = test_decrypt.decrypt(encrypt_text)
    print(decrypt_text)