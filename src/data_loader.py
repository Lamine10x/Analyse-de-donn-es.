import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, sep=';', encoding='latin-1')
    if 'Actions' in df.columns:
        id_col = 'Actions'
    elif 'name' in df.columns:
        id_col = 'name'
    else:
        raise KeyError("Aucune colonne 'Actions' ou 'name' trouvée.")
    if 'Cout par action (en euros)' in df.columns:
        cost_col = 'Cout par action (en euros)'
    elif 'price' in df.columns:
        cost_col = 'price'
    elif 'cost' in df.columns:
        cost_col = 'cost'
    else:
        raise KeyError("Aucune colonne 'Cout par action (en euros)', 'price' ou 'cost' trouvée.")
    if 'Bénéfice après 2 ans' in df.columns:
        profit_col = 'Bénéfice après 2 ans'
    elif 'profit_pct' in df.columns:
        profit_col = 'profit_pct'
    else:
        raise KeyError("Aucune colonne 'Bénéfice après 2 ans' ou 'profit_pct' trouvée.")
    df[id_col] = df[id_col].astype(str)
    df[cost_col] = df[cost_col].astype(float)
    def convert_profit(value, cost):
        if isinstance(value, str) and '%' in value:
            try:
                percentage = float(value.strip('%'))
                return cost * percentage / 100
            except ValueError:
                raise ValueError(f"Format de pourcentage invalide : {value}")
        else:
            return float(value) if profit_col == 'Bénéfice après 2 ans' else cost * float(value) / 100
    df[profit_col] = [convert_profit(df.loc[i, profit_col], df.loc[i, cost_col]) for i in df.index]
    df = df[df[cost_col] > 0]
    return list(zip(df[id_col], df[cost_col], df[profit_col]))

if __name__ == "__main__":
    try:
        data = load_data("data/data_test.csv")
        print("Premières 5 actions chargées :")
        for action in data[:5]:
            print(f"ID: {action[0]}, Coût: {action[1]}, Profit: {action[2]}")
    except Exception as e:
        print(f"Erreur : {e}")