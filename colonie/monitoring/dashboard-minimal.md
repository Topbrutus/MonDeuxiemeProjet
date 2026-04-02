# DASHBOARD-MINIMAL - Cockpit pilote

Tableau de bord trs ès sobre pour l’exploitation pilote interne contrôlée.

## Champs canoniques
- phase actuelle
- dernière validation
- statut projet
- robots actifs
- hamsters actifs
- fourmis actives
- tâches en cours
- bloqueurs
- dernier événement
- healthcheck

## Sources de vérité
- `STATE.md`
- `task_board.json`
- `events.jsonl`
- `colonie/indexes/task_registry.json`
- `colonie/indexes/state_global.json`

## View minimale remandés
```text
Phase : 14
Dernière validation : socle complet prêt
Statut : pilot-ready
Robots actifs : Brutus, Rob, Run
Hamsters actifs : 3
Fourmis actives : 12
Tâches : todo/doing/review/done
Bloqueurs : aucun majeur structurel
Dernier événement : task_0001 figée comme base opératoire pilote
Healthcheck : socle OK / traces OK / sécurité OK
```

## Règles
- cet cockpit ne déploie rimen
- pas de doublon de schéma
- toute néuvelle info doit repasser par hub, indexes et `STATE.md`
