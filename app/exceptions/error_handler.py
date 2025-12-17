from flask import jsonify

def register_error_handlers(app):

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        return jsonify({
            "error": str(error)
        }), 400

    @app.errorhandler(KeyError)
    def handle_key_error(error):
        return jsonify({
            "error": f"Missing field: {str(error)}"
        }), 400

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({
            "error": "Resource not found"
        }), 404

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        return jsonify({
            "error": "Internal Server Error",
            "details": str(error)
        }), 500
