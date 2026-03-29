# PROFESSIONAL DATA ANALYTICS AGENT
## Complete Setup & Usage Guide

---

## 🚀 QUICK START (3 Steps)

### Step 1: Install Dependencies
```bash
pip install groq pandas numpy openpyxl
```

### Step 2: Set API Key
```bash
export GROQ_API_KEY="your-api-key"
```
Or create `.env` file:
```
GROQ_API_KEY=your-api-key
```

### Step 3: Run the Agent
```bash
python analytics_agent.py
```

---

## 📊 WHAT IT DOES

✅ **Automatic Data Loading**
- Auto-loads all CSV and Excel files from folder
- Detects table structure automatically
- No manual configuration needed

✅ **Data Analysis**
- SQL queries for data exploration
- Python transformations
- Pattern detection
- Quality assessment

✅ **Data Cleaning**
- Remove duplicates
- Handle missing values
- Data validation
- Outlier detection

✅ **Insights & Reports**
- Statistical analysis
- Trend identification
- Business recommendations
- Clear explanations

---

## 🎯 HOW TO USE

### Basic Usage
```bash
python analytics_agent.py
```

Output:
```
======================================================================
PROFESSIONAL DATA ANALYTICS AGENT
======================================================================

LOADING DATA
============...

Found data files:
  ✓ Loaded customers.csv as 'customers' (100 rows)
  ✓ Loaded orders.csv as 'orders' (500 rows)

✓ Loaded tables: customers, orders

ANALYSIS MODE
=============

What would you like to analyze?

Examples:
  • Show me the data summary
  • Clean and analyze the data
  • Find patterns and trends

>>>
```

### Commands
```
>>> tables              # Show loaded tables
>>> reset              # Clear conversation
>>> help               # Show commands
>>> quit               # Exit
```

### Analysis Examples
```
>>> Show me a summary of customers
>>> Analyze order patterns
>>> Find duplicate records
>>> Clean the data and show quality report
>>> What's the revenue by region?
>>> Identify anomalies in the data
```

---

## 📁 SETUP YOUR DATA

### Option 1: CSV Files (Easiest)
1. Save your CSV files in the same folder:
```
project_folder/
├── analytics_agent.py
├── customers.csv
├── orders.csv
└── products.csv
```

2. Run:
```bash
python analytics_agent.py
```

The agent automatically:
- ✓ Finds all CSV files
- ✓ Loads them into database
- ✓ Detects table structure
- ✓ Shows preview

### Option 2: Excel Files
1. Save your Excel files (one or multiple sheets):
```
project_folder/
├── analytics_agent.py
└── data.xlsx    (with sheets: customers, orders, products)
```

2. Run:
```bash
python analytics_agent.py
```

---

## 🔧 ADVANCED USAGE

### Custom Python Script
```python
from analytics_agent import DataAnalyticsAgent

# Initialize
agent = DataAnalyticsAgent()

# Load data
agent.load_csv("customers.csv")
agent.load_csv("orders.csv")

# Analyze
result = agent.analyze_data("Show me top customers by revenue")

print(result["insights"])
```

### Direct SQL Queries
```python
agent = DataAnalyticsAgent()
agent.load_csv("data.csv")

# Execute SQL
success, message, df = agent.execute_sql(
    "SELECT * FROM data WHERE amount > 1000"
)

print(df)
```

### Data Transformation
```python
# Execute Python code
success, msg, result = agent.execute_python("""
import pandas as pd
df = pd.read_csv('data.csv')
df['revenue'] = df['quantity'] * df['price']
result = df.groupby('category')['revenue'].sum()
print(result)
""")
```

---

## 📊 EXAMPLE QUERIES

### Data Exploration
```
>>> How many records in each table?
>>> Show table structure and columns
>>> Display sample data from customers
>>> What's the data range for each numeric column?
```

