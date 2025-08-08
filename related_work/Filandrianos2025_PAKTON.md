# PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements

**Authors:** Giorgos Filandrianos et al.  
**Year:** 2025  
**ArXiv ID:** 2506.00608

## CS197 Analysis

### Problem
Contract review is complex, time-intensive, and requires specialized legal expertise, making it largely inaccessible to non-experts. Legal interpretation involves pervasive ambiguity and subjective assessments. Contracts are typically confidential, restricting use with proprietary models and requiring open-source alternatives.

### Assumption in Prior Work
Prior work assumed that single-model approaches or proprietary systems were sufficient for contract analysis. Limited consideration of privacy-preserving requirements and collaborative agent approaches for handling complex legal document analysis.

### Insight
Multi-agent framework with plug-and-play capabilities can handle contract analysis complexities through collaborative agent workflows. Novel retrieval-augmented generation (RAG) component enables automated legal document review that is more accessible, adaptable, and privacy-preserving.

### Technical Overview
- Fully open-source, end-to-end multi-agent framework
- Plug-and-play architecture for adaptability
- Collaborative agent workflows for complex contract analysis
- Novel RAG component specifically designed for legal documents
- Privacy-preserving design using open-source models
- Handles ambiguity and subjective legal assessments

### Proof/Evaluation
Experiments demonstrate PAKTON outperforms both general-purpose and pretrained models across multiple metrics:
- Improved predictive accuracy
- Better retrieval performance
- Enhanced explainability
- Increased completeness
- Better grounded justifications (validated through human study and automated metrics)

### Impact
- Establishes viability of multi-agent approaches for legal document analysis
- Provides privacy-preserving alternative to proprietary legal AI systems
- Demonstrates improved performance through collaborative agent design
- Enables more accessible automated legal document review
- Offers adaptable framework for various legal analysis tasks

## Relevance to Our Work
Highly relevant for demonstrating multi-agent approaches and privacy-preserving legal AI. Validates importance of explainability and grounded justifications. Supports our approach of making legal analysis more accessible while maintaining accuracy.

## Key Contributions
- First fully open-source multi-agent framework for legal contract Q&A
- Novel RAG component specifically designed for legal documents
- Privacy-preserving architecture using open-source models
- Demonstrated improvements across multiple evaluation dimensions
- Plug-and-play design enabling adaptability

## Limitations
- Focus on contract review rather than consumer comprehension
- No evaluation of plain language explanation capabilities
- Limited assessment of consumer accessibility
- Primarily designed for expert-level legal analysis
- No specific focus on landlord-tenant agreements

## Gap Identification
PAKTON addresses technical contract analysis but doesn't focus on consumer comprehension and plain language explanation. This reinforces our bit flip about the need for consumer-oriented legal AI rather than expert-focused systems.

---
*Analysis conducted using CS197 research methodology*