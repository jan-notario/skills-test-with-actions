import pytest
from src.calculations import area_of_circle, get_nth_fibonacci


def test_area_of_circle():
    """Test area of circle with valid radius."""
    assert area_of_circle(1) == 3.141592653589793
    assert area_of_circle(0) == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    assert get_nth_fibonacci(0) == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    assert get_nth_fibonacci(1) == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55


def test_area_of_circle_negative_radius():
    """Test with a negative radius to raise ValueError."""
    # Arrange
    radius = -1

    # Act & Assert
    with pytest.raises(ValueError):
        area_of_circle(radius)


def test_get_nth_fibonacci_negative():
    """Test with a negative number to raise ValueError."""
    # Arrange
    n = -1

    # Act & Assert
    with pytest.raises(ValueError):
        get_nth_fibonacci(n)