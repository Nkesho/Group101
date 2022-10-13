name1 = input("enter name1: ")
name2 = input("enter name2: ")

ammount_of_vowels_in_name1 = 0
ammount_of_vowels_in_name2 = 0

for char in name1:
        if char in "aeiou":
            ammount_of_vowels_in_name1 +=1

for char in name2:
        if char in "aeiou":
            ammount_of_vowels_in_name2 +=1

if ammount_of_vowels_in_name1 > ammount_of_vowels_in_name2:
    print("  1 is more and contains {} vowels".format(ammount_of_vowels_in_name1))
elif ammount_of_vowels_in_name1< ammount_of_vowels_in_name2:
    
    print("  2 is more and contains {} vowels".format(ammount_of_vowels_in_name2))
else:
    print("equal")
