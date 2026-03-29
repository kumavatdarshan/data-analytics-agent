# Data Analytics AI Agent 🤖📊

**Autonomous Python & SQL Execution Engine for Data Analytics**

A sophisticated AI agent that autonomously handles complex data analytics tasks by executing SQL queries and Python code. Perfect for data scientists, analysts, and engineers who need intelligent, hands-off data processing.

---

## Features

✨ **Core Capabilities:**
- 🔍 **Natural Language Processing** - Ask questions in plain English
- 📝 **SQL Query Generation** - Automatic SQL creation and optimization
- 🐍 **Python Code Execution** - Complex data transformations and analysis
- 📊 **Automated Analysis** - Insights extraction and visualization preparation
- 🔄 **Multi-Turn Conversations** - Context-aware dialogue for iterative analysis
- 📈 **Data Validation** - Built-in error handling and result verification

✅ **Advanced Features:**
- Complex JOINs and subqueries
- Time series analysis and forecasting
- Automated data cleaning and normalization
- Statistical analysis and aggregations
- Multi-table transformations
- Error detection and recovery

---

## Installation

### Prerequisites
- Python 3.8+
- Anthropic API Key

### Setup

1. **Clone/Download the agent:**
```bash
# Copy data_analytics_agent.py to your project directory
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set your API key:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

---

## Quick Start

### Basic Usage

```python
from data_analytics_agent import DataAnalyticsAgent

# Initialize the agent
agent = DataAnalyticsAgent()

# Ask a question
result = agent.execute_agent_tasks(
    "What are the top 5 customers by revenue?"
)

# View results
print(result['insights'])
```

### Run Example
```bash
python data_analytics_agent.py
```

This will execute 3 example queries demonstrating the agent's capabilities.

---

## How It Works

### Agent Processing Pipeline

```
User Query
    ↓
[1] Parse Intent & Requirements
    ↓
[2] Generate SQL/Python Code
    ↓
[3] Execute Code Safely
    ↓
[4] Validate Results
    ↓
[5] Analyze & Extract Insights
    ↓
[6] Return Structured Results
```

### Execution Flow

1. **Intent Recognition** - The agent understands what data you need
2. **Code Generation** - Creates optimal SQL queries or Python scripts
3. **Safe Execution** - Runs code in an isolated environment
4. **Error Handling** - Catches and explains any issues
5. **Analysis** - Extracts meaningful insights from results
6. **Response** - Returns structured results with interpretations

---

## Example Queries

### Customer Analysis
```python
agent.execute_agent_tasks(
    "Find customers with the highest growth rate in the last quarter"
)
```

### Revenue Analysis
```python
agent.execute_agent_tasks(
    "Calculate total revenue by region and identify top 3 regions"
)
```

### Data Quality
```python
agent.execute_agent_tasks(
    "Check for missing values, duplicates, and anomalies in the data"
)
```

### Trend Analysis
```python
agent.execute_agent_tasks(
    "Show me monthly sales trends with year-over-year comparison"
)
```

### Complex Transformations
```python
agent.execute_agent_tasks(
    "Create a cohort analysis showing customer lifetime value by signup month"
)
```

---

## API Reference

### DataAnalyticsAgent Class

#### `__init__(api_key: Optional[str] = None)`
Initialize the agent with optional API key.

```python
agent = DataAnalyticsAgent(api_key="sk-...")
```

#### `execute_agent_tasks(user_query: str) -> Dict[str, Any]`
Execute a data analytics task and return structured results.

**Parameters:**
- `user_query` (str): Natural language query

**Returns:**
```python
{
    "query": str,              # Original user query
    "timestamp": str,          # ISO timestamp
    "steps": List[str],        # Execution steps taken
    "results": List[Dict],     # Query results and metadata
    "insights": str            # AI-generated insights
}
```

#### `execute_sql(query: str) -> Tuple[bool, str, Optional[DataFrame]]`
Execute a SQL query directly.

**Parameters:**
- `query` (str): SQL query string

**Returns:**
- `(success: bool, message: str, dataframe: pd.DataFrame)`

#### `execute_python(code: str) -> Tuple[bool, str, Any]`
Execute Python code directly.

**Parameters:**
- `code` (str): Python code string

**Returns:**
- `(success: bool, message: str, result: Any)`

#### `get_execution_history() -> List[Dict[str, Any]]`
Get history of all executed code.

#### `reset_conversation()`
Clear conversation history for a fresh start.

---

## Result Structure

### Execution Result Format
```json
{
  "query": "What are the top customers by revenue?",
  "timestamp": "2024-03-25T10:30:45.123456",
  "steps": [
    "Agent Response Generated",
    "SQL Query 1 Executed: Query executed successfully",
    "SQL Query 2 Executed: Query executed successfully"
  ],
  "results": [
    {
      "type": "SQL",
      "index": 1,
      "success": true,
      "message": "Query executed successfully",
      "rows_affected": 5,
      "columns": ["customer_id", "name", "total_revenue"],
      "preview": {
        "customer_id": {"0": "C-10245", "1": "C-10189"},
        "name": {"0": "Acme Corp", "1": "TechStart Inc"},
        "total_revenue": {"0": 62000, "1": 26500}
      }
    }
  ],
  "insights": "Based on the analysis, Acme Corp is the top customer..."
}
```

---

## Advanced Usage

### Custom Database Connection

```python
from data_analytics_agent import DataAnalyticsAgent
import sqlite3

