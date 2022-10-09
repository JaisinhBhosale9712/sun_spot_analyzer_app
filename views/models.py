from views import db

class Grid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grid_value = db.Column(db.String(200))
    grid_size = db.Column(db.Integer())
    timestamp = db.Column(db.Text(20))
    def __repr__(self):
        return f"id: {self.id}, grid_value: {self.grid_value}, grid_size: {self.grid_size}, timestamp: {self.timestamp}"


