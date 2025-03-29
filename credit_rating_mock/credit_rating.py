from constants import LTV_THRESHOLDS, DTI_THRESHOLDS, CREDIT_SCORE_BONUS, CREDIT_SCORE_PENALTY, \
    LOAN_TYPE_RISK, PROPERTY_TYPE_RISK, RISK_SCORE_RATINGS


class CreditRatingLogic:
    """
    A class that encapsulates the logic for calculating the risk score
    based on mortgage attributes.
    """
    def __init__(self, payload):
        """
        Initializes the CreditRatingLogic object with mortgage details.

        :param payload: Dictionary containing mortgage data.
        """
        self.loan_amount = payload.get('loan_amount')
        self.property_value = payload.get('property_value') or 1
        self.credit_score = payload.get('credit_score')
        self.annual_income = payload.get('annual_income') or 1
        self.debt_amount = payload.get('debt_amount')
        self.loan_type = payload.get('loan_type')
        self.property_type = payload.get('property_type')
        self.risk_score = 0

    def get_credit_rating(self):
        """
        Computes the risk score for the mortgage based on multiple factors.

        :return: The computed risk score.
        """
        self.__apply_ltv_ratio()
        self.__apply_dti_ratio()
        self.__apply_credit_score_restrictions()
        self.__apply_loan_type()
        self.__apply_property_type()
        return self.risk_score

    def __apply_ltv_ratio(self):
        """
        Applies the Loan-to-Value (LTV) ratio risk component to the risk score.
        """
        ltv = self.loan_amount / self.property_value
        self.risk_score += sum(risk for threshold, risk in LTV_THRESHOLDS if ltv > threshold)

    def __apply_dti_ratio(self):
        """
        Applies the Debt-to-Income (DTI) ratio risk component to the risk score.
        """
        dti = self.debt_amount / self.annual_income
        self.risk_score += sum(risk for threshold, risk in DTI_THRESHOLDS if dti > threshold)
    
    def __apply_credit_score_restrictions(self):
        """
        Adjusts the risk score based on the credit score of the applicant.
        """
        if self.credit_score >= 700:
            self.risk_score += CREDIT_SCORE_BONUS
        elif self.credit_score < 650:
            self.risk_score += CREDIT_SCORE_PENALTY
  
    def __apply_loan_type(self):
        """
        Adjusts the risk score based on the loan type (fixed or adjustable).
        """
        self.risk_score += LOAN_TYPE_RISK.get(self.loan_type, 0)
    
    def __apply_property_type(self):
        """
        Adjusts the risk score based on the type of property (single-family, condo, etc.).
        """
        self.risk_score += PROPERTY_TYPE_RISK.get(self.property_type, 0)

    @staticmethod
    def get_total_risk_score(avg_credit_score, total_risk_score):
        """
        Adjusts the total risk score based on the average credit score of all mortgages.

        :param avg_credit_score: The average credit score across all mortgages.
        :param total_risk_score: The accumulated risk score from all mortgages.
        :return: Adjusted total risk score.
        """
        if avg_credit_score >= 700:
            total_risk_score += CREDIT_SCORE_BONUS
        elif avg_credit_score < 650:
            total_risk_score += CREDIT_SCORE_PENALTY
        return total_risk_score

    @staticmethod
    def get_credit_ratings(total_risk_score):
        """
        Determines the final credit rating based on the total risk score.

        :param total_risk_score: The total computed risk score.
        :return: A credit rating (AAA, BBB, C, etc.).
        """
        for threshold, rating in RISK_SCORE_RATINGS:
            if total_risk_score <= threshold:
                return rating
        return "C"

def calculate_credit_rating(mortgages_dict):
    """
    Calculates the overall credit rating for a set of mortgages.

    :param mortgages_dict: Dictionary containing a list of mortgages.
    :return: A credit rating or None if there are no mortgages.
    """
    mortgages = mortgages_dict.get('mortgages')
    if not mortgages:
        return None

    total_credit_points, total_risk_score = 0, 0
    num_mortgages = len(mortgages)

    for mortgage in mortgages:
        total_risk_score += CreditRatingLogic(mortgage).get_credit_rating()
        total_credit_points += mortgage.get('credit_score', 0)

    avg_credit_score = total_credit_points / num_mortgages if num_mortgages else 0
    total_risk_score = CreditRatingLogic.get_total_risk_score(avg_credit_score, total_risk_score)

    return CreditRatingLogic.get_credit_ratings(total_risk_score)

if __name__ == "__main__":
    test_data = {
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
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    }
    rating = calculate_credit_rating(test_data)
    print("Credit Rating:", rating)
