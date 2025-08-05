# Literature Review

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

**ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting** (Wang et al., 2025) ⭐ *Highly Relevant*
- **Problem**: Contract clause retrieval for legal drafting requires understanding precedent quality beyond text similarity
- **Key Insight**: Legal IR requires expert annotation with nuanced 5-star relevance ratings for precedent quality
- **Impact**: First expert-annotated contract retrieval benchmark (114 queries, 126K+ query-clause pairs)
- **Relevance**: Validates expert annotation approach for legal AI benchmarks, establishes legal IR as distinct research area

**What to Read in a Contract? Party-Specific Summarization** (Sancheti et al., 2023) ⭐ *Highly Relevant*
- **Problem**: Contract comprehension varies by party; generic summarization inadequate for party-specific needs
- **Key Insight**: Expert pairwise importance comparisons enable party-specific extractive summarization of legal obligations
- **Impact**: 293K expert annotations for lease agreements, demonstrates domain-specific importance ranking
- **Relevance**: Closest prior work to consumer-focused approach, validates expert annotation methodology for legal comprehension

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

**Material Contracts Corpus** (2025)
- **Problem**: Need large-scale contract dataset for empirical legal research and AI tool development
- **Key Insight**: SEC filings provide rich source of diverse, real-world contracts with metadata
- **Impact**: 1M+ contracts (2000-2023) with ML-based categorization and party linking
- **Relevance**: Demonstrates scale achievable for legal document datasets, provides context for contract complexity trends

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

**Automatic Legal Writing Evaluation of LLMs** (Pires, 2025) ⭐ *Highly Relevant*
- **Problem**: Legal writing evaluation requires domain-specific benchmarks with comprehensive guidelines
- **Key Insight**: LLM judges (OpenAI o1) achieve strong correlation with human legal experts when properly calibrated
- **Impact**: oab-bench with 105 legal questions shows Claude-3.5 Sonnet achieving 7.93/10, passing all 21 exams
- **Relevance**: Validates LLM-as-judge approach for legal domain evaluation, provides methodology for calibrating legal judges

**LEXam: Benchmarking Legal Reasoning on 340 Law Exams** (Fan et al., 2025)
- **Problem**: Long-form legal reasoning evaluation with structured multi-step reasoning requirements
- **Key Insight**: LLM-as-judge paradigm with rigorous human validation enables consistent evaluation of legal reasoning steps
- **Impact**: 4,886 law exam questions with explicit reasoning guidance; scalable evaluation beyond accuracy metrics
- **Relevance**: Demonstrates LLM judge methodology for legal reasoning evaluation, shows structured evaluation approach

**Quantitative LLM Judges** (Sahoo et al., 2025)
- **Problem**: Improving alignment between LLM judge scores and human ratings
- **Key Insight**: Regression models can improve judge accuracy using textual evaluation and scores
- **Impact**: More computationally efficient than fine-tuning, better statistical efficiency with limited human feedback
- **Relevance**: Provides techniques for calibrating our LLM judge evaluation system

**LegalEval-Q: Quality Evaluation of LLM-Generated Legal Text** (2025)
- **Problem**: Legal text evaluation focuses on factual accuracy while neglecting linguistic quality (clarity, coherence, terminology)
- **Key Insight**: Regression models can evaluate legal text quality across multiple dimensions beyond factual correctness
- **Impact**: Analysis of 49 LLMs showing quality plateaus at 14B parameters, reasoning models outperform base architectures
- **Relevance**: Provides framework for multi-dimensional legal text quality evaluation relevant to our plain language assessment

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

**Prolog and LLMs for Rental Law Compliance in New York** (2025) ⭐ *Relevant*
- **Problem**: Automating landlord-tenant legal case analysis requires transparent logical reasoning combined with natural language processing
- **Key Insight**: Hybrid approach separating information extraction (LLMs) from legal reasoning (Prolog) achieves 100% accuracy with transparency
- **Impact**: LogicLease system processes cases in 2.57 seconds with step-by-step reasoning and law citations
- **Relevance**: Direct landlord-tenant domain application showing importance of transparent, accurate legal AI systems

## Summary of Field

The legal AI field shows four major research trends:

**1. Expert-Annotated Legal Benchmarking**: Recognition that general language benchmarks inadequately measure legal AI capabilities. Multiple papers (LegalBench, LEXam, CaseHOLD, ACORD) establish expert annotation and domain-specific evaluation as essential. The field has converged on the necessity of legal expert involvement in dataset creation.

