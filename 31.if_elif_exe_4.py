
birth_date =int(input("Enter birth date only"))

birth_month=int(input("Enter birth month only"))

if birth_date>31 and birth_month>12:
    print("invlid birthdate or month")

elif (birth_date>=21 and birth_month == 3) or (birth_date<=19 and birth_month == 4):
    print("your zodiac sign is aries.")

elif (birth_date>=20 and birth_month == 4) or (birth_date<=20 and birth_month == 5):
    print("your zodiac sign is tauras.")

elif (birth_date>=21 and birth_month == 5) or (birth_date<=21 and birth_month == 6):
    print("your zodiac sign is gemini.")

elif (birth_date>=22 and birth_month == 6) or (birth_date<=22 and birth_month == 7):
    print("your zodiac sign is cancer.")

elif (birth_date>=23 and birth_month == 7) or (birth_date<=22 and birth_month == 8):
    print("your zodiac sign is leo.")

elif (birth_date>=23 and birth_month == 8) or (birth_date<=22 and birth_month == 9):
    print("your zodiac sign is virgo.")

elif (birth_date>=23 and birth_month == 9) or (birth_date<=22 and birth_month == 10):
    print("your zodiac sign is libra.")        

elif (birth_date>=24 and birth_month == 10) or (birth_date<=21 and birth_month == 11):
    print("your zodiac sign is scorpio.")

elif (birth_date>=22 and birth_month == 11) or (birth_date<=21 and birth_month == 12):
    print("your zodiac sign is Sagittarius.")

elif (birth_date>=22 and birth_month == 12) or (birth_date<=19 and birth_month == 1):
    print("your zodiac sign is Capricorn.")

elif (birth_date>=20 and birth_month == 1) or (birth_date<=18 and birth_month == 2):
    print("your zodiac sign is Aquarius.")

else:
    print("your zodiac sign is Pisces.")

