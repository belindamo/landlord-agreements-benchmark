# LegalEval-Q: A New Benchmark for Quality Evaluation of LLM-Generated Legal Text

**Authors:** Yunhan Li et al.  
**Year:** 2025  
**ArXiv ID:** 2505.24826

## CS197 Analysis

### Problem
Current legal AI evaluation benchmarks focus mainly on factual accuracy while neglecting important linguistic quality aspects such as clarity, coherence, and terminology. Need comprehensive evaluation framework that addresses quality dimensions beyond correctness.

### Assumption in Prior Work
Prior legal AI evaluation assumed factual accuracy was the primary measure of quality. Limited attention to linguistic quality aspects crucial for practical legal applications.

### Insight
Legal text quality requires multi-dimensional evaluation including clarity, coherence, and terminology. Regression model approach can effectively evaluate these quality dimensions while revealing fundamental limitations in current training approaches.

### Technical Overview
- Developed regression model for legal text quality evaluation
- Focuses on clarity, coherence, and terminology dimensions
- Created specialized set of legal questions for evaluation
- Analyzed 49 LLMs using comprehensive evaluation framework
- Examined impact of model size, quantization, and architecture choices

### Key Findings
1. Model quality plateaus at 14 billion parameters with only 2.7% improvement at 72 billion
2. Engineering choices (quantization, context length) have negligible impact
3. Reasoning models consistently outperform base architectures
4. Qwen3 series identified as optimal for cost-performance tradeoffs

### Impact
- Establishes standardized evaluation protocols for legal LLMs
- Reveals limitations in current training data refinement approaches
- Provides practical guidance for legal AI deployment decisions
- Offers comprehensive ranking and Pareto analysis for model selection

## Relevance to Our Work
Highly relevant for evaluation methodology focusing on quality dimensions beyond accuracy. Validates importance of clarity and coherence assessment - crucial for consumer-oriented legal AI.

## Key Contributions
- First comprehensive quality evaluation framework for legal LLMs
- Multi-dimensional assessment beyond factual accuracy
- Practical insights for model selection and deployment
- Identification of fundamental training limitations

---
*Analysis conducted using CS197 research methodology*