"""
Submitted by: Varun Ajith Sivaram
Email: varunajith2112@gmail.com

ShapeAi Python & Network Security Bootcamp
Final Project
Qs 1) Write a program in python to generate the MD5 of string data
"""

import hashlib

Str = input("Enter the string to be hashed: ")      # getting the string from user
print("Actual String: " + Str)
byte_val = Str.encode()     # encoding the string to bytes
hmd5 = hashlib.md5(byte_val)
print("Hash of string using MD5 algorithm: " + hmd5.hexdigest())