### Data Cleaning
```
>>> Find and remove duplicate records
>>> Check for missing or null values
>>> Identify data quality issues
>>> Standardize column formats
>>> Remove outliers from the data
```

### Data Analysis
```
>>> What are the top 10 customers by revenue?
>>> Show sales trend by month
>>> Compare performance by region
>>> Find correlation between columns
>>> Analyze customer segments
```

### Business Insights
```
>>> What patterns do you see in the data?
>>> Identify growth opportunities
>>> Flag potential problems
>>> Recommend improvements
>>> Create summary statistics
```

---

## 🎯 REAL WORLD EXAMPLES

### Example 1: Customer Analysis
**Files:** customers.csv, orders.csv

```
>>> Load the data
>>> Analyze customer lifetime value
>>> Find top customers
>>> Identify churn risk
>>> Show regional breakdown
```

### Example 2: Sales Analysis
**Files:** sales.csv, products.csv

```
>>> Show sales trend
>>> Compare product performance
>>> Find seasonal patterns
>>> Calculate growth rate
>>> Identify best sellers
```

### Example 3: Data Cleaning Project
**File:** dirty_data.csv

```
>>> Assess data quality
>>> Find duplicates
>>> Handle missing values
>>> Standardize formats
>>> Create clean dataset
```

---

## 🐛 TROUBLESHOOTING

### Error: GROQ_API_KEY not set
**Solution:**
```bash
export GROQ_API_KEY="your-key-here"
```

Or create `.env`:
```
GROQ_API_KEY=your-key
```

### Error: No CSV files found
**Solution:**
- Move CSV/Excel files to the same folder as analytics_agent.py
- Make sure files have correct extensions (.csv, .xlsx)

### Error: pandas not installed
**Solution:**
```bash
pip install pandas numpy openpyxl
```

### Error: groq not installed
**Solution:**
```bash
pip install groq
```

---

## 💡 TIPS & TRICKS

### Faster Analysis
- Keep queries specific: "Top 10 customers" not "Analyze everything"
- Use smaller datasets for testing
- Ask one question at a time

### Better Results
- Ask questions like a human analyst would
- Provide context about your data
- Follow up with "Why?" or "Can you explain..."

### Saving Results
- Copy and paste important findings
- Use `export` command (in development)
- Save analysis output manually

---

## 🎓 WHAT YOU CAN DO

### ✅ Can Do
- ✓ Load CSV and Excel files
- ✓ Analyze data with SQL
- ✓ Transform data with Python
- ✓ Find patterns and trends
- ✓ Clean and validate data
- ✓ Generate insights
- ✓ Answer business questions
- ✓ Multi-turn conversations

### ⚠️ Limitations
- Limited to local files (CSV, Excel)
- Max response time ~30 seconds
- Works best with structured data
- No real-time data sources yet

---

## 📋 FILE STRUCTURE

```
project/
├── analytics_agent.py          # Main agent (download this!)
├── customers.csv               # Your data
├── orders.csv                  # Your data
├── products.xlsx               # Your data
└── .env                        # Optional: API key
```

---

## ✅ CHECKLIST

Before first use:
- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install groq pandas numpy openpyxl`)
- [ ] Groq API key obtained
- [ ] GROQ_API_KEY environment variable set
- [ ] CSV/Excel files in same folder
- [ ] Run `python analytics_agent.py`

---

## 📞 GETTING HELP

### Common Issues
- Check API key is set correctly
- Ensure files are in same folder
- Verify file format (CSV, XLSX)
- Try simpler questions first

### Getting Better Results
- Be specific in questions
- Ask one thing at a time
- Provide data context
- Use followup questions

---

## 🎉 YOU'RE READY!

Your professional data analytics agent is ready to:
- ✓ Load your data
- ✓ Analyze it
- ✓ Clean it
- ✓ Extract insights
- ✓ Answer questions

### Start with:
```bash
python analytics_agent.py
```

Then ask:
```
>>> Show me a summary of my data
```

Enjoy! 🚀
