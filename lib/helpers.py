
from lib.db.models import Doctor, Patient, session
def add_doctor():
    """Add a new doctor to the database."""
    pass
def add_doctor():
    """Add a new doctor to the database."""
    name = input("Enter doctor name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    new_doctor = Doctor(name=name)
    session.add(new_doctor)
    session.commit()
    print(f"Doctor '{name}' added successfully!")
def add_patient():
    """Add a new patient to the database."""
    pass
    name = input("Enter patient name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    new_patient = Patient(name=name)
    session.add(new_patient)
    session.commit()
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
from lib.db.models import Appointment

def add_appointment():
    try:
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        date = input("Enter appointment date (YYYY-MM-DD): ").strip()

        appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, date=date)
        session.add(appointment)
        session.commit()
        print("Appointment added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def list_appointments():
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments found.")
        return
    print("\nAppointments:")
    for appt in appointments:
        print(f"ID: {appt.id} | Patient: {appt.patient.name} | Doctor: {appt.doctor.name} | Date: {appt.date}")
