# LEXam: Benchmarking Legal Reasoning on 340 Law Exams

## Citation
Fan, Y., Ni, J., Merane, J., et al. (2025). LEXam: Benchmarking Legal Reasoning on 340 Law Exams. arXiv preprint arXiv:2505.12864.

## CS197 Analysis

### Problem
Long-form legal reasoning remains a key challenge for large language models (LLMs) despite recent advances in test-time scaling. Existing legal benchmarks focus on specific tasks rather than comprehensive legal reasoning abilities that mirror real-world legal education and practice.

### Prior Assumptions
- Legal AI evaluation can be adequately captured by specific technical tasks
- Multiple-choice questions sufficiently test legal reasoning capabilities
- General legal benchmarks represent the full spectrum of legal reasoning
- LLM scaling automatically improves complex legal reasoning

### Key Insight
Legal reasoning evaluation requires **structured, multi-step assessment** that mirrors real legal education. Law exams provide a comprehensive evaluation framework because they test the full spectrum of legal reasoning: issue spotting, rule recall, rule application, and analytical reasoning across diverse legal domains.

### Technical Approach
- **LEXam Dataset**: 4,886 law exam questions from 340 law exams
- Coverage: 116 law school courses across various subjects and degree levels
- Languages: English and German
- Question types: 
  - 2,841 long-form, open-ended questions
  - 2,045 multiple-choice questions
- **Explicit reasoning guidance** for open questions (issue spotting, rule recall, rule application)
- **LLM-as-a-Judge evaluation** with rigorous human expert validation

### Evaluation
- Comprehensive evaluation across current state-of-the-art LLMs
- Demonstrates significant challenges for current models on open-ended questions
- Shows effectiveness in differentiating between models with varying capabilities
- Scalable evaluation methodology beyond simple accuracy metrics
- Human expert validation of LLM judge evaluations

### Impact
- Establishes comprehensive benchmark for legal reasoning evaluation
- Demonstrates limitations of current LLMs in structured legal reasoning
- Provides scalable evaluation framework for legal AI development
- Shows importance of multi-step reasoning in legal contexts

### Relevance to Our Work
- Provides methodological framework for structured legal evaluation
- Validates LLM-as-judge approach with expert validation
- Demonstrates importance of multi-step reasoning in legal AI assessment
- Shows need for comprehensive evaluation beyond technical tasks
- Highlights challenges in long-form legal reasoning that our work addresses

### Assumptions Challenged
- **Bit Flip**: Challenges assumption that legal AI evaluation can be reduced to technical tasks by demonstrating the need for comprehensive, structured reasoning assessment that mirrors real legal education and practice