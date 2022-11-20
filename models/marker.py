from dataclasses import dataclass
from extensions import db

@dataclass
class Marker(db.Model):
    __tablename__ = 'marker'

    id: int
    lat: float
    lng: float
    created_at: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat = db.Column(db.Float, primary_key=False)
    lng = db.Column(db.Float, primary_key=False)
    created_at = db.Column(db.DATE, primary_key=False)