class SizeError(Exception):
    def __str__(self):
        return "Grid size not appropriate, grid value length should be (size*size)"

class ValueError(Exception):
    def __str__(self):
        return "Please input both 'size' and 'values' for grid"

class IdError(Exception):
    def __str__(self):
        return "Please enter id in query parameter"

class IdNotfoundError(Exception):
    def __str__(self):
        return "The entered id is not a valid id or was not found in the database"

class Id_x_yError(Exception):
    def __str__(self):
        return "Please enter valid id, x, y in query parameter"

class Id_xError(BaseException):
    def __init__(self, top_bottom):
        self.top_bottom = top_bottom

    def __str__(self):
        return f"Please enter valid id, {self.top_bottom} in query parameter"




