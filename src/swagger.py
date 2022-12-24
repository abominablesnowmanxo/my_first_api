from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = ''
API_URL = '/static/docs/swagger_docs.yaml'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Person list'
    }
)
