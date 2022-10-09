from flask import request, jsonify
from views import application, db
from views.models import Grid
import json
from views.exceptions import SizeError, ValueError
from datetime import datetime as dt
from services.gridvalue_to_gridmatrix import gridmatrix
from services.scores import get_all_score, get_all_score_id, get_min_score, get_max_score, get_top_x_score, \
    get_bottom_x_score
from services.check_args_error import check_id_error, check_id_x_y_error, check_id_x_error


@application.route("/sun-spot-analyser-api/")
def home():
    return jsonify({"message": "Welcome to Sun Spot Analyser web app"})


@application.route("/sun-spot-analyser-api/grid", methods=["POST"])
def grid():
    """
        Posting grid values and grids size to database
        return: id of specific grid (json)
    """
    try:
        if not request.data:
            raise ValueError
    except ValueError as e:
        return jsonify({"message": e.__str__()}), 400
    grid_data = json.loads(request.data)
    grid_size = grid_data["size"] if "size" in grid_data else None
    grid_value = grid_data["values"] if "values" in grid_data else None
    try:
        if not grid_size or not grid_value:
            raise ValueError
    except ValueError as e:
        return jsonify({"message": e.__str__()}), 400

    try:
        grid_value = list(map(int, grid_value.split(",")))
        grid_size = int(grid_size)
    except Exception:
        return jsonify({"message": "Please check the entered values, size should be integer and values should be "
                                   "string!", }), 400

    try:
        if len(grid_value) != grid_size * grid_size:
            raise SizeError
    except SizeError as e:
        return jsonify({"message": e.__str__()}), 400
    grid_matrix = gridmatrix(grid_size, grid_value)
    grid_size = grid_size
    grid_value = json.dumps(grid_matrix)
    timestamp = dt.now().strftime('%d-%m-%y %H:%M')
    try:
        data = Grid(grid_size=grid_size, grid_value=grid_value, timestamp=timestamp)
        db.session.add(data)
        db.session.commit()
        return jsonify({"id": data.id})
    except Exception as e:
        return jsonify({"message": e.__str__()})


@application.route("/sun-spot-analyser-api/scores", methods=["GET"])
def scores():
    """
        args: id of grid
        return: score for each cell in the grid (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    check_error = check_id_error(grid_id)
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    grid_score = get_all_score(grid_values)
    return grid_score



@application.route("/sun-spot-analyser-api/grid_value", methods=["GET"])
def grid_value():
    """
        args: id of grid
        return: grid values as matrix (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    check_error = check_id_error(grid_id)
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    return jsonify({grid.id: grid_values})


@application.route("/sun-spot-analyser-api/cell_score", methods=["GET"])
def cell_scores():
    """
        args: id of grid, x and y values of specific grid
        return: score for specific cell (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    x = request.args.get("x") if "x" in request.args else None
    y = request.args.get("y") if "y" in request.args else None
    check_error = check_id_x_y_error(grid_id, x, y)
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    grid_score = get_all_score_id(grid_values, x, y)
    return grid_score


@application.route("/sun-spot-analyser-api/min_scores", methods=["GET"])
def min_scores():
    """
        args: id of grid
        return: minimum score within the grid and its corresponding x,y location (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    check_error = check_id_error(grid_id)
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    grid_score = get_min_score(grid_values)
    return grid_score


@application.route("/sun-spot-analyser-api/max_scores", methods=["GET"])
def max_scores():
    """
        args: id of grid
        return: maximum score within the grid and its corresponding x,y location (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    check_error = check_id_error(grid_id)
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    grid_score = get_max_score(grid_values)
    return grid_score


@application.route("/sun-spot-analyser-api/top_x_scores", methods=["GET"])
def top_x_scores():
    """
        args: id of grid, x value (for calculating top x values)
        return: Top x score and its corresponding x,y locations (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    top_x = request.args.get("top_x") if "top_x" in request.args else None
    check_error = check_id_x_error(grid_id, top_x, "top_x")
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    grid_score = get_top_x_score(grid_values, top_x)
    return grid_score


@application.route("/sun-spot-analyser-api/bottom_x_scores", methods=["GET"])
def bottom_x_scores():
    """
        args: id of grid, x value (for calculating top x values)
        return: Top x score and its corresponding x,y locations (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    bottom_x = request.args.get("bottom_x") if "bottom_x" in request.args else None
    check_error = check_id_x_error(grid_id, bottom_x, "bottom_x")
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id).first()
    grid_values = json.loads(grid.grid_value)
    grid_score = get_bottom_x_score(grid_values, bottom_x)
    return grid_score



@application.route("/sun-spot-analyser-api/ids", methods=["GET"])
def ids():
    """
        return: List of all ids (json)
    """
    ids = []
    grid = db.session.query(Grid)
    [ids.append(each_id.id) for each_id in grid]
    return jsonify({"IDS": ids})


@application.route("/sun-spot-analyser-api/delete_grid", methods=["DELETE"])
def delete_grid():
    """
        return: List of all ids (json)
    """
    grid_id = request.args.get("id") if "id" in request.args else None
    check_error = check_id_error(grid_id)
    if not "success" in check_error:
        return jsonify(check_error), 400
    grid = db.session.query(Grid).filter_by(id=grid_id)
    grid.delete()
    db.session.commit()
    return jsonify({"message": "successfully deleted data"})