from datetime import datetime

class ParkingSpot:
    def __init__(self, id, is_occupied):
        self.id = id
        self.is_occupied = is_occupied
        self.timestamp = datetime.now()

class User:
    def __init__(self, username):
        self.username = username
