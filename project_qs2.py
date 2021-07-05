"""
Submitted by: Varun Ajith Sivaram
Email: varunajith2112@gmail.com

ShapeAi Python & Network Security Bootcamp
Final Project
Qs 2) Write a program in python to generate hashes of string data using 3 algorithms from hashlib
"""

import hashlib

Str = input("Enter the string to be hashed: ")      # getting the string from user
print("Actual String: " + Str)
byte_val = Str.encode()     # encoding the string to bytes


# Using sha512 algorithm
h_sha512 = hashlib.sha512(byte_val)
print("Hash of string using sha512 algorithm: " + h_sha512.hexdigest())

# Using blake2s algorithm
h_blake2s = hashlib.blake2s(byte_val)
print("Hash of string using blake2s algorithm: " + h_blake2s.hexdigest())

# Using sha256 algorithm
h_sha256 = hashlib.sha256(byte_val)
print("Hash of string using sha256 algorithm: " + h_sha256.hexdigest())
