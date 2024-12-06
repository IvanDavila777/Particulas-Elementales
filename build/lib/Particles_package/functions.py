# particles_package/functions.py
import pandas as pd
from Particles_package.particles import Particle, Fermion, Boson #Importar clases

# Función para agregar una partícula a la lista
def add_particle(particles_list, particle):
    """ Particle: Una particula es un constituyente fundamental del universo.
    """
    particles_list.append(particle)

# Función para mostrar la tabla de partículas
#def show_particles(particles_list):
#    data = {
#        "Nombre": [p.name for p in particles_list],
#        "Símbolo": [p.symbol for p in particles_list],
#        "Tipo": [p.ptype for p in particles_list],
#        "Familia": [p.family for p in particles_list],
#        "Masa (MeV/c^2)": [p.mass for p in particles_list],
#        "Carga (e)": [p.charge for p in particles_list],
#        "Spin": [p.spin for p in particles_list]
#    }
#    df = pd.DataFrame(data)
#    print(df)

def show_particles(particles_list):
    """Muestra todas las partículas en la lista"""
    # Extrae los atributos de cada partícula
    data = [vars(p) for p in particles_list]
    
    # Verifica si los datos fueron agregados correctamente
    if not data:
        print("No hay partículas en la lista.")
    else:
        df = pd.DataFrame(data)
        print(df)
# Mostrar la tabla de partículas
#show_particles()