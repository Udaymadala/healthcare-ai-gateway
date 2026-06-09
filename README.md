\# Healthcare AI Gateway: Privacy and Bias Evaluation Shield



An automated governance gateway and evaluation pipeline engineered to secure Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) architectures processing highly regulated healthcare datasets.



\## 🎯 Project Overview \& Objective

Modern enterprise frameworks deploy generative AI rapidly without native boundary tracking for localized underlying datasets or real-time behavioral auditing. Within a clinical healthcare ecosystem, this introduces severe vectors for Protected Health Information (PHI) exposure and harmful algorithmic bias.



This repository implements a production-ready \*\*Defensive Boundary Middleware Layer\*\* that:

1\. Intercepts incoming pipeline strings to actively discover, flag, and redact specific identifiers mapped to HIPAA boundaries using \*\*Microsoft Presidio\*\*.

2\. Runs validation routines across targeted adversarial evaluation datasets to score clinical treatment uniformity, identifying response drift or demographic bias prior to main production releases.



\---



\## 🧱 Architectural Boundary Topology

The gateway functions as a deterministic proxy standing between upstream data sources and the core machine learning inference engine.



```text

&#x20; \[Raw Patient Charting / Ingestion Data]

&#x20;                  │

&#x20;                  ▼

&#x20; ┌────────────────────────────────────────────────────────┐

&#x20; │         CLINICAL AI SECURITY GATEWAY (Middleware)       │

&#x20; │                                                        │

&#x20; │   ├── Ingestion Boundary: \[Microsoft Presidio]         │

&#x20; │   │   └── Analyzes \& strips PHI based on policy.json   │

&#x20; │   │                                                    │

&#x20; │   └── Evaluation Boundary: \[SafetyEvaluator Engine]    │

&#x20; │       └── Fuzzes demographics for consistency audits.  │

&#x20; └────────────────────────────────────────────────────────┘

&#x20;                  │

&#x20;                  ▼

&#x20; \[Sanitized Vector Database / Secure LLM Processing Inference]

🛡️ Vulnerability Mitigation \& Threat MatrixThis architecture introduces structural controls against critical flaws identified in the OWASP Top 10 for LLM Applications:OWASP LLM Risk IDThreat CategoryGateway Defensive Control MechanismLLM01: Prompt InjectionIndirect/Direct behavioral overrides hidden in clinical documents.Implements system validation loops and context containment blocks.LLM02: Sensitive Info DisclosureAccidental leaking of proprietary or protected patient records (PHI).Deterministic Ingestion Guardrail: Microsoft Presidio interceptor replaces classified entities with \[ENTITY\_REDACTED] tokens pre-inference.LLM03: Training Data PoisoningMalicious or biased datasets skewing clinical logic.Evaluation Boundary Matrix: Audits uniformity thresholds across localized fuzzing datasets to flag anomalies.📋 Compliance \& Framework MappingBy deploying this gateway layer into an enterprise workflow, the organization satisfies core administrative and technical controls across primary regulatory frameworks:1. NIST AI Risk Management Framework (AI RMF)GOVERN: Establishes organizational transparency and technical control policies using config/gateway\_policy.json.MEASURE: Programmatically evaluates deployed model characteristics via the SafetyEvaluator uniformity tracking score.MANAGE: Employs automated sanitization boundaries to continuously respond to and mitigate data-spill risks.2. HIPAA Technical Safeguards (§ 164.306)Data Integrity: Ensures patient records passed to third-party public AI APIs are strictly anonymized, preventing unauthorized exposure of names, corporate phone lines, emails, or government identifiers.🚀 Setup, Installation \& ExecutionPrerequisitesEnsure your Python 3.13 configuration contains the default English language pipelines optimized for Natural Language Processing (NLP) entity extraction:PowerShell# Install core libraries

pip install -r requirements.txt



\# Download required spaCy core pipeline 

python -m spacy download en\_core\_web\_lg

Running the Validation SuiteExecute the interactive primary gateway runtime to process adversarial test strings and evaluate behavioral uniformity matrices:PowerShellpython src/app.py

