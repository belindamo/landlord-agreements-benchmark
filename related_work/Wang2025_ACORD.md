# ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting

**Authors**: Steven H. Wang, Maksim Zubkov, Kexin Fan, Sarah Harrell, Yuyang Sun, Wei Chen, Andreas Plesner, Roger Wattenhofer  
**Year**: 2025  
**Venue**: arXiv:2501.06582  
**URL**: https://arxiv.org/abs/2501.06582

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Contract clause retrieval for legal drafting - lawyers need to find the most relevant precedent clauses when drafting new contracts
- **Why it matters**: Contract drafting is foundational legal work but extremely time-consuming. Lawyers rarely draft from scratch, instead locating and revising precedents. Poor precedent selection leads to litigation risks and invalid clauses.

### Assumption in Prior Work
- **Key assumption**: Legal information retrieval could be handled by general-purpose retrieval systems without domain-specific annotation
- **Inadequacy**: General retrieval lacks understanding of legal nuance, precedent quality, and clause relevance for specific contract types
- **Gap**: No expert-annotated retrieval benchmarks specifically for contract drafting workflow

### Insight
- **Novel contribution**: First retrieval benchmark for contract drafting with full expert annotation across complex clause types
- **Key insight**: Contract clause retrieval requires understanding legal precedent quality and contextual relevance beyond text similarity
- **Innovation**: 5-star relevance rating system capturing legal precedent quality gradations

### Technical Overview
- **Dataset**: 114 queries covering complex clauses (Limitation of Liability, Indemnification, Change of Control, Most Favored Nation)
- **Scale**: 126,000+ query-clause pairs with expert relevance ratings (1-5 stars)
- **Annotation**: Legal experts provide detailed relevance judgments based on precedent quality and applicability
- **Evaluation**: Bi-encoder retrievers + pointwise LLM re-rankers as baseline

### Proof/Evaluation
- **Method**: Expert annotation validation, retrieval performance benchmarking
- **Metrics**: Standard IR metrics (NDCG, MAP) adapted for legal precedent quality
- **Validation**: Multiple legal expert annotators with inter-annotator agreement analysis
- **Results**: Shows substantial room for improvement in current retrieval systems for legal applications

### Impact
- **Field implications**: Establishes contract drafting as distinct IR research area requiring domain expertise
- **Practical impact**: Enables development of legal-specific retrieval systems for contract drafting workflow
- **Research impact**: First benchmark allowing systematic evaluation of legal contract retrieval systems
- **Limitations**: Focus on specific complex clause types, English contracts only

## Key Assumptions Identified
1. **Expert annotation is essential** for legal IR benchmarks (vs. automated similarity)
2. **Legal precedent quality matters** beyond textual similarity for retrieval
3. **Contract drafting workflow** requires specialized retrieval systems
4. **Complex legal clauses** need nuanced relevance assessment

## Relevance to Our Work
**High relevance**: Demonstrates importance of expert-annotated benchmarks for legal AI evaluation
- Similar focus on legal document analysis requiring expert judgment
- Validates approach of using expert annotation for legal AI benchmarks
- Provides precedent for multi-level rating systems in legal evaluation

**Key differences from our approach**:
- Focuses on lawyer-facing retrieval vs. our consumer-facing comprehension
- Technical drafting task vs. plain language explanation task
- Retrieval evaluation vs. comprehension/summarization evaluation

## Potential Bit Flips
1. **Current assumption**: Legal IR should focus on lawyer productivity tools
   **Potential flip**: Focus on consumer-facing legal document understanding tools
2. **Current assumption**: Retrieval quality measured by technical accuracy
   **Potential flip**: Quality measured by end-user comprehension and actionability