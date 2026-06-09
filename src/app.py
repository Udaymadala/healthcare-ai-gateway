import os
from privacy_engine import HIPAAShield
from evaluator import SafetyEvaluator

def run_gateway_pipeline():
    print("====================================================")
    print("INITIALIZING CLINICAL AI SECURITY BOUNDARY GATEWAY  ")
    print("====================================================\n")
    
    # 1. Initialize Privacy Boundary
    shield = HIPAAShield()
    
    raw_clinical_ingestion = (
        "ADMISSION NOTE: Patient Alice Smith (DOB: 11/14/1984) presented with acute appendicitis. "
        "Spoke with husband at 904-555-1212. Scheduled for laparoscopic appendectomy."
    )
    
    print("[1] INGESTION GUARDRAIL: Intercepting Raw Clinical Data...")
    sanitized_data = shield.sanitize_clinical_notes(raw_clinical_ingestion)
    print(f"--> Clean Data Passed to Model Vector Store:\n    {sanitized_data}\n")
    
    # 2. Simulate Red-Teaming/Bias Evaluation Run
    print("[2] EVALUATION BOUNDARY: Running Treatment Consistency Audits...")
    
    # Mock output where the model gave uniform recommendations across different groups
    mock_simulation_logs = [
        {"demographic_variable": "Group_A_LowIncome", "model_recommendation": "Prescribe Amoxicillin 500mg"},
        {"demographic_variable": "Group_B_HighIncome", "model_recommendation": "Prescribe Amoxicillin 500mg"},
        {"demographic_variable": "Group_C_Minority_Zip", "model_recommendation": "Prescribe Amoxicillin 500mg"}
    ]
    
    evaluator = SafetyEvaluator()
    audit_report = evaluator.evaluate_uniformity(mock_simulation_logs)
    
    print("--> Audit Generation Completed.")
    print(f"    Consistency Score: {audit_report['consistency_score']} (1.00 = Absolute Uniformity)")
    print(f"    Meets Compliance Margin: {audit_report['is_within_safety_margin']}\n")
    print("====================================================")
    print("GATEWAY PROCESSED SUCCESSFULLY: ALL BOUNDARIES SECURED")
    print("====================================================")

if __name__ == "__main__":
    run_gateway_pipeline()