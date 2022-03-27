import pygame
import sys

class Grille:

	def __init__(self,ecran):
		"""
		initie la grille
		:param: ecran
		"""
		self.ecran = ecran
		self.lignes = [( (200,0),(200,600)),
            ((400,0),(400,600)),
            ((0,200),(600,200)),
            ((0,400),(600,400)),]
		# initer la grille
		self.grille = [[None for x in range(0,3)] for y in range(0,3)]
		self.compteur_on = False

	def afficher(self):
		"""
		Affiche la grille et les X/O
		"""
		for ligne in self.lignes :

			pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)

		for y in range(0,len(self.grille)):
			for x in range(0,len(self.grille)):


					if self.grille[y][x] == 'X' :

						pygame.draw.line(self.ecran, (0, 0, 0), (x * 200, y * 200), (200 + (x * 200), 200 + (y * 200)), 3)
						pygame.draw.line(self.ecran, (0, 0, 0), ((x * 200), 200 + (y * 200)), (200 + (x * 200), (y * 200)),
					                 3)

					elif self.grille[y][x] == 'O' :

						pygame.draw.circle(self.ecran, (0, 0, 0), (100 + (x * 200), 100 + (y * 200)), 100, 3)

	def print_grille(self):
		"""
		Afficher la grille dans la console
		"""
		print(self.grille)


	def fixer_la_valeur(self,x,y,valeur):
		"""
		Fixe la valeur d'une case dans la grille
		:param: x
		:param: y
		:param: valeur
		"""
		if self.grille[y][x] == None:
			self.grille[y][x] = valeur
			self.compteur_on = True

	def fixer_None(self,x,y,valeur):
		 """
		Attribue la valeur None à la case [y][x]
		 :param: x
		 :param: y
		 :param: valeur
		 """
		 self.grille[y][x] = valeur




class Jeu :

	def __init__(self):

		self.ecran = pygame.display.set_mode((600,600))
		pygame.display.set_caption('Tic Tac Toe ')
		self.jeu_encours = True
		self.grille = Grille(self.ecran)
		# fixer les variables 'X' 'O'
		self.player_X = 'X'
		self.player_O = 'O'

		# fixer le compteur
		self.compteur = 0


		self.clicked = False
		self.game_finished = False
		self.ecran_debut = True


	def fonction_principale(self):
		"""
		Exécute le While loop
		"""
		while self.jeu_encours:

			while self.ecran_debut:
				for event in pygame.event.get():

					if event.type == pygame.QUIT:
						sys.exit()

					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							self.ecran_debut = False
				self.ecran.fill((230, 230, 230))
				self.creer_message('grande', 'Tic Tac Toe', [200, 30, 200, 50], (0, 0, 0))
				self.creer_message('petite', "Ce jeu se joue à deux et chaqu'un se verra attribuer un symbole ",
				                   [50, 130, 400, 50], (0, 0, 0))
				self.creer_message('petite', 'X ou O', [220, 150, 100, 100], (0, 0, 0))
				self.creer_message('petite', 'Le premier joueur qui reussi à aligner 3 de ses symboles gagne',
				                   [50, 170, 200, 50], (0, 0, 0))
				self.creer_message('moyenne', 'Pour recommencer le jeu , appuyer sur Enter', [70, 350, 200, 50],
				                   (0, 0, 0))
				self.creer_message('moyenne', 'Appuyer sur Espace pour commencer le jeu ', [70, 400, 200, 50],
				                   (0, 0, 0))
				self.creer_message('moyenne', 'Pour revenir a cette ecran , appuyer sur ESC ', [70, 450, 200, 50],
				                   (0, 0, 0))

				pygame.display.flip()


			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()
				# ajouter l'evenement qui correspond au clique droit
				if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:

					# obtenir la position de la souris
					position = pygame.mouse.get_pos()
					#print(position)
					position_x ,position_y = position[0]//200 ,position[1]//200
					#print(self.position_x,self.position_y)

					# cond si le compteur est pair ou impair
					#print(self.compteur,self.compteur%2)
					if self.compteur % 2 == 0 :
						self.grille.fixer_la_valeur(position_x, position_y, self.player_X)


					else:
						self.grille.fixer_la_valeur(position_x, position_y, self.player_O)
					if self.grille.compteur_on:
						self.compteur += 1
						self.grille.compteur_on = False

					self.clicked = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.recommencer_le_jeu()

					if event.key == pygame.K_ESCAPE:
						self.ecran_debut = True



			#self.grille.print_grille()
			liste_X = []
			liste_O = []
			liste_lignes_X = []
			liste_colonnes_X = []
			liste_lignes_O = []
			liste_colonnes_O = []
			self.gagnant(liste_X,liste_O,liste_colonnes_X,liste_lignes_X,liste_lignes_O,liste_colonnes_O)


			self.ecran.fill((240,240,240))
			self.grille.afficher()

			pygame.display.flip()
