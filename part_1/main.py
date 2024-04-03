from jose import jwt

# дані для заповнення токена
payload = {"email": "string1", "password": "string1"}

print(payload)
# створення токена з симетричним ключем
encoded = jwt.encode(payload, "secret_key", algorithm='HS256')
print(encoded)

# перевірка токена
decoded = jwt.decode(encoded, "secret_key", algorithms=['HS256'])
print(decoded)

