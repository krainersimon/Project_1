from datetime import datetime
from typing import Dict

# Eingabe der Start-ID
first_experiment_id: int = input("Start-ID eingeben: ")

# Sicherstellen, dass die Eingabe eine gültige ganze Zahl ist
try:
    first_experiment_id = int(first_experiment_id)
except ValueError:
    print("❌ Fehler: Die Eingabe muss eine ganze Zahl sein.")
    exit()

experiments: Dict[int, Dict[str, str]] = {}

heutiges_datum = datetime.today().strftime("%d.%m.%Y")

# 10 Experimente erstellen
for i in range(10):
    experiment_id = first_experiment_id + i
    experiments[experiment_id] = {
        "Versuchsleiter": "Simon",
        "Erstellungsdatum": heutiges_datum
    }

# Ausgabe
print("\n Die ersten fünf Experimente:\n")
for id_num, details in list(experiments.items())[:5]:
    print(f"ID: {id_num}")
    print(f"Versuchsleiter: {details['Versuchsleiter']}")
    print(f"Erstellungsdatum: {details['Erstellungsdatum']}\n")

# ungerade ID
gerade_experimente = sum(1 for id_num in experiments if id_num % 2 == 0)
print(f"Anzahl der Experimente mit gerader ID: {gerade_experimente}")

