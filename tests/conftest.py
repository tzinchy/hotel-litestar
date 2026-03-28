from pytest import fixture
from testcontainers.postgres import PostgresContainer


@fixture(scope="session")
def pytest_configure():
    with PostgresContainer("postgres:16-alpine") as container:
        yield container
