# ACORD: Expert-Annotated Retrieval Dataset for Legal Contract Drafting

**Full Citation:** Plesner, A., et al. (2025). ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting. *arXiv preprint arXiv:2501.06582*.

## CS197 Analysis Structure

### Problem
- **Core Issue**: Information retrieval is foundational to contract drafting because lawyers rarely draft contracts from scratch
- **Specific Challenge**: Lack of expert-annotated retrieval benchmarks for contract clause retrieval
- **Real-world Gap**: Need for systematic evaluation of how well systems can locate relevant precedent clauses

### Prior Work Assumptions
- Previous contract analysis focused on extraction or classification rather than retrieval
- General IR benchmarks inadequate for specialized legal contract drafting tasks
- Most legal datasets lacked comprehensive expert annotation for retrieval relevance

### Key Insight/Innovation
- **Novel Contribution**: First retrieval benchmark for contract drafting fully annotated by experts
- **Focus Areas**: Complex contract clauses including:
  - Limitation of Liability
  - Indemnification  
  - Change of Control
  - Most Favored Nation
- **Scale**: 114 queries with 126,000+ query-clause pairs ranked 1-5 stars by experts

### Technical Approach
1. **Dataset Construction**: Expert annotation of contract clause relevance on 1-5 star scale
2. **Task Definition**: Find most relevant precedent clauses given a query
3. **Evaluation Framework**: 
   - **Retrieval**: Bi-encoder retrievers
   - **Re-ranking**: Pointwise LLM re-rankers
   - **Assessment**: Standard IR metrics with expert relevance judgments

### Evaluation/Proof
- **Baseline Results**: Bi-encoder + LLM re-ranker shows promising results
- **Performance Gap**: Substantial improvements still needed for real legal work
- **Expert Validation**: Comprehensive expert annotation ensures quality ground truth
- **Open Source**: Available as IR benchmark for NLP community

### Impact and Relevance
- **Methodological Innovation**: First expert-annotated contract clause retrieval benchmark
- **Domain Contribution**: Addresses practical needs of legal contract drafting
- **Research Infrastructure**: Provides evaluation framework for legal IR systems
- **Community Resource**: Open benchmark for NLP research

### Connection to Our Work
- **Expert Annotation Methodology**: Validates our approach of using expert judgment for legal document evaluation
- **Contract Focus**: Demonstrates importance of contract-specific evaluation rather than general legal benchmarks
- **Retrieval vs. Comprehension**: Complementary to our comprehension tasks - both require understanding legal document relevance and quality

### Assumptions Made
- Expert annotation is necessary and sufficient for legal IR evaluation
- Complex contract clauses represent the most challenging and important retrieval scenarios
- Bi-encoder + re-ranker architecture is appropriate baseline for legal contract retrieval
- Star-rating scale (1-5) adequately captures expert relevance judgments

### Research Gap Addressed
- Lack of expert-annotated legal retrieval benchmarks
- Need for contract-specific IR evaluation beyond general legal tasks
- Absence of systematic evaluation framework for contract drafting support tools

### Implications for Legal AI
- **Validation of Expert Annotation**: Reinforces importance of domain expert involvement in legal AI evaluation
- **Contract Specialization**: Shows need for contract-specific rather than general legal AI approaches
- **Practical Focus**: Addresses real workflow needs (precedent retrieval) rather than academic tasks

---

*Added to literature review for expert annotation methodology and contract-specific evaluation approach - demonstrates systematic framework for evaluating legal document analysis systems with expert judgment.*