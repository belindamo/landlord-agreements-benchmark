# Experiment Plan: Consumer vs Professional Focus

## Experiment Idea
### Title
Consumer-Focused vs Professional-Focused Legal AI Comparison

### Bit (Problem)
Current legal AI systems assume that technical, lawyer-focused outputs (clause extraction, legal reasoning) provide the most value to end users. This assumption prioritizes professional comprehension over consumer comprehension.

### Flip (Solution)
Consumer-focused AI (plain language summaries + scenario-based Q&A) provides greater real-world utility than professional-focused AI (technical extraction + legal reasoning) for actual tenants making lease decisions.

### Hypothesis
Plain language AI outputs will result in significantly higher comprehension accuracy (≥30% improvement), better decision-making quality (≥50% improvement), and reduced time-to-understanding (≥40% reduction) compared to technical legal analysis outputs.

## Evaluation Plan
### Metrics
- Primary metric: Comprehension accuracy (scored questionnaire on lease key points)
- Secondary metrics:
  - Decision-making quality (scenario-based responses)
  - Time to complete understanding tasks
  - Confidence ratings
  - User preference scores

### Baseline
Professional-focused AI outputs (technical clause extraction, legal terminology, lawyer-style analysis)

### Data Collection
1. Sample lease documents (3 complexity levels: simple/medium/complex)
2. AI-generated outputs for each document in both styles:
   - Consumer-focused: Plain language summaries, scenario-based Q&A
   - Professional-focused: Clause extraction, legal analysis, technical terms
3. Comprehension assessment questionnaires
4. Decision-making scenarios based on lease content

### Analysis Method
- Paired t-tests for comprehension accuracy between conditions
- ANOVA for effects across document complexity levels
- Effect size calculations (Cohen's d)
- Qualitative analysis of user feedback

### Success Criteria
- Consumer-focused approach shows statistically significant improvements (p < 0.05)
- Effect sizes of ≥0.5 (medium effect) for primary measures
- Consistent results across document complexity levels

## Implications
### If Successful
- Validates the core bit flip: consumer comprehension should be prioritized over professional analysis
- Provides foundation for developing consumer-focused legal AI systems
- Challenges current legal AI development paradigms

### If Failed
- Would indicate that technical accuracy is more valuable than comprehension
- Might suggest need for hybrid approaches
- Would inform refinement of consumer-focused methods

### Future Work
- Scale to larger participant pools
- Test across different legal domains (employment, consumer contracts)
- Develop production-ready consumer-focused legal AI system

## Related Works
### Nearest Neighbor Paper
LegalBench (Guha et al., 2023) - evaluates legal reasoning capabilities of language models

### Key Differences
- Focus on end-user comprehension rather than technical legal accuracy
- Consumer-centered evaluation metrics
- Real-world utility testing rather than benchmark performance

### Literature Gap
Most legal AI research focuses on professional use cases and technical accuracy, with limited attention to consumer comprehension and practical utility.

## Vectors (Risk Dimensions)
### Technical Risk
- Difficulty in creating balanced consumer vs professional AI outputs
- Potential bias in comprehension assessment design
- LLM quality differences affecting output comparison

### Methodological Risk
- Participant selection bias toward tech-savvy users
- Learning effects if participants see both conditions
- Experimenter bias in output generation

### Resource Risk
- Limited access to diverse lease documents
- Participant recruitment challenges
- Time constraints for comprehensive evaluation

### Priority
**Priority: 10/10** - This directly tests the core research hypothesis and provides foundation for all subsequent work.