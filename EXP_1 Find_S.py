data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High",   "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High",   "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High",   "Strong", "Cool", "Change", "Yes"]
]


hypothesis = ["Ø", "Ø", "Ø", "Ø", "Ø", "Ø"]


for row in data:
    attributes = row[:-1]   
    result = row[-1]        

    if result == "Yes":     
        for i in range(len(hypothesis)):
            if hypothesis[i] == "Ø":
                hypothesis[i] = attributes[i]
            elif hypothesis[i] != attributes[i]:
                hypothesis[i] = "?"


print("Final Hypothesis:")
print(hypothesis)
