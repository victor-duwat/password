from hashlib import sha512
import json
import random
import string


maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
min = "abcdefghijklmnopqrstuvwxyz"
chi = "0123456789"
car = "!@#$%^&"
majs = random.choice(maj)
mins = random.choice(min)
chis = random.choice(chi)
cars = random.choice(car)
caracteres = majs + mins + chis + cars
reste_du_mot_de_passe = ''.join(random.choice(caracteres) for _ in range(6))
random_password=''.join(random.sample(majs + mins + chis + cars + reste_du_mot_de_passe, 10))
valid=True


def valide(password):
    if not len(password) >= 10:
        print("Veuillez choisir un mot de passe d'au moins 10 caractères")
        valid=False
    if not any(char.isupper() for char in password):
        print("Veuillez entrer un mot de passe contenant une majuscule")
        valid=False
    if not any(char.islower() for char in password):
        print("Veuillez entrer un mot de passe contenant une minuscule")
        valid=False
    if not any(char.isdigit() for char in password):
        print("Veuillez entrer un mot de passe contenant un chiffre")
        valid=False
    if not any(char in car for char in password):
        print("Veuillez entrer un mot de passe contenant un caractère spécial")
        valid=False

utilisateur=input("Veuillez entrez votre nom: ")
choix=input("voulez vous que votre mot de passe soit générer aléatoirement ? ")
if choix=="oui":
    password_input=random_password
else:
    password_input=input("Veuillez entrez votre  mot de passse ")
    

valide(password_input)
while valid is not True:
    password_input=input("Veuillez choisir un autre mot de passe: ")
    valide(password_input)
    if len(password_input) >= 10 and any(char.isupper() for char in password_input) and any(char.islower() for char in password_input) and any(char.isdigit() for char in password_input) and any(char.isdigit() for char in password_input) and any(char in car for char in password_input):
        valid=True
print("Votre mot de passe:",password_input," est correcte")
if valid is True:
    password_input = password_input.encode()
    password_input_sign=sha512(password_input).hexdigest()
print("Et votre mot de passe crypté donne: ",password_input_sign)

nom_fichier="password.txt"
password_input_str=str(password_input_sign)
nom_fichier="password.txt"
# liste =[password_input_str]
with open(nom_fichier, "r") as f:
    try:
        liste = json.load(f)
    except:
        liste = {}        

liste[utilisateur] =  str(password_input)
fp = open(nom_fichier,"w",encoding="utf-8")
json.dump(liste,fp,indent=4)
fp.close()
