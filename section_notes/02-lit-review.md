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

**PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements** (Filandrianos et al., 2025) ⭐ *Highly Relevant*
- **Problem**: Contract review is complex, time-intensive, and inaccessible to non-experts; confidential documents require open-source solutions
- **Key Insight**: Multi-agent collaborative frameworks with RAG components can democratize contract analysis while preserving privacy
- **Impact**: Outperforms general-purpose and pretrained models in accuracy, explainability, and completeness
- **Relevance**: Directly addresses consumer accessibility gap; demonstrates collaborative AI for legal comprehension

**What to Read in a Contract? Party-Specific Summarization** (Sancheti et al., 2022) ⭐ *Highly Relevant*
- **Problem**: Contract summarization needs vary by contracting party; generic summaries inadequate for different stakeholder perspectives
- **Key Insight**: Party-specific importance ranking (tenant vs. landlord) essential for effective legal summarization
- **Impact**: First party-specific legal summarization with ~293K expert-annotated sentence pairs from lease agreements
- **Relevance**: Validates our party-specific approach; demonstrates effectiveness of expert annotation for legal AI

**ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts** (Koreeda & Manning, 2021)
- **Problem**: Contract analysis requires document-level understanding rather than sentence-level tasks; existing approaches inadequate
- **Key Insight**: Document-level NLI with span-based evidence identification handles complex legal linguistic patterns
- **Impact**: 607 annotated contracts demonstrating unique challenges of legal document comprehension
- **Relevance**: Validates document-level understanding approach; shows importance of evidence-grounded legal reasoning

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

**LEXam: Benchmarking Legal Reasoning on 340 Law Exams** (Fan et al., 2025) ⭐ *Highly Relevant*
- **Problem**: Long-form legal reasoning remains challenging despite test-time scaling advances; existing benchmarks inadequate
- **Key Insight**: Law exams provide comprehensive framework testing issue spotting, rule recall, and rule application across legal domains
- **Impact**: 4,886 questions from 340 law exams; demonstrates LLM limitations in structured multi-step legal reasoning
- **Relevance**: Provides methodological framework for structured legal evaluation; validates LLM-as-judge with expert validation

**LegalEval-Q: Quality Evaluation of LLM-Generated Legal Text** (Li & Wu, 2025) ⭐ *Highly Relevant*
- **Problem**: Legal AI evaluation focuses on accuracy while neglecting linguistic quality (clarity, coherence, terminology)
- **Key Insight**: Legal text quality requires specialized evaluation; model scaling shows diminishing returns after 14B parameters
- **Impact**: Analysis of 49 LLMs reveals quality plateaus and importance of reasoning models over base architectures
- **Relevance**: Critical for our evaluation methodology; validates need for quality assessment beyond accuracy in legal contexts

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

The legal AI field shows four major research trends:

**1. Specialized Legal Benchmarking**: Recognition that general language benchmarks inadequately measure legal AI capabilities. Multiple papers (LegalBench, LEXam, CaseHOLD, LegalEval-Q) establish domain-specific evaluation as essential, with emphasis on both accuracy and linguistic quality.

**2. Consumer-Focused Legal Accessibility**: Emerging focus on making legal documents accessible to non-experts through intelligent interfaces (TermSight), party-specific summarization (Sancheti et al.), and multi-agent collaborative frameworks (PAKTON).

**3. Document-Level Understanding**: Shift from sentence-level tasks to comprehensive document analysis through document-level NLI (ContractNLI), multi-step reasoning (LEXam), and structured document processing approaches.

**4. LLM-as-Judge Evaluation**: Convergence on LLM judges as scalable evaluation method with strong human correlation when properly calibrated and prompted, validated across multiple legal reasoning benchmarks.

**Common Technical Assumptions Across Literature**:
- Expert annotation is necessary for legal AI datasets
- Domain-specific approaches outperform general methods
- Document structure significantly impacts LLM performance  
- Plain language conversion requires specialized techniques beyond standard summarization
- Party-specific information needs vary significantly in legal contexts
- Multi-agent and collaborative approaches improve complex legal reasoning
- Quality evaluation must consider clarity, coherence, and terminology alongside accuracy

## Gaps Identified

**1. Consumer-Focused Evaluation at Scale**: While recent work (TermSight, PAKTON) addresses accessibility, comprehensive benchmarks evaluating consumer comprehension across diverse legal documents remain limited.

**2. Landlord-Tenant Specific Analysis**: Limited work specifically on landlord-tenant agreements despite widespread consumer need. Leivaditi et al. (2020) provides technical extraction; Sancheti et al. (2022) shows party-specific summarization potential, but gap remains in comprehensive tenant-focused evaluation.

**3. Integrated Quality and Accessibility Assessment**: While LegalEval-Q addresses quality and TermSight addresses accessibility, no benchmark integrates linguistic quality assessment with consumer comprehension evaluation.

**4. Real-World Document Complexity**: Most datasets use clean, well-formatted documents rather than the complex, varied formatting found in actual rental agreements and consumer contracts.

**5. Multi-Agent Consumer Applications**: While PAKTON demonstrates multi-agent contract analysis, limited exploration of collaborative AI specifically designed for consumer legal comprehension and decision-making.

## How Our Work Fits

Our landlord-tenant agreement benchmark addresses multiple identified gaps:

**Filling the Consumer Focus Gap**: Unlike existing legal AI work targeting professionals, our benchmark evaluates AI's ability to help consumers understand rental agreements through plain language summaries and scenario-based Q&A.

**Domain-Specific Innovation**: Builds on Leivaditi et al.'s lease analysis work but shifts from technical extraction to comprehension evaluation, addressing the specific needs of tenants facing complex lease language.

**Methodological Contributions**: 
- Combines plain language summarization with scenario-based evaluation
- Uses LLM-as-judge methodology calibrated for legal accuracy and plain language quality
- Addresses real-world document complexity with diverse formatting and clauses

**Literature-Level Bit Flip**: Challenges the assumption that legal AI evaluation should prioritize technical accuracy for professional use. Instead, we argue that the highest impact comes from evaluating AI's ability to make legal documents comprehensible and actionable for consumers who must live with the consequences of these agreements, requiring integrated assessment of accuracy, quality, and accessibility.

**Building on Established Methods**: Leverages proven approaches including:
- Expert annotation methodology (CUAD, Sancheti et al.)
- LLM judge evaluation with quality assessment (LEXam, LegalEval-Q)
- Consumer accessibility design (TermSight)
- Party-specific analysis (Sancheti et al.)
- Document-level understanding (ContractNLI)
- Multi-agent collaborative frameworks (PAKTON)

While addressing identified gaps in comprehensive consumer-focused legal AI evaluation.

This positions our work as both practically impactful (addressing real consumer needs) and methodologically novel (first comprehensive consumer-oriented legal document comprehension benchmark).

---
*Enhanced using CS197 research methodology*


---
*This section is being enhanced by The Research Company AI Agent*
