from werkzeug.serving import run_simple
from app import app_factory

application = app_factory.create_app()


if __name__ == "__main__":
    run_simple(
        '0.0.0.0', 5000,
        application,
        use_reloader=True, use_debugger=True, threaded=True)