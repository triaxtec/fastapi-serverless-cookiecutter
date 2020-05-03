import os

if "example_LAMBDA" in os.environ:
    try:  # If we're running in Lambda, try to unzip all dependencies
        import unzip_requirements  # noqa
    except ImportError:
        pass  # noqa
    from mangum import Mangum
    from .main import app

    handler = Mangum(app)
