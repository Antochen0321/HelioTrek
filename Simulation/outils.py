import matplotlib.pyplot as plt
import numpy as np
import math as math
#Peigne de Dirac à partir d'un signal sinusoïdal
def peigne_dirac(thetas, T0, A):
    """On définit le peigne de Dirac à partir d'une sinusoïde d'amplitude A et de période T0.
     On le définit sur thetas qui est la variable prise en compte pour visualiser les intensités. L'intervalle d'observation est:
     -borne<theta<borne avec n_points angles différents."""
    s_n = A * np.sin((1/T0) * math.pi * thetas)
    s_b = np.sign(s_n)
    peigne_dirac = abs(np.convolve(s_b, [-1, 1], 'same')) / 2
    return peigne_dirac

# k le vecteur d'onde
def k(lo):
    """permet de calculer le vecteur d'onde k.
     en fonction de: lo la longueur d'onde en m"""
    return 2 * math.pi / lo


# angle de diffraction theta
def theta_fente(lb, a, i):
    """permet de calculer l'angle de diffraction theta d'une fente
    en fonction de: -lb la longueur d'onde lambda
                    -a la largeur de la fente
                    -i l'angle incident, dans les cas généraux, il est nul"""
    return np.arcsin(lb/a - np.sin(i))

def theta_facette(lb, pas, p, alpha):
    """permet de calculer l'angle de diffraction theta d'une facette.
    en fonction de: -lb la longueur d'onde lambda
                    -pas le nombre de traits par millimètres
                    -p, l'ordre de diffraction, dépend de l'angle incident
                    -alpha, l'angle d'inclinaison de la facette"""
    return p*lb*pas/np.cos(alpha)