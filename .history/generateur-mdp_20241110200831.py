import random

password_length = random.randint(8,12)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

class color:
    password = '\033[93m'

    print("Ton nouveau mot de passe est :",password,"et contient" ,password_length,"caractères")
    print("Enregistre le bien !")