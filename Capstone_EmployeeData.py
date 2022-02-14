from pickle import DICT, GLOBAL
import os

employee_dummy = {"11233" : {"Name" : "Rachmat", "Gender" : "Men", "Age" : 25, "Resident" : "BSD", "Position" : "UI/UX", "Almamater" : "UMN"},
"1555" : {"Name" : "Ahmad", "Gender" : "Men", "Age" : 27, "Resident" : "Serpong", "Position" : "Digital Marketing", "Almamater" : "UPH"}}
employee = {}

def read_all_data():
    for i in employee_dummy:
        print("Employee ID : {}, Name : {}, Gender : {}, Age : {}, Resident : {}, Position : {}, Almamater : {} ".format(i,employee_dummy[i]["Name"], employee_dummy[i]["Gender"], employee_dummy[i]["Age"], employee_dummy[i]["Resident"], employee_dummy[i]["Position"], employee_dummy[i]["Almamater"]))
    menu_read_employee()


def read_spesific_data():
    code = input("Insert Employee ID: ").capitalize()
    if code in employee_dummy.keys():
        print("Employee ID : {}, Name : {}, Gender : {}, Age : {}, Resident : {}, Position : {}, Almamater : {} ".format(code,employee_dummy[code]["Name"], employee_dummy[code]["Gender"], employee_dummy[code]["Age"], employee_dummy[code]["Resident"], employee_dummy[code]["Position"], employee_dummy[code]["Almamater"]))
        menu_read_employee()
    else:
        print("Employee data not exists :( ")
        menu_read_employee()

def menu_read_employee():
    print("1. Report All Employee Data")
    print("2. Report Specific Data")
    print("3. Return Menu")
    read_menu = int(input("Choose menu Report: "))
    if read_menu == 1:
        read_all_data()
    elif read_menu == 2:
        read_spesific_data()
    elif read_menu == 3:
        employee_menu()
    else:
        menu_read_employee()

def create_employee_data():    
    global employee_id, new_employee
    new_employee = {}
    employee_id = input("Employee ID: ")
    if employee_id in employee_dummy.keys():
        print("Data Avaliable")
        employee_menu()
    else:
        global name
        name = input("Employee Name: ")
        new_employee["Name"] = name

        global gender
        gender = input("Sex [Men|Women]: ")
        new_employee["Gender"] = gender

        global age
        age = int(input("Age Employee:"))
        new_employee["Age"] = age

        global resident
        resident = input("Resident: ")
        new_employee["Resident"] = resident
        
        global position
        position = input("Job Position: ")
        new_employee["Position"] = position
        
        global almamater
        almamater = input("Almamater: ") # baik univ maupun job connector 
        new_employee["Almamater"] = almamater
        save_employee_data()
    

def save_employee_data():
    save = input("Save Data [Y|N]?: ").capitalize()
    global employee_dummy
    global employee

    if save == "Y":
        print("Data Saved :) ")
        employee_dummy[employee_id] = new_employee
        menu_create_employee()
    elif save == "N":
        print("Data Not Saved :( ")
        employee_dummy = employee_dummy
        menu_create_employee()
    else:
        save_employee_data()
           

### Menu Create
def menu_create_employee():
    print("1. Add Employee Data")
    print("2. Return Menu")
    create_menu = int(input("Choose Delete Menu: "))
    if create_menu == 1:
        create_employee_data()
    elif create_menu == 2:
        employee_menu()
    else:
        menu_create_employee()


#### Menu Update Data
def menu_update_employee():
    print("1. Update Employee Data")
    print("2. Return Menu")
    update_menu = int(input("Choose Update Menu: "))
    if update_menu == 1:
        check_data()
    elif update_menu == 2:
        employee_menu()
    else:
        menu_update_employee()

def check_data():
    global update_code
    update_code = input("Update Employee ID : ").capitalize()
    if update_code in employee_dummy:
        print("Employee ID : {}, Name : {}, Gender : {}, Age : {}, Resident : {}, Position : {}, Almamater : {} ".format(update_code,employee_dummy[update_code]["Name"], employee_dummy[update_code]["Gender"], employee_dummy[update_code]["Age"], employee_dummy[update_code]["Resident"], employee_dummy[update_code]["Position"], employee_dummy[update_code]["Almamater"]))
        update_data()
    else:
        print("Data Doesn't Exist :( ")
        menu_update_employee()
    
def edit_column():
    update_key = input("Enter column that into edit: ").capitalize()
    if update_key in employee_dummy[update_code]:
        change_data = input("Enter {} New : ".format(update_key)).capitalize()
        m = 1
        while m != 0:
            save_update = input("Are you sure to update data [Y|N]?: ").capitalize()
            if save_update == 'Y':
                employee_dummy[update_code][update_key] = change_data
                print("Data Updated")
                menu_update_employee()
                m = 0
            elif save_update == 'N':
                print("Data Doesn't Update")
                menu_update_employee()
                m = 0
            else:
                m = 1
    else:
        print("Please enter to right column :3")
        edit_column()

def update_data():
    update_choose = input("Press Y for update and N for not update [Y|N] : ").capitalize()
    if update_choose == 'Y':
        edit_column()
    elif update_choose == 'N':
        print("Data Doesn't Update :(")
        menu_update_employee()
    else:
        update_data()

#### Delete Menu Data

def menu_delete_employee():
    print("1. Delete Employee Data")
    print("2. Return Menu")
    delete_menu = int(input("Choose Delete Menu : "))
    if delete_menu == 1:
        delete_data()
    elif delete_menu == 2:
        employee_menu()
    else:
        menu_delete_employee()

def delete_data():
    global delete_code
    delete_code = input("Enter Employee ID : ").capitalize()
    if delete_code in employee_dummy.keys():
        delete_data_notif()
    else:
        print("Data Not Exist :( ")
        menu_delete_employee()

def delete_data_notif():
    hapus_data = input("Are you sure to delete data? [Y|N]:  ").capitalize()
    if hapus_data == 'Y':
        print("Data Now Delete :) ")
        employee_dummy.pop(delete_code)
        menu_delete_employee()
    elif hapus_data == 'N':
        print("Data Doesn't Delete :( ")
        menu_delete_employee()
    else:
        delete_data_notif()

def employee_menu():
    try:
        print("==== Blizz Employee Data ===\n ")
        print("1. Read Blizz Employee")
        print("2. Insert Blizz Employee")
        print("3. Update Blizz Employee")
        print("4. Delete Blizz Employee")
        print("5. Exit Menu")
        option = int(input("Select Menu: "))
        if option == 1:
            os.system('cls')
            menu_read_employee()
        elif option == 2:
            os.system('cls')
            menu_create_employee()
        elif option == 3:
            os.system('cls')
            menu_update_employee()
        elif option == 4:
            os.system('cls')
            menu_delete_employee()
        elif option == 5:
            os.system('cls')
            global exit
            exit = 0
            print("Thank you for Program :)")
        else:
            print("Option Invalid :( ")
            employee_menu()
    except:
        employee_menu()

employee_menu()
        