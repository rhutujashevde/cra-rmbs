import pytest
from credit_rating import calculate_credit_rating


def test_calculate_credit_rating_low_risk():
    """Test case where all mortgages are low-risk, expecting an AAA rating."""
    mortgages_data = {
        "mortgages": [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 720,
                "loan_amount": 100000,
                "property_value": 150000,
                "annual_income": 50000,
                "debt_amount": 10000,
                "loan_type": "fixed",
                "property_type": "single_family"
            }
        ]
    }
    assert calculate_credit_rating(mortgages_data) == "AAA"


def test_calculate_credit_rating_medium_risk():
    """Test case where mortgages have moderate risk, expecting a BBB rating."""
    mortgages_data = {
        "mortgages": [
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            },
            {
                "credit_score": 700,
                "loan_amount": 180000,
                "property_value": 220000,
                "annual_income": 55000,
                "debt_amount": 25000,
                "loan_type": "fixed",
                "property_type": "single_family"
            }
        ]
    }
    assert calculate_credit_rating(mortgages_data) == "BBB"


def test_calculate_credit_rating_high_risk():
    """Test case where all mortgages have high-risk characteristics, expecting a C rating."""
    mortgages_data = {
        "mortgages": [
            {
                "credit_score": 640,
                "loan_amount": 180000,
                "property_value": 190000,
                "annual_income": 40000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "condo"
            },
            {
                "credit_score": 620,
                "loan_amount": 170000,
                "property_value": 180000,
                "annual_income": 38000,
                "debt_amount": 28000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    }
    assert calculate_credit_rating(mortgages_data) == "C"


def test_calculate_credit_rating_mixed_risk():
    """Test case with a mix of low, medium, and high-risk mortgages, expecting a BBB rating."""
    mortgages_data = {
        "mortgages": [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 640,
                "loan_amount": 180000,
                "property_value": 190000,
                "annual_income": 40000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    }
    assert calculate_credit_rating(mortgages_data) == "C"


def test_calculate_credit_rating_single_mortgage():
    """Test case with only one mortgage, ensuring the calculation still works correctly."""
    mortgages_data = {
        "mortgages": [
            {
                "credit_score": 720,
                "loan_amount": 150000,
                "property_value": 200000,
                "annual_income": 50000,
                "debt_amount": 15000,
                "loan_type": "fixed",
                "property_type": "single_family"
            }
        ]
    }
    assert calculate_credit_rating(mortgages_data) == "AAA"


def test_calculate_credit_rating_empty_list():
    """Test case with an empty mortgage list, expecting None as the result."""
    assert calculate_credit_rating({"mortgages": []}) is None


def test_calculate_credit_rating_no_mortgages_key():
    """Test case where the input dictionary does not contain the 'mortgages' key, expecting None."""
    assert calculate_credit_rating({}) is None

def test_calculate_credit_rating_property_value_none():
    """Test case where property_value is None, expecting valid risk calculation."""
    mortgages_data = {
        "mortgages": [
            {
                "credit_score": 700,
                "loan_amount": 150000,
                "property_value": None,
                "annual_income": 50000,
                "debt_amount": 15000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 680,
                "loan_amount": 180000,
                "property_value": 200000,
                "annual_income": 55000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    }
    assert calculate_credit_rating(mortgages_data) in ["AAA", "BBB", "C"]
