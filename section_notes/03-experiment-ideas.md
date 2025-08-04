# Experiment Ideas

## Core Bit Flip Testing Framework

**Central Hypothesis**: Consumer-focused legal AI (plain language + scenario-based comprehension) provides greater real-world utility than professional-focused legal AI (technical extraction + legal reasoning).

## Proposed Experiments

### Experiment 1: Consumer Comprehension vs. Professional Analysis (Primary)
**Thesis**: AI systems optimized for consumer comprehension will demonstrate superior real-world utility compared to systems optimized for professional legal analysis.

**Bit Flip Test**: Direct comparison between consumer-focused and professional-focused AI approaches on identical landlord-tenant documents.

**Hypotheses**:
- H1: Plain language summaries will increase tenant comprehension scores by ≥30% compared to technical legal analysis
- H2: Scenario-based Q&A will result in ≥50% more accurate tenant decision-making than clause-level extraction
- H3: Consumer-focused outputs will reduce time-to-understanding by ≥40%

**Experimental Design**:
- **Independent Variables**: 
  - AI approach (consumer-focused vs. professional-focused)
  - Document complexity (simple/medium/complex leases)
  - Participant legal expertise (layperson/some experience/legal background)
- **Dependent Variables**:
  - Comprehension accuracy (scored questionnaire)
  - Decision-making quality (scenario responses)
  - Time to complete understanding tasks
  - Confidence ratings
  - Preference scores
- **Procedure**:
  1. Recruit 120 participants (40 per expertise level)
  2. Randomly assign to consumer-focused or professional-focused AI condition
  3. Present 3 lease documents of varying complexity
  4. Measure comprehension and decision-making across conditions
  5. Cross-over design: participants experience both conditions

**Validity Threats & Mitigations**:
- **Selection bias**: Stratified random sampling across demographics
- **Learning effects**: Counterbalanced presentation order
- **Demand characteristics**: Blind participants to research hypothesis
- **Experimenter bias**: Automated scoring where possible

**Success Criteria**:
- Consumer-focused approach shows statistically significant improvements (p < 0.05)
- Effect sizes of ≥0.5 (medium effect) for primary measures
- Qualitative feedback supports quantitative findings

### Experiment 2: LLM Judge Calibration for Consumer-Focused Evaluation
**Thesis**: LLM judges can be calibrated to reliably evaluate consumer-focused legal AI outputs with high correlation to human expert judgment.

**Hypotheses**:
- H1: Properly prompted LLM judges will achieve ≥0.8 correlation with human expert ratings
- H2: Multi-aspect evaluation (accuracy, clarity, completeness) will outperform holistic scoring
- H3: Judge performance will vary systematically by legal document complexity

**Experimental Design**:
- **Independent Variables**:
  - Judge model (GPT-4o, Claude Sonnet 4, Gemini Pro)
  - Prompting strategy (holistic vs. multi-aspect vs. chain-of-thought)
  - Document complexity (simple/medium/complex)
- **Dependent Variables**:
  - Correlation with human expert ratings
  - Inter-judge reliability
  - Calibration scores (confidence vs. accuracy)
- **Procedure**:
  1. Generate 200 AI outputs across consumer-focused tasks
  2. Collect human expert ratings (3 legal aid professionals)
  3. Evaluate with different LLM judges and prompting strategies
  4. Calculate correlations and reliability metrics

**Success Criteria**:
- Best judge configuration achieves ≥0.8 correlation with humans
- Inter-judge reliability ≥0.7 across conditions
- Identification of optimal prompting strategy for consumer-focused evaluation

### Experiment 3: Document Complexity Impact on Consumer Understanding
**Thesis**: Document complexity differentially affects consumer comprehension, with AI assistance providing greater benefit for complex documents.

**Hypotheses**:
- H1: AI assistance benefit increases with document complexity
- H2: Plain language summaries show greater benefit than Q&A for complex documents
- H3: Consumer confidence correlates inversely with document complexity without AI assistance

**Experimental Design**:
- **Independent Variables**:
  - Document complexity (5-point scale based on readability, clause density, legal jargon)
  - AI assistance type (none/plain summary/Q&A/combined)
- **Dependent Variables**:
  - Comprehension accuracy
  - Task completion time
  - Confidence ratings
  - Perceived document difficulty
- **Procedure**:
  1. Create complexity-rated document set (50 documents across complexity spectrum)
  2. Test 80 participants across AI assistance conditions
  3. Within-subjects design for complexity, between-subjects for AI type

