import tkinter as tk
from tkinter import ttk, messagebox
from brute_force import brute_force_investment
from optimized_solution import optimized_investment
from data_loader import load_data
import time

def run_analysis(file_path, budget, method):
    try:
        shares = load_data(file_path)
        if not shares:
            messagebox.showerror("Erreur", "Aucune donnée chargée.")
            return

        start_time = time.time()
        if method == "brute":
            actions, cost, profit = brute_force_investment(file_path, budget)
            method_name = "Force Brute"
        elif method == "optimized":
            actions, cost, profit = optimized_investment(file_path, budget)
            method_name = "Solution Optimisée"

        end_time = time.time()
        execution_time = end_time - start_time

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"\n=== Résultats pour {file_path} ===\n")
        result_text.insert(tk.END, f"{method_name} :\n")
        result_text.insert(tk.END, f"  Actions : {actions}\n")
        result_text.insert(tk.END, f"  Coût total : {cost} F CFA\n")
        result_text.insert(tk.END, f"  Profit total : {profit} F CFA\n")
        result_text.insert(tk.END, f"  Temps d'exécution : {execution_time} secondes\n")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def clean_dataset(file_path):
    try:
        shares = load_data(file_path)
        if shares:
            messagebox.showinfo("Succès", f"Dataset {file_path} nettoyé avec succès.")
            return file_path
        else:
            messagebox.showwarning("Avertissement", f"Échec du nettoyage de {file_path}.")
            return None
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du nettoyage : {e}")
        return None

def on_analyze():
    file_path = dataset_var.get()
    if file_path == "Autre":
        file_path = custom_path_entry.get().strip()
        if not file_path:
            messagebox.showerror("Erreur", "Veuillez entrer un chemin personnalisé.")
            return
    budget = float(budget_entry.get() or 500000)
    clean = clean_var.get()
    if clean:
        file_path = clean_dataset(file_path)
        if not file_path:
            return
    method = method_var.get()
    run_analysis(file_path, budget, method)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Analyse d'Investissements en Actions")
root.geometry("600x400")

# Variables
dataset_var = tk.StringVar(value="data/data_test.csv")
method_var = tk.StringVar(value="optimized")
clean_var = tk.BooleanVar(value=False)

# Frame pour les datasets
dataset_frame = ttk.LabelFrame(root, text="Sélection du Dataset")
dataset_frame.pack(pady=10, padx=10, fill="x")
ttk.Label(dataset_frame, text="Choisissez un dataset :").pack(side=tk.LEFT)
datasets = ["data/data_test.csv", "data/dataset1_Python+P3.csv", "data/dataset2_Python+P3.csv", "Autre"]
ttk.OptionMenu(dataset_frame, dataset_var, "data/data_test.csv", *datasets).pack(side=tk.LEFT, padx=5)
custom_path_entry = ttk.Entry(dataset_frame)
custom_path_entry.pack(side=tk.LEFT, padx=5)

# Frame pour le nettoyage
clean_frame = ttk.LabelFrame(root, text="Nettoyage")
clean_frame.pack(pady=10, padx=10, fill="x")
ttk.Checkbutton(clean_frame, text="Nettoyer le dataset", variable=clean_var).pack(side=tk.LEFT)

# Frame pour la méthode
method_frame = ttk.LabelFrame(root, text="Méthode d'Analyse")
method_frame.pack(pady=10, padx=10, fill="x")
ttk.Radiobutton(method_frame, text="Force Brute", variable=method_var, value="brute").pack(side=tk.LEFT, padx=5)
ttk.Radiobutton(method_frame, text="Solution Optimisée", variable=method_var, value="optimized").pack(side=tk.LEFT, padx=5)

# Frame pour le budget
budget_frame = ttk.LabelFrame(root, text="Budget")
budget_frame.pack(pady=10, padx=10, fill="x")
ttk.Label(budget_frame, text="Budget (F CFA, défaut 500000) :").pack(side=tk.LEFT)
budget_entry = ttk.Entry(budget_frame)
budget_entry.pack(side=tk.LEFT, padx=5)
budget_entry.insert(0, "500000")

# Bouton d'analyse
analyze_button = ttk.Button(root, text="Lancer l'Analyse", command=on_analyze)
analyze_button.pack(pady=10)

# Zone de résultats
result_frame = ttk.LabelFrame(root, text="Résultats")
result_frame.pack(pady=10, padx=10, fill="both", expand=True)
result_text = tk.Text(result_frame, height=10)
result_text.pack(fill="both", expand=True)

# Démarrer la boucle principale
root.mainloop()