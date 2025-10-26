vo = "aeiou"
wo = input("ENTER a string: ").lower()
vc = 0
cc = 0

for i in range(len(wo)):
    if wo[i].isalpha():        # consider letters only
        if wo[i] in vo:
            vc += 1
        else:
            cc += 1

print("Vowels:", vc)
print("Consonants:", cc)
