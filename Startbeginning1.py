choice = input("What language would you prefer? Write 'eng', 'ru', 'ukr'")
if choice == "eng":
    stand = "Can the patient walk? print '+' or '-'"
    airways = "Does the patient have spontaneous breathing? write'+' or '-'"
    breath ="restore airway patency. Does the patient have spontaneous breathing now? write'+' or '-'"
    breath3 = "Do 5 gold breathes. Does the patient have spontaneous breathing? write'+' or '-'"
    age = "Is the patint a child 6 years or early? write'+' or '-'"
    breathing_rate = "Is breathing rate more then 30 in 1 minut? For children: is breathing rate less then 15 or more then 45? write'+' or '-'"
    pulse = "Does the patient have pulse on radial artery? write'+' or '-'"
    conscious = "Is he conscious? write'+' or '-'"
    g = "green"
    r = "red"
    y = "yellow"
    b = "black"
elif choice == "ru":
    stand = "Пациент может ходить? Напишите '+' или '-'"
    airways = "У пациента есть спонтанное дыхание? Напишите '+' или '-'"
    breath = "Восстановите проходимость дыхательных путей. Появилось ли спонтанное дыхание? Напишите '+' или '-'"
    breath3 = "Сделайте 5 золотых вдохов. У пациента появилось спонтанное дыхание? Напишите '+' или '-'"
    age = "Пациент - ребенок 6 лет или младше? Напишите '+' или '-'"
    breathing_rate = "Для взрослых: частота дыхания больше 30 в минуту? Для детей: частота дыхания меньше 15 или больше 45? Напишите '+' или '-'"
    pulse = "У пациента есть пульс на лучевой артерии? Напишите '+' или '-'"
    conscious = "Пациент в сознании? Напишите '+' или '-'"
    g = "зеленый"
    r = "красный"
    y = "желтый"
    b = "черный"  
else:
    stand = "Пацієнт може ходити? Напишіть '+' чи '-'"
    airways = "У пацієнта є спонтанне дихання? Напишіть '+' чи '-'"
    breath ="Відновіть прохідність дихальних шляхів. Чи з'явилося спонтанне дихання? Напишіть '+' чи '-'"
    breath3 = "Зробіть 5 золотих вдихів. У пацієнта з'явилось спонтанне дихання? Напишіть '+' чи '-'"
    age = "Пацієнт - дитина 6 років або молодше? Напишіть '+' чи '-'"
    breathing_rate = "Для дорослих: частота дихання більше 30 в минуту? Для дітей: частота дихання менше 15 або більше 45? Напишіть '+' чи '-'"
    pulse = "У пацієнта є пульс на променевій артеріі? Напишіть '+' чи '-'"
    conscious = "Пацієнт в свідомості? Напишіть '+' чи '-'"
    g = "зелений"
    r = "червоний"
    y = "жовтий"
    b = "чорний"
    
stand1=(input(stand))
if stand1 == "+":
    print(g)
    input
else:
    airways1=(input(airways))
    if airways1 =="-":
        breath1=(input(breath))
        if breath1 == "-":
            age1=input(age)
            if age1 =="+":
                breath31 = input(breath3)
                if breath31 == "-":
                    print(b)
                    input
                else:
                    print(r)
                    input
            else:
                print(b)
                input
        else:
            print(r)
            input
    else:
        breathing_rate1 = input(breathing_rate)
        if breathing_rate1 == "+":
            print(r)
            input
        else:
            pulse1 = input(pulse)
            if pulse1 == "-":
                print(r)
                input
            else:
                conscious1 = input(conscious)
                if conscious1 == "+":
                    print(y)
                    input
                else:
                    print(r)
                    input()   
    
    
#eye_opening, verbal_response, motor_response, consciousness15, consciousness14, \
        #consciousness11, consciousness9, consciousness7, consciousness5, consciousness3, E4, E3, E2, E1, V5, V4, V3, V2,\
        #V1, M6, M5, M4, M3, M2, M1, hr
    
    
        

