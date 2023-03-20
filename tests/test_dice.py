import src.functions as fc
import pytest


@pytest.fixture
def N():
    return 100000


@pytest.fixture
def faces(N):
    faces = [fc.dice_rolling() for _ in range(N)]
    return faces


@pytest.fixture
def probabilities(faces, N):
    p = [faces.count(i + 1) / N for i in range(6)]
    return p


def test_type():
    assert isinstance(fc.dice_rolling(), int), "The function should return an integer"


def test_min_value(faces):
    assert all(
        face >= 1 for face in faces
    ), "The function should return a minimum value of 1"


def test_max_value(faces):
    assert all(
        face <= 6 for face in faces
    ), "The function should return a maximum value of 6"


def test_uniform_distribution(probabilities):
    assert all(pytest.approx(p, abs=1e-2) == 1 / 6 for p in probabilities)
