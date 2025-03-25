# Logobi des poiscailles (Fishoby)

by Maxime muscle, Raphaël Houbart, Anaëlle Pollart, Diaby Diakite, Hyppolite Valatta & Yslem Essid

# Liste des fichiers

- "main.py" : programme principal appelant les fonctions du jeu contenues dans le fichier "jeu.py".
- "jeu.py" : programme contenant les différentes fonctions nécessaire au jeu.
- "images et assets" : dossiers contenant les images.

## - Pré-requis 

- Installer Python

- Installer les différentes librairies :

```python
import pygame
import random
import math 
``` 


## Comment jouer :

### Execution du programme

- Lancer le programme dans un terminal :

```python 
main.py
```

Le paramétrage du jeu débute alors.

## Règles du jeu :
Le jeu est simple, il consiste à attraper le plus de poisson possible. Les poissons apparaissent à droite 
de l’écran et se déplacent en suivant le mouvement d’une parabole générée aléatoirement. On 
commence la partie avec un score de 0. Lorsqu’on attrape un poisson, on gagne 5 points, si l’on rate 
un poisson, on perd 5 points. De plus, parmi les poissons se cachent des méduses, si l’on en attrape 
une par mégarde, on perd 5 points. Pour attraper des poissons, il suffit de cliquer sur eux. Pareil pour 
les méduses, on les attrape en cliquant dessus. 

