import csv

with open ('troupes_coreferenced.csv', newline='') as csvfile:
        troupe_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        troupLookup = {}

        for row in troupe_reader:
                all_combos = []
                for x in range(0,4):
                        for y in range(0,4):
                                if x != y:
                                        if len(row[x]) > 0 and len(row[y]) > 0:
                                                all_combos.append(row[x] + "|" + row[y])

		for a_combo in all_combos:
                        if a_combo not in troupLookup:
                                troupLookup[combo] = 0
                                troupLookup[combo] = troupLookup[combo] + 1
