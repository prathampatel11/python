
birth_date_1 =int(input("Enter the male birth date only"))

birth_month_1=int(input("Enter the male birth month only"))

birth_date_2 =int(input("Enter the female birth date only"))

birth_month_2=int(input("Enter the female birth month only"))

if (birth_date_1>=21 and birth_month_1 == 3) or (birth_date_1<=19 and birth_month_1 == 4):
    print("your zodiac sign is aries.")

elif (birth_date_1>=20 and birth_month_1 == 4) or (birth_date_1<=20 and birth_month_1 == 5):
    print("your zodiac sign is tauras.")

elif (birth_date_1>=21 and birth_month_1 == 5) or (birth_date_1<=21 and birth_month_1 == 6):
    print("your zodiac sign is gemini.")

elif (birth_date_1>=22 and birth_month_1 == 6) or (birth_date_1<=22 and birth_month_1 == 7):
    print("your zodiac sign is cancer.")

elif (birth_date_1>=23 and birth_month_1 == 7) or (birth_date_1<=22 and birth_month_1 == 8):
    print("your zodiac sign is leo.")

elif (birth_date_1>=23 and birth_month_1 == 8) or (birth_date_1<=22 and birth_month_1 == 9):
    print("your zodiac sign is virgo.")

elif (birth_date_1>=23 and birth_month_1 == 9) or (birth_date_1<=22 and birth_month_1 == 10):
    print("your zodiac sign is libra.")        

elif (birth_date_1>=24 and birth_month_1 == 10) or (birth_date_1<=21 and birth_month_1 == 11):
    print("your zodiac sign is scorpio.")

elif (birth_date_1>=22 and birth_month_1 == 11) or (birth_date_1<=21 and birth_month_1 == 12):
    print("your zodiac sign is Sagittarius.")

elif (birth_date_1>=22 and birth_month_1 == 12) or (birth_date_1<=19 and birth_month_1 == 1):
    print("your zodiac sign is Capricorn.")

elif (birth_date_1>=20 and birth_month_1 == 1) or (birth_date_1<=18 and birth_month_1 == 2):
    print("your zodiac sign is Aquarius.")

elif  (birth_date_1>=19 and birth_month_1 == 2) or (birth_date_1<=22 and birth_month_1 == 3):
    print("your zodiac sign is Pisces.")

else:
    print("invlid birthdate or month")

print("now down has female zodiac sign.")

if (birth_date_2>=21 and birth_month_2 == 3) or (birth_date_1<=19 and birth_month_2 == 4):
    print("your zodiac sign is aries.")

elif (birth_date_2>=20 and birth_month_2 == 4) or (birth_date_1<=20 and birth_month_2 == 5):
    print("your zodiac sign is tauras.")

elif (birth_date_2>=21 and birth_month_2 == 5) or (birth_date_1<=21 and birth_month_2 == 6):
    print("your zodiac sign is gemini.")

elif (birth_date_2>=22 and birth_month_2 == 6) or (birth_date_1<=22 and birth_month_2 == 7):
    print("your zodiac sign is cancer.")

elif (birth_date_2>=23 and birth_month_2 == 7) or (birth_date_1<=22 and birth_month_2 == 8):
    print("your zodiac sign is leo.")

elif (birth_date_2>=23 and birth_month_2 == 8) or (birth_date_1<=22 and birth_month_2 == 9):
    print("your zodiac sign is virgo.")

elif (birth_date_2>=23 and birth_month_2 == 9) or (birth_date_1<=22 and birth_month_2 == 10):
    print("your zodiac sign is libra.")        

elif (birth_date_2>=24 and birth_month_2 == 10) or (birth_date_1<=21 and birth_month_2 == 11):
    print("your zodiac sign is scorpio.")

elif (birth_date_2>=22 and birth_month_2 == 11) or (birth_date_1<=21 and birth_month_2 == 12):
    print("your zodiac sign is Sagittarius.")

elif (birth_date_2>=22 and birth_month_2 == 12) or (birth_date_1<=19 and birth_month_2 == 1):
    print("your zodiac sign is Capricorn.")

elif (birth_date_2>=20 and birth_month_2 == 1) or (birth_date_1<=18 and birth_month_2 == 2):
    print("your zodiac sign is Aquarius.")

elif  (birth_date_2>=19 and birth_month_2 == 2) or (birth_date_2<=22 and birth_month_2 == 3):
    print("your zodiac sign is Pisces.")

else:
    print("invlid birthdate or month")

print("now let we check match zodiac sign and check compability male and female.")


fire = ["aries", "leo", "sagittarius"]
earth = ["taurus", "virgo", "capricorn"]
air = ["gemini", "libra", "aquarius"]
water = ["cancer", "scorpio", "pisces"]
 