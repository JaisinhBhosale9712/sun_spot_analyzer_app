from views.exceptions import IdError, IdNotfoundError, Id_x_yError, Id_xError
from views import db
from views.models import Grid


def check_id_error(grid_id):
    try:
        if not grid_id:
            raise IdError
    except IdError as e:
        return {"message": e.__str__()}
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    try:
        if not grid:
            raise IdNotfoundError
    except IdNotfoundError as e:
        return {"message": e.__str__()}
    return "success"


def check_id_x_y_error(grid_id, x, y):
    try:
        if not grid_id or not x or not y:
            raise Id_x_yError
    except Id_x_yError as e:
        return {"message": e.__str__()}
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    try:
        if not grid:
            raise IdNotfoundError
    except IdNotfoundError as e:
        return {"message": e.__str__()}
    try:
        if int(x) and int(y):
            pass
    except Exception as e:
        return {"message": e.__str__()}
    try:
        if int(x) > grid.grid_size or int(y) > grid.grid_size or int(x) < 1 or int(y) < 1:
            raise Id_x_yError
    except Id_x_yError as e:
        return {"message": e.__str__()}
    return "success"


def check_id_x_error(grid_id, x, top_bottom):
    try:
        if not grid_id:
            raise IdError
    except IdError as e:
        return {"message": e.__str__()}
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    try:
        if not grid:
            raise IdNotfoundError
    except IdNotfoundError as e:
        return {"message": e.__str__()}
    try:
        if not x:
            raise Id_xError(top_bottom)
    except Id_xError as e:
        return {"message": e.__str__()}
    try:
        if int(x):
            pass
    except Exception as e:
        return {"message": e.__str__()}
    try:
        if int(x) > grid.grid_size * grid.grid_size or int(x) < 1:
            raise Id_xError(top_bottom)
    except Id_xError as e:
        return {"message": e.__str__()}
    return "success"
