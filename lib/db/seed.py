from lib.db.models import Doctor, Patient, session

# Sample doctors
doctors = [
    Doctor(name="Dr. Alice"),
    Doctor(name="Dr. Bob"),
]

# Sample patients
patients = [
    Patient(name="Jane Doe"),
    Patient(name="John Smith"),
]

# Add to DB
session.add_all(doctors + patients)
session.commit()

print("Database seeded with sample doctors and patients!")
