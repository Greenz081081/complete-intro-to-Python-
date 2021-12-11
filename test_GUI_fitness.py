from GUI_fitness import compute_age,\
    kg_from_lb, cm_from_in, body_mass_index,\
        basal_metabolic_rate
from pytest import approx
import pytest

def test_compute_age():
    assert compute_age("2015-10-21") == 6
    assert compute_age("2019-12-8") == 2
    assert compute_age("2003-4-6") == 18
    assert compute_age("2011-7-16") == 10

def test_kg_from_lb():
    assert kg_from_lb(145) == approx(65.77089365)
    assert kg_from_lb(155) == approx(70.30681735)
    assert kg_from_lb(158) == approx(71.66759446)
    assert kg_from_lb(100) == approx(45.359237)

def test_cm_from_in():
    assert cm_from_in(65) == approx(165.1)
    assert cm_from_in(55) == approx(139.7)
    assert cm_from_in(58) == approx(147.32)
    assert cm_from_in(80) == approx(203.2)

def test_body_mass_index():
    assert body_mass_index(145, 55) == approx(479.33884297520666)
    assert body_mass_index(155, 60) == approx(430.55555555555554)
    assert body_mass_index(125, -25) == approx(2000.0)
    assert body_mass_index(160, 45) == approx(790.1234567901234)

def test_basal_metabolic_rate():
    assert basal_metabolic_rate("M", 145, 55, 19) == approx(2187.0090000000005)
    assert basal_metabolic_rate("F", 155, -25, 21) == approx(1712.498)
    assert basal_metabolic_rate("M", 125, 60, 18) == approx(1948.7410000000002)
    assert basal_metabolic_rate("F", 165, 45, 20) == approx(2026.158)

pytest.main(["-v", "--tb=line", "-rN", __file__])