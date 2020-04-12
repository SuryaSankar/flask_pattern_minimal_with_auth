from contextlib import contextmanager
import json
from pprint import PrettyPrinter
from toolspy import merge
import app.models as models
from app.app_factory import create_app


def run_interactive_shell():
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False

    # Needed for making the console work in app request context
    ctx = app.test_request_context()
    ctx.push()

    pprint = PrettyPrinter(indent=4).pprint

    try:
        import IPython
        IPython.embed()
    except:
        import code
        code.interact(local=merge(locals(), globals()))


if __name__ == '__main__':
    run_interactive_shell()
