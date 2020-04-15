from app.app_factory import create_app
import app.models as models
import IPython


def run_interactive_shell():
    app = create_app()

    # Needed for making the console work in app request context
    ctx = app.test_request_context()
    ctx.push()

    IPython.embed()


if __name__ == '__main__':
    run_interactive_shell()
