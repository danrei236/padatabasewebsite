from app import db

class Member(db.Model):
    # Personal Details
    id = db.Column(db.Integer, primary_key=True)
    first_names = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(13), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    language = db.Column(db.String(20), nullable=False)

    # Contact Details
    mobile_number = db.Column(db.String(10), nullable=False)
    alternative_number = db.Column(db.String(10))

    # Address Details
    ward = db.Column(db.String(2), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    municipality = db.Column(db.String(100), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    street_address = db.Column(db.String(100), nullable=False)
    suburb = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(4), nullable=False)

    # Voting Details
    iec_registered = db.Column(db.String(3), nullable=False)
    pat_no = db.Column(db.String(100))
    voting_district = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Member('{self.first_names}', '{self.surname}', '{self.id_number}')"
