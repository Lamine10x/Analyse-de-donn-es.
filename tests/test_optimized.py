from optimized_solution import optimized_investment
from data_loader import load_data

def test_optimized():
    # Test avec data_test.csv
    file_path = "data/data_test.csv"
    budget = 500000
    actions, cost, profit = optimized_investment(file_path, budget)
    assert len(actions) > 0, "Aucune action sélectionnée par Optimisée"
    assert cost <= budget, "Coût dépasse le budget avec Optimisée"
    assert profit == 99080.0, "Profit incorrect, attendu 99080.0 F CFA"
    print(f"Test Optimisé réussi : Actions {actions}, Coût {cost} F CFA, Profit {profit} F CFA")

if __name__ == "__main__":
    test_optimized()