# write a program that return current Date (google search)

def getcurrentdate(fmt="%d-%m-%y"):
    from datetime import date
    current_date = date.today()
    return current_date

current_date = getcurrentdate()
print(current_date.strftime("%d/%m/%Y"))    