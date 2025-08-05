# What to Read in a Contract? Party-Specific Summarization of Legal Obligations, Entitlements, and Prohibitions

## Citation
Sancheti, A., Garimella, A., Srinivasan, B. V., & Rudinger, R. (2022). What to Read in a Contract? Party-Specific Summarization of Important Obligations, Entitlements, and Prohibitions in Legal Documents. arXiv preprint arXiv:2212.09825.

## CS197 Analysis

### Problem
Reviewing and comprehending key obligations, entitlements, and prohibitions in legal contracts can be a tedious task due to their length and domain-specificity. Furthermore, the key rights and duties requiring review vary for each contracting party, making generic summaries inadequate.

### Prior Assumptions
- Contract summarization is a general task that can be addressed with standard NLP techniques
- All contracting parties need the same information from contract summaries
- Importance ranking in legal documents follows general text importance patterns
- Standard extractive summarization methods work effectively for legal contracts

### Key Insight
Contract summarization must be **party-specific** to be truly useful. Different contracting parties (e.g., tenant vs. landlord) need different information extracted and prioritized from the same contract. Legal importance differs fundamentally from general text importance and requires domain-specific ranking approaches.

### Technical Approach
- **CONTRASUM**: Two-module extractive summarization system
  1. **Content Categorizer**: Identifies sentences containing obligations, entitlements, and prohibitions for each party
  2. **Importance Ranker**: Compares importance among sentences within each category for each party
- Dataset: ~293K sentence pairs from lease agreements with expert importance annotations
- Pairwise importance ranking trained on legal expert annotations
- Pipeline-based approach for party-specific summary generation

### Evaluation
- Automatic metrics against text ranking baselines
- Human evaluation for summary quality
- Demonstrates effectiveness over general-purpose ranking methods
- Validates need for domain-specific importance measures

### Impact
- First party-specific legal contract summarization approach
- Demonstrates that legal importance differs from general text importance
- Provides framework for personalized legal document comprehension
- Shows effectiveness of expert annotation in legal AI systems

### Relevance to Our Work
- **Highly Relevant**: Directly addresses consumer-focused legal document comprehension
- Validates party-specific approach (tenant vs. landlord perspectives)
- Demonstrates effectiveness of expert-annotated legal datasets
- Shows importance of domain-specific ranking for legal documents
- Focuses on practical consumer needs rather than expert analysis

### Assumptions Challenged
- **Bit Flip**: Challenges assumption that contract summarization is a generic task by demonstrating the critical need for party-specific, legally-informed importance ranking that serves different stakeholder perspectives