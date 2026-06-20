import re

regex = r"^d(?=.*)"[0-5])(?=.*\s).J$"
tekst = input("unesi string:")

if re.match(regex, tekst):
print("podudaranje")
else:
print("nema podudaranja")

