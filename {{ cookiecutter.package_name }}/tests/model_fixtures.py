import pytest


@pytest.fixture
def my_model_factory(factory_session):
    """ An example of what a fixture to create a model for testing might look like """
    model = object()  # You'd use your SQLAlchemy model here
    factory_session.add(model)
    return model
