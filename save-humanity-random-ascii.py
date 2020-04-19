import random
import string

#constant to store number of ascii letters to be used. ower number results is higher chance of match
ASCII_LETTERS_TO_PICK = 3

results = []
patientList = []
virusList = []

N = int(input("how many patients would you like to check DNA maching?: "))
while N > 10:
    print("Maximum 10 patients can be requested to check matching in each run")
    N = int(input("how many patients would you like to check DNA maching?: "))
    
lenV = int(input("length of DNA for virus?: "))
lenP = int(input("length of DNA for patient?: "))

while lenV > lenP:
    print("\nVirus DNA length cannot be longer than patient's DNA. Please enter again!\n")
    lenV = int(input("length of DNA for virus?: "))
    lenP = int(input("length of DNA for patient?: "))
    
for k in range(N):
    asci = string.ascii_lowercase
    asci = "".join([asci[random.randint(0, len(asci) - 1)] for _ in range(ASCII_LETTERS_TO_PICK)])
    patient = [asci[random.randint(0, len(asci) - 1)] for _ in range(lenP)]
    virus = [asci[random.randint(0, len(asci) - 1)] for _ in range(lenV)]
    patient = ''.join(patient)
    virus = ''.join(virus)
    patientList.append(patient)
    virusList.append(virus)
    #patient DNA pairs
    pairs = ["".join([patient[i + j] for j in range(len(virus))]) for i in range(len(patient) - len(virus) + 1)]
    legalMatches = ["".join([item[i] for i in range(len(item)) if item[i] == virus[i]]) for item in pairs]
    legalIndices = [str(i) for i in range(len(pairs)) if ((len(pairs[i]) == len(legalMatches[i])) or ((len(pairs[i]) - 1) == len(legalMatches[i])))]
    results.append(" ".join(legalIndices))

# print out
print("\nNumber of patients: {}".format(N))
for i in range(len(results)):
    if results[i] == "":
        print("\nPatient ({}):\nNo match!".format(i+1))
        print("DNA of patient: {}\nDNA of virus: {}".format(patientList[i],virusList[i]))
        continue
    print("\nPatient ({}):\nMatched indices: {}".format(i+1, results[i]))
    print("DNA of patient: {}\nDNA of virus: {}".format(patientList[i],virusList[i]))