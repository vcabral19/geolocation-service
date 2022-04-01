import pytest
from starlette.testclient import TestClient

import tests.dependencies_test as dependencies
from app.main import app

print(f"ENVIRONMENT: {dependencies.env}")


@pytest.fixture(scope="function")
def testclient():

    with TestClient(app) as client:
        # Application 'startup' handlers are called on entering the block.
        yield client
    # Application 'shutdown' handlers are called on exiting the block.
