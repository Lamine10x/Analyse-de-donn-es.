from brute_force import brute_force_investment
from data_loader import load_data

def test_brute_force():
    # Test avec data_test.csv
    file_path = "data/data_test.csv"
    budget = 500000
    actions, cost, profit = brute_force_investment(file_path, budget)
    assert len(actions) > 0, "Aucune action sélectionnée par Force Brute"
    assert cost <= budget, "Coût dépasse le budget avec Force Brute"
    assert profit == 99080.0, "Profit incorrect, attendu 99080.0 F CFA"
    print(f"Test Force Brute réussi : Actions {actions}, Coût {cost} F CFA, Profit {profit} F CFA")

if __name__ == "__main__":
    test_brute_force()