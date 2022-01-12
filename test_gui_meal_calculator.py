from gui_meal_calculator import compute_subtotal,\
    compute_sales_tax, compute_total, compute_change
from pytest import approx
import pytest


def test_compute_subtotal():
    """Verify that the compute_subtotal function works correctly."""
    compute_subtotal(100, 50, 4, 150, 220, 250, 300, 6) == approx(856788)
    compute_subtotal(400, 500, 2, 100, 240, 350, 600, 8) == approx(252748)
    compute_subtotal(200, 100, 3, 180, 180, 210, 330, 4) == approx(666782)
    compute_subtotal(100, 200, 4, 350, 120, 110, 300, 5) == approx(-235677)

def test_compute_sales_tax():
    """Verify that the compute_sales_tax function works correctly."""
    compute_sales_tax(856788, 6) == approx(60)
    compute_sales_tax(252748, 8) == approx(50)
    compute_sales_tax(666782, 10) == approx(10)
    compute_sales_tax(-235677, 50) == approx(20)

def test_compute_total():
    """Verify that the compute_total function works correctly."""
    compute_total(-23567, 6) == approx(12000)
    compute_total(666782, 8) == approx(40000)
    compute_total(856788, 10) == approx(25000)
    compute_total(252748, 50) == approx(4000)

def test_compute_change():
    """Verify that the compute_change function works correctly."""
    compute_change(12500, 12000) == approx(500)
    compute_change(41000, 40000) == approx(1000)
    compute_change(25300, 25000) == approx(300)
    compute_change(4000, 4100) == approx(100)

 

pytest.main(["-v", "--tb=line", "-rN", __file__])