# What to Read in a Contract? Party-Specific Summarization of Legal Obligations, Entitlements, and Prohibitions

**Authors**: Abhilasha Sancheti, Aparna Garimella, Balaji Vasan Srinivasan, Rachel Rudinger  
**Year**: 2023  
**Venue**: EMNLP 2023  
**Paper URL**: https://arxiv.org/abs/2212.09825  

## Summary

Introduces party-specific extractive summarization for legal contracts, focusing on obligations, entitlements, and prohibitions relevant to each contracting party.

## CS197 Analysis

### Problem
Legal contracts are lengthy and domain-specific, making it tedious for parties to understand their specific rights and duties. Key obligations requiring review vary for each contracting party, but existing summarization approaches treat all content equally.

### Prior Assumptions
- Generic summarization approaches work effectively for legal contracts
- Contract summarization doesn't need to account for different party perspectives
- Standard importance metrics capture what matters in legal documents

### Insight
Contract summarization should be party-specific, focusing on obligations, entitlements, and prohibitions relevant to each party. Legal importance differs fundamentally from general text importance and requires domain expertise.

### Technical Approach
- **Two-Module System**: Content categorizer identifies sentences containing obligations/entitlements/prohibitions, importance ranker orders sentences by relevance
- **Expert Annotations**: ~293K sentence pairs from lease agreements with pairwise importance comparisons by legal experts
- **Party-Specific Design**: Separate analysis for tenant vs. landlord perspectives
- **Pipeline Architecture**: Extractive summarization combining categorization and ranking

### Evaluation
- Human evaluation showing system effectiveness
- Comparison against various baselines using automatic and human metrics
- Focus on domain-specific importance rather than generic summarization quality
- Validation that domain expertise essential for legal summarization

### Impact
- First party-specific legal summarization dataset with expert annotations
- Demonstrates domain expertise crucial for legal summarization tasks
- Shows importance of considering different party perspectives in legal documents
- Provides foundation for more sophisticated legal document analysis

## Relevance to Our Work

This work provides crucial methodological insights for our benchmark:

1. **Party-Specific Analysis**: Validates importance of considering tenant vs. landlord perspectives
2. **Expert Annotation**: Shows necessity of legal expertise in creating quality datasets
3. **Legal-Specific Importance**: Demonstrates that legal documents require specialized evaluation criteria
4. **Extractive Approach**: Provides model for evidence-based summarization in legal contexts

## Key Insights for Literature Review

- **Domain Expertise**: Legal summarization requires specialized approaches beyond general NLP
- **Perspective Matters**: Different parties need different information from same contract
- **Evaluation Design**: Legal tasks need domain-appropriate evaluation metrics
- **Scalability**: Expert pairwise comparisons can create large-scale training data

## Application to Our Benchmark

Our work builds on these insights by:
- Focusing specifically on tenant perspective in rental agreements
- Incorporating expert legal annotation in our evaluation design
- Emphasizing practical consumer needs rather than technical extraction
- Validating that consumer understanding requires specialized approaches

## Citation
```bibtex
@article{sancheti2023contrasum,
  title={What to Read in a Contract? Party-Specific Summarization of Important Obligations, Entitlements, and Prohibitions in Legal Documents},
  author={Sancheti, Abhilasha and Garimella, Aparna and Srinivasan, Balaji Vasan and Rudinger, Rachel},
  journal={EMNLP},
  year={2023}
}
```