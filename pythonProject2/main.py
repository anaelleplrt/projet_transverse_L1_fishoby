import pygame
import jeu
pygame.init()
# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définir les dimensions de la fenêtre
largeur = 800
hauteur = 800
taille_fenetre = (largeur, hauteur)

# Charger les images
fond = pygame.image.load("assets/fond.png")
fond = pygame.transform.scale(fond, taille_fenetre)
jouer_img = pygame.image.load("assets/jouer.png")
jouer_img = pygame.transform.scale(jouer_img, (200, 80))
options_img = pygame.image.load("assets/options.png")
options_img = pygame.transform.scale(options_img, (200, 80))
quitter_img = pygame.image.load("assets/quitter.png")
quitter_img = pygame.transform.scale(quitter_img, (200, 80))

# Charger la musique de fond
"""jeu_lancé=0
while jeu_lancé==0:"""
pygame.mixer.music.load("assets/musique_fond.mp3")
pygame.mixer.music.play(-1)  # -1 pour jouer en boucle

# Définir la police d'écriture
police = pygame.font.SysFont("comicsansms", 50)

# Définir la fonction pour afficher le texte
def afficher_texte(texte, couleur, position):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = position
    ecran.blit(texte_surface, texte_rect)

# Créer la fenêtre
ecran = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Peche aux poissons")


# Boucle principale du programme
en_cours = True
while en_cours:
    # Gérer les événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            x, y = evenement.pos
            if jouer_rect.collidepoint(x, y):
                print("Vous avez choisi de jouer.")
                # Ajouter ici le code pour lancer le jeu
                # Exemple :
                print("Le jeu va être lancé.")
                """jeu_lancé=1"""
                jeu.lancement()
                en_cours = False
            elif options_rect.collidepoint(x, y):
                print("Vous avez choisi les options.")
                print("Les options vont être affichées.")
            elif quitter_rect.collidepoint(x, y):
                en_cours = False

    # Afficher les images et les boutons
    ecran.blit(fond, (0, 0))
    jouer_rect = ecran.blit(jouer_img, (300, 200))
    options_rect = ecran.blit(options_img, (300, 300))
    quitter_rect = ecran.blit(quitter_img, (300, 400))

    # Afficher le texte
    afficher_texte("Peche aux poissons", BLANC, (largeur / 2, 100))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Arrêter la musique de fond
pygame.mixer.music.stop()

# Quitter Pygame
pygame.quit()
