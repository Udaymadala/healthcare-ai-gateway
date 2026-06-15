# Healthcare AI Gateway: Privacy and Bias Evaluation Shield

An automated safety guardrail built to protect patient data and ensure fairness when healthcare systems use Artificial Intelligence (AI).

## 🎯 What This Project Does (Overview)
When hospitals and clinics use modern AI models to read patient charts, two major security risks happen:
1. **Data Leaks:** Private patient data (like names, phone numbers, and emails) can accidentally be sent to public AI systems, violating medical privacy laws like HIPAA.
2. **Hidden Bias:** An AI system might give different medical recommendations or risk scores to a male patient versus a female patient, even if they have the exact same symptoms.

This project creates a **Digital Gateway** that sits between the patient database and the AI. It stops dangerous data before it reaches the model and runs consistency tests to ensure the AI treats everyone fairly.

---

## 🧱 How the Data Flows (Step-by-Step)

This system acts as a secure bridge, processing data through four distinct layers:

> **1. Patient Data Ingestion**
> Raw clinical notes, medical records, or user prompts enter the pipeline.
 
> **2. Privacy Filtering Layer (Microsoft Presidio)**
> The gateway automatically scans the text, strips out private identifiers (Names, Phone Lines, Emails), and replaces them with anonymous safety tokens like `[ENTITY_REDACTED]`.

> **3. Fairness & Bias Auditing Layer (SafetyEvaluator Engine)**
> The system duplicates the sanitized text, swaps demographic variables (testing identical cases for both "Male" and "Female"), and verifies if the AI's internal recommendations remain uniform and unbiased.

> **4. Downstream AI Processing**
> The fully audited, anonymous, and verified data is safely passed to the Large Language Model or Vector Database for clinical use.

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

```powershell
pip install -r requirements.txt
python -m spacy download en_core_web_lg