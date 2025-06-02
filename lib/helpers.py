
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
