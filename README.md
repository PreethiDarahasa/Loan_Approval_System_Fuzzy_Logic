# Fuzzy Logic Loan Approval System

A fuzzy logic-based system that evaluates loan applications by considering multiple parameters to determine eligibility for loan approval. This system uses fuzzy inference to handle the uncertainty and vagueness inherent in financial decision-making.

## Project Overview

This system evaluates loan applications based on five key parameters:
- **Monthly Income** (USD)
- **Credit Score** (300-850)
- **Age** (18-80 years)
- **Employment Duration** (years)
- **Debt-to-Income Ratio** (percentage)

The system outputs an approval score (0-100) and provides one of three decisions:
- **APPROVED** (Score ≥ 60)
- **UNDER REVIEW** (Score 30-59)
- **DENIED** (Score < 30)

## Features

- **Fuzzy Logic Engine**: Uses scikit-fuzzy for robust fuzzy inference
- **Multiple Input Parameters**: Considers 5 financial indicators
- **Intelligent Rules**: 12 carefully crafted fuzzy rules for decision making
- **Interactive Mode**: Command-line interface for manual evaluation
- **Batch Testing**: Pre-configured test cases for demonstration
- **Visualization**: Membership function plotting capability
- **Input Validation**: Comprehensive error checking for all inputs

## Requirements

- Python 3.7 or higher
- NumPy
- scikit-fuzzy
- Matplotlib

## Installation

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd Loan_Approval_System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:
   ```bash
   pip install numpy scikit-fuzzy matplotlib
   ```

## Usage

### Running the System

Execute the main script:
```bash
python loan_approval_system.py
```

The system will:
1. Run predefined test cases showing different scenarios
2. Enter interactive mode where you can input your own values

### Interactive Mode Example

```
=== Interactive Mode ===
Enter your loan details for evaluation:
Monthly Income ($): 75000
Credit Score (300-850): 720
Age: 32
Employment Duration (years): 6
Debt-to-Income Ratio (%): 25

=== LOAN EVALUATION RESULTS ===
Approval Score: 75.23/100
Decision: APPROVED
🎉 Congratulations! Your loan application is likely to be approved.
```

### Using as a Python Module

```python
from loan_approval_system import LoanApprovalSystem

# Initialize the system
loan_system = LoanApprovalSystem()

# Evaluate a loan application
score, decision = loan_system.evaluate_loan(
    income_val=80000,           # Monthly income
    credit_score_val=750,       # Credit score
    age_val=35,                 # Age
    employment_duration_val=8,   # Years of employment
    debt_to_income_val=20       # Debt-to-income ratio %
)

print(f"Approval Score: {score:.2f}")
print(f"Decision: {decision}")
```

## System Parameters

### Input Ranges
- **Income**: $0 - $200,000 (monthly)
- **Credit Score**: 300 - 850
- **Age**: 18 - 80 years
- **Employment Duration**: 0 - 40 years
- **Debt-to-Income Ratio**: 0 - 100%

### Membership Functions

#### Income Categories
- **Low**: $0 - $50,000
- **Medium**: $30,000 - $120,000
- **High**: $100,000 - $200,000

#### Credit Score Categories
- **Poor**: 300 - 550
- **Fair**: 500 - 700
- **Good**: 650 - 800
- **Excellent**: 750 - 850

#### Debt-to-Income Categories
- **Low**: 0 - 25%
- **Medium**: 20 - 60%
- **High**: 50 - 100%

## Fuzzy Rules Logic

The system uses 12 fuzzy rules that capture real-world loan approval logic:

### High Approval Rules
- High income + Excellent credit + Long employment + Low debt → **APPROVED**
- High income + Good credit + Medium employment + Low debt → **APPROVED**
- Medium income + Excellent credit + Long employment + Low debt → **APPROVED**

### Review Rules
- Medium income + Good credit + Medium employment + Medium debt → **REVIEW**
- High income + Fair credit + Medium employment + Medium debt → **REVIEW**

### Denial Rules
- Low income + Poor credit → **DENIED**
- High debt + Poor credit → **DENIED**
- Low income + Short employment → **DENIED**

## Visualization

To view the membership functions:

```python
from loan_approval_system import LoanApprovalSystem

loan_system = LoanApprovalSystem()
loan_system.plot_membership_functions()
```

This will display graphs showing how each input parameter is categorized using fuzzy logic.

## Test Cases

The system includes four predefined test cases:

1. **High Income, Excellent Credit**: Typically approved
2. **Medium Income, Good Credit**: Usually approved or under review
3. **Low Income, Poor Credit**: Usually denied
4. **Medium Income, Fair Credit, High Debt**: Typically under review

## Customization

### Adding New Rules
You can modify the `setup_rules()` method to add new fuzzy rules:

```python
# Example: Add a rule for young applicants with good credit
ctrl.Rule(self.age['young'] & self.credit_score['good'] & 
          self.income['medium'], self.loan_approval['approved'])
```

### Adjusting Membership Functions
Modify the `setup_membership_functions()` method to change the parameter ranges and categories.

### Changing Decision Thresholds
Adjust the score thresholds in the `evaluate_loan()` method:
- Currently: APPROVED ≥ 60, REVIEW 30-59, DENIED < 30


**Built with:** Python, NumPy, scikit-fuzzy, and Matplotlib 
