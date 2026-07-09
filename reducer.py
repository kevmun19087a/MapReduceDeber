import os
from collections import defaultdict

accesos = defaultdict(list)

for file in os.listdir('splits'):
    if file.endswith('.out'):
        with open(f"splits/{file}", 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                usuario, fecha, hora = line.split(" ")
                accesos[usuario].append(f"{fecha} {hora}")

print("=== Accesos fuera del horario laboral (08:00:00 - 18:00:00) ===")
for usuario, lista in accesos.items():
    print(f"{usuario} {len(lista)}")

print("\n=== Detalle de fechas y horas por usuario ===")
for usuario, lista in accesos.items():
    print(f"\nUsuario: {usuario}")
    for fecha_hora in sorted(lista):
        print(f"  - {fecha_hora}")

with open("resultados.txt", "w") as out:
    for usuario, lista in accesos.items():
        out.write(f"{usuario}: {len(lista)}\n")
        for fecha_hora in sorted(lista):
            out.write(f"  - {fecha_hora}\n")
        out.write("\n")