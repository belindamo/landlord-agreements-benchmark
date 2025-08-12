# ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting

**Authors**: Steven H. Wang, Maksim Zubkov, Kexin Fan, Sarah Harrell, Yuyang Sun, Wei Chen, Andreas Plesner, Roger Wattenhofer  
**Year**: 2025  
**Venue**: ACL 2025  
**Paper URL**: https://arxiv.org/abs/2501.06582  

## Summary

ACORD introduces the first expert-annotated benchmark for contract clause retrieval, addressing the foundational task of finding relevant precedent clauses for contract drafting.

## CS197 Analysis

### Problem
Contract drafting relies heavily on finding and adapting relevant precedent clauses, but no benchmarks exist for this critical task. Lawyers rarely draft contracts from scratch, instead locating and revising the most relevant precedents.

### Prior Assumptions
- LLMs can generate effective contract clauses from scratch
- General retrieval methods work well for legal contract drafting
- Contract drafting is primarily a generation rather than retrieval task

### Insight
Contract drafting is fundamentally a clause retrieval and adaptation task. Lawyers work from precedents, making clause retrieval the foundational capability for effective legal AI systems.

### Technical Approach
- **Dataset Scale**: 114 queries and over 126,000 query-clause pairs
- **Expert Annotation**: Each query-clause pair ranked on 1-5 star relevance scale
- **Complex Clauses**: Focuses on sophisticated contract elements (Limitation of Liability, Indemnification, Change of Control, Most Favored Nation)
- **Retrieval Architecture**: Bi-encoder retrieval paired with pointwise LLM re-rankers
- **Professional Quality**: Uses real commercial contract clauses from professional practice

### Evaluation
- First expert-annotated benchmark specifically for contract clause retrieval
- Demonstrates substantial room for improvement in current systems
- Shows bi-encoder + LLM re-ranker architecture as promising approach
- Reveals gaps between current capabilities and professional legal requirements

### Impact
- Establishes clause retrieval as foundational legal AI task
- Provides rigorous evaluation framework for contract drafting systems
- Demonstrates importance of expert annotation in legal AI benchmarks
- Reveals limitations of current LLM approaches for professional legal work

## Relevance to Our Work

ACORD provides important insights for our consumer-focused benchmark:

1. **Expert Annotation**: Validates importance of professional legal expertise in dataset creation
2. **Task Definition**: Shows how to structure retrieval tasks for legal documents
3. **Evaluation Methodology**: Demonstrates effective ranking-based evaluation approaches
4. **Professional vs. Consumer**: Highlights gap between professional legal AI and consumer needs

## Contrast with Our Approach

While ACORD targets professional legal practice, our work focuses on consumer comprehension:

- **Audience**: Professional lawyers vs. consumers/tenants
- **Task**: Clause retrieval vs. document comprehension
- **Documents**: Commercial contracts vs. residential lease agreements
- **Evaluation**: Technical retrieval quality vs. consumer understanding

## Key Insights for Literature Review

- **Precedent-Based Work**: Confirms legal work relies on precedent adaptation rather than generation
- **Expert Annotation**: Demonstrates necessity of legal professional involvement
- **Task Complexity**: Shows sophisticated legal reasoning required for contract work
- **Evaluation Standards**: Establishes high bar for legal AI system evaluation

## Citation
```bibtex
@article{wang2025acord,
  title={ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting},
  author={Wang, Steven H and Zubkov, Maksim and Fan, Kexin and Harrell, Sarah and Sun, Yuyang and Chen, Wei and Plesner, Andreas and Wattenhofer, Roger},
  journal={ACL},
  year={2025}
}
```