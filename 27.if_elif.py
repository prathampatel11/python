day = int(input("Enter week day ="))
if day==1: #== != < > <= >=
    print("Monday")
    print("_"*100)
    print("Days choghadliya : Amrit, Kaal, Shubh, Rog, Udveg, Chaal, Laabh, Amrit")
    print("Night choghadliya : Rog, Kaal, Laabh, Udveg, Shubh, Amrit, Chaal, Rog")
elif day==2:
    print("Tuesday")
    print("_"*100)
    print("Days choghadiya : Rog, Udveg, Chaal, Laabh, Amrit, Kaal, Shubh, Rog")
    print("Night choghadiya : Kaal, Laabh, Udveg, Shubh, Amrit, Chaal, Rog, Kaal")
elif day==3:
    print("Wednesday")
    print("_"*100)
    print("Days choghadiya : Laabh, Amrit, Kaal, Shubh, Rog, Udveg, Chaal, Laabh")
    print("Night choghadiya : Laabh, Udveg, Shubh, Amrit, Chaal, Rog, Kaal, Laabh")
elif day==4:
    print("Thursday")
    print("_"*100)
    print("Days choghadiya : Shubh, Rog, Udveg, Chaal, Laabh, Amrit, Kaal, Shubh")
    print("Night choghadiya : Udveg, Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg")
elif day==5:
    print("Friday")
    print("_"*100)
    print("Days choghadiya : Chaal, Laabh, Amrit, Kaal, Shubh, Rog, Udveg, Chaal")
    print("Night choghadiya : Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh")
elif day==6:
    print("Saturday")
    print("_"*100)
    print("Days choghadiya : Kaal, Shubh, Rog, Udveg, Chaal, Laabh, Amrit, Kaal")
    print("Night choghadiya : Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh, Amrit")
elif day==7:
    print("Sunday")
    print("_"*100)
    print("Days choghadiya : Udveg, Chaal, Laabh, Amrit, Kaal, Shubh, Rog, Udveg")
    print("Night choghadiya : Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh")
else:
    print("it is not valid day of week")
    
print(""" Amrit → Very auspicious (best time)
Shubh → Good time
Laabh → Gain/profit (favorable)
Chaal (Char) → Neutral (okay for routine work)
Udveg → Stressful (avoid important work)
Rog → Illness (inauspicious)
Kaal → Very inauspicious (avoid completely)
Best Choghadia to Use
-----------------------
Amrit, Shubh, Laabh
-----------------------
Avoid
Kaal, Rog, Udveg""")