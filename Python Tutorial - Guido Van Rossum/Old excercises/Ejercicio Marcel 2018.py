list_of_quantities = []
list_of_proms = []

with open("sample_data.csv", "r") as table:
    all_lines = table.readlines()
    cont1 = 0
    sum1 = 0
    hours = list(range(24))
    for hour in hours:
        for line in all_lines:
            if int(line[11]+line[12]) == hour:
                cont1 += 1
                sum1 += float(line[20:])
        list_of_quantities.append((hour,cont1,sum1))

for tuple in list_of_quantities:
    if tuple[2] != 0:
      list_of_proms.append((tuple[0],tuple[2]/tuple[1]))
    else:
        continue

print(list_of_quantities)
print(list_of_proms)
print(len(all_lines))
