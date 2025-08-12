# ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts

**Authors**: Yuta Koreeda, Christopher D. Manning  
**Year**: 2021  
**Venue**: Findings of EMNLP 2021  
**Paper URL**: https://arxiv.org/abs/2110.01799  

## Summary

ContractNLI introduces document-level natural language inference for contracts, where systems classify hypotheses as entailed, contradicted, or not mentioned by contracts while identifying supporting evidence.

## CS197 Analysis

### Problem
Contract review is a time-consuming and expensive process, creating barriers for smaller companies and individuals who cannot afford professional legal services. Manual contract analysis is prone to errors and scales poorly.

### Prior Assumptions
- Legal AI focused primarily on extraction tasks (entities, clauses) rather than understanding and inference
- Contract analysis could be handled by general NLP methods
- Document-level reasoning in legal contexts was not systematically evaluated

### Insight
Document-level natural language inference can automate key aspects of contract review by systematically classifying whether hypotheses about contract terms are supported by the document text, enabling automated risk assessment.

### Technical Approach
- **Dataset**: 607 annotated non-disclosure agreements (NDAs) 
- **Task Design**: Multi-task learning combining NLI classification and evidence identification
- **Evidence Handling**: Multi-label binary classification over spans rather than start/end token prediction
- **Document Processing**: Sophisticated context segmentation for handling long documents
- **Labels**: 17 fixed hypotheses tested across all contracts

### Evaluation
- First dataset for document-level legal NLI
- Evidence spans comprehensively marked by experts
- Shows existing models fail badly on the task
- Introduces strong baseline with improved context handling

### Impact
- Enables automated contract review and risk assessment
- Provides framework for comprehension-based evaluation rather than just extraction
- Demonstrates importance of document-level understanding in legal AI
- Shows linguistic characteristics of contracts (negations by exceptions) create unique challenges

## Relevance to Our Work

ContractNLI provides a crucial methodological foundation for our benchmark:

1. **Document-level comprehension**: Validates focusing on understanding rather than just extraction
2. **Evidence-based evaluation**: Shows importance of requiring systems to identify supporting evidence
3. **Expert annotation**: Demonstrates need for legal expert involvement in dataset creation
4. **Hypothesis-driven approach**: Provides template for scenario-based evaluation

## Key Insights for Literature Review

- **Methodological Innovation**: First to apply document-level NLI to legal contracts
- **Task Design**: Multi-task learning with evidence identification improves performance
- **Domain Challenges**: Legal language characteristics require specialized approaches
- **Evaluation Framework**: Establishes pattern for comprehension-based legal AI evaluation

## Citation
```bibtex
@article{koreeda2021contractnli,
  title={ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts},
  author={Koreeda, Yuta and Manning, Christopher D},
  journal={Findings of EMNLP},
  year={2021}
}
```