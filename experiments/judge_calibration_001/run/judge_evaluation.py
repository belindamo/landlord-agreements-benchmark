#!/usr/bin/env python3
"""
LLM Judge Calibration Experiment
Testing correlation between LLM judges and human expert ratings
"""

import json
import numpy as np
from scipy.stats import pearsonr, spearmanr
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_sample_data():
    """Load sample AI outputs and human expert ratings"""
    with open('sample_ai_outputs.json', 'r') as f:
        return json.load(f)

def load_judge_prompts():
    """Load different prompting strategies for LLM judges"""
    with open('judge_prompts.json', 'r') as f:
        return json.load(f)

def simulate_llm_judge_ratings(ai_output, prompt_type, seed=42):
    """
    Simulate LLM judge ratings for this proof-of-concept
    In a real implementation, this would call actual LLM APIs
    """
    np.random.seed(seed + hash(ai_output['id'] + prompt_type))
    
    # Simulate different judge behavior based on prompt type
    if prompt_type == 'holistic_prompt':
        # Holistic tends to be less precise, more variable
        base_score = 7.5
        noise = np.random.normal(0, 1.2)
    elif prompt_type == 'multi_aspect_prompt':
        # Multi-aspect tends to be more systematic, less noisy
        base_score = 8.0
        noise = np.random.normal(0, 0.8)
    elif prompt_type == 'chain_of_thought_prompt':
        # Chain-of-thought tends to be more thoughtful, slightly higher
        base_score = 8.2
        noise = np.random.normal(0, 0.9)
    else:  # consumer_focused_prompt
        # Consumer-focused most aligned with expert judgment
        base_score = 8.5
        noise = np.random.normal(0, 0.7)
    
    # Adjust based on document complexity
    complexity_adjustment = {
        'simple': 0.5,
        'medium': 0.0,
        'complex': -0.3
    }
    
    final_score = base_score + noise + complexity_adjustment.get(ai_output['complexity'], 0)
    final_score = max(1, min(10, final_score))  # Clamp to 1-10 range
    
    return {
        'accuracy': round(final_score + np.random.normal(0, 0.3), 1),
        'clarity': round(final_score + np.random.normal(0, 0.3), 1),
        'completeness': round(final_score + np.random.normal(0, 0.3), 1),
        'overall': round(final_score, 1)
    }

def calculate_human_expert_averages(expert_ratings):
    """Calculate average human expert ratings"""
    aspects = ['accuracy', 'clarity', 'completeness', 'overall']
    averages = {}
    
    for aspect in aspects:
        scores = [expert_ratings[expert][aspect] for expert in expert_ratings]
        averages[aspect] = np.mean(scores)
    
    return averages

def calculate_correlations(human_ratings, llm_ratings):
    """Calculate correlation between human and LLM ratings"""
    aspects = ['accuracy', 'clarity', 'completeness', 'overall']
    correlations = {}
    
    for aspect in aspects:
        human_scores = [hr[aspect] for hr in human_ratings]
        llm_scores = [lr[aspect] for lr in llm_ratings]
        
        pearson_r, pearson_p = pearsonr(human_scores, llm_scores)
        spearman_r, spearman_p = spearmanr(human_scores, llm_scores)
        
        correlations[aspect] = {
            'pearson_r': pearson_r,
            'pearson_p': pearson_p,
            'spearman_r': spearman_r,
            'spearman_p': spearman_p
        }
    
    return correlations

def run_experiment():
    """Execute the full judge calibration experiment"""
    logger.info("Starting LLM Judge Calibration Experiment")
    
    # Load data and prompts
    sample_data = load_sample_data()
    judge_prompts = load_judge_prompts()
    
    results = {
        'experiment_id': 'judge_calibration_001',
        'timestamp': datetime.now().isoformat(),
        'prompt_strategies': list(judge_prompts.keys()),
        'sample_size': len(sample_data),
        'results_by_prompt': {}
    }
    
    # Test each prompting strategy
    for prompt_name, prompt_template in judge_prompts.items():
        logger.info(f"Testing prompt strategy: {prompt_name}")
        
        human_ratings = []
        llm_ratings = []
        
        for item in sample_data:
            # Calculate human expert averages
            human_avg = calculate_human_expert_averages(item['human_expert_ratings'])
            human_ratings.append(human_avg)
            
            # Simulate LLM judge ratings
            llm_rating = simulate_llm_judge_ratings(item, prompt_name)
            llm_ratings.append(llm_rating)
        
        # Calculate correlations
        correlations = calculate_correlations(human_ratings, llm_ratings)
        
        results['results_by_prompt'][prompt_name] = {
            'correlations': correlations,
            'human_ratings': human_ratings,
            'llm_ratings': llm_ratings
        }
        
        # Log key findings
        overall_pearson = correlations['overall']['pearson_r']
        logger.info(f"{prompt_name} - Overall Pearson correlation: {overall_pearson:.3f}")
    
    # Identify best performing strategy
    best_strategy = max(results['results_by_prompt'].keys(), 
                       key=lambda x: results['results_by_prompt'][x]['correlations']['overall']['pearson_r'])
    
    best_correlation = results['results_by_prompt'][best_strategy]['correlations']['overall']['pearson_r']
    
    results['summary'] = {
        'best_strategy': best_strategy,
        'best_correlation': best_correlation,
        'success_criteria_met': best_correlation >= 0.8
    }
    
    logger.info(f"Best performing strategy: {best_strategy} (r = {best_correlation:.3f})")
    logger.info(f"Success criteria (r ≥ 0.8) met: {results['summary']['success_criteria_met']}")
    
    # Save results
    with open('results/experiment_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    # Create results directory
    import os
    os.makedirs('results', exist_ok=True)
    
    # Run experiment
    results = run_experiment()
    
    print("\n=== EXPERIMENT COMPLETE ===")
    print(f"Best Strategy: {results['summary']['best_strategy']}")
    print(f"Best Correlation: {results['summary']['best_correlation']:.3f}")
    print(f"Success Criteria Met: {results['summary']['success_criteria_met']}")