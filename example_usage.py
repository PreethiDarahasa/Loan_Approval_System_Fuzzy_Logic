#!/usr/bin/env python3
"""
Simple example usage of the Fuzzy Logic Loan Approval System
This script demonstrates basic usage without the interactive interface.
"""

from loan_approval_system import LoanApprovalSystem

def run_examples():
    """Run several example loan evaluations"""
    
    print(" Fuzzy Logic Loan Approval System - Quick Examples\n")
    
    # Initialize the system
    loan_system = LoanApprovalSystem()
    
    # Example applications
    examples = [
        {
            "name": "John Doe - High Earner",
            "income": 120000,
            "credit_score": 780,
            "age": 35,
            "employment_duration": 8,
            "debt_to_income": 20
        },
        {
            "name": "Jane Smith - Average Profile",
            "income": 65000,
            "credit_score": 680,
            "age": 29,
            "employment_duration": 4,
            "debt_to_income": 35
        },
        {
            "name": "Mike Johnson - Risky Profile",
            "income": 35000,
            "credit_score": 520,
            "age": 26,
            "employment_duration": 1,
            "debt_to_income": 65
        }
    ]
    
    for example in examples:
        print(f"Evaluating: {example['name']}")
        print(f"Income: ${example['income']:,}/month")
        print(f"   Credit Score: {example['credit_score']}")
        print(f"   Age: {example['age']} years")
        print(f"   Employment: {example['employment_duration']} years")
        print(f"   Debt-to-Income: {example['debt_to_income']}%")
        
        try:
            score, decision = loan_system.evaluate_loan(
                example['income'],
                example['credit_score'],
                example['age'],
                example['employment_duration'],
                example['debt_to_income']
            )
            
            print(f" Approval Score: {score:.1f}/100")
            print(f" Decision: {decision}")
            
            # Add emoji for visual feedback
            if decision == "APPROVED":
                print("   Likely to be approved!\n")
            elif decision == "UNDER REVIEW":
                print("   Requires manual review\n")
            else:
                print("   Application denied\n")
                
        except Exception as e:
            print(f"   Error: {e}")
        

if __name__ == "__main__":
    run_examples() 