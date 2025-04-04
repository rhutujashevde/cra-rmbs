# **Mortgage Credit Rating System**  

This project provides a **credit rating system** that evaluates mortgage applications based on financial risk factors such as **loan amount, property value, debt, credit score, loan type, and property type**. The system assigns a **risk score** to each mortgage and determines an overall credit rating.

## **Table of Contents**
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Further Improvements & Scalability](#further-improvements--scalability)

---

## **Overview**
The **Mortgage Credit Rating System** processes a list of mortgage applications and assigns an overall credit rating using predefined risk factors. It helps **financial institutions, lenders, and analysts** assess the creditworthiness of applicants before approving loans.

---

## **Installation & Setup**
### **Prerequisites**
Ensure you have **Python 3.7+** installed.

### **1. Clone the repository**
```bash
git clone https://github.com/rhutujashevde/cra-rmbs.git
cd cra-rmbs
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the script**
```bash
python credit_rating.py
```

---

## **Usage**
### **Calling the function in Python**
```python
from credit_rating import calculate_credit_rating

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
        }
    ]
}

credit_rating = calculate_credit_rating(mortgages_data)
print(f"Credit Rating: {credit_rating}")
```

---

## **Example Input & Output**
### **Input JSON**
```json
{
  "mortgages": [
    {
      "credit_score": 750,
      "loan_amount": 200000,
      "property_value": 250000,
      "annual_income": 60000,
      "debt_amount": 20000,
      "loan_type": "fixed",
      "property_type": "single_family"
    }
  ]
}
```

### **Output**
```
AAA
```

---

## **Running Tests**
### **1. Run Tests Using Pytest**
```bash
pytest -rA test_credit_rating.py
```

---

## **Further Improvements & Scalability**

### **1️⃣ Error Handling & Input Validation**
- Implement serializer for input JSON validation.
- Implement stricter validation for JSON input to check missing fields or incorrect types.

### **2️⃣ Performance Optimization**
- Vectorized computations using NumPy/Pandas to process large datasets efficiently.
- **Parallel Processing**: Use `multiprocessing` to handle multiple mortgages simultaneously.
- **Batch Processing**: If processing large mortgage datasets, implement a streaming approach to avoid memory overflow.

### **3️⃣ API Integration**
- Convert the function into a **REST API** using FastAPI or Flask, making it scalable for web applications.
- Add **asynchronous support** using `asyncio` to handle multiple requests efficiently.

### **4️⃣ Database Integration**
- Store mortgage data in **PostgreSQL or MongoDB** for better data management.
- Enable **historical data analysis** by storing previous credit ratings.

### **5️⃣ Customization & Risk Model Expansion**
- Allow users to **adjust risk factor weights** (e.g., give more importance to LTV vs. credit score).
- Implement **machine learning models** to predict mortgage defaults based on historical data.
