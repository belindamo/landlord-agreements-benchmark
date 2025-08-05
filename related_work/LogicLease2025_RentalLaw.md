# Prolog and LLMs for Rental Law Compliance in New York

**Authors**: [Authors not clearly listed in abstract]  
**Year**: 2025  
**Venue**: arXiv:2502.09204  
**URL**: https://arxiv.org/abs/2502.09204

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Automating analysis of landlord-tenant legal cases for compliance with rental laws in New York State
- **Why it matters**: Legal cases require careful logical reasoning following laws, but interactions with non-technical users must be in natural language

### Assumption in Prior Work
- **Key assumption**: LLMs alone can handle legal reasoning tasks effectively
- **Inadequacy**: LLMs suffer from hallucinations and lack transparent logical reasoning in legal contexts
- **Gap**: Need for systems that combine logical reasoning with natural language processing for legal compliance

### Insight
- **Novel contribution**: Hybrid approach separating information extraction (LLMs) from legal reasoning (Prolog) for transparency
- **Key insight**: Legal reasoning benefits from explicit logical programming while natural language processing leverages LLM strengths
- **Innovation**: LogicLease system achieving 100% accuracy on rental law compliance with transparent reasoning

### Technical Overview
- **Architecture**: LLMs extract information from case descriptions, Prolog handles legal logic and compliance determination
- **Domain**: New York State landlord-tenant law compliance analysis
- **Approach**: Information extraction → Logical reasoning → Natural language explanation with law citations
- **Performance**: 100% accuracy, 2.57 second average processing time

### Proof/Evaluation
- **Method**: Accuracy testing on landlord-tenant legal cases with ground truth compliance determinations
- **Metrics**: Accuracy, processing time, reasoning transparency (hallucination avoidance)
- **Validation**: Systematic testing across different case types and legal scenarios
- **Results**: Perfect accuracy with clear step-by-step legal reasoning and specific law citations

### Impact
- **Field implications**: Demonstrates hybrid AI approaches for legal reasoning can achieve high accuracy with transparency
- **Practical impact**: Provides automated legal compliance analysis for landlord-tenant relationships
- **Research impact**: Shows separation of concerns (information extraction vs. reasoning) benefits legal AI
- **Limitations**: Limited to New York rental law, requires rule encoding for different jurisdictions

## Key Assumptions Identified
1. **Hybrid approaches outperform pure LLM** solutions for legal reasoning tasks
2. **Transparency is essential** for legal AI systems (explainable reasoning)
3. **Domain-specific legal logic** can be encoded effectively in logical programming languages
4. **Separation of information extraction and reasoning** improves system reliability

## Relevance to Our Work
**Medium-high relevance**: Direct landlord-tenant domain overlap with system evaluation approach
- Same domain focus (landlord-tenant relationships)
- Emphasis on system transparency and explainability
- Systematic evaluation approach with accuracy metrics
- Integration of legal knowledge with AI systems

**Key differences from our approach**:
- Focuses on legal compliance analysis vs. document comprehension
- Targets legal professionals vs. consumers
- Logical reasoning system vs. plain language explanation system
- Case analysis vs. lease agreement analysis

## Potential Bit Flips
1. **Current assumption**: Legal AI should focus on professional-level legal analysis
   **Potential flip**: Focus on consumer-level legal document understanding
2. **Current assumption**: Legal reasoning requires formal logical programming
   **Potential flip**: Natural language explanation can be sufficient for consumer applications
3. **Current assumption**: Accuracy is the primary measure of legal AI success
   **Potential flip**: Comprehensibility and accessibility are equally important metrics