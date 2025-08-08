# Literature Review

# Literature Review

## Key Papers

### Legal Benchmarking and Evaluation

**LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning** (Guha et al., 2023)
- **Problem**: Need systematic evaluation of LLM capabilities in legal contexts beyond general language benchmarks
- **Key Insight**: Legal reasoning requires specialized evaluation with expert collaboration across diverse legal tasks
- **Impact**: Established legal reasoning as distinct evaluation category, identified significant performance gaps in current LLMs
- **Relevance**: Provides methodological framework for domain-specific legal benchmarking

**LEXam: Benchmarking Legal Reasoning on 340 Law Exams** (Fan et al., 2025) ⭐ *Comprehensive*
- **Problem**: Long-form legal reasoning remains challenging for LLMs despite advances in test-time scaling
- **Assumption in prior work**: General reasoning benchmarks sufficient to measure legal reasoning capabilities
- **Key Insight**: Legal reasoning requires comprehensive assessment with explicit reasoning guidance (issue spotting, rule recall, rule application) that mirrors actual legal education
- **Impact**: Most comprehensive legal reasoning benchmark (4,886 questions), demonstrates LLM struggles with structured multi-step reasoning, provides validated LLM-as-Judge framework
- **Relevance**: Establishes gold standard for legal reasoning evaluation, validates our LLM-as-Judge methodology

**ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification** (Liu et al., 2025) ⭐ *Highly Relevant*
- **Problem**: Need systematic evaluation of whether open-source LLMs match proprietary LLMs for clause-level legal risk identification
- **Assumption in prior work**: General benchmarks sufficient; limited comparison between proprietary and open-source models
- **Key Insight**: Multi-dimensional evaluation reveals proprietary models outperform open-source in correctness, but most LLMs perform at junior legal assistant level
- **Impact**: First comprehensive proprietary vs open-source legal benchmark, practical guidance for deployment decisions, demonstrates need for targeted fine-tuning
- **Relevance**: Validates domain-specific benchmarking approach and multi-dimensional evaluation methodology

**Identifying Legal Holdings with LLMs** (Arvin et al., 2025)
- **Problem**: Assessing LLM performance on established legal benchmarks (CaseHOLD)
- **Key Insight**: Performance scales with model size, maintained under citation anonymization (not just memorization)
- **Impact**: Shows promise for legal analytics while highlighting current limitations
- **Relevance**: Validates scaling approaches and memorization concerns for legal AI

**LegalEval-Q: Quality Evaluation of LLM-Generated Legal Text** (Li et al., 2025)
- **Problem**: Current evaluation focuses on factual accuracy while neglecting linguistic quality (clarity, coherence, terminology)
- **Assumption in prior work**: Factual accuracy is primary measure of legal AI quality
- **Key Insight**: Legal text quality requires multi-dimensional evaluation; model performance plateaus at 14B parameters
- **Impact**: First standardized quality evaluation for legal LLMs, reveals fundamental training limitations, provides cost-performance guidance
- **Relevance**: Critical for our plain language evaluation methodology, validates focus on clarity and coherence

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

**PAKTON: Multi-Agent Framework for Legal Contract Q&A** (Filandrianos et al., 2025)
- **Problem**: Contract review is complex, time-intensive, requires expertise; contracts are confidential limiting proprietary model use
- **Assumption in prior work**: Single-model approaches or proprietary systems sufficient for contract analysis
- **Key Insight**: Multi-agent collaborative workflows with privacy-preserving RAG enable accessible, adaptable legal document review
- **Impact**: Outperforms single models in accuracy, retrieval, explainability, and completeness; fully open-source framework
- **Relevance**: Validates multi-agent approaches and privacy-preserving design for legal document analysis

**LogicLease: Rental Law Compliance Analysis in New York** (Sehgal & Liu, 2025) ⭐ *Domain-Specific*
- **Problem**: Landlord-tenant legal cases need automated analysis combining transparent reasoning with natural language accessibility
- **Assumption in prior work**: Either pure LLM or rule-based systems alone sufficient for legal analysis
- **Key Insight**: Neuro-symbolic approach (LLM + Prolog) separates information extraction from legal reasoning, achieving transparency while avoiding hallucinations
- **Impact**: 100% accuracy in 2.57 seconds per case, transparent step-by-step reasoning with legal citations
- **Relevance**: Directly addresses landlord-tenant domain but focuses on legal compliance rather than consumer comprehension - validates our bit flip

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

The legal AI field shows four major research trends with recent 2025 developments:

**1. Comprehensive Legal Benchmarking**: Evolution from simple legal QA to comprehensive evaluation frameworks. Recent work (LEXam, ContractEval, LegalEval-Q) establishes multi-dimensional evaluation as essential, measuring not just accuracy but clarity, coherence, reasoning quality, and practical applicability.

