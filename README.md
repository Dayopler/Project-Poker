# Project-Poker

##Description
Le projet-poker est un projet python simulant une partie de Poker.
Le groupe est consititué de Titouan GLOCK et Yanis GATEBLE.

###Principe 
Une Fenêtre s'ouvre pour une partie de Poker et la partie est lancée.
Il y a un joueur (vous), 3 IA et un croupier (distributeur de carte et cagnotte globale).

Le joueur (vous) est le joueur de référence car toutes vos mises sont obligatoirement
suivies pas les IA, il décide également quand finir un tour (en arretant d'ajouter
de l'argent et en "misant").

##How to Use
```python
from PokerGame import Game

if __name__ == "__main__":
    Game()
```

###Structure du Code

A la racine du projet nous retrouvons **requirements.txt** qui donne les 
packages à installer
####dependeces 
```txt
pip install PyQt5Designer
pip install PyQt5
```
**main_window.py**, l'excution de la page

Un dossier **TU** qui regroupe les fichiers des Tests Unitaires.

Un dossier **PokerGame** qui viens regrouper plusieurs dossiers:
- CardMatch : regroupe les combinaisons 
- DeckManager : gestion du Deck
- Players : regroupe la création des joueurs et du Dealer
- Seed : s'occupe de la génération de seed pour refaire la même génération de cartes

Un dossier **GUI** qui regroupe :
- interface_content.py : Fichier qui s'occupe de l'affichage de tout ce que l'on souhaite
- un dossier *component* qui vient regrouper les fonctionnalités que l'on retrouve de la page graphique
  (exemple: la fonctionalité des boutons et MAJ de l'argent des joeurs)








