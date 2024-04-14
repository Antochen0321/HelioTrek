import matplotlib.pyplot as plt
import numpy as np
import math as math
import sunpy as sp
import astropy.units as u
from matplotlib.widgets import Slider
import outils as o
from donnees import *

def intensite_fente(theta, L_fe, k):
    """Permet de calculer l'intensité lumineuse en sortie d'une fente du réseau.
     En fonction de : -theta, l'angle de diffraction
                      -L_f la longueur de la fente
                      -k le vecteur d'onde"""
    arg = k * L_fe * theta / 2
    I = np.sinc(arg)
    return (L_fe * I)**2

def intensite_facette(theta, L_fa, k, alpha, n):
    """Permet de calculer l'intensité lumineuse en sortie d'une facette du réseau.
    En fonction de: -alpha l'angle d'inclinaison de la facette par rapport au réseau
                    -theta,l'angle de diffraction
                    -L_fa la longueur de la facette en m
                    -k le vecteur d'ondes et de alpha
                    -l'angle d'inclinaison de la facette
                    -n, la position du croisement entre le rayon lumineux et la facette, 0 étant la base de la facette,
                    l'endroit ou elle est la plus large. Donc 0<n<L_fa, arbitrairement n = L_fa/2"""
    arg = (k * L_fa * theta + n * alpha) / 2
    I = np.sinc(arg)
    return (L_fa * I)**2

def intensite_reseau(L_fa, k, alpha, n, N, n_points, borne):
    """Permet de calculer l'intensité lumineuse en sortie d'un réseau.
        En fonction de: -alpha l'angle d'inclinaison de la facette par rapport au réseau
                        -n_points le nombre d'angles de diffraction compris entre -borne et borne pour lesquels on regarde l'intensité.
                        -L_fa la longueur de la facette en m
                        -k le vecteur d'ondes et de alpha
                        -l'angle d'inclinaison de la facette
                        -N, le nombre total de facettes
                        -n, la position du croisement entre le rayon lumineux et la facette, 0 étant la base de la facette,
                    l'endroit ou elle est la plus large. Donc 0<n<L_fa, arbitrairement n = L_fa/2"""
    thetas = np.linspace(-borne, borne, n_points)
    u = k * thetas
    I_conv = (L_fa * np.sinc(u * L_fa / 2)) ** 2
    arg = (k * L_fa * thetas + n * alpha) / (2*N)
    I_fac = np.sinc(arg)
    I_fac = (L_fa * I_fac)**2
    T0 = 1/(2*math.pi*N/L_fa)
    p = o.peigne_dirac(thetas, T0, 1)
    res = p * I_fac
    plt.show()
    res = np.convolve(res, I_conv, 'same')
    #attention, cette fois la fonction renvoie 2 arguments, les angles thetas (axe x pour tracer) et les        intensités lumineuses (axe y pour tracer)
    return thetas, res

