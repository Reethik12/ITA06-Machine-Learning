import csv


with open("C:/Users/chait/Desktop/training.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)


num_attributes = len(data[0]) - 1
S = ["Ø"] * num_attributes
G = [["?"] * num_attributes]


for row in data:
    attributes = row[:-1]
    outcome = row[-1]

    if outcome == "Yes":
       
        for i in range(num_attributes):
            if S[i] == "Ø":
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = "?"

       
        G = [g for g in G if all(s == "?" or s == g[i] for i, s in enumerate(S))]

    else:
        
        new_G = []
        for g in G:
            for i in range(num_attributes):
                if S[i] != "?" and S[i] != attributes[i]:
                    new_hypothesis = g.copy()
                    new_hypothesis[i] = S[i]
                    if new_hypothesis not in new_G:
                        new_G.append(new_hypothesis)
        G = new_G


print("S (Most Specific Hypothesis):")
print(S)

print("\nG (Most General Hypotheses):")
for g in G:
    print(g)