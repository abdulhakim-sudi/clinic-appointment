from lib.db.models import Doctor, Patient, session

def add_doctor():
    name = input("Enter doctor name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    new_doctor = Doctor(name=name)
    session.add(new_doctor)
    session.commit()
    print(f"Doctor '{name}' added successfully!")

def add_patient():
    name = input("Enter patient name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    new_patient = Patient(name=name)
    session.add(new_patient)
    session.commit()
    print(f"Patient '{name}' added successfully!")

def list_doctors():
    doctors = session.query(Doctor).all()
    if not doctors:
        print("No doctors found.")
        return
    print("\nDoctors:")
    for doctor in doctors:
        print(f"{doctor.id}: {doctor.name}")

def list_patients():
    patients = session.query(Patient).all()
    if not patients:
        print("No patients found.")
        return
    print("\nPatients:")
    for patient in patients:
        print(f"{patient.id}: {patient.name}")
