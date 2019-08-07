from app.app import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rider = db.relationship("Rider", uselist=False, back_populates="user") 
    driver = db.relationship("Driver", uselist=False, back_populates="user") 

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('UTF-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    




