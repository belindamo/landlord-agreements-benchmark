# PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements

## Citation
Filandrianos, G. et al. (2025). PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements. arXiv preprint arXiv:2506.00608.

## CS197 Analysis

### Problem
Contract review is a complex and time-intensive task that typically demands specialized legal expertise, rendering it largely inaccessible to non-experts. Legal interpretation is rarely straightforward—ambiguity is pervasive, and judgments often hinge on subjective assessments. Additionally, contracts are usually confidential, restricting their use with proprietary models and necessitating reliance on open-source alternatives.

### Prior Assumptions
- Contract analysis requires specialized legal expertise
- Proprietary models are unsuitable for confidential legal documents
- Single-model approaches can handle complex legal document analysis
- Contract analysis is primarily a technical extraction task

### Key Insight
Contract analysis can be democratized through a fully open-source, end-to-end, multi-agent framework with plug-and-play capabilities. The complexity of contract analysis is better addressed through collaborative agent workflows and novel retrieval-augmented generation (RAG) components rather than monolithic approaches.

### Technical Approach
- Multi-agent collaborative framework
- Novel RAG component for legal document retrieval
- Plug-and-play architecture for adaptability
- Open-source implementation for privacy preservation
- End-to-end contract analysis pipeline

### Evaluation
Human study and automated metrics evaluating:
- Predictive accuracy
- Retrieval performance  
- Explainability
- Completeness
- Grounded justifications

Results: PAKTON outperforms both general-purpose and pretrained models across all evaluation dimensions.

### Impact
- Makes contract analysis more accessible to non-experts
- Addresses privacy concerns through open-source approach
- Demonstrates effectiveness of multi-agent collaboration in legal AI
- Provides scalable framework for automated legal document review

### Relevance to Our Work
- Directly addresses consumer accessibility gap in legal AI
- Validates multi-agent approaches for complex legal document analysis  
- Demonstrates importance of privacy-preserving legal AI solutions
- Shows potential for collaborative AI systems in legal comprehension tasks

### Assumptions Challenged
- **Bit Flip**: Challenges assumption that legal AI must be expert-focused by demonstrating accessible, collaborative frameworks for consumer-level contract analysis