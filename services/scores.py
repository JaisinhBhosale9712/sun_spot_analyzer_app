from flask import jsonify
from operator import attrgetter


def get_all_score(grid_value):
    all_scores = []
    g = grid_value
    for row_index, each_row in enumerate(g):
        for column_index, each_column in enumerate(each_row):
            center = g[row_index][column_index]
            center_right = g[row_index][column_index + 1] if column_index + 1 < len(g[0]) else 0
            center_left = g[row_index][column_index - 1] if column_index - 1 > -1 else 0
            top = g[row_index - 1][column_index] if row_index - 1 > -1 else 0
            top_right = g[row_index - 1][column_index + 1] if row_index - 1 > -1 and column_index + 1 < len(
                g[0]) else 0
            top_left = g[row_index - 1][column_index - 1] if row_index - 1 > -1 and column_index - 1 > -1 else 0
            bottom = g[row_index + 1][column_index] if row_index + 1 < len(g) else 0
            bottom_right = g[row_index + 1][column_index + 1] if row_index + 1 < len(g) and column_index + 1 < len(
                g[0]) else 0
            bottom_left = g[row_index + 1][column_index - 1] if row_index + 1 < len(g) and column_index - 1 > -1 else 0
            score = center + center_right + center_left \
                    + top + top_right + top_left \
                    + bottom + bottom_right + bottom_left
            all_scores.append({"x": row_index + 1, "y": column_index + 1, "score": score}, )
    return jsonify({"score": all_scores})


def get_all_score_id(grid_value, x, y):
    all_scores = []
    g = grid_value
    for row_index, each_row in enumerate(g):
        for column_index, each_column in enumerate(each_row):
            if row_index == int(x) - 1 and column_index == int(y) - 1:
                center = g[row_index][column_index]
                center_right = g[row_index][column_index + 1] if column_index + 1 < len(g[0]) else 0
                center_left = g[row_index][column_index - 1] if column_index - 1 > -1 else 0
                top = g[row_index - 1][column_index] if row_index - 1 > -1 else 0
                top_right = g[row_index - 1][column_index + 1] if row_index - 1 > -1 and column_index + 1 < len(
                    g[0]) else 0  ###
                top_left = g[row_index - 1][column_index - 1] if row_index - 1 > -1 and column_index - 1 > -1 else 0
                bottom = g[row_index + 1][column_index] if row_index + 1 < len(g) else 0
                bottom_right = g[row_index + 1][column_index + 1] if row_index + 1 < len(g) and column_index + 1 < len(
                    g[0]) else 0
                bottom_left = g[row_index + 1][column_index - 1] if row_index + 1 < len(
                    g) and column_index - 1 > -1 else 0
                score = center + center_right + center_left \
                        + top + top_right + top_left \
                        + bottom + bottom_right + bottom_left
                all_scores.append({"x": row_index + 1, "y": column_index + 1, "score": score}, )
                break
    return jsonify({"score": all_scores})


def get_min_score(grid_value):
    all_scores = get_all_score(grid_value).json["score"]
    min_score = min(all_scores, key=lambda x: x["score"])
    return jsonify(min_score)


def get_max_score(grid_value):
    all_scores = get_all_score(grid_value).json["score"]
    max_score = max(all_scores, key=lambda x: x["score"])
    return jsonify(max_score)


def get_top_x_score(grid_value, top_x):
    all_scores = get_all_score(grid_value).json["score"]
    top_x_scores = sorted(all_scores, key=lambda x: x["score"], reverse=True)[:int(top_x)]
    return jsonify(top_x_scores)


def get_bottom_x_score(grid_value, bottom_x):
    all_scores = get_all_score(grid_value).json["score"]
    bottom_x_score = sorted(all_scores, key=lambda x: x["score"])[:int(bottom_x)]
    return jsonify(bottom_x_score)
