def ispisi_unatrag(tekst):
    if tekst == "":
        return

    print(tekst[-1], end="")
    ispisi_unatrag(tekst[:-1])







    from modul import ispisi_unatrag

unos = input("Unesi string: ")
ispisi_unatrag(unos)