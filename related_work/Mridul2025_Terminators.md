# Terminators: Terms of Service Parsing and Auditing Agents

**Authors**: Maruf Ahmed Mridul, Inwon Kang, Oshani Seneviratne  
**Year**: 2025  
**Venue**: ArXiv Preprint  
**Paper URL**: https://arxiv.org/abs/2505.11672  

## Summary

Terminators introduces a modular agentic framework using LLMs to parse and audit Terms of Service documents through structured, interpretable workflows.

## CS197 Analysis

### Problem
Terms of Service documents are lengthy and written in complex legal language, making them difficult for users to understand. Traditional approaches treat ToS understanding as a black-box summarization problem.

### Prior Assumptions
- ToS understanding is primarily a summarization task
- Single-step processing is sufficient for legal document analysis
- Black-box approaches provide adequate transparency for legal AI

### Insight
Breaking ToS analysis into interpretable steps (term extraction, verification, accountability planning) enhances both usability and auditability while minimizing hallucinations.

### Technical Approach
- **Modular Architecture**: Three-step process of term extraction, verification, and accountability planning
- **Agentic Framework**: Uses multiple specialized agents for different analysis tasks
- **Structured Workflow**: Interpretable pipeline rather than end-to-end black box
- **Hallucination Control**: Strategies to minimize false information in legal analysis
- **Auditability Focus**: Designed for transparency and regulatory oversight

### Evaluation
- Demonstrated on OpenAI ToS using GPT-4o
- Focus on auditability and transparency rather than traditional metrics
- Emphasis on verifiable, actionable components
- Validation of reduced hallucination through structured approach

### Impact
- Promotes ethical use of web content through greater transparency
- Enables automated policy audits for regulatory oversight
- Empowers users to understand digital rights and obligations
- Shows promise of agentic approaches for legal document analysis

## Relevance to Our Work

Terminators provides methodological insights for structured legal document analysis:

1. **Modular Design**: Shows benefits of breaking complex legal tasks into interpretable steps
2. **Auditability**: Demonstrates importance of transparency in legal AI systems
3. **Agent Architecture**: Provides framework for sophisticated legal document processing
4. **Consumer Empowerment**: Validates focus on helping users understand their rights

## Key Insights for Literature Review

- **Structured Processing**: Multi-step approaches superior to black-box summarization
- **Transparency**: Legal AI requires interpretable, auditable workflows
- **Agentic Design**: Specialized agents can handle complex legal reasoning tasks
- **Ethical Focus**: Legal AI should promote user empowerment and transparency

## Methodological Contributions

- **Interpretable Workflow**: Breaks legal analysis into verifiable components
- **Hallucination Control**: Structured approach reduces false information
- **Audit Framework**: Enables regulatory and civic oversight of AI systems
- **User Empowerment**: Translates opaque terms into actionable information

## Application to Our Benchmark

Our work can incorporate insights from Terminators by:
- Considering structured workflows for legal document analysis
- Emphasizing transparency and auditability in evaluation design
- Focusing on consumer empowerment through understanding
- Validating interpretability alongside accuracy

## Citation
```bibtex
@article{mridul2025terminators,
  title={Terminators: Terms of Service Parsing and Auditing Agents},
  author={Mridul, Maruf Ahmed and Kang, Inwon and Seneviratne, Oshani},
  journal={arXiv preprint arXiv:2505.11672},
  year={2025}
}
```