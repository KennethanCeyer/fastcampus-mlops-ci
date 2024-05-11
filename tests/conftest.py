import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from typing import Generator
from app import app
import torch


@pytest.fixture(scope="module")
def mock_client() -> TestClient:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_model() -> Generator[MagicMock, None, None]:
    with patch("ml_models.xor.XORModel.forward", autospec=True) as mock:
        yield mock
