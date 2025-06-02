from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    appointments = relationship('Appointment', back_populates='patient')

    def __repr__(self):
        return f"<Patient {self.name}, Age: {self.age}>"

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)

    appointments = relationship('Appointment', back_populates='doctor')

    def __repr__(self):
        return f"<Doctor {self.name}, Spec: {self.specialization}>"

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    appointment_time = Column(DateTime, default=datetime.utcnow)

    patient = relationship('Patient', back_populates='appointments')
    doctor = relationship('Doctor', back_populates='appointments')

    def __repr__(self):
        return f"<Appointment {self.appointment_time} | Patient {self.patient_id} with Doctor {self.doctor_id}>"
