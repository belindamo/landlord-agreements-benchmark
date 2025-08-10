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

**ContractNLI: Document-level NLI for Contracts** (Koreeda & Manning, 2021)
- **Problem**: Contract review is time-consuming and expensive, creating barriers for smaller entities
- **Prior Assumptions**: Legal AI focused on extraction tasks rather than understanding and inference
- **Insight**: Document-level natural language inference can automate contract review by classifying hypotheses as entailed, contradicted, or not mentioned
- **Technical Approach**: Multi-task learning with evidence identification as multi-label classification over spans
- **Evaluation**: 607 annotated contracts with 17 hypotheses, evidence spans marked by experts
- **Impact**: First dataset for document-level legal NLI, enables automated contract review and risk assessment
- **Relevance**: Provides framework for comprehension-based evaluation rather than just extraction tasks

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

**ACORD: Expert-Annotated Dataset for Legal Contract Clause Retrieval** (Wang et al., 2025)
- **Problem**: Contract drafting relies on finding relevant precedent clauses, but no benchmarks exist for this critical task
- **Prior Assumptions**: LLMs can generate contracts from scratch effectively
- **Insight**: Lawyers rarely draft from scratch - clause retrieval from precedents is foundational to contract drafting
- **Technical Approach**: Expert-annotated dataset with 114 queries and 126K+ query-clause pairs ranked 1-5 stars
- **Evaluation**: Bi-encoder retrieval with LLM re-ranking, tested on complex clauses (indemnification, liability, etc.)
- **Impact**: First expert-annotated benchmark for contract clause retrieval, reveals gaps in current LLM capabilities
- **Relevance**: Demonstrates importance of precedent-based evaluation and expert annotation for legal AI

**Contract Summarization for Party-Specific Obligations** (Sancheti et al., 2023)
- **Problem**: Contracts are long and complex, making it difficult for parties to understand their specific obligations
- **Prior Assumptions**: Generic summarization approaches work for legal contracts
- **Insight**: Contract summarization should be party-specific, focusing on obligations, entitlements, and prohibitions for each party
- **Technical Approach**: Two-module system with content categorizer and importance ranker, using expert pairwise comparisons
- **Evaluation**: 293K sentence pairs from lease agreements annotated by legal experts for importance
- **Impact**: First party-specific legal summarization dataset, shows domain expertise crucial for legal summarization
- **Relevance**: Validates party-specific approach to legal document comprehension and expert annotation methodology

### Plain Language and Accessibility

**Plain English Summarization of Contracts** (Manor & Li, 2019) ⭐ *Highly Relevant*
- **Problem**: Converting complex legal language to plain English for user comprehension
- **Key Insight**: Legal summarization requires simultaneous abstraction, compression, and style transfer
- **Impact**: Demonstrates that standard NLP methods inadequate for legal language simplification
- **Relevance**: Directly addresses our plain language summarization task and consumer accessibility goals

**TermSight: Making Service Contracts Approachable** (Huang et al., 2025)
- **Problem**: Terms of service are unreadable but legally binding
- **Prior Assumptions**: Making legal documents accessible requires only simplification
- **Key Insight**: AI-powered reading interfaces with visual summaries, categorization, and contextualized definitions significantly improve accessibility
- **Technical Approach**: Multi-feature interface with relevance highlighting, power balance visualization, plain-language categorization, and contextual definitions
- **Evaluation**: Within-subjects study (N=20) measuring reading difficulty and willingness to read ToS
- **Impact**: Shows measurable improvements in user comprehension and willingness to read legal documents
- **Relevance**: Validates user-centered approach to legal document accessibility and multi-modal interface design

**Terminators: Terms of Service Parsing and Auditing Agents** (Mridul et al., 2025)  
- **Problem**: ToS documents are lengthy and written in complex legal language, difficult for users to understand
- **Prior Assumptions**: ToS understanding is a black-box summarization problem
- **Insight**: Breaking ToS analysis into interpretable steps (term extraction, verification, accountability planning) enhances auditability
- **Technical Approach**: Modular agentic framework using LLMs with structured workflow to minimize hallucinations
- **Evaluation**: Demonstrated on OpenAI ToS using GPT-4o, focus on auditability and transparency
- **Impact**: Promotes ethical use through greater transparency and enables automated policy audits
- **Relevance**: Shows promise of agentic approaches for legal document analysis and transparency

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

The legal AI field shows four major research trends with emerging sophistication:

**1. Specialized Legal Benchmarking**: Recognition that general language benchmarks inadequately measure legal AI capabilities. Multiple papers (LegalBench, LEXam, CaseHOLD, ContractNLI, ACORD) establish domain-specific evaluation as essential, with growing focus on expert annotation and real-world legal tasks.

