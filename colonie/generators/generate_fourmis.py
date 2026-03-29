import argparse
from pathlib import Path

OUTPUT_DIR = Path("colonie/fourmis")

def build_fourmi(idx: int, hamster_parent: str, specialite: str, couleur: str) -> str:
    fourmi_id = f"fourmi_{idx:04d}"
    return f"""# {fourmi_id}
- Hamster parent : {hamster_parent}
- Specialite : {specialite}
- Couleur logique : {couleur}
- Points : 0
- Jeton interne : {fourmi_id}_{hamster_parent}_v1
- Etat : non-actif
- Sorties autorisees : micro-taches specialisees
- Notes : genere automatiquement
"""

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=2)
    parser.add_argument("--specialites", nargs="+", default=["analyse","tri"])
    parser.add_argument("--hamster", default="hamster_001")
    args = parser.parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    couleurs = ["AND+","NOR-","OR+","XNOR+"]
    start = 9000
    for offset in range(args.count):
        idx = start + offset
        specialite = args.specialites[offset % len(args.specialites)]
        couleur = couleurs[offset % len(couleurs)]
        path = OUTPUT_DIR / f"fourmi_{idx:04d}.md"
        path.write_text(build_fourmi(idx, args.hamster, specialite, couleur), encoding="utf-8")
        print(path)

if __name__ == "__main__":
    main()
