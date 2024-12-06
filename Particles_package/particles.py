# particles_package/particles.py
import pandas as pd
#Definimos la clase particle, aqui guardaremos toda la data de las particulas.
class Particle:
  def __init__(self, name, symbol, ptype, family, mass, charge, spin):
    """

    Args:
      name: nombre de la particula
      symbol: simbolo de la particula
      ptype: tipo de particula (ejemplo: Fermion, boson, etc)
      family: Familia a la que pertenece la particula (ejemplo: Leptones, quarks, etc)
      mass: masa de la particula en unidades de [GeV]
      charge: carga de la particula en unidades de [e]
      spin: spin de la particula
    """
    self.name = name #Nombre de la particula
    self.symbol = symbol #simbolo
    self.ptype = ptype #tipo de particula (ejemplo: Fermion, Boson, etc)
    self.family = family #familia a la que pertenece la particula
    self.mass = mass #Masa en [GeV/c^2]
    self.charge = charge #Carga en [e]
    self.spin = spin #spin

# Clase para Fermiones (hereda de Particle)
class Fermion(Particle):
    def __init__(self, name, symbol, family, mass, charge, spin):
        super().__init__(name, symbol, "Fermion", family, mass, charge, spin)

# Clase para Bosones (hereda de Particle)
class Boson(Particle):
    def __init__(self, name, symbol, mass, charge, spin):
        super().__init__(name, symbol, "Boson", "-", mass, charge, spin)