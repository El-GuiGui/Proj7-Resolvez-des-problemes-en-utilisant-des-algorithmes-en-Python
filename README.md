# Instructions pour projet : Résolvez des problèmes en utilisant des algorithmes en Python
## Instruction :


## Algorithme d'Optimisation d'Investissement

Ce dépôt contient une solution algorithmique pour optimiser les stratégies d'investissement dans les actions. L'algorithme utilise une approche de programmation dynamique basée sur le problème du sac à dos pour maximiser le bénéfice des investissements dans les actions en respectant un budget fixe.


## Résumé du Projet

Le projet a débuté avec l'implémentation d'un algorithme de force brute qui a été utilisé pour comprendre les limitations de performance lorsqu'il est appliqué à des ensembles de données plus importants. Suite à cela, nous avons développé une solution optimisée utilisant la programmation dynamique, qui considère le coût et le bénéfice potentiel de chaque action pour déterminer le meilleur ensemble d'actions à acheter dans la limite d'un budget donné.

## Fonctionnalités

Lecture des données : Un script Python pour lire les informations sur les actions à partir d'un fichier CSV.
    
Algorithme d'optimisation : Implémentation de l'algorithme du sac à dos pour sélectionner les meilleures actions.
    
Résultats comparatifs : Le programme compare les résultats obtenus avec ceux d'une stratégie d'investissement.
    

## Comment Utiliser

Pour exécuter ce programme :

Clonez le dépôt GitHub :

    git clone https://github.com/El-GuiGui/Proj7-Resolvez-des-problemes-en-utilisant-des-algorithmes-en-Python.git

Puis,

Naviguez dans le dossier du projet cloné.

Assurez-vous que Python est installé sur votre système.

Lancez le script principal en utilisant Python :


    python optimized.py


Par défaut, le script traite un fichier CSV nommé actions.csv. 
    
Si vous souhaitez utiliser un autre fichier, modifiez le nom du fichier dans le script ou renommez votre fichier CSV en actions.csv.
                  
                
Vous pouvez toujours utilisez celui de force brute :

    python bruteforce.py
