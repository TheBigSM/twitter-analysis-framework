# Twitter Data Analysis for LLM Agent Fine-tuning

This workspace provides **memory-efficient, modular analysis** of three Twitter datasets (Climate, COVID-19, Tech) to identify active users and behavioral patterns for LLM agent fine-tuning.

## 🎯 **Objective**

Identify and analyze **active Twitter users** (6+ tweets) to extract behavioral patterns, network structures, and engagement metrics suitable for training LLM agents that understand social media dynamics.

**Key Features:**
- **Memory-efficient processing** optimized for 16GB RAM systems
- **Modular analysis** with separate notebooks for each dataset
- **Privacy-first design** with automatic data protection
- **Public sharing ready** with comprehensive documentation
- **LLM training focused** data export and insights

## 📁 **Files Structure**

```
twitter_data/
├── 📊 Data Files (private - not in git)
│   ├── climate_tweets2.jsonl      # Climate dataset
│   ├── covid_tweets2.jsonl        # COVID-19 dataset  
│   └── tech_tweets2.jsonl         # Tech dataset (largest)
│
├── 📓 Analysis Notebooks
│   ├── climate_analysis.ipynb     # Climate-specific analysis
│   ├── covid_analysis.ipynb       # COVID-19-specific analysis
│   └── tech_analysis.ipynb        # Tech analysis (gradual processing)
│
├── 📄 Analysis Results
│   ├── climate_analysis_summary.md    # Climate analysis summary
│   ├── covid_analysis_summary.md      # COVID-19 analysis summary
│   └── tech_analysis_summary.md       # Tech analysis summary
│
├── 🔧 Utilities
│   ├── workflow_manager.py        # Workflow management script
│   ├── .gitignore                 # Git ignore file (protects private data)
│   └── README.md                  # This file
│
└── 📤 Output Files (generated - private)
    ├── climate_llm_training_data.json
    ├── covid_llm_training_data.json
    ├── tech_llm_training_data.json
    └── tech_analysis_checkpoint.pkl
```

## 🚀 **Quick Start**

### 1. Check Status
```bash
python workflow_manager.py --status
```

### 2. Run Analysis
Open the appropriate notebook in VS Code:
- **Climate**: `climate_analysis.ipynb` 
- **COVID-19**: `covid_analysis.ipynb`
- **Tech**: `tech_analysis.ipynb` (requires gradual processing)

### 3. Execute Cells
Run all cells sequentially in each notebook. The tech notebook may require multiple sessions.

### 4. View Results
After running analysis, check the generated markdown summaries:
- `climate_analysis_summary.md`
- `covid_analysis_summary.md`
- `tech_analysis_summary.md`

## 📊 **Analysis Features**

### 🔍 **Active User Identification**
- Users with **6+ tweets** (configurable threshold)
- Tweet count distribution analysis
- Activity level categorization

### 🤝 **Behavioral Analysis**
- **Engagement patterns**: Retweet vs. reply vs. original content rates
- **Network behavior**: Mention patterns and user interactions
- **Content analysis**: Hashtag usage and topic engagement
- **Temporal patterns**: Activity timing and frequency

### 📈 **Visualizations**
- Tweet count distributions
- Engagement type breakdowns
- Top hashtags and mentions
- User activity level distributions

### 📤 **LLM Training Data Export**
Each notebook exports:
1. **Structured JSON data** for LLM training (private - not committed to git)
2. **Markdown summary reports** with analysis insights (committed to git)

**JSON Structure** (for LLM training):
```json
{
  "dataset_info": {
    "name": "Dataset Name",
    "total_tweets": 1000000,
    "active_users": 5000,
    "export_timestamp": "2024-01-01T00:00:00"
  },
  "users": [
    {
      "user_id": "12345",
      "tweet_count": 25,
      "retweets": 8,
      "replies": 5,
      "original_tweets": 12,
      "top_hashtags": [{"hashtag": "climate", "count": 10}],
      "top_mentions": [{"mention": "user123", "count": 3}],
      "sample_tweets": ["tweet text 1", "tweet text 2"],
      "activity_pattern": {
        "retweet_rate": 32.0,
        "reply_rate": 20.0,
        "original_rate": 48.0
      }
    }
  ]
}
```

**Markdown Summaries** contain:
- Dataset overview and statistics
- Active user analysis
- Behavioral patterns and insights
- Top hashtags and mentions
- Engagement metrics
- Key findings for LLM training

## 💾 **Memory Management**

### 🎯 **16GB RAM Optimized**
- **Chunked processing**: Small batches (3K-10K tweets)
- **Memory monitoring**: Automatic usage tracking
- **Aggressive cleanup**: Garbage collection after each chunk
- **Data limiting**: Truncated storage per user to prevent bloat

### 🔄 **Gradual Processing (Tech Dataset)**
The tech dataset uses special gradual processing:
- **Session-based**: 30 chunks per session
- **Checkpointing**: Resume from last processed line
- **Memory thresholds**: Stop at 85% RAM usage
- **Progress tracking**: Detailed status reporting

## 📓 **Notebook Details**

### 🌍 **Climate Analysis (`climate_analysis.ipynb`)**
- **Memory-efficient** processing for climate discussions
- **Environmental hashtags** and topic analysis
- **Climate activist** behavior patterns
- **Moderate dataset size** - single session processing

