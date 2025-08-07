# ContraSUM: Party-Specific Contract Summarization

**Full Citation:** Sancheti, A., Garimella, A., Srinivasan, B. V., & Rudinger, R. (2022). What to Read in a Contract? Party-Specific Summarization of Important Obligations, Entitlements, and Prohibitions in Legal Documents. *arXiv preprint arXiv:2212.09825*.

## CS197 Analysis Structure

### Problem
- **Core Issue**: Legal contracts are long and written in legalese, requiring manual hours to understand
- **Specific Challenge**: Need for party-specific summaries focusing on obligations, entitlements, and prohibitions
- **Real-world Impact**: Companies hire legal experts or use tools for contract analysis due to comprehension difficulty

### Prior Work Assumptions
- Previous contract analysis focused on general summarization or entity extraction
- Most legal NLP work targeted legal professionals rather than contracting parties
- Existing systems didn't differentiate between different types of legal commitments (obligations vs. entitlements vs. prohibitions)

### Key Insight/Innovation
- **Novel Approach**: Party-specific summarization that categorizes content into three key types:
  1. **Obligations** - what a party must do
  2. **Entitlements** - what a party is allowed to do/receive
  3. **Prohibitions** - what a party cannot do
- **Methodological Innovation**: Two-module system combining content categorization with importance ranking

### Technical Approach
1. **Data Collection**: ~293K pairwise importance comparison annotations by legal experts on lease agreements
2. **System Architecture**:
   - **Content Categorizer**: Identifies sentences containing obligations, entitlements, prohibitions for each party
   - **Importance Ranker**: Compares importance among sentences within each category to produce ranked lists
3. **Summary Generation**: Selects most important sentences per category per party

### Evaluation/Proof
- **Automatic Evaluation**: Compared against text ranking baselines
- **Human Evaluation**: Assessment by domain experts
- **Dataset**: Focus on lease agreements with expert annotations
- **Metrics**: Effectiveness measured through both automated and human evaluation

### Impact and Relevance
- **Direct Relevance**: Most similar to our landlord-tenant agreement comprehension task
- **Methodological Contribution**: Demonstrates importance of party-specific analysis in legal documents
- **Dataset Contribution**: Expert-annotated lease agreement dataset for contract analysis research
- **System Innovation**: First system to explicitly categorize legal commitments by type and importance

### Connection to Our Work
- **Shared Domain**: Focus on lease/rental agreements
- **Complementary Approach**: Their extractive summarization complements our plain language comprehension evaluation
- **Expert Annotation**: Validates our approach of using expert annotation for legal document analysis
- **Party-Specific Focus**: Aligns with our consumer-focused approach, though they focus on both parties

### Assumptions Made
- Legal contracts can be meaningfully categorized into obligations, entitlements, and prohibitions
- Pairwise importance comparisons by experts can be used to train ranking systems
- Party-specific summarization is more useful than generic contract summaries
- Expert annotations on one domain (lease agreements) can generalize to contract analysis methods

### Research Gap Addressed
- Lack of party-specific contract analysis tools
- Need for structured categorization of legal commitments
- Absence of large-scale expert-annotated contract datasets

---

*Added to literature review as directly relevant to landlord-tenant agreement analysis - demonstrates expert annotation methodology and party-specific approach to legal document comprehension.*