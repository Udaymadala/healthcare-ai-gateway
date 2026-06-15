# Healthcare AI Gateway: Privacy and Bias Evaluation Shield

An automated safety guardrail built to protect patient data and ensure fairness when healthcare systems use Artificial Intelligence (AI).

## 🎯 What This Project Does (Overview)
When hospitals and clinics use modern AI models to read patient charts, two major security risks happen:
1. **Data Leaks:** Private patient data (like names, phone numbers, and emails) can accidentally be sent to public AI systems, violating medical privacy laws like HIPAA.
2. **Hidden Bias:** An AI system might give different medical recommendations or risk scores to a male patient versus a female patient, even if they have the exact same symptoms.

This project creates a **Digital Gateway** that sits between the patient database and the AI. It stops dangerous data before it reaches the model and runs consistency tests to ensure the AI treats everyone fairly.

---

## 🧱 How the Data Flows (Step-by-Step)

Here is how information moves securely through this system:

[Step 1: Patient Data] 
       │
       ▼
[Step 2: Privacy Filter (Microsoft Presidio)]
* Scans the text automatically.
* Instantly removes private details (Names, Emails, Phone Numbers).
* Replaces them with blank safety tags like [ENTITY_REDACTED].
       │
       ▼
[Step 3: Fairness Audit (SafetyEvaluator Engine)]
* Fuzzes demographic data (tests identical cases swapping "Male" and "Female").
* Measures if the AI changes its behavior based on demographics.
* Calculates a final safety score.
       │
       ▼
[Step 4: Secure AI Processing]
* The fully sanitized and audited data is safe to be processed.

---

## 🛡️ Major Security Flaws Defeated

By placing this gateway in front of an AI system, we protect against critical security vulnerabilities:

- **Preventing Sensitive Data Exposure:** By using deterministic text filters, private health details are stripped out completely *before* data can leave the internal environment. 
- **Catching Biased Logic:** The system continuously tracks treatment uniformity across testing groups, raising a red flag if the AI's logic begins to drift or discriminate.
- **Framework Grounding:** This process aligns directly with standard industry defensive practices, including the **NIST AI Risk Management Framework** and **HIPAA Technical Safeguards**.

---

## 🚀 Setup & Execution Instructions

### 1. Download System Dependencies
To set up the language processing engine on your computer, open your terminal inside the project folder and run these two lines:

pip install -r requirements.txt
python -m spacy download en_core_web_lg

### 2. Run the Gateway Test
To run the automated security checks and see the filters in action, execute this command:

python src/app.py