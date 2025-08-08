# LEXam: Benchmarking Legal Reasoning on 340 Law Exams

**Authors:** Yu Fan, Jingwei Ni, Jakob Merane, Etienne Salimbeni, Yang Tian, Yoan Hermstrüwer, Yinya Huang, Mubashara Akhtar, Florian Geering, Oliver Dreyer, Daniel Brunner, Markus Leippold, Mrinmaya Sachan, Alexander Stremitzer, Christoph Engel, Elliott Ash, Joel Niklaus  
**Institution:** ETH Zurich, University of Zurich, University of Lausanne, Max Planck Institute, Omnilex, University of St. Gallen, Swiss Federal Supreme Court, Niklaus.ai  
**Year:** 2025  
**ArXiv ID:** 2505.12864

## CS197 Analysis

### Problem
Long-form legal reasoning remains a key challenge for large language models despite advances in test-time scaling. Existing legal benchmarks inadequately assess structured, multi-step legal reasoning required for real legal practice.

### Assumption in Prior Work
Prior legal AI evaluation assumed that general reasoning benchmarks or simple legal Q&A tasks were sufficient to measure legal reasoning capabilities. Limited focus on structured legal thinking processes like issue spotting, rule recall, and rule application.

### Insight
Legal reasoning evaluation requires comprehensive assessment across diverse legal subjects with explicit reasoning guidance. Real legal competency demands structured multi-step reasoning that mirrors actual legal education and practice, not just factual knowledge retrieval.

### Technical Overview
- Compiled 340 law exams from 116 law school courses
- Created dataset of 4,886 questions in English and German
- Includes 2,841 long-form open-ended questions and 2,045 multiple-choice questions
- Provides explicit reasoning guidance for open questions (issue spotting, rule recall, rule application)
- Employs LLM-as-Judge evaluation paradigm with human expert validation
- Covers range of legal subjects and degree levels

### Proof/Evaluation
- Comprehensive evaluation reveals significant challenges for current LLMs
- Models notably struggle with open questions requiring structured, multi-step legal reasoning
- Dataset effectively differentiates between models with varying capabilities
- LLM-as-Judge evaluation validated against human expert assessment
- Provides scalable method for assessing legal reasoning quality beyond accuracy metrics

### Impact
- Establishes comprehensive benchmark for legal reasoning evaluation
- Reveals limitations in current LLM legal reasoning capabilities
- Provides framework for evaluating structured legal thinking processes
- Enables systematic comparison of legal AI capabilities
- Sets foundation for improving legal reasoning in language models

## Relevance to Our Work
Highly relevant for establishing evaluation methodology and understanding current limitations in legal reasoning. Validates need for structured evaluation approaches and demonstrates importance of multi-step reasoning assessment. Supports our LLM-as-Judge methodology and comprehensive evaluation framework.

## Key Contributions
- Most comprehensive legal reasoning benchmark to date (4,886 questions across diverse subjects)
- Explicit reasoning guidance reflecting actual legal thinking processes
- Validated LLM-as-Judge evaluation paradigm for legal reasoning
- Bilingual evaluation capability (English/German)
- Open benchmark enabling reproducible legal reasoning research

## Limitations
- Focus on academic legal reasoning rather than practical consumer applications
- Limited evaluation of plain language explanation capabilities
- No assessment of consumer comprehension or accessibility
- Emphasis on expert-level legal reasoning vs. consumer communication

## Gap Identification
LEXam focuses on professional legal reasoning competency but doesn't address consumer-facing applications where legal concepts need to be explained in accessible terms. This validates our focus on consumer comprehension rather than expert-level legal analysis.

---
*Analysis conducted using CS197 research methodology*