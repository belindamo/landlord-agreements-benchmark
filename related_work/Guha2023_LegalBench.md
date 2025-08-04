# LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models

**Authors**: Neel Guha, Julian Nyarko, Daniel E. Ho, Christopher Ré, et al.  
**Year**: 2023  
**Venue**: NeurIPS  
**URL**: https://digitalcommons.osgoode.yorku.ca/all_papers/380/

## CS197 Analysis Framework

### Problem
- **What problem is being solved**: Measuring legal reasoning capabilities of Large Language Models across diverse legal tasks
- **Why it matters**: Legal domain has unique reasoning requirements that general benchmarks don't capture. Need systematic evaluation of LLM capabilities in legal contexts

### Assumption in Prior Work
- **Key assumption**: General language understanding benchmarks (GLUE, SuperGLUE) are sufficient to evaluate model capabilities in specialized domains
- **Inadequacy**: Legal reasoning involves specialized knowledge, complex logical structures, and domain-specific language that differs significantly from general language tasks
- **Gap**: Lack of comprehensive, expert-designed legal reasoning benchmarks

### Insight
- **Novel contribution**: Collaboratively built benchmark with legal experts covering diverse legal reasoning tasks
- **Key insight**: Legal reasoning is multi-faceted requiring different types of analysis (rule application, case analysis, statutory interpretation, etc.)
- **Innovation**: Expert-in-the-loop benchmark design ensuring legal validity and practical relevance

### Technical Overview
- **Approach**: Multi-task benchmark with expert-designed tasks across legal sub-domains
- **Coverage**: Multiple areas of law (contracts, torts, constitutional law, etc.)
- **Task types**: Rule application, case reasoning, statutory interpretation, legal classification
- **Evaluation**: Standardized metrics adapted for legal reasoning tasks
- **Collaboration**: Built with practicing lawyers and legal scholars

### Proof/Evaluation
- **Method**: Systematic evaluation of major LLMs across all benchmark tasks
- **Models tested**: GPT-3/4, PaLM, various legal-specific fine-tuned models
- **Results**: Significant performance gaps between models, highlighting challenges in legal reasoning
- **Validation**: Expert review of benchmark tasks and model outputs

### Impact
- **Field implications**: Establishes legal reasoning as distinct evaluation category for NLP
- **Research impact**: Provides standardized benchmark for legal NLP research
- **Practical impact**: Identifies specific areas where current LLMs struggle in legal contexts
- **Future work**: Creates foundation for systematic legal AI development

## Key Assumptions Identified
1. **Legal reasoning requires specialized evaluation** (vs. general language benchmarks)
2. **Expert collaboration is essential** for valid legal AI evaluation
3. **Multi-task approach captures legal reasoning complexity** better than single tasks
4. **Current LLMs have significant gaps** in legal reasoning capabilities

## Relevance to Our Work
**High relevance**: Provides methodological framework for legal AI benchmarking
- Demonstrates importance of expert-designed legal benchmarks
- Shows multi-task evaluation approach
- Validates need for domain-specific legal AI evaluation

**Methodological lessons**:
- Expert collaboration crucial for benchmark validity
- Need diverse task types to capture domain complexity
- Standardized evaluation metrics important for comparability
- Gap analysis helps identify improvement areas

**Differences from our approach**:
- Broader legal domain vs. specific landlord-tenant focus
- Rule-based reasoning vs. document comprehension focus
- Professional legal reasoning vs. consumer-oriented explanation

## Potential Bit Flips
1. **Current assumption**: Legal AI should emulate lawyer-level reasoning
   **Potential flip**: Legal AI should focus on making law accessible to non-experts
2. **Current assumption**: Comprehensive legal knowledge is the goal
   **Potential flip**: Specialized, deep domain expertise is more valuable than breadth