from itertools import combinations
from data_loader import load_data

def brute_force_investment(file_path, budget=500000):
    """
    Implémente une solution de force brute pour sélectionner les actions maximisant le profit.
    Explore toutes les combinaisons possibles et retourne la meilleure combinaison.
    - Paramètre : file_path (chemin du fichier CSV), budget (max 500000 F CFA par défaut)
    - Retourne : (liste des IDs des actions sélectionnées, coût total, profit total)
    """
    # Charger les données
    shares = load_data(file_path)
    n = len(shares)
    max_profit = 0.0
    best_comb = []
    best_cost = 0
    
    # Explorer toutes les combinaisons possibles
    for r in range(n + 1):
        for comb in combinations(range(n), r):
            # Vérifier que chaque indice dans comb est valide
            try:
                # Calculer le coût et le profit de la combinaison actuelle
                total_cost = sum(shares[i][1] for i in comb if len(shares[i]) > 1)
                total_profit = sum(shares[i][2] for i in comb if len(shares[i]) > 2)
                
                # Vérifier si la combinaison respecte le budget et améliore le profit
                if total_cost <= budget and total_profit > max_profit:
                    max_profit = total_profit
                    best_comb = [shares[i][0] for i in comb]  # Stocker les IDs
                    best_cost = total_cost
            except IndexError as e:
                print(f"Erreur d'index pour la combinaison {comb}: {e}")
                continue
    
    return best_comb, best_cost, max_profit

if __name__ == "__main__":
    # Test de la fonction avec le dataset 1
    result = brute_force_investment("data/dataset1_Python+P3.csv")
    actions, cost, profit = result
    print("Actions sélectionnées :", actions)
    print("Coût total :", cost, "F CFA")
    print("Profit total :", profit, "F CFA")