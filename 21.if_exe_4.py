
brother_1_age = int(input("enter_the_age_of_brother_1 ="))

brother_2_age = int(input("enter_the_age_of_brother_2 ="))

if brother_1_age<brother_2_age:
    print("elder_brother_is_brother_2")
    print("elder_brother_age_is",brother_2_age)

if brother_1_age>brother_2_age:
    print("elder_brother_is_brother_1")
    print("elder_brother_age_is",brother_1_age)

if brother_1_age==brother_2_age:
    print("no_one_is_elder_brother.brothers_age_are_same.")