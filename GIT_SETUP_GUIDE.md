# Git Setup and Usage Guide

## Quick Setup
```bash
# Initialize repository
git init

# Add files (only safe files will be added due to .gitignore)
git add .

# First commit
git commit -m "Initial commit: Twitter analysis notebooks and framework"

# Add remote repository (replace with your actual repo URL)
git remote add origin https://github.com/yourusername/twitter-analysis.git

# Push to remote
git push -u origin main
```

## What Gets Committed vs. Ignored

### ✅ **Files that WILL be committed (safe to share):**
- `README.md` - Project documentation
- `workflow_manager.py` - Analysis workflow script
- `climate_analysis.ipynb` - Climate analysis notebook
- `covid_analysis.ipynb` - COVID analysis notebook  
- `tech_analysis.ipynb` - Tech analysis notebook
- `*_analysis_summary.md` - Generated analysis summaries
- `.gitignore` - This protection file

### 🚫 **Files that are IGNORED (private data):**
- `*.jsonl` - Raw Twitter data files (climate_tweets2.jsonl, etc.)
- `*.json` - Exported training data and analysis results
- `*.csv` - Generated CSV exports
- `*.pkl` - Checkpoint files
- Any other sensitive data files

## Repository Structure
```
twitter_data/
├── .gitignore                    # Protects private data
├── README.md                     # Project documentation
├── workflow_manager.py           # Analysis workflow
├── climate_analysis.ipynb        # Climate dataset analysis
├── covid_analysis.ipynb          # COVID dataset analysis
├── tech_analysis.ipynb           # Tech dataset analysis
├── *_analysis_summary.md         # Generated summaries
└── [PRIVATE DATA FILES IGNORED]  # All *.jsonl, *.json, *.csv, etc.
```

## Safety Notes
- The `.gitignore` file protects all data files from being committed
- You can safely run `git add .` - private data will be automatically excluded
- Summary markdown files are included as they contain aggregate statistics only
- All raw tweets, user data, and exports are protected

## Updating the Repository
```bash
# Check status (see what will be committed)
git status

# Add new changes
git add .

# Commit changes
git commit -m "Update analysis notebooks with new features"

# Push to remote
git push
```

## Adding Collaborators
When sharing this repository:
1. Collaborators will get all the analysis code and notebooks
2. They will need their own Twitter data files
3. They can run the analysis on their own datasets
4. The notebooks are ready to use - just place data files in the directory
