# Literature Review

# Literature Review

## Key Papers

### Legal Benchmarking and Evaluation

**LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning** (Guha et al., 2023)
- **Problem**: Need systematic evaluation of LLM capabilities in legal contexts beyond general language benchmarks
- **Prior Assumptions**: General language benchmarks adequately measure legal AI capabilities
- **Key Insight**: Legal reasoning requires specialized evaluation with expert collaboration across diverse legal tasks
- **Technical Approach**: Collaborative benchmark creation with legal experts across multiple legal reasoning categories
- **Evaluation**: Systematic evaluation revealing significant performance gaps in current LLMs on legal tasks
- **Impact**: Established legal reasoning as distinct evaluation category, foundational benchmark for legal AI
- **Relevance**: Provides methodological framework for domain-specific legal benchmarking

**LEXam: Benchmarking Legal Reasoning on 340 Law Exams** (Fan et al., 2025)
- **Problem**: Long-form legal reasoning remains challenging for LLMs despite advances in test-time scaling
- **Prior Assumptions**: Test-time scaling improvements would transfer directly to complex legal reasoning tasks
- **Key Insight**: Law exam evaluation with explicit reasoning guidance reveals structured legal thinking requirements
- **Technical Approach**: 4,886 questions from 340 law exams with explicit reasoning guidance (issue spotting, rule recall, application)
- **Evaluation**: LLM-as-judge paradigm with human expert validation for consistent reasoning assessment
- **Impact**: Demonstrates LLM struggles with multi-step legal reasoning, provides scalable evaluation framework
- **Relevance**: Shows importance of structured evaluation for legal AI systems

**Identifying Legal Holdings with LLMs** (Arvin et al., 2025)
- **Problem**: Assessing LLM performance on established legal benchmarks (CaseHOLD)
- **Prior Assumptions**: LLM legal performance primarily due to memorization of training data
- **Key Insight**: Performance scales with model size, maintained under citation anonymization (not just memorization)
- **Technical Approach**: Novel citation anonymization test preserving semantic meaning while using fictitious case names
- **Evaluation**: Systematic evaluation across model sizes (3B to 90B+) with and without citation information
- **Impact**: Shows promise for legal analytics (0.744 macro F1) while validating non-memorization performance
- **Relevance**: Validates scaling approaches and addresses memorization concerns for legal AI

### Contract Analysis and Document Comprehension

**A Benchmark for Lease Contract Review** (Leivaditi et al., 2020) ⭐ *Most Relevant*
- **Problem**: Automating lease agreement review for entity extraction and red flag detection
- **Prior Assumptions**: General contract analysis methods adequate for lease agreements
- **Key Insight**: Lease agreements require specialized analysis distinct from general contracts
- **Technical Approach**: ALeaseBERT model trained on 179 lease documents with expert annotations
- **Evaluation**: Entity extraction and red flag detection tasks with domain-specific metrics
- **Impact**: First specialized dataset and model for lease analysis, established need for domain-specific approaches
- **Relevance**: Direct predecessor work in lease agreement analysis

**ContraSUM: Party-Specific Contract Summarization** (Sancheti et al., 2022) ⭐ *Highly Relevant*
- **Problem**: Legal contracts are long and complex, requiring manual hours for parties to understand their obligations
- **Prior Assumptions**: Generic contract summarization sufficient; no need for party-specific or commitment-type analysis
- **Key Insight**: Party-specific summarization categorizing obligations, entitlements, and prohibitions provides more useful analysis
- **Technical Approach**: Two-module system with content categorizer and importance ranker using 293K expert annotations
- **Evaluation**: Automatic and human evaluation comparing against text ranking baselines on lease agreements
- **Impact**: First party-specific contract analysis system with structured commitment categorization
- **Relevance**: Most similar to our landlord-tenant focus, demonstrates expert annotation methodology for contract analysis

**CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review** (Hendrycks et al., 2021)
- **Problem**: Need large-scale expert-annotated dataset for legal contract analysis
- **Prior Assumptions**: General NLP datasets adequate for legal contract tasks
- **Key Insight**: Expert annotation essential for legal AI, transformer performance influenced by model design and data size
- **Technical Approach**: 13,000+ expert annotations across 510 contracts for 41 label types
- **Evaluation**: Contract clause extraction and classification with expert-validated ground truth
- **Impact**: Foundation dataset for contract analysis research, established expert annotation standards
- **Relevance**: Demonstrates expert annotation methodology and contract analysis task design