### Experiment 4: Real-World Utility Validation
**Thesis**: Consumer-focused AI outputs lead to measurably better real-world outcomes for tenants facing actual lease decisions.

**Hypotheses**:
- H1: Tenants using consumer-focused AI will identify ≥40% more concerning lease clauses
- H2: AI-assisted tenants will report ≥30% higher confidence in lease negotiations
- H3: Consumer-focused summaries will lead to ≥25% more informed questions during lease signing

**Experimental Design**:
- **Participants**: 60 prospective tenants actively searching for housing
- **Procedure**:
  1. Pre-intervention baseline: tenant reviews lease without AI assistance
  2. Intervention: same tenant reviews lease with consumer-focused AI
  3. Post-intervention: tenant completes lease comprehension assessment
  4. Follow-up: survey on actual lease negotiation outcomes
- **Measures**:
  - Red flag identification accuracy
  - Quality of tenant questions/concerns raised
  - Negotiation outcome satisfaction
  - Perceived empowerment and understanding

## Priority Order

1. **Experiment 1** (Consumer vs. Professional Focus) - **HIGH PRIORITY**
   - Directly tests core bit flip assumption
   - Provides foundation for all other experiments
   - Timeline: 6-8 weeks

2. **Experiment 2** (LLM Judge Calibration) - **HIGH PRIORITY**
   - Essential for scalable evaluation methodology
   - Enables larger-scale follow-up studies
   - Timeline: 4-5 weeks

3. **Experiment 3** (Document Complexity Impact) - **MEDIUM PRIORITY**
   - Validates generalizability across document types
   - Informs practical deployment decisions
   - Timeline: 5-6 weeks

4. **Experiment 4** (Real-World Validation) - **MEDIUM PRIORITY**
   - Provides ecological validity
   - Requires longer timeline for recruitment
   - Timeline: 8-10 weeks

## Resource Requirements

### Human Resources
- **Research coordinator** (0.5 FTE): Participant recruitment, data collection coordination
- **Legal expert consultants** (3 professionals × 20 hours each): Human rating validation
- **UX researcher** (0.25 FTE): User study design and analysis
- **Data analyst** (0.25 FTE): Statistical analysis and visualization

### Technical Resources
- **Computing**: Standard GPU access for LLM inference (~$500/month for 3 months)
- **LLM API costs**: ~$2,000 for comprehensive judge evaluation
- **Survey platform**: Qualtrics or similar (~$200/month)
- **Statistical software**: R/Python (open source)

### Participant Compensation
- **Experiment 1**: 120 participants × $25 = $3,000
- **Experiment 3**: 80 participants × $20 = $1,600
- **Experiment 4**: 60 participants × $40 = $2,400
- **Total participant costs**: $7,000

### Document Acquisition
- **Legal document licensing**: ~$1,500 for diverse lease collection
- **Expert legal review**: $3,000 for document validation and complexity rating

**Total Estimated Budget**: $15,000-20,000

## Success Criteria

### Primary Success Metrics
1. **Bit Flip Validation**: Consumer-focused approach demonstrates statistically significant superiority (p < 0.05, effect size ≥ 0.5) across ≥2 key metrics
2. **Judge Reliability**: LLM judge achieves ≥0.8 correlation with human experts
3. **Real-World Impact**: Measurable improvement in tenant outcomes in naturalistic setting
4. **Methodological Contribution**: Established evaluation framework adopted by ≥2 follow-up studies

### Secondary Success Metrics
1. **Generalizability**: Results hold across document complexity levels
2. **Practical Utility**: System outputs rated as "useful" by ≥80% of participants
3. **Efficiency Gains**: ≥30% reduction in time-to-comprehension
4. **Publication Impact**: Results published in venue with ≥15% acceptance rate

### Failure Criteria and Contingencies
- **No significant difference between approaches**: Investigate moderating factors, refine consumer-focused methods
- **Poor judge reliability**: Develop alternative evaluation methods, increase human annotation
- **Low real-world impact**: Examine deployment context, user training needs
- **High dropout rates**: Simplify experimental procedures, increase compensation

### Long-term Impact Goals
1. **Field Influence**: Challenge professional-focused legal AI assumptions across ≥3 subsequent papers
2. **Practical Deployment**: Framework adopted by ≥1 legal aid organization
3. **Methodological Legacy**: Consumer comprehension evaluation becomes standard in legal AI research
4. **Policy Impact**: Results inform accessibility requirements for consumer-facing legal technology

---
*Enhanced using CS197 research methodology with rigorous experimental design*