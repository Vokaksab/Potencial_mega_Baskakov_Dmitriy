with open("scientist.txt", encoding="utf8") as file:
    lines = file.readlines()
data = []
scientists = set()
for line in lines:
    scientist, drug, date, component = line.strip().split("#")
    if drug not in scientists:
        scientists.add(drug)
    data.append((scientist, drug, date, component))
data.sort(key=lambda x: (x[2].split("-")))
with open("scientist_origin.txt", "w") as file:
    for line in data:
        file.write("#".join(line) + "\n")
alloupur_sci = [x[0] for x in data if x[1] == "Аллопуринол"]
original = min([x for x in data if x[1] == "Аллопуринол"], key=lambda x:
               x[2])[0]
print(alloupur_sci)
print(original)