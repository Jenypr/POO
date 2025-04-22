a = input()
b = input()
c = input()

if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:  # mamifero
        if c == "onivoro":
            print("homem")
        else:
            print("vaca")
else:  # invertebrado
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:  # anelideo
        if c == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")