**ACORD: Expert-Annotated Contract Clause Retrieval Dataset** (Plesner et al., 2025)
- **Problem**: Information retrieval fundamental to contract drafting, but lacks expert-annotated retrieval benchmarks
- **Prior Assumptions**: General IR benchmarks sufficient for legal contract retrieval tasks
- **Key Insight**: Contract clause retrieval requires specialized evaluation with expert relevance judgments
- **Technical Approach**: 114 queries with 126,000+ query-clause pairs rated 1-5 stars by experts, focusing on complex clauses
- **Evaluation**: Bi-encoder retrievers with pointwise LLM re-rankers on expert-annotated relevance judgments
- **Impact**: First expert-annotated contract clause retrieval benchmark for legal IR research
- **Relevance**: Validates expert annotation approach and contract-specific evaluation methodology

**The Hidden Structure - Improving Legal Document Understanding** (Braun et al., 2025)
- **Problem**: Impact of document structure on LLM processing of legal contracts
- **Prior Assumptions**: LLMs can process legal documents effectively regardless of formatting and structure
- **Key Insight**: Document structure significantly affects performance, prompt engineering crucial for optimal results
- **Technical Approach**: Systematic evaluation of document formatting and prompting strategies on legal contract tasks
- **Evaluation**: Accuracy measurements showing 20-point improvements with proper structuring
- **Impact**: Demonstrates critical importance of document preprocessing for legal AI systems
- **Relevance**: Critical for our document processing and evaluation methodology

### Plain Language and Accessibility

**Plain English Summarization of Contracts** (Manor & Li, 2019) ⭐ *Highly Relevant*
- **Problem**: Converting complex legal language to plain English for user comprehension
- **Prior Assumptions**: Standard text summarization methods adequate for legal language simplification
- **Key Insight**: Legal summarization requires simultaneous abstraction, compression, and style transfer
- **Technical Approach**: Multi-task learning combining summarization with style transfer for legal-to-plain language conversion
- **Evaluation**: Human evaluation of comprehensibility and accuracy of plain language outputs
- **Impact**: Demonstrates that standard NLP methods inadequate for legal language simplification
- **Relevance**: Directly addresses our plain language summarization task and consumer accessibility goals

**TermSight: Making Service Contracts Approachable** (Huang et al., 2025)
- **Problem**: Terms of service are unreadable but legally binding, burdening users with complex legal terminology
- **Prior Assumptions**: Legal documents inherently incomprehensible to consumers; no effective solutions for accessibility
- **Key Insight**: AI-powered reading interfaces can significantly reduce difficulty and increase user engagement through multiple support levels
- **Technical Approach**: Multi-level interface with visual summaries, categorized plain-language summaries, and contextualized definitions
- **Evaluation**: Within-subjects study (N=20) showing reduced difficulty and increased willingness to read
- **Impact**: Demonstrates measurable improvements in consumer legal document comprehension
- **Relevance**: Validates user-centered approach to legal document accessibility

**SimplifyMyText: Plain Language Text Simplification** (Färber et al., 2025)
- **Problem**: Limited availability of simplified materials creates barriers to comprehension for diverse audiences
- **Prior Assumptions**: General text simplification adequate for legal and specialized content
- **Key Insight**: Plain language practices require tailored customization for different target groups and simplicity levels
- **Technical Approach**: LLM-based system (GPT-4, Llama-3) with flexible customization for various audiences and input formats
- **Evaluation**: Multi-metric evaluation across different target groups and simplification levels
- **Impact**: First comprehensive plain language system leveraging LLMs for inclusive content creation
- **Relevance**: Demonstrates LLM capabilities for plain language conversion aligned with our accessibility goals

### LLM-as-Judge Evaluation

