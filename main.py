
def groesste(inhalt:list):
  breite:int = 0
  for element in inhalt:
    if len(element) > breite:
      breite = len(element)
  return breite

def strich(text:str):
  oben_unten:str = "+"+len(text)*"-"+"+"
  return oben_unten

#construct = ""

def kasten(text:str):
  inhalt:list = text.split("\n")
  breite = groesste(inhalt)
  hoehe = len(inhalt)
  constrct = ""
  for element in inhalt:
    while len(element) < breite:
      element+=" """
    constrct+= "|"+element+"|\n" #DAS HIER 

  return constrct

print(kasten("Jetzt\nsollte das \nfunktionieren"))

#print("\n")
#print("     Lorem Ipsum      ".rstrip())

