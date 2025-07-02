#!/usr/bin/env python3
"""
Twitter Data Analysis Workflow Manager

This script provides a simple command-line interface to manage the analysis workflow
for the three Twitter datasets (climate, covid, tech) with memory-efficient processing.

Usage:
    python workflow_manager.py --help
    python workflow_manager.py --status
    python workflow_manager.py --analyze climate
    python workflow_manager.py --analyze covid  
    python workflow_manager.py --analyze tech
    python workflow_manager.py --export all
"""

import argparse
import json
import os
import sys
from pathlib import Path

def check_file_exists(filename):
    """Check if a file exists and return its size"""
    if os.path.exists(filename):
        size_mb = os.path.getsize(filename) / (1024 * 1024)
        return True, size_mb
    return False, 0

def get_dataset_status():
    """Get status of all datasets and analysis files"""
    datasets = {
        'climate': {
            'data_file': 'climate_tweets2.jsonl',
            'notebook': 'climate_analysis.ipynb',
            'export_file': 'climate_llm_training_data.json'
        },
        'covid': {
            'data_file': 'covid_tweets2.jsonl', 
            'notebook': 'covid_analysis.ipynb',
            'export_file': 'covid_llm_training_data.json'
        },
        'tech': {
            'data_file': 'tech_tweets2.jsonl',
            'notebook': 'tech_analysis.ipynb', 
            'export_file': 'tech_llm_training_data.json',
            'checkpoint_file': 'tech_analysis_checkpoint.pkl'
        }
    }
    
    print("📊 Twitter Dataset Analysis Status")
    print("=" * 50)
    
    for name, files in datasets.items():
        print(f"\n🔍 {name.upper()} Dataset:")
        
        # Check data file
        exists, size = check_file_exists(files['data_file'])
        status = f"✅ {size:.1f} MB" if exists else "❌ Missing"
        print(f"  Data file: {status}")
        
        # Check notebook
        exists, _ = check_file_exists(files['notebook'])
        status = "✅ Ready" if exists else "❌ Missing"
        print(f"  Notebook: {status}")
        
        # Check export file
        exists, size = check_file_exists(files['export_file'])
        status = f"✅ {size:.1f} MB" if exists else "⏳ Not exported"
        print(f"  Export file: {status}")
        
        # Check checkpoint for tech dataset
        if 'checkpoint_file' in files:
            exists, size = check_file_exists(files['checkpoint_file'])
            status = f"✅ {size:.1f} MB" if exists else "⏳ No checkpoint"
            print(f"  Checkpoint: {status}")

def print_instructions():
    """Print usage instructions"""
    print("\n📋 Analysis Workflow Instructions")
    print("=" * 50)
    print("""
🚀 Getting Started:

1. **Climate Dataset Analysis:**
   - Open: climate_analysis.ipynb
   - Run all cells sequentially
   - Memory-efficient processing for moderate dataset

2. **COVID-19 Dataset Analysis:**
   - Open: covid_analysis.ipynb  
   - Run all cells sequentially
   - Memory-efficient processing for moderate dataset

3. **Tech Dataset Analysis:**
   - Open: tech_analysis.ipynb
   - Run gradual processing cells
   - May require multiple sessions for large dataset
   - Progress is automatically saved

4. **Export Data:**
   - Each notebook exports LLM training data
   - JSON format with user behavior patterns
   - Ready for fine-tuning workflows

💡 Memory Management:
   - Designed for 16GB RAM systems
   - Automatic cleanup and monitoring
   - Chunked processing for large datasets
   - Resumable processing with checkpoints

📈 Expected Output:
   - Active users (6+ tweets) identification
   - Behavioral pattern analysis
   - Hashtag and mention networks
   - Structured export for LLM training
""")

def main():
    parser = argparse.ArgumentParser(
        description="Twitter Data Analysis Workflow Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python workflow_manager.py --status
    python workflow_manager.py --help
        """
    )
    
    parser.add_argument(
        '--status', 
        action='store_true',
        help='Show status of all datasets and analysis files'
    )
    
    parser.add_argument(
        '--instructions',
        action='store_true', 
        help='Show detailed workflow instructions'
    )
    
    args = parser.parse_args()
    
    if args.status:
        get_dataset_status()
        print_instructions()
    elif args.instructions:
        print_instructions()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
