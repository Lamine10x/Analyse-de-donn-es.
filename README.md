# Analyse d'Investissement en Actions

## Description

Ce projet vise à analyser des portefeuilles d'actions pour maximiser les profits dans les limites d'un budget donné (500000 F CFA par défaut). Il implémente deux approches : une recherche exhaustive par force brute et une solution optimisée basée sur la programmation dynamique. Les données sont chargées depuis des fichiers CSV, prétraitées, et les résultats sont comparés.

## Prérequis

- Python 3.x
- Environnement virtuel (recommandé)
- Bibliothèques Python :
  - `pandas`

## Installation

1. Clone le dépôt ou télécharge les fichiers dans `C:\Users\diall\Documents\data analysis\`.
2. Crée un environnement virtuel :
   ```bash
   python -m venv venv
   ```

Active l'environnement virtuel :

Windows : venv\Scripts\activate

Installe les dépendances :
bashpip install pandas

Structure du Projet

src/

main.py : Script principal pour analyser les datasets complets.
main_test.py : Script de test avec un petit dataset (data_test.csv).
brute_force.py : Implémentation de la recherche exhaustive.
optimized_solution.py : Implémentation de la solution optimisée.
data_loader.py : Module pour charger et prétraiter les données CSV.

data/

data_test.csv : Dataset de test avec des actions simples.
dataset1_Python+P3.csv : Premier dataset complet.
dataset2_Python+P3.csv : Deuxième dataset complet.

docs/

presentation/ : Dossiers pour les slides (ex. slide_test.md).
report/ : Dossiers pour les rapports (ex. test_results.txt).

Utilisation

Active l'environnement virtuel :
bashvenv\Scripts\activate

Exécute les scripts :

Test rapide avec data_test.csv :
bashpython src/main_test.py

Analyse des datasets complets :
bashpython src/main.py

Vérifie les résultats dans la console ou dans docs/report/test_results.txt.

Résultats Actuels
Test avec data_test.csv (20 octobre 2025, 05:18 AM GMT)

Force Brute :

Actions : ['Action-4', 'Action-5', 'Action-6', 'Action-8', 'Action-10', 'Action-11', 'Action-13', 'Action-18', 'Action-19', 'Action-20']
Coût total : 498000 F CFA
Profit total : 99080 F CFA
Temps : 3.58 secondes

Solution Optimisée :

Actions : ['Action-5', 'Action-8', 'Action-18']
Coût total : 96000 F CFA
Profit total : 99080 F CFA
Temps : 2.44 secondes

Conclusion : L'optimisée est plus efficace (3 actions vs 10, même profit, temps réduit de 1.14s).

Prochaines Étapes

Tester dataset1_Python+P3.csv (~196610 F CFA) et dataset2_Python+P3.csv (~193780 F CFA) avec main.py.
Ajuster le budget (ex. 100000 F CFA) pour des tests supplémentaires.
Mettre à jour la diapositive (docs/presentation/slide_test.md) et le rapport (docs/report/test_results.txt) avec les nouveaux résultats.

Contributeurs

Touré Lamine
