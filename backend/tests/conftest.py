import pytest
from faker import Faker


@pytest.fixture(name="faker")
def fixture_faker() -> Faker:
    generator = Faker()
    return generator
