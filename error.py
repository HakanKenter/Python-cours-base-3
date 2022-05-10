try: 
    s = input("Entrer un nombre : ")
    nombre = int(s)
    print("Vous avez entrer {}".format(nombre))
except ValueError:
    print("Ce n'est pas un nombre")