**2. Document-to-Human Communication**: Growing focus on making legal documents accessible to non-experts through plain language conversion (Manor & Li, TermSight) and party-specific summarization (Sancheti et al.) rather than just expert-level analysis. This represents a shift from lawyer-facing to user-facing applications.

**3. LLM-as-Judge Evaluation**: Convergence on LLM judges as scalable evaluation method with strong human correlation when properly calibrated and prompted. Recent work (Pires, LEXam, LegalEval-Q) demonstrates reliable legal domain evaluation using LLM judges with domain-specific guidelines.

**4. Hybrid Legal AI Systems**: Emerging trend toward systems that combine multiple AI approaches for transparency and accuracy (LogicLease using Prolog+LLMs, structured evaluation frameworks). Recognition that pure LLM approaches may be insufficient for high-stakes legal applications.

**Common Technical Assumptions Across Literature**:
- Expert annotation is necessary for legal AI datasets
- Domain-specific approaches outperform general methods
- Document structure significantly impacts LLM performance  
- Plain language conversion requires specialized techniques beyond standard summarization
- LLM scaling generally improves legal task performance
- Party-specific or user-specific perspectives are crucial for legal document analysis
- Transparency and explainability are essential for legal AI systems

## Gaps Identified

**1. Consumer-Focused Legal AI**: Despite recent progress in party-specific summarization (Sancheti et al.), most work still targets legal professionals or contracting parties rather than general consumers who need legal documents explained in truly accessible terms. The gap between "party-specific" and "consumer-accessible" remains significant.

**2. Plain Language Legal Evaluation**: While LLM judge frameworks exist for legal reasoning (Pires, LEXam), limited work exists on calibrating judges specifically for plain language quality assessment. Most evaluation focuses on legal accuracy rather than comprehensibility for non-experts.

**3. End-to-End Document Comprehension**: Existing benchmarks test specific technical tasks (entity extraction in Leivaditi et al., clause retrieval in ACORD) rather than holistic document understanding and explanation capabilities needed by consumers.

**4. Landlord-Tenant Comprehension Gap**: While LogicLease addresses legal compliance analysis and Leivaditi et al. covers entity extraction, no work specifically addresses consumer comprehension of landlord-tenant agreements. The domain has legal AI applications but lacks consumer-facing comprehension evaluation.

**5. Real-World Document Complexity**: Most datasets use clean, well-formatted documents rather than the complex, varied formatting found in actual rental agreements that consumers encounter.

**6. Scalable Consumer Evaluation**: No established methodology for evaluating legal AI systems from a consumer comprehension perspective using scalable methods like LLM judges calibrated for accessibility rather than legal accuracy.

## How Our Work Fits

Our landlord-tenant agreement benchmark addresses multiple identified gaps:

**Filling the Consumer Focus Gap**: Unlike existing legal AI work targeting professionals, our benchmark evaluates AI's ability to help consumers understand rental agreements through plain language summaries and scenario-based Q&A.

**Domain-Specific Innovation**: Builds on Leivaditi et al.'s lease analysis work but shifts from technical extraction to comprehension evaluation, addressing the specific needs of tenants facing complex lease language.

**Methodological Contributions**: 
- Combines plain language summarization with scenario-based evaluation
- Uses LLM-as-judge methodology calibrated for legal accuracy and plain language quality
- Addresses real-world document complexity with diverse formatting and clauses

**Literature-Level Bit Flip**: Challenges the assumption that legal AI should focus on professional-level legal reasoning or even party-specific summarization for contracting parties. Instead, we argue that the highest impact comes from making legal documents comprehensible to everyday consumers who must live with the consequences of these agreements but lack legal training.

**Building on Established Methods**: Leverages proven approaches from recent advances:
- Expert annotation methodology validated by ACORD, CUAD, and Sancheti et al.
- LLM-as-judge evaluation frameworks demonstrated effective by Pires, LEXam, and LegalEval-Q
- Plain language accessibility focus from Manor & Li and TermSight
- Party-specific analysis insights from Sancheti et al., adapted for consumer perspective
- Domain-specific benchmarking principles established across legal AI literature

**Novel Methodological Contributions**:
- First consumer-focused legal document comprehension benchmark
- LLM judge calibration specifically for plain language accessibility rather than legal accuracy
- Integration of document comprehension with scenario-based evaluation
- Bridging the gap between party-specific legal analysis and consumer accessibility needs

This positions our work as both practically impactful (addressing real consumer needs) and methodologically novel (first comprehensive consumer-oriented legal document comprehension benchmark).

---
*Enhanced using CS197 research methodology*


---
*This section is being enhanced by The Research Company AI Agent*