agent = DataAnalyticsAgent()

# Connect to custom database
custom_db = sqlite3.connect("your_database.db")
agent.database = custom_db
```

### Iterative Analysis

```python
# Multi-turn conversation
agent.execute_agent_tasks("Show me customer trends")
agent.execute_agent_tasks("Break down by region")
agent.execute_agent_tasks("What's the growth rate?")
```

### Execution History

```python
# Get all executed code and results
history = agent.get_execution_history()
for execution in history:
    print(f"{execution['type']}: {execution['code']}")
```

---

## Data Sources

The agent supports multiple data sources:

### SQLite / SQL Databases
- Standard SQL queries via pandas/sqlalchemy
- Complex joins and aggregations
- Transaction support

### CSV/Excel Files
- Automatic detection and import
- Data type inference
- Pandas integration

### Cloud Data Warehouses
- Snowflake (with sqlalchemy)
- BigQuery (with pandas-gbq)
- Redshift (via SQLAlchemy)

### APIs & REST Endpoints
- JSON data fetching
- Pandas-compatible inputs

---

## Best Practices

### ✅ Do's
- Be specific in your queries
- Provide context about your data
- Ask follow-up questions for refinement
- Use the agent for complex analytical tasks
- Check execution history for debugging

### ❌ Don'ts
- Don't use for sensitive personal data
- Don't assume 100% accuracy without verification
- Don't run without API key set
- Don't query extremely large tables without filters
- Don't ignore error messages

---

## Troubleshooting

### API Key Issues
```
Error: ANTHROPIC_API_KEY not found
Solution: Set environment variable or pass to __init__()
```

### Database Connection Errors
```
Error: sqlite3.OperationalError
Solution: Ensure database file exists and is readable
```

### Timeout Errors
```
Error: Request timeout
Solution: Break down complex queries into smaller pieces
```

### Out of Memory
```
Error: Memory limit exceeded
Solution: Add LIMIT clauses or filter data before processing
```

---

## Performance Optimization

### Query Optimization
1. Add indexes to frequently queried columns
2. Use appropriate JOIN types
3. Filter early in the pipeline
4. Avoid SELECT * when possible

### Python Code Optimization
1. Use vectorized pandas operations
2. Minimize loops with NumPy
3. Cache repeated calculations
4. Use appropriate data types

### Agent Tuning
1. Be clear and specific in queries
2. Provide relevant context
3. Use iterative refinement
4. Monitor execution history

---

## Examples

### Example 1: Revenue Analysis
```python
query = "Calculate total revenue by customer and show top 5"
result = agent.execute_agent_tasks(query)

print(result['insights'])
# Output: "The top 5 customers generated $250,000 in revenue..."
```

### Example 2: Data Quality Check
```python
query = "Check data quality - missing values, duplicates, outliers"
result = agent.execute_agent_tasks(query)

print(result['steps'])
# Shows validation steps taken
```

### Example 3: Time Series Analysis
```python
query = "Show monthly sales trends for the last 12 months"
result = agent.execute_agent_tasks(query)

for step in result['steps']:
    print(f"• {step}")
```

---

## Output Examples

### Successful Execution
```
✓ Query Executed Successfully
  Processed 1.2M rows in 2.34s
  Memory used: 456 MB
  
Top 5 Customers:
- Acme Corp: $52,480 (+23.5%)
- TechStart Inc: $48,920 (+18.2%)
- Global Solutions: $44,150 (+15.8%)
```

### With Insights
```
Key Insights:
• Top customers show 15-23% YoY growth
• Average order value increasing trend
• Churn risk identified in 3 accounts
• Seasonal pattern detected in Q4
```

---

## Limitations

- Max query complexity: Moderate (use multiple queries for very complex analysis)
- Real-time: Results reflect data at execution time
- Accuracy: AI-generated SQL should be reviewed for critical decisions
- Size: Optimal for datasets under 10GB in memory
- Latency: API calls add 1-5 seconds per request

---

## Contributing

Found a bug? Want to improve the agent?

1. Test the specific case
2. Document the issue
3. Suggest improvements
4. Share your results

---

## License

This data analytics agent is provided as-is. Use with appropriate oversight for critical business decisions.

---

## Support

For issues with:
- **Anthropic API**: Check docs at https://docs.anthropic.com
- **Pandas/Python**: Visit https://pandas.pydata.org/docs
- **SQL**: Review https://www.sqlite.org/docs.html
- **This Agent**: Review the code comments and error messages

---

## Version History

### v1.0.0 (Current)
- Initial release
- SQL query execution
- Python code execution
- Multi-turn conversations
- Result validation
- Error handling

---

## Next Steps

1. **Install** the agent on your machine
2. **Set up** your data source
3. **Run** example queries
4. **Integrate** into your workflow
5. **Monitor** execution history
6. **Refine** for your use case

---

**Happy analyzing! 📊✨**
