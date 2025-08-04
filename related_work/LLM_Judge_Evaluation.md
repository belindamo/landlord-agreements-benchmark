# LLM-as-Judge: Evaluation Frameworks and Reliability

**Key Papers**:
- Li et al. (2024): "LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation"
- Sahoo et al. (2025): "Quantitative LLM Judges" 
- Li et al. (2025): "A Comprehensive Assessment on the Robustness of LLM-as-a-Judge"

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Scalable, automated evaluation of LLM outputs using other LLMs as judges
- **Why it matters**: Human evaluation is expensive, slow, and doesn't scale. Traditional metrics (BLEU, ROUGE) inadequate for evaluating complex, open-ended LLM outputs

### Assumption in Prior Work
- **Key assumption**: Human evaluation is the gold standard, but automated metrics can provide reasonable proxies
- **Inadequacy**: Traditional metrics don't capture semantic quality, coherence, or task-specific requirements
- **Gap**: Need for automated evaluation that correlates well with human judgment while being scalable

### Insight
- **Novel contribution**: LLMs can serve as reliable judges for evaluating other LLM outputs when properly prompted
- **Key insight**: Judge LLMs can capture nuanced quality aspects that traditional metrics miss
- **Innovation**: Systematic frameworks for prompt engineering, bias mitigation, and reliability assessment

### Technical Overview
- **Approach**: Use stronger LLMs to evaluate outputs of target LLMs using detailed rubrics
- **Methods**: Zero-shot judging, few-shot with examples, pairwise comparison, scoring rubrics
- **Reliability techniques**: Multiple judge consensus, calibration with human scores, bias detection
- **Robustness**: Defense against adversarial attacks on judge models

### Proof/Evaluation
- **Correlation with humans**: Strong correlation (0.8+) with human scores across multiple domains
- **Consistency**: Good inter-judge agreement between different LLM judges
- **Robustness**: Various attacks tested (prompt injection, position bias, etc.)
- **Scalability**: Orders of magnitude faster and cheaper than human evaluation

### Impact
- **Field implications**: Enables large-scale evaluation of LLM systems
- **Research impact**: Accelerates research by providing reliable automated evaluation
- **Practical impact**: Makes comprehensive evaluation feasible for industry applications
- **Limitations**: Still vulnerable to certain biases and attacks, requires careful prompt engineering

## Key Assumptions Identified
1. **Stronger LLMs can reliably evaluate weaker LLMs** when properly prompted
2. **Detailed rubrics and prompt engineering** are essential for reliable judgment
3. **Judge reliability can be measured and improved** through systematic approaches
4. **Multiple judges and consensus methods** improve evaluation quality

## Relevance to Our Work
**Critical relevance**: LLM-as-judge is central to our evaluation methodology
- Our benchmark uses LLM judges to evaluate plain language summaries and Q&A responses
- Need reliable, scalable evaluation for 100+ documents
- Must ensure judge reliability and minimize bias

**Direct applications**:
- Rubric-based evaluation for plain language quality
- Automated scoring of Q&A accuracy and completeness  
- Scalable evaluation across diverse lease agreements
- Validation against human expert ratings

**Key considerations for our work**:
- Must calibrate judge performance against human expert ratings
- Need robust prompts that capture legal domain requirements
- Should use multiple judges or consensus methods for reliability
- Must test for domain-specific biases in legal context

## Potential Bit Flips
1. **Current assumption**: Human evaluation is always the gold standard
   **Potential flip**: LLM judges can be more consistent and comprehensive than humans for certain tasks
2. **Current assumption**: Evaluation should focus on correctness metrics
   **Potential flip**: Evaluation should focus on user utility and comprehensibility
3. **Current assumption**: Expert judges are better than non-expert judges
   **Potential flip**: Non-expert judges better represent end-user perspective for consumer-facing applications

## Methodological Framework for Our Benchmark
Based on LLM-as-judge literature, our evaluation should include:
1. **Detailed rubrics** for plain language quality, accuracy, completeness
2. **Multiple judge consensus** to ensure reliability
3. **Calibration studies** with human expert ratings
4. **Bias testing** for legal domain-specific issues
5. **Robustness evaluation** against adversarial inputs