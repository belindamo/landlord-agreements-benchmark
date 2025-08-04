# Literature Review

## Key Papers

### Legal Benchmarking and Evaluation

**LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning** (Guha et al., 2023)
- **Problem**: Need systematic evaluation of LLM capabilities in legal contexts beyond general language benchmarks
- **Key Insight**: Legal reasoning requires specialized evaluation with expert collaboration across diverse legal tasks
- **Impact**: Established legal reasoning as distinct evaluation category, identified significant performance gaps in current LLMs
- **Relevance**: Provides methodological framework for domain-specific legal benchmarking

**LEXam: Benchmarking Legal Reasoning on 340 Law Exams** (Fan et al., 2025)
- **Problem**: Long-form legal reasoning remains challenging for LLMs despite advances in test-time scaling
- **Key Insight**: Law exam evaluation with explicit reasoning guidance reveals structured legal thinking requirements
- **Impact**: Demonstrates LLM struggles with multi-step legal reasoning, provides scalable evaluation framework
- **Relevance**: Shows importance of structured evaluation for legal AI systems

**Identifying Legal Holdings with LLMs** (Arvin et al., 2025)
- **Problem**: Assessing LLM performance on established legal benchmarks (CaseHOLD)
- **Key Insight**: Performance scales with model size, maintained under citation anonymization (not just memorization)
- **Impact**: Shows promise for legal analytics while highlighting current limitations
- **Relevance**: Validates scaling approaches and memorization concerns for legal AI

### Contract Analysis and Document Comprehension

**A Benchmark for Lease Contract Review** (Leivaditi et al., 2020) ⭐ *Most Relevant*
- **Problem**: Automating lease agreement review for entity extraction and red flag detection
- **Key Insight**: Lease agreements require specialized analysis distinct from general contracts
- **Impact**: First specialized dataset (179 documents) and ALeaseBERT model for lease analysis
- **Relevance**: Direct predecessor work in lease agreement analysis, demonstrates need for domain-specific approaches

**CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review** (Hendrycks et al., 2021)
- **Problem**: Need large-scale expert-annotated dataset for legal contract analysis
- **Key Insight**: Expert annotation essential for legal AI, transformer performance influenced by model design and data size
- **Impact**: 13,000+ annotations provide foundation for contract analysis research
- **Relevance**: Demonstrates expert annotation methodology and contract analysis task design

**The Hidden Structure - Improving Legal Document Understanding** (Braun et al., 2025)
- **Problem**: Impact of document structure on LLM processing of legal contracts
- **Key Insight**: Document structure significantly affects performance, prompt engineering crucial for optimal results
- **Impact**: Shows 20-point accuracy improvements with proper structuring and prompting
- **Relevance**: Critical for our document processing and evaluation methodology

### Plain Language and Accessibility

**Plain English Summarization of Contracts** (Manor & Li, 2019) ⭐ *Highly Relevant*
- **Problem**: Converting complex legal language to plain English for user comprehension
- **Key Insight**: Legal summarization requires simultaneous abstraction, compression, and style transfer
- **Impact**: Demonstrates that standard NLP methods inadequate for legal language simplification
- **Relevance**: Directly addresses our plain language summarization task and consumer accessibility goals

**TermSight: Making Service Contracts Approachable** (Huang et al., 2025)
- **Problem**: Terms of service are unreadable but legally binding
- **Key Insight**: AI-powered reading interfaces can significantly reduce difficulty and increase user engagement
- **Impact**: Shows measurable improvements in user comprehension and willingness to read legal documents
- **Relevance**: Validates user-centered approach to legal document accessibility

### LLM-as-Judge Evaluation

**LLMs-as-Judges: A Comprehensive Survey** (Li et al., 2024)
- **Problem**: Need scalable, automated evaluation of LLM outputs beyond traditional metrics
- **Key Insight**: LLMs can serve as reliable judges when properly prompted and calibrated
- **Impact**: Enables large-scale evaluation with strong correlation to human judgment (0.8+)
- **Relevance**: Central to our evaluation methodology using LLM judges for scalable assessment

**Quantitative LLM Judges** (Sahoo et al., 2025)
- **Problem**: Improving alignment between LLM judge scores and human ratings
- **Key Insight**: Regression models can improve judge accuracy using textual evaluation and scores
- **Impact**: More computationally efficient than fine-tuning, better statistical efficiency with limited human feedback
- **Relevance**: Provides techniques for calibrating our LLM judge evaluation system

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

The legal AI field shows three major research trends:

**1. Specialized Legal Benchmarking**: Recognition that general language benchmarks inadequately measure legal AI capabilities. Multiple papers (LegalBench, LEXam, CaseHOLD) establish domain-specific evaluation as essential.

**2. Document-to-Human Communication**: Growing focus on making legal documents accessible to non-experts through plain language conversion (Manor & Li, TermSight) rather than just expert-level analysis.

**3. LLM-as-Judge Evaluation**: Convergence on LLM judges as scalable evaluation method with strong human correlation when properly calibrated and prompted.

**Common Technical Assumptions Across Literature**:
- Expert annotation is necessary for legal AI datasets
- Domain-specific approaches outperform general methods
- Document structure significantly impacts LLM performance  
- Plain language conversion requires specialized techniques beyond standard summarization
- LLM scaling generally improves legal task performance

## Gaps Identified

**1. Consumer-Focused Legal AI**: Most work targets legal professionals rather than end consumers who need legal documents explained in accessible terms.

**2. Landlord-Tenant Specific Analysis**: Limited work specifically on landlord-tenant agreements despite widespread consumer need. Leivaditi et al. (2020) is closest but focuses on technical extraction rather than comprehension.

**3. End-to-End Comprehension Evaluation**: Existing benchmarks test technical tasks (entity extraction, classification) rather than holistic document understanding and explanation.

**4. Real-World Document Complexity**: Most datasets use clean, well-formatted documents rather than the complex, varied formatting found in actual rental agreements.

**5. LLM Judge Calibration for Legal Domain**: While general LLM judge frameworks exist, limited work on calibrating judges specifically for legal accuracy and plain language quality assessment.

## How Our Work Fits

Our landlord-tenant agreement benchmark addresses multiple identified gaps:

**Filling the Consumer Focus Gap**: Unlike existing legal AI work targeting professionals, our benchmark evaluates AI's ability to help consumers understand rental agreements through plain language summaries and scenario-based Q&A.

**Domain-Specific Innovation**: Builds on Leivaditi et al.'s lease analysis work but shifts from technical extraction to comprehension evaluation, addressing the specific needs of tenants facing complex lease language.

**Methodological Contributions**: 
- Combines plain language summarization with scenario-based evaluation
- Uses LLM-as-judge methodology calibrated for legal accuracy and plain language quality
- Addresses real-world document complexity with diverse formatting and clauses

**Literature-Level Bit Flip**: Challenges the assumption that legal AI should focus on professional-level legal reasoning. Instead, we argue that the highest impact comes from making legal documents comprehensible to consumers who must live with the consequences of these agreements.

**Building on Established Methods**: Leverages proven approaches (expert annotation from CUAD, LLM judge evaluation from survey literature, plain language focus from Manor & Li) while addressing identified gaps in consumer-focused legal AI.

This positions our work as both practically impactful (addressing real consumer needs) and methodologically novel (first comprehensive consumer-oriented legal document comprehension benchmark).

---
*Enhanced using CS197 research methodology*
