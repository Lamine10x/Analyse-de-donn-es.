# Analyse des Résultats : Test avec data_test.csv

## Résultats de la Force Brute

- **Actions sélectionnées** : ['Action-4', 'Action-5', 'Action-6', 'Action-8', 'Action-10', 'Action-11', 'Action-13', 'Action-18', 'Action-19', 'Action-20'] (10 actions)
- **Coût total** : 498000 F CFA
- **Profit total** : 99080 F CFA
- **Temps d'exécution** : 2.42 secondes

## Résultats de la Solution Optimisée

- **Actions sélectionnées** : ['Action-5', 'Action-8', 'Action-18'] (3 actions)
- **Coût total** : 96000 F CFA
- **Profit total** : 99080 F CFA
- **Temps d'exécution** : 1.94 secondes

## Comparaison et Conclusion

- **Efficacité** : La solution optimisée atteint le même profit maximal (99080 F CFA) avec 3 actions contre 10 pour la force brute, tout en utilisant un coût moindre (96000 vs 498000 F CFA).
- **Performance** : Temps comparable (1.94s vs 2.42s), mais l’optimisée est plus scalable pour de grands datasets.
- **Recommandation** : Privilégier la solution optimisée pour la soutenance et les datasets complets.

## Prochaines étapes

- Tester avec `dataset1_Python+P3.csv` (~196610 F CFA) et `dataset2_Python+P3.csv` (~193780 F CFA).
- Ajuster le budget si nécessaire.
