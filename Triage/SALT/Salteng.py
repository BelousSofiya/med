print("""Step 1: Sort. Global sorting:
1.The patient can walk - assess 3rd
2.The patient can move/make purposeful movements - assess 2nd
3.The patient can't move/is still/has an obvious life threat - assess 1st
Step 2: Assess. Individual Assessment. Lifesaving interventions:
1.Control major hemorrhage
2.Open airway(if child consider 2 rescue breaths
3.Chest decompression
4.Autoinjector antidotes""")
stand = input("""Step 3:
Can the patient breath? Write 'yes' or 'no'""")
if stand == "no":
    print("black")
else:
    questions = input("""1.Does the patient have a peripheral pulse?
2.Is the patient not in respiratory distress?
3.Is hemorrhage controlled?
4.Does the patient follow commands or make purposeful movements?
All 'yes' - write 'yes', any 'no' - write 'no'""")
    if questions=="yes":
        injuries = input("Minor injuries only? Write 'yes' or 'no'")
        if injuries=="yes":
            print("green")
        else:
            print("yellow")
    else:
        resources = input("""The patient is likely to survive given the available resources.
Write 'yes' or 'no'""")
        if resources=="no":
            print("blue")
        else:
            print("red")


