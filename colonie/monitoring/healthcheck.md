# HEALTHCHECK - Pilote interne

Boot sain si existent et lisibles :
- `README.md`
- `STATE.md`
- `colonie/core/project_manifest.json`
- `colonie/indexes/state_global.json`
- `task_board.json`
- `colonie/indexes/task_registry.json`
- `events.jsonl` et `colonie/hub/events.jsonl`
- `colonie/monitoring/dashboard-minimal.md`
- `colonie/monitoring/dashboard_schema.json`
- `colonie/security/external_actions_policy.md`

## Contrôles minimum
- phase = 14
- status projet = pilot-ready
- task_0001 tracé dans le hub et le task registry
- aucun action externe réelle
- dashboard sobre, sans doublon de schéma

## Verdict
- socle OK
- traces OK
- sécurité OK
- dashboard OK
