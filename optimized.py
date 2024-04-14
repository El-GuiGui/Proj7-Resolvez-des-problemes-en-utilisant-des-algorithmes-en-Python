# Lit les informations des actions à partir du fichier CSV que l'on a indiqué en fin de ce script.
def read_actions(filepath):
    actions = []
    with open(filepath, "r") as file:
        # Saute l'en-tête des titles
        next(file)
        for line in file:
            name, cost, profit_percentage = line.strip().split(",")
            # Convertir le coût en centimes
            cost = int(float(cost) * 100)
            profit_percentage = float(profit_percentage)
            profit = cost * (profit_percentage / 100)
            actions.append((name, cost, profit))
    return actions


def optimize_investment(actions, budget=500):
    # Filtrer pour exclure les actions dont le coût est de 0
    actions = [action for action in actions if action[1] > 0]

    # Convertir le budget en centimes
    budget_in_cents = budget * 100
    # Récupere le nombre d'actions après le filtre
    n = len(actions)
    dp_table = [[0 for _ in range(budget_in_cents + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget_in_cents + 1):
            action_name, action_cost, action_profit = actions[i - 1]
            if action_cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - action_cost] + action_profit)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    result = []
    w = budget_in_cents
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            result.append(actions[i - 1])
            w -= actions[i - 1][1]

    # Profit total en centimes
    total_profit = dp_table[n][budget_in_cents]
    # Calcul du coût total
    total_cost = sum(action[1] for action in result)

    # Convertir les résultats de centimes en euros
    result_euros = [(name, cost / 100, profit / 100) for (name, cost, profit) in result]
    total_profit_euros = total_profit / 100
    total_cost_euros = total_cost / 100

    return result_euros, total_profit_euros, total_cost_euros


# Paramêtres des fonctions
# Ajout du path du fichier csv
file_path = "actions2.csv"
actions_data = read_actions(file_path)
best_combination, best_profit, total_cost = optimize_investment(actions_data)


# Print # Affichage
print("Meilleure combinaison d'actions:")
for action in best_combination:
    print(f"{action[0]}: Coût = {action[1]}€, Bénéfice = {action[2]}€")

print(f"\nBénéfice total: {best_profit}€")
print(f"Coût total: {total_cost}€")
