import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class LoanApprovalSystem:
    def __init__(self):
        """Initialize the fuzzy logic loan approval system"""
        self.setup_fuzzy_variables()
        self.setup_membership_functions()
        self.setup_rules()
        self.setup_control_system()
    
    def setup_fuzzy_variables(self):
        """Define input and output variables for the fuzzy system"""
        # Input variables
        self.income = ctrl.Antecedent(np.arange(0, 200001, 1000), 'income')  # Monthly income in USD
        self.credit_score = ctrl.Antecedent(np.arange(300, 851, 1), 'credit_score')  # Credit score 300-850
        self.age = ctrl.Antecedent(np.arange(18, 81, 1), 'age')  # Age 18-80
        self.employment_duration = ctrl.Antecedent(np.arange(0, 41, 1), 'employment_duration')  # Years of employment
        self.debt_to_income = ctrl.Antecedent(np.arange(0, 101, 1), 'debt_to_income')  # Debt-to-income ratio %
        
        # Output variable
        self.loan_approval = ctrl.Consequent(np.arange(0, 101, 1), 'loan_approval')  # Approval score 0-100
    
    def setup_membership_functions(self):
        """Define membership functions for all variables"""
        
        # Income membership functions
        self.income['low'] = fuzz.trimf(self.income.universe, [0, 0, 50000])
        self.income['medium'] = fuzz.trimf(self.income.universe, [30000, 80000, 120000])
        self.income['high'] = fuzz.trimf(self.income.universe, [100000, 200000, 200000])
        
        # Credit score membership functions
        self.credit_score['poor'] = fuzz.trimf(self.credit_score.universe, [300, 300, 550])
        self.credit_score['fair'] = fuzz.trimf(self.credit_score.universe, [500, 650, 700])
        self.credit_score['good'] = fuzz.trimf(self.credit_score.universe, [650, 750, 800])
        self.credit_score['excellent'] = fuzz.trimf(self.credit_score.universe, [750, 850, 850])
        
        # Age membership functions
        self.age['young'] = fuzz.trimf(self.age.universe, [18, 18, 30])
        self.age['middle'] = fuzz.trimf(self.age.universe, [25, 45, 65])
        self.age['senior'] = fuzz.trimf(self.age.universe, [55, 80, 80])
        
        # Employment duration membership functions
        self.employment_duration['short'] = fuzz.trimf(self.employment_duration.universe, [0, 0, 2])
        self.employment_duration['medium'] = fuzz.trimf(self.employment_duration.universe, [1, 5, 10])
        self.employment_duration['long'] = fuzz.trimf(self.employment_duration.universe, [8, 40, 40])
        
        # Debt-to-income ratio membership functions
        self.debt_to_income['low'] = fuzz.trimf(self.debt_to_income.universe, [0, 0, 25])
        self.debt_to_income['medium'] = fuzz.trimf(self.debt_to_income.universe, [20, 40, 60])
        self.debt_to_income['high'] = fuzz.trimf(self.debt_to_income.universe, [50, 100, 100])
        
        # Loan approval membership functions
        self.loan_approval['denied'] = fuzz.trimf(self.loan_approval.universe, [0, 0, 30])
        self.loan_approval['review'] = fuzz.trimf(self.loan_approval.universe, [20, 50, 70])
        self.loan_approval['approved'] = fuzz.trimf(self.loan_approval.universe, [60, 100, 100])
    
    def setup_rules(self):
        """Define fuzzy rules for loan approval"""
        self.rules = [
            # High approval rules - prime candidates
            ctrl.Rule(self.income['high'] & self.credit_score['excellent'] & 
                     self.employment_duration['long'] & self.debt_to_income['low'] & self.age['middle'], 
                     self.loan_approval['approved']),
            
            ctrl.Rule(self.income['high'] & self.credit_score['good'] & 
                     self.employment_duration['medium'] & self.debt_to_income['low'] & self.age['middle'], 
                     self.loan_approval['approved']),
            
            ctrl.Rule(self.income['medium'] & self.credit_score['excellent'] & 
                     self.employment_duration['long'] & self.debt_to_income['low'] & self.age['middle'], 
                     self.loan_approval['approved']),
            
            # High approval for seniors with excellent profiles
            ctrl.Rule(self.income['high'] & self.credit_score['excellent'] & 
                     self.employment_duration['long'] & self.debt_to_income['low'] & self.age['senior'], 
                     self.loan_approval['approved']),
            
            # Review rules - need manual evaluation
            ctrl.Rule(self.income['medium'] & self.credit_score['good'] & 
                     self.employment_duration['medium'] & self.debt_to_income['medium'] & self.age['middle'], 
                     self.loan_approval['review']),
            
            ctrl.Rule(self.income['high'] & self.credit_score['fair'] & 
                     self.employment_duration['medium'] & self.debt_to_income['medium'] & self.age['middle'], 
                     self.loan_approval['review']),
            
            ctrl.Rule(self.income['medium'] & self.credit_score['good'] & 
                     self.employment_duration['long'] & self.debt_to_income['medium'] & self.age['young'], 
                     self.loan_approval['review']),
            
            # Special considerations for young applicants
            ctrl.Rule(self.income['high'] & self.credit_score['good'] & 
                     self.employment_duration['short'] & self.debt_to_income['low'] & self.age['young'], 
                     self.loan_approval['review']),
            
            # Denial rules - high risk profiles
            ctrl.Rule(self.income['low'] & self.credit_score['poor'] & self.age['young'], 
                     self.loan_approval['denied']),
            
            ctrl.Rule(self.debt_to_income['high'] & self.credit_score['poor'] & self.employment_duration['short'], 
                     self.loan_approval['denied']),
            
            ctrl.Rule(self.income['low'] & self.employment_duration['short'] & self.credit_score['poor'], 
                     self.loan_approval['denied']),
            
            ctrl.Rule(self.credit_score['poor'] & self.employment_duration['short'] & self.debt_to_income['high'], 
                     self.loan_approval['denied']),
            
            # Additional review cases
            ctrl.Rule(self.income['low'] & self.credit_score['good'] & 
                     self.employment_duration['long'] & self.debt_to_income['low'] & self.age['middle'], 
                     self.loan_approval['review']),
            
            # Senior-specific rules
            ctrl.Rule(self.income['medium'] & self.credit_score['good'] & 
                     self.employment_duration['long'] & self.debt_to_income['low'] & self.age['senior'], 
                     self.loan_approval['review']),
        ]
    
    def setup_control_system(self):
        """Setup the control system with rules"""
        self.loan_ctrl = ctrl.ControlSystem(self.rules)
        self.loan_simulation = ctrl.ControlSystemSimulation(self.loan_ctrl)
    
    def evaluate_loan(self, income_val, credit_score_val, age_val, employment_duration_val, debt_to_income_val):
        """
        Evaluate loan approval based on input parameters
        
        Parameters:
        - income_val: Monthly income in USD
        - credit_score_val: Credit score (300-850)
        - age_val: Age in years
        - employment_duration_val: Years of employment
        - debt_to_income_val: Debt-to-income ratio as percentage
        
        Returns:
        - approval_score: Loan approval score (0-100)
        - decision: String indicating the decision
        """
        
        # Input validation
        if not (0 <= income_val <= 200000):
            raise ValueError("Income must be between 0 and 200,000")
        if not (300 <= credit_score_val <= 850):
            raise ValueError("Credit score must be between 300 and 850")
        if not (18 <= age_val <= 80):
            raise ValueError("Age must be between 18 and 80")
        if not (0 <= employment_duration_val <= 40):
            raise ValueError("Employment duration must be between 0 and 40 years")
        if not (0 <= debt_to_income_val <= 100):
            raise ValueError("Debt-to-income ratio must be between 0 and 100%")
        
        # Set input values
        self.loan_simulation.input['income'] = income_val
        self.loan_simulation.input['credit_score'] = credit_score_val
        self.loan_simulation.input['age'] = age_val
        self.loan_simulation.input['employment_duration'] = employment_duration_val
        self.loan_simulation.input['debt_to_income'] = debt_to_income_val
        
        # Compute the result
        self.loan_simulation.compute()
        
        approval_score = self.loan_simulation.output['loan_approval']
        
        # Determine decision based on score
        if approval_score >= 60:
            decision = "APPROVED"
        elif approval_score >= 30:
            decision = "UNDER REVIEW"
        else:
            decision = "DENIED"
        
        return approval_score, decision
    
    def plot_membership_functions(self):
        """Plot membership functions for visualization"""
        fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 12))
        
        # Income
        self.income.view(ax=axes[0, 0])
        axes[0, 0].set_title('Income Membership Functions')
        
        # Credit Score
        self.credit_score.view(ax=axes[0, 1])
        axes[0, 1].set_title('Credit Score Membership Functions')
        
        # Age
        self.age.view(ax=axes[1, 0])
        axes[1, 0].set_title('Age Membership Functions')
        
        # Employment Duration
        self.employment_duration.view(ax=axes[1, 1])
        axes[1, 1].set_title('Employment Duration Membership Functions')
        
        # Debt-to-Income
        self.debt_to_income.view(ax=axes[2, 0])
        axes[2, 0].set_title('Debt-to-Income Ratio Membership Functions')
        
        # Loan Approval
        self.loan_approval.view(ax=axes[2, 1])
        axes[2, 1].set_title('Loan Approval Membership Functions')
        
        plt.tight_layout()
        plt.show()

