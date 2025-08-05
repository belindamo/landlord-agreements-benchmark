# Automatic Legal Writing Evaluation of LLMs

**Authors**: Ramon Pires  
**Year**: 2025  
**Venue**: arXiv:2504.21202  
**URL**: https://arxiv.org/abs/2504.21202

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Evaluating legal writing remains challenging due to complexity of assessing open-ended responses in legal domain
- **Why it matters**: Need systematic benchmarks for legal writing evaluation that are public, frequently updated, with comprehensive guidelines

### Assumption in Prior Work
- **Key assumption**: General language benchmarks can adequately assess legal writing capabilities
- **Inadequacy**: Legal writing requires domain-specific evaluation criteria and expert knowledge
- **Gap**: Lack of specialized legal writing benchmarks with comprehensive evaluation guidelines

### Insight
- **Novel contribution**: oab-bench using Brazilian Bar Examination with comprehensive evaluation guidelines and reference materials
- **Key insight**: LLMs can serve as reliable automated judges for legal writing when properly calibrated with human expertise
- **Innovation**: Demonstrates strong correlation between frontier LLM judges (OpenAI o1) and human scores

### Technical Overview
- **Dataset**: 105 questions across seven areas of law from recent Brazilian Bar Examination editions
- **Evaluation**: Comprehensive guidelines and reference materials used by human examiners
- **Models**: Evaluated Claude-3.5 Sonnet (best performer, 7.93/10), OpenAI o1 (as judge)
- **Approach**: LLM-as-judge evaluation framework with rigorous human expert validation

### Proof/Evaluation
- **Method**: Model performance on legal writing tasks, LLM judge correlation with human scores
- **Metrics**: Average scores out of 10, pass/fail rates on exams, correlation coefficients
- **Validation**: Human expert validation of automated evaluation, approved exam analysis
- **Results**: Claude-3.5 Sonnet passes all 21 exams; strong LLM judge-human correlation despite subjective nature

### Impact
- **Field implications**: Establishes feasibility of automated legal writing evaluation using LLM judges
- **Practical impact**: Enables scalable assessment of legal writing capabilities across models
- **Research impact**: Provides methodology for legal writing evaluation with domain-specific guidelines
- **Limitations**: Portuguese/Brazilian law focus, may not generalize to other legal systems

## Key Assumptions Identified
1. **Domain-specific evaluation guidelines** are essential for legal writing assessment
2. **LLM judges can achieve reliable correlation** with human legal experts when properly designed
3. **Bar examination materials** provide appropriate benchmarking standards for legal writing
4. **Comprehensive reference materials** improve evaluation consistency and quality

## Relevance to Our Work
**High relevance**: Directly addresses LLM-as-judge evaluation methodology for legal domain
- Validates our planned LLM-as-judge evaluation approach for legal content
- Provides evidence for strong human-LLM correlation in legal evaluation
- Demonstrates importance of domain-specific evaluation guidelines  
- Shows feasibility of scalable legal content evaluation

**Key differences from our approach**:
- Professional legal writing vs. plain language comprehension evaluation
- Portuguese/Brazilian law vs. US landlord-tenant law
- Bar exam questions vs. document comprehension tasks
- Legal professional competency vs. consumer accessibility assessment

## Potential Bit Flips
1. **Current assumption**: Legal evaluation should focus on professional competency
   **Potential flip**: Focus on consumer comprehension and accessibility
2. **Current assumption**: Legal writing evaluation requires complex legal reasoning
   **Potential flip**: Plain language quality assessment can be equally valid evaluation target
3. **Current assumption**: Bar exam standards represent optimal evaluation criteria
   **Potential flip**: Consumer understanding standards may be more relevant for accessibility applications