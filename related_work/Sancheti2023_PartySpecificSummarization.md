# What to Read in a Contract? Party-Specific Summarization of Legal Obligations, Entitlements, and Prohibitions

**Authors**: Abhilasha Sancheti, Aparna Garimella, Balaji Vasan Srinivasan, Rachel Rudinger  
**Year**: 2023  
**Venue**: arXiv:2212.09825  
**URL**: https://arxiv.org/abs/2212.09825

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Contract comprehension is tedious due to length and domain-specificity; different parties need to understand different rights/duties
- **Why it matters**: Contract review costs significant time/money; parties need to understand their specific obligations without wading through irrelevant clauses

### Assumption in Prior Work
- **Key assumption**: Generic contract summarization serves all parties equally well
- **Inadequacy**: Rights and duties requiring review vary significantly for each contracting party
- **Gap**: No party-specific importance ranking for contract summarization

### Insight
- **Novel contribution**: Party-specific extractive summarization recognizing that contract importance varies by contracting party
- **Key insight**: Legal experts can provide reliable pairwise importance comparisons for party-specific contract elements
- **Innovation**: Pipeline combining content categorization (obligations/entitlements/prohibitions) with importance ranking

### Technical Overview
- **Dataset**: ~293K sentence pairs from lease agreements with expert pairwise importance annotations
- **Task Design**: Extract most important obligations, entitlements, and prohibitions for each party
- **Architecture**: (1) Content categorizer identifies sentence types, (2) Importance ranker orders sentences within categories
- **Annotation**: Legal experts provide party-specific pairwise importance comparisons

### Proof/Evaluation
- **Method**: Automatic metrics + human evaluation comparing against text ranking baselines
- **Metrics**: ROUGE scores, human preference judgments on summary quality
- **Validation**: Expert annotation quality assessment, inter-annotator agreement analysis
- **Results**: Domain-specific importance ranking significantly outperforms generic summarization approaches

### Impact
- **Field implications**: Establishes party-specific legal document summarization as distinct research area
- **Practical impact**: Enables automated generation of party-specific contract summaries for faster review
- **Research impact**: Largest expert-annotated dataset for legal contract importance ranking
- **Limitations**: Focus on lease agreements only, extractive (not abstractive) summarization

## Key Assumptions Identified
1. **Party-specific perspective is crucial** for legal document summarization
2. **Expert annotation can capture legal importance** better than automated methods
3. **Obligation/entitlement/prohibition categorization** provides useful structure for legal analysis
4. **Pairwise comparison** is more reliable than absolute importance rating for experts

## Relevance to Our Work
**Very high relevance**: Most similar prior work to our consumer-focused approach
- Similar focus on making contracts comprehensible to specific parties (consumers)
- Expert annotation methodology for legal document analysis
- Lease agreement domain overlap
- Importance-based summarization approach

**Key differences from our approach**:
- Targets contracting parties vs. general consumers
- Extractive summarization vs. plain language explanation + Q&A
- No LLM-as-judge evaluation framework
- Professional-level vs. plain language output

## Potential Bit Flips
1. **Current assumption**: Contract summarization should maintain legal language
   **Potential flip**: Translate legal language to plain English for consumer comprehension
2. **Current assumption**: Serve contracting parties (sophisticated users)
   **Potential flip**: Serve general consumers who need to understand contracts they're signing
3. **Current assumption**: Extractive summarization preserves legal precision
   **Potential flip**: Abstractive explanation prioritizes comprehension over legal precision