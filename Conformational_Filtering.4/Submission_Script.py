import sys

input_file = "crest_conformers.xyz"
output_file = "crest_rotamers_sel.xyz"
ewin_kcal = 6.0
au2kcal = 627.509

def read_xyz(filename):
    structures = []
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line: break
            try:
                natoms = int(line.strip())
            except ValueError:
                break
            comment = f.readline()
            try:
                energy = float(comment.strip().split()[0])
            except:
                energy = 0.0
            coords = []
            for _ in range(natoms):
                coords.append(f.readline())
            structures.append({"n": natoms, "e": energy, "c": comment, "xyz": coords})
    return structures

try:
    data = read_xyz(input_file)
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
    sys.exit(1)
if not data:
    print("Error: No structures found!")
    sys.exit(1)
min_e = min(s["e"] for s in data)
print(f"Lowest Energy: {min_e:.6f} Hartrees")
kept = [s for s in data if (s["e"] - min_e) * au2kcal <= ewin_kcal]
with open(output_file, 'w') as f:
    for s in kept:
        f.write(f"{s['n']}\n")
        f.write(s["c"])
        for line in s["xyz"]:
            f.write(line)
print(f"Success! Filtered down to {len(kept)} structures.")
