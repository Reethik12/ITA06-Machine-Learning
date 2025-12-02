import csv

file = open("enjoysport.csv", "r")
csv_reader = csv.reader(file)

dataset = []
for row in csv_reader:
    dataset.append(row)

file.close()   

concepts = [row[:-1] for row in dataset]   
target = [row[-1] for row in dataset]      

print("Concepts:", concepts)
print("Target:", target)

def candidate_elimination(concepts, target):

    specific_h = None
    for i in range(len(target)):
        if target[i] == "yes":
            specific_h = concepts[i].copy()
            break

    general_h = [["?" for _ in specific_h]]

    print("\nInitial S:", specific_h)
    print("Initial G:", general_h)

    for i in range(len(target)):
        instance = concepts[i]
        output = target[i]

        print("\nExample", i+1, ":", instance, "->", output)

        if output == "yes":
            # Generalize S
            for j in range(len(specific_h)):
                if instance[j] != specific_h[j]:
                    specific_h[j] = "?"
        else:
            # Specialize G
            new_rules = []
            for j in range(len(specific_h)):
                if instance[j] != specific_h[j]:
                    rule = ["?" for _ in specific_h]
                    rule[j] = specific_h[j]
                    new_rules.append(rule)
            general_h.extend(new_rules)

        print("Updated S:", specific_h)
        print("Updated G:", general_h)

    cleaned_g = []
    for g in general_h:
        if g != ["?" for _ in specific_h] and g not in cleaned_g:
            cleaned_g.append(g)

    return specific_h, cleaned_g

final_s, final_g = candidate_elimination(concepts, target)

print("\nFinal Specific Hypothesis S:", final_s)
print("Final General Hypothesis G:", final_g)
