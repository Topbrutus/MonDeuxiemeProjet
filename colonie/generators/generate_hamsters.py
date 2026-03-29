import argparse
from pathlib import Path

TEMPLATE = Path("colonie/templates/hamster_template.md")
OUTPUT_DIR = Path("colonie/hamsters")

def build_hamster(idx: int) -> str:
    hamster_id = f"hamster_{idx:03d}"
    return f"""# {hamster_id}
- Nom : {hamster_id}
- Robot parent : Run
- Mission : A definir
- Points couleurs : {{}}
- Prestige : 0
- Radiote : non
- Jeton interne : {hamster_id}_genesis_v1
- Etat : non-actif
- Notes : genere automatiquement
"""

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, choices=[1,3,10], default=1)
    args = parser.parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    start = 900
    for offset in range(args.count):
        idx = start + offset
        path = OUTPUT_DIR / f"hamster_{idx:03d}.md"
        path.write_text(build_hamster(idx), encoding="utf-8")
        print(path)

if __name__ == "__main__":
    main()
