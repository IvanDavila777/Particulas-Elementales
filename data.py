from Particles_package.particles import Fermion, Boson
from Particles_package.functions import add_particle

# Lista para almacenar partículas
particles = []

# Crear y agregar partículas
add_particle(particles, Fermion("Electrón", "e", "Leptones", 0.51099895, "-1", "1/2"))
add_particle(particles, Fermion("Muón", "μ", "Leptones", 105.6583755, "-1", "1/2"))
add_particle(particles, Fermion("Tau", "τ", "Leptones", 1776.93, "-1", "1/2"))
add_particle(particles, Fermion("Neutrino Electrón", "ν_e", "Leptones", 0.0000008, "0", "1/2"))
add_particle(particles, Fermion("Neutrino Muón", "ν_μ", "Leptones", 0.0000008, "0", "1/2"))
add_particle(particles, Fermion("Neutrino Tau", "ν_τ", "Leptones", 0.0000008, "0", "1/2"))
add_particle(particles, Fermion("Up", "u", "Quarks", 2.16, "2/3", "1/2"))
add_particle(particles, Fermion("Down", "d", "Quarks", 4.70, "-1/3", "1/2"))
add_particle(particles, Fermion("Strange", "s", "Quarks", 93.5, "-1/3", "1/2"))
add_particle(particles, Fermion("Charm", "c", "Quarks", 1273, "2/3", "1/2"))
add_particle(particles, Fermion("Bottom", "b", "Quarks", 4183, "-1/3", "1/2"))
add_particle(particles, Fermion("Top", "t", "Quarks", 172570, "2/3", "1/2"))

#Agregar bosones conocidos
add_particle(particles, Boson("Fotón", "γ", 0, "0", "1"))
add_particle(particles, Boson("Gluón", "g", 0, "0", "1"))
add_particle(particles, Boson("Bosón W+", "W+", 80369.2, "1", "1"))
add_particle(particles, Boson("Bosón Z", "Z", 91188, "0", "1"))
add_particle(particles, Boson("Bosón de Higgs", "H", 125200, "0", "0"))
