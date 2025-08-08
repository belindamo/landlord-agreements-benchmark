# ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts

**Authors:** Shuang Liu, Zelong Li, Ruoyun Ma, Haiyan Zhao, Mengnan Du  
**Institution:** Carnegie Mellon University, Rutgers University, Stanford University, New Jersey Institute of Technology  
**Year:** 2025  
**ArXiv ID:** 2508.03080

## CS197 Analysis

### Problem
Need systematic evaluation of whether open-source LLMs could match proprietary LLMs in identifying clause-level legal risks in commercial contracts. The growing interest in locally deploying open-source LLMs for legal tasks while preserving data confidentiality creates urgent need for benchmarking.

### Assumption in Prior Work
Prior work assumed that general benchmarks or limited legal evaluations were sufficient to assess LLM capabilities in legal contexts. Lacked comprehensive comparison between proprietary and open-source models on specific legal tasks.

### Insight
First benchmark specifically designed to thoroughly evaluate clause-level legal risk identification using the Contract Understanding Atticus Dataset (CUAD). Demonstrates that performance evaluation requires assessment across multiple dimensions: correctness, output effectiveness, model size effects, reasoning modes, and quantization impacts.

### Technical Overview
- Evaluated 4 proprietary and 15 open-source LLMs on CUAD dataset
- Assessed performance across five key dimensions:
  1. Correctness vs output effectiveness comparison
  2. Model size scaling effects
  3. Impact of reasoning ("thinking") mode
  4. Frequency of "no related clause" responses
  5. Model quantization trade-offs
- Used established legal benchmark with expert annotations

### Proof/Evaluation
Comprehensive evaluation revealed five key findings:
1. Proprietary models outperform open-source in correctness and effectiveness
2. Larger open-source models generally perform better, with diminishing returns at scale
3. Reasoning mode improves effectiveness but reduces correctness (over-complication)
4. Open-source models show more "laziness" with frequent "no related clause" responses
5. Quantization speeds inference but reduces performance

### Impact
- Establishes first comprehensive benchmark for comparing proprietary vs open-source LLMs on legal risk identification
- Provides practical guidance for organizations choosing between model types for legal applications
- Reveals that current open-source models require targeted fine-tuning for high-stakes legal settings
- Demonstrates most LLMs perform at junior legal assistant level
- Code availability enables reproducible legal LLM evaluation

## Relevance to Our Work
Highly relevant as it provides methodological framework for legal benchmarking and validates need for domain-specific evaluation. Shows importance of clause-level analysis and multi-dimensional evaluation metrics. Supports our approach of comprehensive evaluation beyond simple accuracy metrics.

## Key Contributions
- First benchmark specifically comparing proprietary vs open-source LLMs for legal risk identification
- Multi-dimensional evaluation framework for legal AI assessment
- Practical insights for legal AI deployment decisions
- Open-source evaluation tool for reproducible research

## Limitations
- Focus on commercial contracts rather than consumer agreements
- Limited to English language evaluation
- CUAD dataset constraints may not reflect all legal document types
- No evaluation of consumer comprehension or plain language aspects

---
*Analysis conducted using CS197 research methodology*