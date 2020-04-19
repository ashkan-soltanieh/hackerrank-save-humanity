results = []
N = int(input("how many patients would you like to check?: "))
while N > 10:
    print("\nMaximum 10 patients can be requested to check matching in each run")
    N = int(input("\nhow many patients would you like to check dna maching?: "))
for k in range(N):
    dnas = input("Test No. ({}): DNA of Patient and Virus (space separated): ".format(k+1))
    patient, virus = dnas.strip().split()
    resultTemp = []
    legalMatches = []
    #split patient dna into pairs of same length as virus
    pairs = ["".join([patient[i + j] for j in range(len(virus))]) for i in range(len(patient) - len(virus) + 1)]
    
    #finds all match pairs
    for item in pairs:
        for i in range(len(item)):
            if item[i] == virus[i]:
                resultTemp.append(item[i])
        
        legalMatches.append("".join(resultTemp))
        resultTemp = []

    # finds index of all mathches
    legalIndices = []
    for i in range(len(pairs)):
        if ((len(pairs[i]) == len(legalMatches[i])) or ((len(pairs[i]) - 1) == len(legalMatches[i]))):
            legalIndices.append(str(i))
    
    legalIndices = " ".join(legalIndices)
    results.append(legalIndices)

# print out
print("\nNumber of patients: {}".format(N))
for i in range(len(results)):
    if results[i] == "":
        print("\nPatient ({}):\nNo match!".format(i+1))
        continue
    print("\nPatient ({}):\n{}".format(i+1, results[i]))