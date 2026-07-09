import sys

filename = sys.argv[1]

# Horario laboral: 08:00:00 a 18:00:00 (ambos límites incluidos como "dentro")
HORA_INICIO = "08:00:00"
HORA_FIN = "18:00:00"

resultados = []

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        partes = line.split(" ")
        fecha = partes[0]
        hora = partes[1]
        usuario = partes[2].split(":")[1]

        if hora < HORA_INICIO or hora > HORA_FIN:
            resultados.append(f"{usuario} {fecha} {hora}")

with open(f"{filename}.out", 'w') as out:
    for r in resultados:
        out.write(r + "\n")
