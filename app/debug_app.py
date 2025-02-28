from flask import Flask, request, jsonify
from werkzeug.exceptions import UnsupportedMediaType
import logging


def create_app():
    app = Flask(__name__)

    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    @app.route(
        "/",
        defaults={"path": ""},
        methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    )
    @app.route(
        "/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    )
    def catch_all(path):
        # Log the request details
        logger.debug("Request path: %s", path)
        logger.debug("Request Method: %s", request.method)
        logger.debug("Request URL: %s", request.url)
        logger.debug("Request Headers: %s", dict(request.headers))
        logger.debug("Request Args: %s", request.args)
        logger.debug("Request Form: %s", request.form)
        try:
            json_data = request.json
        except UnsupportedMediaType:
            logger.critical("cant get a json data")
            json_data = None

        if json_data:
            logger.debug("Request JSON: %s", json_data)

        logger.debug("Request Data: %s", request.data.decode('utf-8'))

        # Return a response
        return jsonify(
            {
                "method": request.method,
                "url": request.url,
                "headers": dict(request.headers),
                "args": request.args,
                "form": request.form,
                "json": json_data,
                "data": request.data.decode("utf-8"),
            },
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
