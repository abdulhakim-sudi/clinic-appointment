from lib.helpers import add_doctor, add_patient, list_doctors, list_patients
from lib.db.models import create_tables

def main():
    create_tables()  # Ensure tables exist before anything else

    while True:
        print("""
=== Clinic Appointment System ===
1. Add Patient
2. Add Doctor
3. List Patients
4. List Doctors
5. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_patient()
        elif choice == "2":
            add_doctor()
        elif choice == "3":
            list_patients()
        elif choice == "4":
            list_doctors()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