**2. Document-to-Human Communication**: Growing focus on making legal documents accessible to non-experts through plain language conversion (Manor & Li, TermSight, Terminators) rather than just expert-level analysis. Evolution from simple summarization to multi-modal interfaces and structured analysis.

**3. LLM-as-Judge Evaluation**: Convergence on LLM judges as scalable evaluation method with strong human correlation when properly calibrated and prompted.

**4. Task-Specific Legal AI**: Shift from generic NLP to specialized legal tasks like clause retrieval (ACORD), party-specific summarization (Sancheti et al.), and document-level inference (ContractNLI), recognizing unique requirements of legal work.

**Common Technical Assumptions Across Literature**:
- Expert annotation is necessary for legal AI datasets (validated by ACORD, CUAD, ContractNLI)
- Domain-specific approaches outperform general methods (demonstrated across all benchmarks)
- Document structure significantly impacts LLM performance (Braun et al., ContractNLI)
- Plain language conversion requires specialized techniques beyond standard summarization (Manor & Li, TermSight)
- LLM scaling generally improves legal task performance
- Precedent-based work patterns are fundamental to legal practice (ACORD insights)
- Party-specific analysis is crucial for contract understanding (Sancheti et al.)

## Gaps Identified

**1. Consumer-Focused Legal AI**: Despite advances in accessibility (TermSight, Terminators), most work still targets legal professionals rather than end consumers who must live with contract consequences.

**2. Landlord-Tenant Specific Analysis**: Limited work specifically on landlord-tenant agreements despite widespread consumer need. Leivaditi et al. (2020) remains closest but focuses on technical extraction rather than comprehension. Other contract work (ACORD, CUAD) focuses on commercial contracts.

**3. End-to-End Comprehension Evaluation**: While ContractNLI advances document-level understanding, most benchmarks still test technical tasks (entity extraction, clause retrieval) rather than holistic consumer comprehension and actionable explanation.

**4. Real-World Document Complexity**: Most datasets use clean, well-formatted documents rather than the complex, varied formatting found in actual rental agreements. ACORD uses professional contract templates rather than consumer-facing documents.

**5. LLM Judge Calibration for Legal Domain**: While general LLM judge frameworks exist, limited work on calibrating judges specifically for legal accuracy and plain language quality assessment in consumer contexts.

**6. Integration of Multi-Modal Approaches**: TermSight shows promise for visual interfaces, but most legal AI remains text-only despite documents often containing complex formatting, tables, and visual elements crucial for understanding.

**7. Validation of Consumer Understanding**: Limited empirical validation that AI-generated explanations actually improve consumer comprehension and decision-making, as opposed to professional efficiency.

## How Our Work Fits

Our landlord-tenant agreement benchmark addresses multiple identified gaps:

**Filling the Consumer Focus Gap**: Unlike existing legal AI work targeting professionals, our benchmark evaluates AI's ability to help consumers understand rental agreements through plain language summaries and scenario-based Q&A.

**Domain-Specific Innovation**: Builds on Leivaditi et al.'s lease analysis work but shifts from technical extraction to comprehension evaluation, addressing the specific needs of tenants facing complex lease language.

**Methodological Contributions**: 
- Combines plain language summarization with scenario-based evaluation
- Uses LLM-as-judge methodology calibrated for legal accuracy and plain language quality
- Addresses real-world document complexity with diverse formatting and clauses

**Literature-Level Bit Flip**: Challenges the assumption that legal AI should focus on professional-level legal reasoning (as in ACORD, ContractNLI) or technical extraction (as in CUAD). Instead, we argue that the highest impact comes from making legal documents comprehensible to consumers who must live with the consequences of these agreements.

**Building on Established Methods**: Leverages proven approaches from multiple sources:
- Expert annotation methodology (CUAD, ACORD, ContractNLI)
- LLM judge evaluation frameworks (Li et al., Sahoo et al.)
- Plain language accessibility focus (Manor & Li, TermSight) 
- Party-specific analysis (Sancheti et al.)
- Document-level comprehension tasks (ContractNLI)
While uniquely addressing identified gaps in consumer-focused legal AI.

**Novel Methodological Contributions**:
- First benchmark specifically for consumer comprehension of rental agreements
- Integration of accessibility principles with rigorous evaluation methodology  
- Real-world document complexity rather than clean professional templates
- Validation framework for consumer understanding rather than professional efficiency

This positions our work as both practically impactful (addressing real consumer needs) and methodologically novel (first comprehensive consumer-oriented legal document comprehension benchmark).

---
*Enhanced using CS197 research methodology*


---
*This section is being enhanced by The Research Company AI Agent*
