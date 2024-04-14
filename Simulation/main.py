from intensites import *
from donnees import *

# données: ecrire les paramètres ici

p = 10
pi = math.pi
borne = pi
n_points = 10001
# Calculs, ne pas modifier

lambdas = np.linspace(400 * 10**(-9), 800*10**(-9), p)
k = o.k(lambdas)
thetas = np.linspace(-borne, borne, n_points)
print(N)
for n in range(len(lambdas)):
    """intensites = intensite_facette(thetas,L_fa, k[n], alpha, L_fa / 2)"""
    thetas, intensites = intensite_reseau(L_res, k[n], alpha, n, N, n_points, borne)
    plt.plot(thetas, intensites)
plt.show()