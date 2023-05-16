import pygame
import random
import math
def lancement():
    # Initialisation de Pygame
    pygame.init()

    # Définition des couleurs utilisées dans le jeu
    BLANC = (255, 255, 255)
    BLEU = (0, 0, 255)
    NOIR = (0, 0, 0)
    ROUGE = (255, 0, 0)

    # Définition des constantes du jeu
    LARGEUR = 800
    HAUTEUR = 800
    TAILLE_POISSON = 100
    VITESSE_POISSON = 550
    TEMPS_POISSON = 1500
    TEMPS_MAX = 30000
    SCORE_PAR_POISSON = 5

    # Chargement de l'arrière-plan
    arriere_plan = pygame.image.load("images/background.png")

    # Chargement de l'image du poisson
    image_poisson = pygame.image.load("images/fish.png")

    taille_poisson = (100, 80)  # Spécifiez les dimensions souhaitées
    image_poisson = pygame.transform.scale(image_poisson, taille_poisson)
    image_sac = pygame.image.load("images/bag.png")

    # Création de la fenêtre de jeu
    ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Pêche aux poissons")

    # Création de la police de caractères utilisée pour afficher le score
    police_score = pygame.font.SysFont("Arial", 30)

    # Initialisation du score
    score = 0

    # Liste des poissons
    poissons = []

    # Définition de la classe Poisson
    class Poisson:
        def __init__(self, y, hauteur, angle):
            self.x = LARGEUR
            self.y = y
            self.temps = pygame.time.get_ticks()
            self.angle = angle # Angle de départ aléatoire
            self.hauteur = hauteur  # Hauteur spécifiée aléatoirement

        def afficher(self):
            ecran.blit(image_poisson, (self.x, self.y))

        def tomber(self):
            temps_ecoule = pygame.time.get_ticks() - self.temps
            t = temps_ecoule / 1000  # Conversion en secondes
            self.x = LARGEUR - VITESSE_POISSON * math.cos(self.angle) * t  # Équation de x(t)
            self.y = -0.5 * 9.8 * t ** 2 + VITESSE_POISSON * math.sin(self.angle) * t + self.hauteur  # Équation de y(t)

        def est_peche(self):
            return pygame.time.get_ticks() - self.temps >= TEMPS_POISSON

    # Définition de la classe sacs
    class Sacs:
        def __init__(self, y, hauteur, angle):
            self.x = LARGEUR
            self.y = y
            self.temps = pygame.time.get_ticks()
            self.angle = angle  # Angle de départ aléatoire
            self.hauteur = hauteur  # Hauteur spécifiée aléatoirement

        def afficher(self):
            ecran.blit(image_sac, (self.x, self.y))

        def tomber(self):
            temps_ecoule = pygame.time.get_ticks() - self.temps
            t = temps_ecoule / 1000  # Conversion en secondes
            self.x = LARGEUR - VITESSE_POISSON * math.cos(self.angle) * t  # Équation de x(t)
            self.y = -0.5 * 9.8 * t ** 2 + VITESSE_POISSON * math.sin(self.angle) * t + self.hauteur  # Équation de y(t)

        def est_peche(self):
            return pygame.time.get_ticks() - self.temps >= TEMPS_POISSON

    # Boucle principale du jeu
    horloge = pygame.time.Clock()
    temps_debut = pygame.time.get_ticks()
    jeu_termine = False
    poissons_peches = 0  # Nouvelle variable pour compter les poissons péchés
    while not jeu_termine:
        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                jeu_termine = True  # Terminer le jeu si l'utilisateur ferme la fenêtre
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for poisson in poissons:
                    if ((poisson.x - x) ** 2 + (poisson.y - y) ** 2) ** 0.5 <= TAILLE_POISSON:
                        if not poisson.est_peche():
                            score += SCORE_PAR_POISSON
                            poissons_peches += 1  # Incrémenter le compteur de poissons péchés
                        poissons.remove(poisson)
                        break  # Sortir de la boucle après avoir trouvé et péché le poisson

        # Mise à jour et affichage des poissons
        tab_elements = []
        for poisson in poissons:
            poisson.tomber()
            if poisson.x + TAILLE_POISSON < 0 or poisson.y + TAILLE_POISSON >= HAUTEUR or poisson.y + TAILLE_POISSON < 0 :  # Vérifier si le poisson est sorti par la gauche ou par le bas
                score -= 10
                tab_elements.append(poisson)
                if score <= 0:
                    jeu_termine = True  # Terminer le jeu si le score atteint 0 ou moins

        # Affichage du fond d'écran
        ecran.blit(arriere_plan, (0, 0))
        # Affichage des poissons
        for poisson in poissons:
            poisson.afficher()

        # Affichage du score
        texte_score = police_score.render(f"Score : {score}", True, NOIR)
        ecran.blit(texte_score, (10, 10))

        # Suppression des poissons tombés
        for poisson in tab_elements:
            poissons.remove(poisson)

        pygame.display.flip()

        # Ajout d'un nouveau poisson
        if pygame.time.get_ticks() - temps_debut >= random.randint(500, 1500):
            hauteur = random.randint(100, 500)  # Exemple de plage de hauteur de sorti des poissons
            angle = random.uniform(-math.pi / 4, math.pi / 4)
            poissons.append(Poisson(0, hauteur, angle))
            temps_debut = pygame.time.get_ticks()

        # Conditions de fin du jeu
        if jeu_termine:

            ecran.fill(BLANC)
            texte_game_over = police_score.render("Game Over", True, ROUGE)
            ecran.blit(texte_game_over, (LARGEUR // 2 - 70, HAUTEUR // 2 - 50))
            texte_poissons_peches = police_score.render(f"Poissons péchés : {poissons_peches}", True, ROUGE)
            ecran.blit(texte_poissons_peches, (LARGEUR // 2 - 120, HAUTEUR // 2))
            pygame.display.flip()
            attente = True
            while attente:
                for evenement in pygame.event.get():
                    if evenement.type == pygame.QUIT:
                        attente = False
                        jeu_termine = True  # Terminer complètement le jeu
                horloge.tick(30)  # Limiter la boucle à
    pygame.quit()
