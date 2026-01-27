class Animal():
    def __init__(self, nom, edat, especie):
        self.nom = nom
        self.edat = edat
        self.especie = especie

    def presentar(self):
        print(f"Aquest és {self.nom}, té {self.edat} anys i és de l'especie {self.especie}")

class Refugi():
    def __init__(self, titol="RFMF", llista_animals=[]):
        self.llista = llista_animals
        self.titol = titol

    def afegir_animal(self, animal):
        self.llista.append(animal)

    def mostrar_llistat(self):
        for un_animal in self.llista:
            un_animal.presentar()

    def comprovar_animal(self, animal):
        if animal in self.llista:
            animal.presentar()
        else:
            print("No s'ha trobat a aquest animal en aquest refugi")

    def buscar_animal_per_nom(self, nom):
        for buscar_animal in self.llista:
            if buscar_animal.nom == nom:
                return f"{nom} si que es troba en el refugi {self.titol}"
        return f"Ho sent, {nom} no es troba en el refugi {self.titol}"
        
maxim = Animal("Maximus", 4, "gos")
rex = Animal("Roar", 4489, "T-rex")
bobo = Animal("El Gato con Botas", 67, "gat")
lala = Animal("Sonia", 25, "serp")

veterinaria_torregrosa = Refugi("veterinaria_torregrosa", [maxim, bobo])
veterinaria_torregrosa.mostrar_llistat()
print(".")
veterinaria_torregrosa.afegir_animal(rex)
veterinaria_torregrosa.mostrar_llistat()
print(".")
veterinaria_torregrosa.afegir_animal(lala)
veterinaria_torregrosa.mostrar_llistat()
print(".")
veterinaria_torregrosa.comprovar_animal(67)
veterinaria_torregrosa.comprovar_animal(rex)
veterinaria_torregrosa.comprovar_animal("El Gato con Botas")
print(".")
print(".")
print(".")
cerca_ss = veterinaria_torregrosa.buscar_animal_per_nom(67)
print(cerca_ss)
cerca_t = veterinaria_torregrosa.buscar_animal_per_nom(rex)
print(cerca_t)
cerca_gat = veterinaria_torregrosa.buscar_animal_per_nom("El Gato con Botas")
print(cerca_gat)
