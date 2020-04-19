results = []

N = int(input("Number of tests to be checked (Max. 10): "))
while N > 10:
    N = int(input("You entered {}. Number of tests must be 10 or less. Enter again: ".format(N)))

for k in range(N):
    dnas = input("Test No.{}: DNA of human and virus(Space-separated): ".format(k + 1))
    patient, virus = dnas.split()
    # pairs list stores divided patients DNA based on length on virus DNA
    pairs = ["".join([patient[i + j] for j in range(len(virus))]) for i in range(len(patient) - len(virus) + 1)]
    # legalMatches list stores list of matched letters
    legalMatches = ["".join([pair[i] for i in range(len(pair)) if pair[i] == virus[i]]) for pair in pairs]
    # legalIndecies list finds the index of matched letters
    legalIndices = [str(i) for i in range(len(pairs)) if ((len(pairs[i]) == len(legalMatches[i])) or ((len(pairs[i]) - 1) == len(legalMatches[i])))]
    results.append(" ".join(legalIndices))

# print out
for i in range(len(results)):
    if results[i] == "":
        print("Match index(es) of test ({}): No Match!".format(i + 1))
        continue
    print("Match index(es) of test ({}): {}".format(i + 1, results[i]))