**LLMs-as-Judges: A Comprehensive Survey** (Li et al., 2024)
- **Problem**: Need scalable, automated evaluation of LLM outputs beyond traditional metrics
- **Prior Assumptions**: Human evaluation only reliable method; automated metrics insufficient for complex tasks
- **Key Insight**: LLMs can serve as reliable judges when properly prompted and calibrated
- **Technical Approach**: Systematic analysis of prompting strategies, calibration methods, and correlation studies
- **Evaluation**: Meta-analysis showing 0.8+ correlation with human judgment across tasks
- **Impact**: Enables large-scale evaluation with strong human-AI agreement
- **Relevance**: Central to our evaluation methodology using LLM judges for scalable assessment

**Quantitative LLM Judges** (Sahoo et al., 2025)
- **Problem**: Improving alignment between LLM judge scores and human ratings
- **Prior Assumptions**: LLM judges inherently aligned with human preferences without calibration
- **Key Insight**: Regression models can improve judge accuracy using textual evaluation and scores
- **Technical Approach**: Regression-based calibration using textual evaluations paired with numerical scores
- **Evaluation**: Computational efficiency and statistical efficiency improvements over fine-tuning approaches
- **Impact**: More efficient calibration method with better performance under limited human feedback
- **Relevance**: Provides techniques for calibrating our LLM judge evaluation system

**oab-bench: Brazilian Bar Exam Legal Writing Evaluation** (Pires et al., 2025)
- **Problem**: Lack of benchmarks for evaluating legal writing with comprehensive evaluation guidelines
- **Prior Assumptions**: General writing evaluation sufficient for legal domain assessment
- **Key Insight**: Legal writing requires specialized evaluation incorporating domain expertise and structured guidelines
- **Technical Approach**: 105 questions across seven law areas with comprehensive grading guidelines from human examiners
- **Evaluation**: LLM-as-judge evaluation showing strong correlation with human scores for approved exams
- **Impact**: First comprehensive legal writing benchmark with validated automated evaluation
- **Relevance**: Demonstrates LLM judge effectiveness for legal text quality assessment

**LegalEval-Q: Quality Evaluation for Legal Text** (Li & Wu, 2025)
- **Problem**: Current legal AI evaluation focuses on factual accuracy while neglecting linguistic quality aspects
- **Prior Assumptions**: Factual accuracy sufficient metric for legal text evaluation
- **Key Insight**: Legal text quality requires multi-dimensional assessment including clarity, coherence, and terminology
- **Technical Approach**: Regression model evaluating quality across three dimensions, tested on 49 LLMs
- **Evaluation**: Statistical analysis revealing quality plateau at 14B parameters, minimal impact of engineering choices
- **Impact**: First comprehensive quality-focused legal text evaluation framework
- **Relevance**: Supports our multi-dimensional evaluation approach emphasizing clarity and accessibility

### Legal AI Applications

**LRAGE: Legal Retrieval Augmented Generation Evaluation Tool** (Park et al., 2025)
- **Problem**: Holistic evaluation of RAG systems in legal domain across multiple components
- **Key Insight**: Legal RAG performance depends on retrieval corpora, algorithms, rerankers, LLMs, and metrics
- **Impact**: Open-source tool for systematic legal RAG evaluation across languages
- **Relevance**: Provides framework for comprehensive legal AI system evaluation

**Evaluating Tenant-Landlord Tensions Using Generative AI** (Ren et al., 2024)
- **Problem**: Understanding tenant concerns through social media data analysis
- **Key Insight**: LDA + GPT-4 can classify and reveal temporal trends in tenant concerns
- **Impact**: Shows AI can identify patterns in landlord-tenant relationships and policy impacts
- **Relevance**: Demonstrates AI applications in landlord-tenant domain, validates problem importance

## Summary of Field

The legal AI field shows four major research trends:

**1. Specialized Legal Benchmarking**: Recognition that general language benchmarks inadequately measure legal AI capabilities. Multiple papers (LegalBench, LEXam, CaseHOLD, LegalEval-Q) establish domain-specific evaluation as essential, with recent work expanding from accuracy to quality assessment.

**2. Consumer-Focused Legal Accessibility**: Growing emphasis on making legal documents accessible to non-experts through plain language conversion (Manor & Li, TermSight, SimplifyMyText) and user-centered interfaces rather than just expert-level analysis.

