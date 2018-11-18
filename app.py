#!/usr/bin/env python3

import json
import sys
from typing import Dict, List

import flask
import flask_restful

from recommendation_system.users import Users, NoSuchUser

app = flask.Flask(__name__)
api = flask_restful.Api(app)
users = Users(users="data/users.csv", ratings="data/ratings.csv")


class WeightedScores(flask_restful.Resource):
    @staticmethod
    def get(name: str) -> List[Dict[str, float]]:
        result = []
        try:
            # we can't simply use the namedtuples from weighted_scores()
            # because they're translated into lists in the JSON reply,
            # so we create a dict for each item
            for item in users.weighted_scores(name):
                result.append({"movie": item.movie, "score": item.score})
        except NoSuchUser:
            response = json.dumps({
                "message": "User {} does not exist".format(name)
            })
            flask.abort(flask.Response(response=response, status=400))
        return result


api.add_resource(WeightedScores, "/api/weighted-scores/<string:name>")


class UserList(flask_restful.Resource):
    @staticmethod
    def get() -> List[str]:
        return users.user_list()


api.add_resource(UserList, "/api/user-list")


@app.route("/", defaults={"filename": None})
@app.route("/<filename>")
def ui(filename: str) -> flask.Response:
    if not filename:
        filename = "index.html"
    return flask.send_from_directory("ui", filename)


def main() -> int:
    app.run(host="0.0.0.0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
