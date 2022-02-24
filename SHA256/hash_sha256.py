import hashlib
data1 = "12345"
data2 = "12346"
hash1 = hashlib.sha256(data1.encode()).hexdigest()
hash2 = hashlib.sha256(data2.encode()).hexdigest()
print(hash1)
print(hash2)