**3. LLM-as-Judge Evaluation**: Convergence on LLM judges as scalable evaluation method with strong human correlation (0.8+) when properly calibrated and prompted, with specialized applications in legal writing assessment (oab-bench).

**4. Contract-Specific Analysis**: Recognition that different legal document types require specialized approaches, with focused work on contracts (CUAD, ACORD, ContraSUM) and leases (Leivaditi et al.) rather than general legal text processing.

**Common Technical Assumptions Across Literature**:
- Expert annotation is necessary for legal AI datasets (validated across CUAD, ACORD, ContraSUM, LEXam)
- Domain-specific approaches outperform general methods (consistent across legal vs. general benchmarks)
- Document structure significantly impacts LLM performance (Braun et al. show 20-point improvements)
- Plain language conversion requires specialized techniques beyond standard summarization (Manor & Li, SimplifyMyText)
- LLM scaling improves legal task performance, but with diminishing returns (LegalEval-Q shows plateau at 14B parameters)
- Multi-dimensional quality assessment necessary beyond accuracy (clarity, coherence, terminology from LegalEval-Q)
- Party-specific analysis more useful than generic document processing (ContraSUM demonstrates for contracts)

## Gaps Identified

**1. Consumer-Focused Legal AI**: Most work targets legal professionals rather than end consumers who need legal documents explained in accessible terms.

**2. Landlord-Tenant Specific Analysis**: Limited work specifically on landlord-tenant agreements despite widespread consumer need. Leivaditi et al. (2020) is closest but focuses on technical extraction rather than comprehension.

**3. End-to-End Comprehension Evaluation**: Existing benchmarks test technical tasks (entity extraction, classification) rather than holistic document understanding and explanation.

**4. Real-World Document Complexity**: Most datasets use clean, well-formatted documents rather than the complex, varied formatting found in actual rental agreements.

**5. Integrated Quality and Accessibility Evaluation**: While LegalEval-Q addresses quality and TermSight addresses accessibility, no work comprehensively evaluates both legal accuracy and consumer comprehensibility in integrated benchmarks.

**6. Real-World Consumer Use Cases**: Limited evaluation on actual consumer scenarios where legal document comprehension leads to actionable decisions (e.g., understanding lease obligations before signing).

## How Our Work Fits

Our landlord-tenant agreement benchmark addresses multiple identified gaps:

**Filling the Consumer Focus Gap**: Unlike existing legal AI work targeting professionals, our benchmark evaluates AI's ability to help consumers understand rental agreements through plain language summaries and scenario-based Q&A.

**Domain-Specific Innovation**: Builds on Leivaditi et al.'s lease analysis work but shifts from technical extraction to comprehension evaluation, addressing the specific needs of tenants facing complex lease language.

**Methodological Contributions**: 
- Combines plain language summarization with scenario-based evaluation
- Uses LLM-as-judge methodology calibrated for legal accuracy and plain language quality
- Addresses real-world document complexity with diverse formatting and clauses

**Literature-Level Bit Flip**: Challenges the assumption that legal AI should focus on professional-level legal reasoning and extraction tasks. Instead, we argue that the highest impact comes from making legal documents comprehensible to consumers who must live with the consequences of these agreements.

**Building on Established Methods**: 
- Expert annotation methodology (CUAD, ACORD, ContraSUM)
- LLM-as-judge evaluation with validation (LEXam, oab-bench, Sahoo et al.)
- Multi-dimensional quality assessment (LegalEval-Q combining accuracy and linguistic quality)
- Plain language accessibility focus (Manor & Li, TermSight, SimplifyMyText)
- Party-specific analysis approach (ContraSUM's obligations/entitlements framework)

**Novel Contributions**:
- First comprehensive consumer-oriented legal document comprehension benchmark
- Integration of legal accuracy with accessibility evaluation
- Real-world consumer decision-making scenarios rather than academic legal tasks
- Landlord-tenant domain specialization addressing identified gap

This positions our work as both practically impactful (addressing real consumer needs) and methodologically novel (first comprehensive consumer-oriented legal document comprehension benchmark).

---
*Enhanced using CS197 research methodology*


---
*This section is being enhanced by The Research Company AI Agent*