def main():
    """Main function to demonstrate the loan approval system"""
    print("=== Fuzzy Logic Loan Approval System ===\n")
    
    # Initialize the system
    loan_system = LoanApprovalSystem()
    
    # Test cases
    test_cases = [
        {
            "name": "High Income, Excellent Credit",
            "income": 150000,
            "credit_score": 800,
            "age": 35,
            "employment_duration": 10,
            "debt_to_income": 15
        },
        {
            "name": "Medium Income, Good Credit",
            "income": 70000,
            "credit_score": 720,
            "age": 28,
            "employment_duration": 5,
            "debt_to_income": 35
        },
        {
            "name": "Low Income, Poor Credit",
            "income": 30000,
            "credit_score": 450,
            "age": 25,
            "employment_duration": 1,
            "debt_to_income": 60
        },
        {
            "name": "Medium Income, Fair Credit, High Debt",
            "income": 80000,
            "credit_score": 650,
            "age": 40,
            "employment_duration": 8,
            "debt_to_income": 70
        }
    ]
    
    print("Testing different loan scenarios:\n")
    
    for i, case in enumerate(test_cases, 1):
        print(f"{i}. {case['name']}")
        print(f"   Income: ${case['income']:,}")
        print(f"   Credit Score: {case['credit_score']}")
        print(f"   Age: {case['age']}")
        print(f"   Employment Duration: {case['employment_duration']} years")
        print(f"   Debt-to-Income Ratio: {case['debt_to_income']}%")
        
        try:
            score, decision = loan_system.evaluate_loan(
                case['income'],
                case['credit_score'],
                case['age'],
                case['employment_duration'],
                case['debt_to_income']
            )
            
            print(f"   → Approval Score: {score:.2f}")
            print(f"   → Decision: {decision}")
            
        except Exception as e:
            print(f"   → Error: {e}")
        
        print("-" * 50)
    
    # Interactive mode
    print("\n=== Interactive Mode ===")
    print("Enter your loan details for evaluation:")
    
    try:
        income = float(input("Monthly Income ($): "))
        credit_score = int(input("Credit Score (300-850): "))
        age = int(input("Age: "))
        employment_duration = float(input("Employment Duration (years): "))
        debt_to_income = float(input("Debt-to-Income Ratio (%): "))
        
        score, decision = loan_system.evaluate_loan(
            income, credit_score, age, employment_duration, debt_to_income
        )
        
        print(f"\n=== LOAN EVALUATION RESULTS ===")
        print(f"Approval Score: {score:.2f}/100")
        print(f"Decision: {decision}")
        
        if decision == "APPROVED":
            print(" Congratulations! Your loan application is likely to be approved.")
        elif decision == "UNDER REVIEW":
            print(" Your application requires manual review. Additional documentation may be needed.")
        else:
            print(" Unfortunately, your application does not meet the current criteria.")
            
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 