from itertools import combinations

# Liste des actions
actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 20),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18),
]


# Calcul du bénéfice etde la meilleure combinaison
def optimize_investment(actions, budget=500):  # -changer la valeur au besoin du budget d'investissement du client
    best_combination = []
    best_profit = 0

    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            total_cost = sum(action[1] for action in combination)
            total_profit = sum(action[1] * action[2] / 100 for action in combination)

            if total_cost <= budget and total_profit > best_profit:
                best_profit = total_profit
                best_combination = combination

    return best_combination, best_profit


# Résultat et affichage bénéfice total .
best_combination, best_profit = optimize_investment(actions)
# Calcul du coût total des actions choisis
total_cost = sum(action[1] for action in best_combination)
print("Meilleure combinaison d'actions à acheter:")
for action in best_combination:
    print(f"{action[0]}: Coût = {action[1]}, Bénéfice = {action[1] * action[2] / 100} €")

print(f"\nCoût total des actions: {total_cost} €")
print(f"\nBénéfice total: {best_profit} €")
