import numpy as np
# Données initales
# Précision: toutes les longueurs sont en mm et tous les angles en degrés.

a_soleil = 0.53  # 9.3*10**(-3) rad, diamètre angulaire du soleil, angle formé entre les rayons du soleil et l'axe
# perpendiculaire à l'appareil.

# Téléobjectif

ft = 300

# fc et fd à calculer, ce sont les lentilles convergentes et divergentes composant le téléobjectif"""

# Colimateur et Objectif

f1 = 80 * 10**(-3) #en m
f2 = 125 * 10**(-3) #en m
diam = 25.4 * 10**(-3) #en m

# Fente

epf = 10 * 10 ** (-6)  # eppaisseur des fentes en m
L_fe = 4.5 * 10**(-3) # Longueur des fentes en m

# Réseau/Facettes, pour un réseau de 2400 t/mm

L_fa = 1 / 2400 * 10**(-3) #epaisseur d'une facette en m
n_fa = 25 * 2400 #nombre de facettes sur le réseau
ep_fa = 100 * 10**(-9) #epaisseur de la facette en m
alpha = np.arctan(ep_fa/L_fa)
pas = 2400 * 10**3 #nombre de traits par millimètres
L_res = 25 * 10**(-3) #longueur du reseau
N = pas * L_res