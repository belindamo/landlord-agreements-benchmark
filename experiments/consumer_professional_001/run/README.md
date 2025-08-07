# Experiment Run: Consumer vs Professional Legal AI

This directory contains the implementation and execution of the consumer comprehension vs professional analysis experiment.

## Files
- `experiment_runner.py` - Main experiment execution script
- `data_generator.py` - Generates consumer and professional AI outputs
- `evaluation_framework.py` - Implements comprehension testing framework
- `sample_documents.json` - Test lease documents
- `results/` - Experiment results and analysis files

## Usage
1. Run data generation: `python data_generator.py`
2. Execute experiment: `python experiment_runner.py`
3. Results will be saved to `results/experiment_results.json`

## Dependencies
- OpenAI API key for GPT-4 generation
- Sample lease documents from data/ folder
- Evaluation framework from judge calibration experiment