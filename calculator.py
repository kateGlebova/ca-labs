def calorie_calc(sex, weight, height, age, load):
    if load == 0:
        AMR = 1.2
    elif 1 <= load <= 3:
        AMR = 1.375
    elif 3 <= load <= 5:
        AMR = 1.55
    elif 6 <= load <= 7:
        AMR = 1.725
    elif load > 7:
        AMR = 1.9
    if sex == 'male':
        BMR = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)
    else:
        BMR = 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)
    return AMR*BMR