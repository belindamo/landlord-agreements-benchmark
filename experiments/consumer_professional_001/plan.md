# Experiment Plan: Consumer Comprehension vs. Professional Analysis

## Experiment Idea
### Title
Consumer Comprehension vs. Professional Analysis for Landlord-Tenant Legal AI

### Bit (Problem)
Legal AI systems are optimized for professional legal analysis (technical extraction, clause identification, legal reasoning) rather than consumer comprehension. This creates a fundamental mismatch between what consumers need (plain language understanding, scenario-based guidance, actionable insights) and what current systems provide (technical accuracy, legal completeness, professional terminology).

### Flip (Solution)
AI systems optimized for consumer comprehension (plain language summaries, scenario-based Q&A, real-world implications) will demonstrate superior real-world utility compared to systems optimized for professional legal analysis when evaluated on actual tenant decision-making tasks.

### Hypothesis
Consumer-focused legal AI will outperform professional-focused legal AI across key comprehension and decision-making metrics:
- H1: Plain language summaries increase tenant comprehension scores by ≥30% vs technical analysis
- H2: Scenario-based Q&A results in ≥50% more accurate decision-making vs clause extraction
- H3: Consumer-focused outputs reduce time-to-understanding by ≥40%

## Evaluation Plan
### Metrics
- Primary metric: Tenant comprehension accuracy (scored questionnaire)
- Secondary metrics:
  - Decision-making quality (scenario responses)
  - Time to complete understanding tasks
  - Confidence ratings
  - Preference scores

### Baseline
Professional-focused AI approach using:
- Technical clause extraction
- Legal terminology preservation
- Comprehensive legal analysis format

### Data Collection
1. Use existing lease documents from data/ folder
2. Generate both consumer-focused and professional-focused AI outputs
3. Create comprehension questionnaires and decision scenarios
4. Test framework using smaller pilot study (10 documents)

### Analysis Method
- Paired t-tests for within-subjects comparisons
- Effect size calculation (Cohen's d)
- Qualitative analysis of participant feedback
- Time-series analysis of comprehension tasks

### Success Criteria
- Consumer-focused approach shows statistically significant improvements (p < 0.05)
- Effect sizes of ≥0.5 (medium effect) for primary measures
- Consistent superiority across document complexity levels

## Implications
### If Successful
- Validates core bit flip assumption about consumer-focused legal AI
- Establishes new evaluation paradigm for legal AI research
- Provides foundation for consumer-focused deployment strategies

### If Failed
- Indicates professional accuracy may be prerequisite for consumer utility
- Suggests need for hybrid approaches balancing accuracy and accessibility
- May require more sophisticated consumer-focused methodologies

### Future Work
- Scale to larger participant pools and document sets
- Test across other legal domains beyond landlord-tenant
- Develop adaptive AI that adjusts based on user expertise level

## Related Works
### Nearest Neighbor Paper
Manor et al. (2019) on plain English legal contracts, but focused on contract drafting rather than comprehension

### Key Differences
- Focus on AI-assisted comprehension rather than contract generation
- Emphasis on real-world decision-making scenarios rather than legal accuracy
- Consumer outcome optimization rather than professional workflow enhancement

### Literature Gap
No existing work directly compares consumer-focused vs professional-focused legal AI on actual comprehension and decision-making outcomes

## Vectors (Risk Dimensions)
### Technical Risk
- AI output quality variations affecting fair comparison
- Difficulty maintaining equivalent information content across approaches
- Prompt engineering challenges for consistent consumer focus

### Methodological Risk
- Participant recruitment bias toward legally sophisticated users
- Learning effects from exposure to both conditions
- Measurement validity for "real-world utility" construct

### Resource Risk
- Limited access to diverse tenant populations
- Time constraints for comprehensive document coverage
- Computational costs for generating dual AI outputs

### Priority
**10/10** - Critical test of core research hypothesis, foundation for entire research program