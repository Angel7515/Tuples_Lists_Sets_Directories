import os # MODULE FOR FUNCTION WITH THE OS
import time as tm # MODULE FOR FUNCTION SLEEP
# THIS IS THE PRESENTATION
print("\t\tWELCOME TO PROGRAM FOR TUPLES - LISTS - SETS - DIRECTORIES")
print("\t\t\tTHIS IS A PRACTICE OF THE PYTHON COURSE")
print("\t\t CREATED BY: ING. MIGUEL ANGEL ANDRADE AYALA")
print("\t\t Email: 77angelayala55@gmail.com")

# THIS IS THE MAIN MENU
print(" PLEASE, SELECT AN OPTION BELOW")
print("\n\t\t 1. TUPLES\n\t\t 2. LIST\n\t\t 3. SETS\n\t\t 4. DIRECTORIES")
Choice = input("\t\t YOUR CHOICE ->  ") # SELECTED DATA ENTRY
tm.sleep(1) # WAIT A SECOND
os.system("cls") # COMMAND TO CLEAN THE SCREEN IF YOU S.O. IS LINUX USE "clear"
if Choice == '1':
    print("\t\t\t TUPLES (Item,Item,Item)")
elif Choice == '2':
    print("\t\t\t LISTS [Item,Item,Item]")
elif Choice == '3':
    print("\t\t\t SETS [Item,Item,Item]")
elif Choice == '4':
    print("\t\t\t LISTS [Item,Item,Item]")
else: 
    print(" XXX ELECCION FUERA DE RANGO XXX")