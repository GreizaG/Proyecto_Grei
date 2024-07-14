from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Technicians(db.Model):
    __tablename__ = "technicians"
    id = db.Column(db.Integer, primary_key=True)
    complete_name = db.Column(db.String(50), nullable=False)
    card_id_type = db.Column(db.String(20))
    id_number = db.Column(db.BigInteger, unique=True)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(20), nullable=False, default='technician')
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return 'Tecnico: {}'.format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "complete_name": self.complete_name,
            "card_id_type": self.card_id_type,
            "id_number": self.id_number,
            "user_type": self.user_type 
        }

class Vehicles(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    plate_vin = db.Column(db.String(17), nullable=False, unique=True)
    odometer = db.Column(db.BigInteger, nullable=False)
    service_type = db.Column(db.String(20))
    entry_date = db.Column(db.Date)
    entry_time = db.Column(db.Time)
    brand = db.Column(db.String(10))
    model = db.Column(db.String(10))
    status_service = db.Column(db.String(20), nullable=False)
    place = db.Column(db.String(20))
    conversion_kit = db.Column(db.String(20))

    def __repr__(self):
        return 'Ingresa vehículo de placa/VIN: {}'.format(self.plate_vin)

    def serialize(self):
        return {
            "id": self.id,
            "plate_vin": self.plate_vin,
            "odometer": self.odometer,
            "entry_date": self.entry_date,
            "entry_time": self.entry_time,
            "brand": self.brand,
            "status_service": self.status_service,
            "place": self.place,
            "model": self.model,
            "conversion_kit": self.conversion_kit
        }

class Comercials(db.Model):
    __tablename__ = "comercials"
    id = db.Column(db.Integer, primary_key=True)
    complete_name = db.Column(db.String(50), nullable=False)
    card_id_type = db.Column(db.String(20))
    id_number = db.Column(db.BigInteger, unique=True)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(20), nullable=False, default='technician')
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return 'Tecnico: {}'.format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "complete_name": self.complete_name,
            "card_id_type": self.card_id_type,
            "id_number": self.id_number,
            "user_type": self.user_type 
        }