**2. Neuro-Symbolic and Multi-Agent Approaches**: Growing recognition that pure LLM approaches have limitations in legal contexts. Recent systems (LogicLease, PAKTON) combine symbolic reasoning with neural approaches or use collaborative agents for better accuracy, transparency, and explainability.

**3. Document-to-Human Communication**: Emerging focus on making legal documents accessible to non-experts through plain language conversion (Manor & Li, TermSight, Plain Language Summarization research) rather than just expert-level analysis.

**4. Domain-Specific Privacy-Preserving Systems**: Recognition of confidentiality requirements in legal domain driving development of open-source, privacy-preserving alternatives (PAKTON, ContractEval comparison of open vs proprietary models).

**Evolving Technical Assumptions Across Literature**:
- Expert annotation remains necessary but insufficient - need for consumer comprehension evaluation
- Domain-specific approaches essential but must balance technical accuracy with accessibility
- Multi-dimensional evaluation required (accuracy, clarity, coherence, explainability, privacy)
- Document structure critically impacts performance but consumer-facing applications need simplified presentation
- LLM scaling improves task performance but plateaus around 14B parameters for legal quality metrics
- **New assumption being challenged**: Legal AI should prioritize professional-level reasoning over consumer comprehension

## Gaps Identified

**1. Consumer-Focused Legal AI**: Despite advances in legal reasoning (LEXam, ContractEval) and domain-specific analysis (LogicLease), most work targets legal professionals rather than end consumers who need legal documents explained in accessible terms.

**2. Landlord-Tenant Consumer Comprehension**: While LogicLease (2025) achieves perfect legal compliance analysis for landlord-tenant cases, it focuses on expert-level legal reasoning rather than consumer comprehension. Gap persists between technical legal analysis and accessible consumer explanations.

**3. End-to-End Consumer Comprehension Evaluation**: Existing comprehensive benchmarks (LEXam, ContractEval, LegalEval-Q) test professional-level reasoning or linguistic quality but not holistic consumer understanding and practical applicability.

**4. Real-World Document Complexity for Consumers**: Most datasets use clean, well-formatted legal documents rather than the complex, varied formatting found in actual rental agreements that consumers encounter.

**5. Consumer-Calibrated LLM Judges**: While LLM judge frameworks are well-established for legal accuracy, limited work exists on calibrating judges specifically for consumer comprehension, plain language quality, and practical utility assessment.

**6. Privacy-Preserving Consumer Legal AI**: Despite advances in privacy-preserving legal systems (PAKTON), limited work on consumer-accessible interfaces that maintain confidentiality while providing understandable explanations.

## How Our Work Fits

Our landlord-tenant agreement benchmark addresses multiple identified gaps:

**Filling the Consumer Focus Gap**: Unlike existing legal AI work targeting professionals, our benchmark evaluates AI's ability to help consumers understand rental agreements through plain language summaries and scenario-based Q&A.

**Domain-Specific Innovation**: Builds on Leivaditi et al.'s lease analysis work but shifts from technical extraction to comprehension evaluation, addressing the specific needs of tenants facing complex lease language.

**Methodological Contributions**: 
- Combines plain language summarization with scenario-based evaluation
- Uses LLM-as-judge methodology calibrated for legal accuracy and plain language quality
- Addresses real-world document complexity with diverse formatting and clauses

**Literature-Level Bit Flip**: Challenges the dominant assumption across recent legal AI research (LEXam, ContractEval, LogicLease) that legal AI should prioritize professional-level legal reasoning and technical accuracy. Instead, we argue that the highest impact comes from making legal documents comprehensible to consumers who must live with the consequences of these agreements, particularly in high-stakes domains like housing.

**Building on State-of-the-Art Methods**: Leverages proven approaches from recent advances:
- Multi-dimensional evaluation framework from LegalEval-Q (clarity, coherence, terminology)
- LLM-as-Judge methodology validated by LEXam and comprehensive survey literature  
- Domain-specific benchmarking approach established by ContractEval and LogicLease
- Privacy-preserving design principles from PAKTON
- Plain language focus from Manor & Li and accessibility research
- Expert annotation methodology from CUAD and recent benchmarking work

**Methodological Innovation**: Combines technical rigor from recent legal AI advances with consumer accessibility focus, creating first benchmark that evaluates AI's ability to make complex legal documents understandable to non-experts rather than just technically accurate for professionals.

This positions our work as both practically impactful (addressing real consumer needs) and methodologically novel (first comprehensive consumer-oriented legal document comprehension benchmark).

---
*Enhanced using CS197 research methodology*


---
*This section is being enhanced by The Research Company AI Agent*
