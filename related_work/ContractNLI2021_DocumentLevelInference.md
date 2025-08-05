# ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts

## Citation
Koreeda, Y., & Manning, C. D. (2021). ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts. arXiv preprint arXiv:2110.01799.

## CS197 Analysis

### Problem
Reviewing contracts is a time-consuming procedure that incurs large expenses to companies and social inequality to those who cannot afford professional legal services. Existing NLP approaches focus on sentence-level tasks rather than document-level understanding required for comprehensive contract analysis.

### Prior Assumptions  
- Contract analysis can be reduced to sentence-level NLP tasks
- Standard NLI approaches work effectively for legal documents
- Evidence identification is primarily about finding start/end tokens
- Legal document characteristics don't significantly impact model performance

### Key Insight
Contract analysis requires **document-level natural language inference** that can handle the unique linguistic characteristics of legal documents, such as negations by exceptions. Evidence identification should be modeled as multi-label classification over spans rather than token-level prediction.

### Technical Approach
- **Document-level NLI task**: Given hypotheses and contract, classify as entailed/contradicting/neutral
- **Evidence identification**: Multi-label classification over spans instead of start/end token prediction
- **Sophisticated context segmentation** for handling long documents
- **607 annotated contracts** from EDGAR database
- **Novel evaluation framework** combining logical inference with evidence span identification

### Evaluation
- Demonstrates that existing models fail badly on contract NLI task
- Shows effectiveness of span-based evidence identification approach
- Reveals that linguistic characteristics of contracts (negations by exceptions) contribute significantly to task difficulty
- Provides strong baseline with substantial room for improvement

### Impact
- Establishes document-level NLI as important paradigm for legal document analysis
- Demonstrates unique challenges of legal document comprehension
- Provides dataset and framework for advancing legal document understanding
- Shows importance of handling legal document linguistic characteristics

### Relevance to Our Work
- Validates document-level understanding approach for legal contracts
- Demonstrates importance of evidence identification in legal document analysis
- Shows challenges specific to legal document linguistic characteristics
- Provides methodological framework for comprehensive contract evaluation
- Supports our focus on holistic document comprehension rather than just extraction

### Assumptions Challenged
- **Bit Flip**: Challenges assumption that contract analysis is primarily a sentence-level task by demonstrating the need for document-level inference that handles complex legal linguistic patterns and provides evidence-grounded reasoning for comprehensive contract understanding