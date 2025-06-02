from lib.helpers import (
    add_doctor,
    add_patient,
    list_doctors,
    list_patients,
    add_appointment,
    list_appointments,
)

def main():
    while True:
        print("\n=== Clinic Appointment System ===")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. List Patients")
        print("4. List Doctors")
        print("5. Add Appointment")
        print("6. List Appointments")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_patient()
        elif choice == '2':
            add_doctor()
        elif choice == '3':
            list_patients()
        elif choice == '4':
            list_doctors()
        elif choice == '5':
            add_appointment()
        elif choice == '6':
            list_appointments()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
