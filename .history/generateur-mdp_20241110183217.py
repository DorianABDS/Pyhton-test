import random

password_length = 8

password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"

password = "".join(random.choices(password_chars, k=password_length))

print("Ton nouveau mot de passe est :",password)