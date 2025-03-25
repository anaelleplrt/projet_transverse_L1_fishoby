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
easy_img = pygame.image.load("assets/easy.png")
easy_img = pygame.transform.scale(easy_img, (70, 60))
normal_img = pygame.image.load("assets/normal.png")
normal_img = pygame.transform.scale(normal_img, (140, 60))
hard_img = pygame.image.load("assets/hard.png")
hard_img = pygame.transform.scale(hard_img, (200, 60))
fishobi_img = pygame.image.load("assets/fishobi.png")
fishobi_img = pygame.transform.scale(fishobi_img,(400,400))

# Charger la musique de fond

pygame.mixer.music.load("assets/musique_fond.mp3")
pygame.mixer.music.play(-1)  # -1 pour jouer en boucle

# Définir la police d'écriture
police = pygame.font.SysFont("script", 80)

# Définir la fonction pour afficher le texte
def afficher_texte(texte, couleur, position):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = position
    ecran.blit(texte_surface, texte_rect)

# Créer la fenêtre
ecran = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Fish'obi")


# Boucle principale du programme
en_cours = True
while en_cours:
    # Gérer les événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            x, y = evenement.pos
            if easy_rect.collidepoint(x, y):
                print("Le jeu va être lancé.")
                jeu.lancement(550)
                en_cours = False
            elif normal_rect.collidepoint(x, y):
                print("Le jeu va être lancé.")
                jeu.lancement(700)
                en_cours = False
            elif hard_rect.collidepoint(x, y):
                print("Le jeu va être lancé.")
                jeu.lancement(950)
                en_cours = False


    # Afficher les images et les boutons
    ecran.blit(fond, (0, 0))
    easy_rect = ecran.blit(easy_img, (360, 200))
    normal_rect = ecran.blit(normal_img, (325, 300))
    hard_rect = ecran.blit(hard_img, (300, 400))
    fishobi_rect = ecran.blit(fishobi_img, (350, 350))

    # Afficher le texte
    afficher_texte("Fish'obi", BLANC, (largeur / 2, 100))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Arrêter la musique de fond
pygame.mixer.music.stop()

# Quitter Pygame
pygame.quit()