### 🦠 **COVID-19 Analysis (`covid_analysis.ipynb`)**
- **Pandemic-focused** user behavior analysis
- **Health-related hashtags** and mentions
- **Crisis communication** patterns
- **Moderate dataset size** - single session processing

### 💻 **Tech Analysis (`tech_analysis.ipynb`)**
- **Gradual processing** for large dataset
- **Technology hashtags** and dev community analysis
- **Professional network** behavior patterns
- **Large dataset** - multi-session processing with checkpoints

## 🔧 **Configuration Options**

### Adjustable Parameters:
- `min_tweets`: Minimum tweets for "active user" classification (default: 6)
- `chunk_size`: Processing batch size (default: 3K-10K)
- `max_chunks_per_session`: Session limits (default: 30-50)
- `memory_threshold`: RAM usage limit (default: 85%)

### Memory Settings:
```python
# Example configuration
analyzer = TechTwitterAnalyzer('tech_tweets2.jsonl')
analyzer.memory_threshold = 80  # Lower threshold for more conservative processing
analyzer.aggressive_cleanup = True  # Enable aggressive memory management
```

## 📊 **Expected Outputs**

### 📈 **Analysis Results**
- **Active user counts** and percentages
- **Engagement statistics** (retweet/reply/original rates)
- **Top hashtags** by dataset
- **User activity distributions**

### � **Summary Reports** (Markdown)
Each analysis generates a comprehensive markdown summary:
- **Dataset overview** with key statistics
- **Active user analysis** and behavioral patterns
- **Top hashtags and mentions** with engagement metrics
- **Visual insights** and key findings
- **LLM training recommendations**

### �📤 **Export Files** (Private)
- **JSON training data** for each dataset (not committed to git)
- **Structured user profiles** with behavioral metrics
- **Sample tweets** for context understanding
- **Network patterns** for social behavior modeling

## 🛠 **Technical Requirements**

- **Python 3.8+**
- **16GB RAM** (minimum recommended)
- **Required packages**: pandas, numpy, matplotlib, seaborn, psutil, collections
- **Storage**: ~2-5GB for output files depending on dataset sizes

## 📋 **Workflow Steps**

1. **📊 Status Check**: Run `workflow_manager.py --status`
2. **🌍 Climate Analysis**: Complete `climate_analysis.ipynb`
3. **🦠 COVID Analysis**: Complete `covid_analysis.ipynb`
4. **💻 Tech Analysis**: Run `tech_analysis.ipynb` (may require multiple sessions)
5. **� Review Summaries**: Check generated `.md` files for insights
6. **�📤 Data Export**: Collect JSON files from each notebook (private)
7. **🤖 LLM Training**: Use exported data for agent fine-tuning

## 🔒 **Privacy & Git Management**

This repository is configured to protect private data:
- **Data files** (`.jsonl`, `.json`, `.csv`, `.pkl`) are **not committed** to git
- **Analysis notebooks** and **summary reports** are public and safe to share
- **Output files** containing actual data are automatically excluded via `.gitignore`
- Only **code, documentation, and insights** are tracked in version control

## 🚨 **Memory Management Tips**

### For Large Datasets:
- **Monitor RAM usage** during processing
- **Run tech analysis** in multiple sessions
- **Close other applications** to free memory
- **Use checkpointing** to resume interrupted sessions

### If Memory Issues Occur:
- **Reduce chunk_size** (e.g., from 5000 to 2000)
- **Lower max_chunks_per_session** (e.g., from 30 to 15)
- **Enable aggressive cleanup** in analyzer settings
- **Process datasets separately** (one at a time)

## 🎯 **Use Cases for LLM Training**

The exported data supports training for:
- **Social media agent** behavior simulation
- **Topic-specific discussion** agents (climate, health, tech)
- **Engagement pattern** modeling
- **User behavior** prediction
- **Network analysis** and community detection
- **Content recommendation** based on user patterns

## 🔍 **Troubleshooting**

### Common Issues:
- **Memory exhaustion**: Reduce chunk sizes, enable aggressive cleanup
- **File not found**: Check dataset file paths and names
- **JSON decode errors**: Datasets may have malformed lines (automatically skipped)
- **Slow processing**: Normal for large datasets, use gradual processing

### Performance Tips:
- **Close unnecessary applications** before processing
- **Use SSD storage** for faster I/O
- **Process one dataset at a time** to maximize available memory
- **Monitor system resources** during processing

---

## 📞 **Support & Usage**

### **For Analysis Questions:**
1. Check the **workflow_manager.py** status output
2. Review **notebook cell outputs** for error messages
3. Monitor **memory usage** during processing
4. Use **checkpointing** to resume interrupted sessions
5. Check **markdown summary files** for analysis insights

### **For Public Sharing:**
- This repository is **safe to share publicly** as configured
- All **private data is protected** by `.gitignore`
- **Notebooks and summaries** contain no sensitive information
- **Code and insights** are ready for collaborative development

### **Repository Structure:**
- **Public files**: Notebooks, code, documentation, summaries
- **Private files**: Data files, exports, checkpoints (automatically excluded)

---

*Designed for efficient analysis of large Twitter datasets on consumer hardware (16GB RAM) with focus on LLM agent training data extraction and public collaboration.*
