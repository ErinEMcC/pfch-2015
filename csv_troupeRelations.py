import csv
import pprint

with open ('troupes_coreferenced.csv', newline='') as csvfile:
        troupe_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        #create a new dictionary to store all the troupe relation pairs and their counts/weights
        troupePairs = {}

        for row in troupe_reader:
                all_combos = []
                for x in range(0,4):
                        for y in range(0,4):
                                if x != y:
                                        if len(row[x]) > 0 and len(row[y]) > 0:
                                                all_combos.append(row[x] + "|" + row[y])

                for a_combo in all_combos:
                        if a_combo not in troupePairs:
                                troupePairs[a_combo] = 0
                        troupePairs[a_combo] = troupePairs[a_combo] + 1

        pprint.pprint (troupePairs)
