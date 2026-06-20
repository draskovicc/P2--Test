# Standardna funkcija
def pozdrav(ime):
    print(f"Pozdrav"{ime}!")
          
# Lambda funkcija
dobrodosao = lambda ime: print(f"dobrodošao "{ime}!")
                               
# Treća funkcija prima drugu funkciju kao argument
def ispisi_dobrodoslicu(funkcija):
funkcija("DRAZAN") 

# Poziv treće funkcije
ispisi_dobrodoslicu(pozdrav)
ispisi_dobrodoslicu(dobrodosao)