from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import json

class HIPAAShield:
    def __init__(self, config_path: str = "config/gateway_policy.json"):
        with open(config_path, "r") as f:
            self.policy = json.load(f)
        
        # Initialize Presidio Engine
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
        self.blocked_entities = self.policy.get("blocked_entities", [])

    def sanitize_clinical_notes(self, text: str) -> str:
        """
        Analyzes and redacts PHI entities defined in configuration policies 
        to ensure strict HIPAA compliance prior to RAG processing.
        """
        if not self.policy.get("enforce_hipaa", True):
            return text

        # Step 1: Detect PII/PHI
        analysis_results = self.analyzer.analyze(
            text=text, 
            language="en", 
            entities=self.blocked_entities
        )
        
        # Step 2: Configure operators dynamically based on policy
        operators = {}
        for entity in self.blocked_entities:
            operators[entity] = OperatorConfig("replace", {"new_value": f"[{entity}_REDACTED]"})

        # Step 3: Anonymize text
        anonymized_result = self.anonymizer.anonymize(
            text=text,
            analyzer_results=analysis_results,
            operators=operators
        )
        
        return anonymized_result.text

if __name__ == "__main__":
    # Quick debug block
    shield = HIPAAShield()
    sample_chart = "Patient John Doe visited Jacksonville Medical Center. SSN: 000-12-3456. Phone: 904-555-0199."
    print("Sanitized Output:\n", shield.sanitize_clinical_notes(sample_chart))