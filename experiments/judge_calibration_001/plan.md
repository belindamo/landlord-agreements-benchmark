# Experiment Plan: LLM Judge Calibration for Consumer-Focused Legal AI

## Experiment Idea
### Title
LLM Judge Calibration for Consumer-Focused Legal AI Evaluation

### Bit (Problem)
Current legal AI evaluation relies on expert human annotation, which is expensive and doesn't scale. For consumer-focused legal AI to be viable, we need automated evaluation methods that correlate strongly with human judgment on consumer comprehension tasks.

### Flip (Solution)
LLM judges can be calibrated specifically for consumer-focused legal AI evaluation using multi-aspect prompting strategies, achieving high correlation with human expert ratings while maintaining scalability.

### Hypothesis
Properly prompted LLM judges will achieve ≥0.8 correlation with human expert ratings on consumer-focused legal AI outputs, with multi-aspect evaluation outperforming holistic scoring.

## Evaluation Plan
### Metrics
- Primary metric: Pearson correlation between LLM judge scores and human expert ratings
- Secondary metrics:
  - Inter-judge reliability (Cronbach's alpha)
  - Calibration accuracy (confidence vs. actual accuracy)
  - Bias analysis across document complexity levels

### Baseline
- Random scoring baseline
- Simple keyword-based scoring
- Single-aspect holistic evaluation

### Data Collection
1. Generate 50 consumer-focused AI outputs using sample lease documents
2. Collect human expert ratings from 3 legal aid professionals
3. Evaluate with different LLM judges using varied prompting strategies
4. Calculate correlations and reliability metrics

### Analysis Method
- Correlation analysis (Pearson, Spearman)
- Inter-rater reliability analysis
- Bias detection across document complexity
- Qualitative analysis of judge reasoning

### Success Criteria
- Best judge configuration achieves ≥0.8 correlation with humans
- Inter-judge reliability ≥0.7 across conditions
- Identification of optimal prompting strategy for consumer-focused evaluation

## Implications
### If Successful
- Establishes scalable evaluation methodology for consumer-focused legal AI
- Enables larger-scale experiments and continuous evaluation
- Provides validated framework for other researchers

### If Failed
- Highlights limitations of automated evaluation for legal comprehension
- Indicates need for more sophisticated evaluation approaches
- May require hybrid human-AI evaluation systems

### Future Work
- Scale to larger document sets
- Apply to other legal domains beyond landlord-tenant
- Develop specialized judge training protocols

## Related Works
### Nearest Neighbor Paper
LLM-as-judge methods from PaperBench and similar evaluation frameworks

### Key Differences
- Focus on consumer comprehension rather than technical accuracy
- Multi-aspect evaluation specifically for legal clarity and completeness
- Calibration for legal aid rather than professional legal analysis

### Literature Gap
No existing work evaluates LLM judges specifically for consumer-focused legal AI comprehension tasks

## Vectors (Risk Dimensions)
### Technical Risk
- LLM judge inconsistency across different document types
- Prompt sensitivity affecting reliability
- Model availability and API limitations

### Methodological Risk
- Human expert rating reliability
- Sample size limitations
- Bias in document selection

### Resource Risk
- API costs for multiple LLM evaluations
- Time constraints for human expert collection
- Access to diverse legal documents

### Priority
**9/10** - Critical foundation for all subsequent evaluation work