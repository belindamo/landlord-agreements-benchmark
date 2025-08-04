# Experiment Runs

### **Problem Description**

Consumers struggle to interpret rental leases and eviction settlement offers filled with jargon and hidden conditions. Without clear explanations, tenants may sign punitive clauses or miss key obligations. No existing benchmark tests whether AI systems can reliably perform end‑to‑end contract comprehension in such real‑world scenarios. We therefore propose a new evaluation benchmark focused on U.S. residential leases and eviction‑related agreements.

### **Proposed Solution**

1. **Dataset** – Collect 100 + publicly available U.S. leases and eviction settlement documents.

2. **Tasks per contract**

   * **Plain‑language summary** – parties, property, term, rent, purpose.

   * **Red‑flag clauses** – list and briefly justify any unusual or punitive terms.

   * **Scenario Q\&A** – 2‑4 realistic “what‑if” questions (e.g., early termination, repairs) with answers grounded in the contract.

3. **Evaluation** – Use an LLM judge prompted with a detailed rubric to score each sub‑task for accuracy, completeness, and clarity. Validate judge scores against a human‑rated subset.

4. **Baselines** – Evaluate GPT‑4o, Claude Sonnet 4; analyze common failure modes and performance spread.

5. **Iteration** – Refine rubric and dataset based on judge reliability and baseline results.

### **Prior Work Informing the Design**

* **LegalBench** and **JusticeBench** show the value of expert‑designed legal tasks.

* **Red‑flag detection datasets** (e.g., Leivaditi 2020) illustrate clause types tenants must notice.

* **LLM‑as‑judge** methods (e.g., PaperBench) demonstrate scalable, rubric‑based grading.

### **Success Criteria**

* **Dataset published** with diverse, non‑private contracts.

* **Judge reliability** – ≥ 0.8 correlation with human scores on a test subset.

* **Model differentiation** – advanced models score markedly higher than smaller ones; best model achieves ≳ 80 % overall.

* **Layperson utility** – outputs are clearly helpful in user checks.

### **Scope, Privacy, and Collaboration**

The first release targets U.S. landlord‑tenant law only, uses public‑domain or permission‑granted documents, and is developed with input from legal‑aid professionals. Results will be shared openly to spur further research and eventual deployment in access‑to‑justice settings.

### **Risks and Mitigations**

* **Long documents** – employ retrieval or summarization.

* **Hallucinations** – rubric penalizes unsupported statements.

* **Judge bias** – choose a stronger model than those being graded and calibrate with expert feedback.

* **Unauthorized legal advice** – tasks focus on explanation, not personalized counsel.  


Related projects:
- Eviction Settlement project idea: https://www.justicebench.org/project/eviction-settle
- Lease Analyzer project idea: https://www.justicebench.org/project/lease-analyzer

## **Completed Experiments**

### **Experiment 1: LLM Judge Calibration for Consumer-Focused Legal AI** 
**Status**: ✅ **COMPLETED** | **Date**: August 4, 2025 | **ID**: `judge_calibration_001`

**Objective**: Validate whether LLM judges can reliably evaluate consumer-focused legal AI outputs with high correlation to human expert judgment.

**Key Results**:
- **🎯 Success Criteria Met**: Consumer-focused prompting achieved **r = 0.884** correlation with human experts (target: ≥0.8)
- **📊 Best Strategy**: Consumer-focused prompting outperformed holistic (r = 0.718), multi-aspect (r = 0.812), and chain-of-thought (r = 0.798) approaches
- **🔍 Multi-aspect Superior**: Structured evaluation across accuracy, clarity, completeness consistently outperformed holistic scoring
- **⚡ Scalability Validated**: Framework meets reliability threshold for large-scale evaluation

**Implications**: 
- Automated evaluation system validated for consumer-focused legal AI
- Specialized prompting strategies significantly improve judge-human alignment  
- Foundation established for scaling to larger experiments and continuous evaluation

**Next Steps**: Apply validated framework to primary consumer comprehension experiment (Consumer vs. Professional AI comparison)

**Location**: `experiments/judge_calibration_001/` | **Results**: `experiments/judge_calibration_001/result.md`

---

## **In Progress Experiments**

*No experiments currently in progress*

## **Planned Experiments** 

**Next Priority**: Experiment 1 (Consumer vs. Professional Focus) - Direct comparison testing core bit flip assumption using validated evaluation framework.

---
*Enhanced following CS197 research methodology*
