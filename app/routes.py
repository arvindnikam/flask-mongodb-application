from flask import Blueprint

## Base
from app.controllers import base_controller
base_blueprint = Blueprint('base_blueprint', __name__)
base_blueprint.route('/', methods=['GET'])(base_controller.index)
# ------------------------------------------------------------------------------------------------------------------------------------ #

## Master Data
from app.controllers.master_data import location_controller
location_blueprint = Blueprint('location_blueprint', __name__)
location_blueprint.route('/search', methods=['POST'])(location_controller.search)
location_blueprint.route('/analyze', methods=['POST'])(location_controller.analyze)
# ------------------------------------------------------------------------------------------------------------------------------------ #

## Support
from app.controllers import support_query_controller
support_query_blueprint = Blueprint('support_query_blueprint', __name__)
support_query_blueprint.route('/create', methods=['POST'])(support_query_controller.create)
support_query_blueprint.route('/<query_id>/update', methods=['PUT', 'PATCH'])(support_query_controller.update)
support_query_blueprint.route('/search', methods=['POST'])(support_query_controller.search)
# ------------------------------------------------------------------------------------------------------------------------------------ #


def initialize_routes(app):
    @app.before_request
    def before_request(): base_controller.before_request()
    @app.after_request
    def after_request(response): return base_controller.after_request(response)

    app.register_blueprint(base_blueprint)

    app.register_blueprint(location_blueprint, url_prefix='/api/v1/master_data/locations')
    app.register_blueprint(support_query_blueprint, url_prefix='/api/v1/support_queries')
