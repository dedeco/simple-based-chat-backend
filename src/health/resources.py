from http import HTTPStatus

from flask_restful import Resource, Api

from src.health import health_blueprint

health_restfull = Api(health_blueprint)


class HealthCheck(Resource):

    def get(self):
        return {"ping": "pong"} \
            , HTTPStatus.OK


health_restfull.add_resource(HealthCheck, '/')
