import unittest
from views import application
import json

class FlaskTestCase(unittest.TestCase):

    def base_test(self):
        """
            ensures that flask app was setup correctly
        """
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api")
        self.assertEqual(response.status_code, 200)
    ###
    def test_grid_post_success(self):
        tester = application.test_client(self)
        response = tester.post("/sun-spot-analyser-api/grid", data=json.dumps({ "size": 3, "values": "4, 2, 3, 2, 2, 1, 3, 2, 1"}))
        self.assertEqual(response.status_code, 200)

    def test_grid_post_nodata(self):
        tester = application.test_client(self)
        response = tester.post("/sun-spot-analyser-api/grid", data="")
        self.assertEqual(response.status_code, 400)

    def test_grid_post_wrongdata(self):
        tester = application.test_client(self)
        response = tester.post("/sun-spot-analyser-api/grid",
                               data=json.dumps({"size": 2, "values": "4, 2, 3"}))
        self.assertEqual(response.status_code, 400)
    ###
    def test_scores_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/scores?id=1")
        self.assertEqual(response.status_code, 200)

    def test_scores_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/scores")
        self.assertEqual(response.status_code, 400)

    def test_scores_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/scores?id=A")
        self.assertEqual(response.status_code, 400)    
    ###   
    def test_grid_value_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/grid_value?id=1")
        self.assertEqual(response.status_code, 200)

    def test_grid_value_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/grid_value")
        self.assertEqual(response.status_code, 400)

    def test_grid_value_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/grid_value?id=A")
        self.assertEqual(response.status_code, 400)
    ###
    def test_cell_score_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/cell_score?id=1&x=1&y=1")
        self.assertEqual(response.status_code, 200)

    def test_cell_score_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/cell_score")
        self.assertEqual(response.status_code, 400)

    def test_cell_score_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/cell_score?id=1&x=P&y=1")
        self.assertEqual(response.status_code, 400)
    ###
    def test_min_scores_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/min_scores?id=1")
        self.assertEqual(response.status_code, 200)

    def test_min_scores_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/min_scores")
        self.assertEqual(response.status_code, 400)

    def test_min_scores_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/min_scores?id=A")
        self.assertEqual(response.status_code, 400)  
    ###
    def test_max_scores_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/max_scores?id=1")
        self.assertEqual(response.status_code, 200)

    def test_max_scores_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/max_scores")
        self.assertEqual(response.status_code, 400)

    def test_max_scores_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/max_scores?id=A")
        self.assertEqual(response.status_code, 400)
    ###
    def test_top_x_scores_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/top_x_scores?id=1&top_x=4")
        self.assertEqual(response.status_code, 200)

    def test_top_x_scores_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/top_x_scores")
        self.assertEqual(response.status_code, 400)

    def test_top_x_scores_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/top_x_scores?id=A&top_x=C")
        self.assertEqual(response.status_code, 400) 
    ###
    def test_bottom_x_scores_success(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/bottom_x_scores?id=1&bottom_x=3")
        self.assertEqual(response.status_code, 200)

    def test_bottom_x_scores_noargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/bottom_x_scores")
        self.assertEqual(response.status_code, 400)

    def test_bottom_x_scores_wrongargs(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/bottom_x_scores?id=A&bottom_x=I")
        self.assertEqual(response.status_code, 400)
    ###
    def test_ids(self):
        tester = application.test_client(self)
        response = tester.get("/sun-spot-analyser-api/ids")
        self.assertEqual(response.status_code, 200)
    ###
    def test_delete_grid_noargs(self):
        tester = application.test_client(self)
        response = tester.delete("/sun-spot-analyser-api/delete_grid")
        self.assertEqual(response.status_code, 400)

    def test_delete_grid_wrongargs(self):
        tester = application.test_client(self)
        response = tester.delete("/sun-spot-analyser-api/delete_grid?id=A")
        self.assertEqual(response.status_code, 400)    


if __name__ == "__main__":
    unittest.main()