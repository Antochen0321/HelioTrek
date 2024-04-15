import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
import numpy as np
from typing import List, Tuple, Any, Dict, Optional
import requests
from sunpy.data.sample import AIA_193_IMAGE

#Le module SunPy comprends une banque d'image préimportées, on utilise une image du module à titre d'exemple
AIA_193_IMAGE = AIA_193_IMAGE

###Fonctions Ouverture d'images
#Ces fonctions permettent d'ouvrir une image depuis un URL et de les afficher sur Python

def load_from_url(url: str) -> np.ndarray:
    return np.asarray(Image.open(requests.get(url, stream=True).raw))

def show(img:np.ndarray):
    im = Image.fromarray(img)
    print(im.size, im.mode, im.format, img.min(),  img.max())
    display(im)

def imshow(img):
    import cv2
    import IPython
    _,ret = cv2.imencode('.jpg', img)
    i = IPython.display.Image(data=ret)
    IPython.display.display(i)

"""
imageLue = load_from_url('https://observations-solaires.obspm.fr/sites/oss/IMG/jpg/ha_col.jpg')

imshow(imageLue)
"""

###Détection de taches

import sunpy.map #module de la librairie SunPy permettant d'établir quels sont les pixels brillants

aiamap_mask = sunpy.map.Map(AIA_193_IMAGE)
aiamap = sunpy.map.Map(AIA_193_IMAGE)
mask = aiamap.data < aiamap.max() * 0.10 #Définit un seuil de brillance à partir duquel les pixels sont considérés comme appartenant à une tâche
aiamap_mask.mask = mask
data2 = ndimage.gaussian_filter(aiamap.data * ~mask, 14) #Compare chaque pixel au seuil
data2[data2 < 100] = 0
aiamap2 = sunpy.map.Map(data2, aiamap.meta)
labels, n = ndimage.label(aiamap2.data)


#On affiche l'image initiale en entourant les zones de tâches
fig = plt.figure()
ax = fig.add_subplot(projection=aiamap)
aiamap.plot(axes=ax)
ax.contour(labels)
plt.figtext(0.3, 0.2, f'Number of regions = {n}', color='white') #permet d'entourer les tâches solaires
plt.show()

#On affiche maintenant seulement les pixels détectés comme faisant partie d'une tâche
fig = plt.figure()
ax = fig.add_subplot(projection=aiamap_mask)
aiamap_mask.plot(axes=ax)
plt.colorbar()
plt.show()
