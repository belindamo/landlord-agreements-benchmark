# LogicLease: Prolog and LLMs for Rental Law Compliance in New York

**Authors:** Sanskar Sehgal, Yanhong A. Liu  
**Institution:** Stony Brook University  
**Year:** 2025  
**ArXiv ID:** 2502.09204

## CS197 Analysis

### Problem
Legal cases require careful logical reasoning following laws, while interactions with non-technical users must be in natural language. Landlord-tenant legal cases need automated analysis that combines transparent legal reasoning with accessible natural language interaction.

### Assumption in Prior Work
Prior legal AI work assumed that either pure LLM approaches or traditional rule-based systems alone were sufficient for legal analysis. Limited focus on combining logical reasoning with natural language processing for transparency and accuracy.

### Insight
Neuro-symbolic approach combining LLMs for information extraction with Prolog for legal reasoning achieves greater transparency and control while avoiding hallucinations common in pure LLM approaches. Separation of concerns enables reliable legal logic with natural language accessibility.

### Technical Overview
- Combines LLMs for information extraction with Prolog for legal reasoning
- Focuses specifically on landlord-tenant legal cases in New York State
- Analyzes case descriptions and cites relevant laws
- Achieves transparency through step-by-step logical reasoning
- Separates information extraction from legal reasoning for better control
- Provides clear citations to specific legal statutes

### Proof/Evaluation
- Achieved 100% accuracy on test cases
- Average processing time of 2.57 seconds per case
- Demonstrated robustness across various case scenarios
- Avoided hallucinations common in pure LLM approaches
- Provided clear, step-by-step reasoning with legal citations
- Outperformed state-of-the-art LLM-based legal analysis systems

### Impact
- Demonstrates viability of neuro-symbolic approaches for legal AI
- Provides transparent and explainable legal reasoning
- Shows how to combine accuracy with interpretability in legal applications
- Establishes framework for reliable legal compliance analysis
- Addresses specific landlord-tenant legal domain needs

## Relevance to Our Work
Extremely relevant as it directly addresses landlord-tenant legal analysis with focus on transparency and accuracy. Validates importance of our domain focus and demonstrates need for specialized approaches to rental law. Shows how to achieve both technical accuracy and user accessibility.

## Key Contributions
- First neuro-symbolic system specifically for landlord-tenant legal analysis
- Achieves perfect accuracy while maintaining transparency
- Demonstrates effective separation of information extraction and legal reasoning
- Provides framework for avoiding LLM hallucinations in legal contexts
- Offers practical system for real-world legal compliance checking

## Limitations
- Limited to New York State rental law
- Focuses on legal compliance rather than consumer comprehension
- No evaluation of plain language explanation capabilities
- Professional-oriented rather than consumer-accessible interface
- Limited to case analysis rather than document comprehension

## Gap Identification
LogicLease addresses legal accuracy in landlord-tenant domain but doesn't focus on consumer comprehension and accessibility. This reinforces our bit flip - the gap between technical legal analysis and consumer-understandable explanations of rental agreements.

## Bit Flip Validation
LogicLease represents the technical legal analysis assumption we're challenging. While it achieves perfect legal accuracy, it doesn't address consumer comprehension needs - validating our focus on making legal documents accessible to tenants.

---
*Analysis conducted using CS197 research methodology*