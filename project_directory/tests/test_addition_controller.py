import pytest
from ..controllers import addition_controller

@pytest.mark.parametrize("payload, expected_result", [
    ([[1, 2], [3, 4]], [3, 7]),
    ([[1, 2, 3], [4, 5, 6]], [6, 15]),
    # Add more test cases for edge scenarios
])
def test_process_batch(payload, expected_result):
    response = addition_controller.process_batch("id0101", payload)
    assert response.response == expected_result
    assert response.status == "complete"
