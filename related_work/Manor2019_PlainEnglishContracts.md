# Plain English Summarization of Contracts

**Authors**: Laura Manor, Junyi Jessy Li  
**Year**: 2019  
**Venue**: arXiv:1906.00424  
**URL**: https://arxiv.org/abs/1906.00424

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Generating plain English summaries of legal contracts (terms of service) to help users understand what they're agreeing to
- **Why it matters**: 98% of users don't read terms of service due to length and complexity, yet these are binding legal agreements. Information overload and difficult language are primary barriers

### Assumption in Prior Work
- **Key assumption**: Standard abstractive/extractive summarization methods can handle legal document simplification
- **Inadequacy**: Legal language requires heavy abstraction, compression, and style transfer that standard methods can't handle
- **Gap**: Lack of specialized approaches for legal-to-plain-language conversion

### Insight
- **Novel contribution**: First dataset pairing legal text with plain English summaries, highlighting unique challenges of legal language simplification
- **Key insight**: Legal summarization requires three simultaneous tasks: abstraction, compression, AND style transfer
- **Innovation**: Demonstrates that legal language simplification is qualitatively different from general text summarization

### Technical Overview
- **Dataset**: Legal text snippets paired with plain English summaries
- **Analysis**: Shows heavy abstraction required (78-word legal text → 19-word summary)
- **Evaluation**: Manual quality verification, comparison with extractive methods
- **Findings**: Unsupervised extractive methods fail due to abstraction level and style differences

### Proof/Evaluation
- **Method**: Manual evaluation of summary quality, comparison with baseline methods
- **Results**: Standard extractive methods perform poorly on legal text
- **Analysis**: Demonstrates need for specialized legal language processing
- **Validation**: Human evaluation confirms quality of expert-written plain language summaries

### Impact
- **Field implications**: Establishes legal language simplification as distinct NLP challenge
- **Practical impact**: Addresses critical access-to-justice problem for consumers
- **Research impact**: Creates first benchmark for legal-to-plain language conversion
- **Call to action**: Explicitly calls for development of new techniques for legal language simplification

## Key Assumptions Identified
1. **Plain language summarization is distinct from standard summarization** due to legal language complexity
2. **Style transfer is as important as content compression** for legal documents
3. **Manual expert annotation is necessary** for high-quality plain language versions
4. **Current NLP methods are inadequate** for legal language simplification

## Relevance to Our Work
**Very high relevance**: Directly addresses our plain language summarization task
- Same goal: making legal documents accessible to non-experts
- Same challenge: converting complex legal language to plain English
- Same finding: standard NLP approaches insufficient for legal domain

**Direct applicability**:
- Validates need for specialized legal language processing
- Demonstrates importance of plain language for consumer protection
- Shows heavy abstraction/style transfer requirements
- Provides methodological framework for legal summarization evaluation

**Key differences**:
- Focuses on terms of service vs. landlord-tenant agreements
- Dataset creation focus vs. our benchmark evaluation focus
- Academic research vs. our practical application focus

## Potential Bit Flips
1. **Current assumption**: Legal documents should maintain formal legal language
   **Potential flip**: Legal documents should prioritize comprehensibility over legal precision
2. **Current assumption**: AI should extract information from legal documents
   **Potential flip**: AI should translate legal documents into accessible formats
3. **Current assumption**: Legal professionals are the primary users of legal AI
   **Potential flip**: Consumers/non-experts are the most important users of legal AI

## Connections to Our Bit Flip
This paper strongly supports our research direction:
- **Our bit**: Legal AI benchmarks focus on professional-level legal reasoning
- **Our flip**: Legal AI should focus on consumer comprehension and accessibility
- **Validation**: Manor & Li show that plain language conversion is a distinct, unsolved challenge that directly serves consumer needs