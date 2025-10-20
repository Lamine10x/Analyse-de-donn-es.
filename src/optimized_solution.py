from data_loader import load_data

def optimized_investment(file_path, budget=500000):
    """
    Implémente une solution optimisée avec programmation dynamique pour sélectionner
    les actions maximisant le profit dans les contraintes de budget.
    - Paramètre : file_path (chemin du fichier CSV), budget (max 500000 F CFA par défaut)
    - Retourne : (liste des IDs des actions sélectionnées, coût total, profit total)
    """
    # Charger les données
    shares = load_data(file_path)
    n = len(shares)
    
    # Initialiser le tableau de programmation dynamique
    dp = [0.0 for _ in range(int(budget) + 1)]
    
    # Remplir le tableau dp avec la meilleure valeur possible pour chaque poids
    for i in range(n):
        id_i, cost_i, profit_i = shares[i]
        for w in range(int(budget), int(cost_i) - 1, -1):
            dp[w] = max(dp[w], dp[w - int(cost_i)] + profit_i)
    
    # Récupérer le profit maximum
    max_profit = dp[int(budget)]
    
    # Backtracking pour trouver les actions sélectionnées
    selected = []
    w = int(budget)
    for i in range(n - 1, -1, -1):
        id_i, cost_i, profit_i = shares[i]
        if w >= int(cost_i) and abs(dp[w] - (dp[w - int(cost_i)] + profit_i)) < 1e-6:
            selected.append(id_i)
            w -= int(cost_i)
    selected.reverse()  # Restaurer l'ordre original
    
    # Calculer le coût total des actions sélectionnées
    total_cost = sum(cost for id_i, cost, profit in shares if id_i in selected)
    
    return selected, total_cost, max_profit

if __name__ == "__main__":
    # Test de la fonction avec le dataset 1
    result = optimized_investment("data/dataset1_Python+P3.csv")
    actions, cost, profit = result
    print("Actions sélectionnées :", actions)
    print("Coût total :", cost, "F CFA")
    print("Profit total :", profit, "F CFA") 
    
    from data_loader import load_data

def optimized_investment(file_path, budget=500000):
    shares = load_data(file_path)
    n = len(shares)
    dp = [0.0 for _ in range(int(budget) + 1)]
    for i in range(n):
        id_i, cost_i, profit_i = shares[i]
        for w in range(int(budget), int(cost_i) - 1, -1):
            dp[w] = max(dp[w], dp[w - int(cost_i)] + profit_i)
    max_profit = dp[int(budget)]
    selected = []
    w = int(budget)
    for i in range(n - 1, -1, -1):
        id_i, cost_i, profit_i = shares[i]
        if w >= int(cost_i) and abs(dp[w] - (dp[w - int(cost_i)] + profit_i)) < 1e-6:
            selected.append(id_i)
            w -= int(cost_i)
    selected.reverse()
    total_cost = sum(cost for id_i, cost, profit in shares if id_i in selected)
    return selected, total_cost, max_profit

if __name__ == "__main__":
    result = optimized_investment("data/dataset1_Python+P3.csv")
    actions, cost, profit = result
    print("Actions sélectionnées :", actions)
    print("Coût total :", cost, "F CFA")
    print("Profit total :", profit, "F CFA")