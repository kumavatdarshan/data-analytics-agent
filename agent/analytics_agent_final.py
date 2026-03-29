#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROFESSIONAL DATA ANALYTICS AGENT - FINAL VERSION
Real execution, real results, no fluff
"""

import os
import sys
import sqlite3
import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Load .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

# UTF-8 support
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class DataAnalyticsAgent:
    """Professional data analytics agent with REAL execution."""
    
    def __init__(self):
        """Initialize agent."""
        self.api_key = os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            print("ERROR: Set GROQ_API_KEY in .env or environment")
            sys.exit(1)
        
        try:
            from groq import Groq
            self.client = Groq(api_key=self.api_key)
        except:
            print("ERROR: pip install groq")
            sys.exit(1)
        
        self.db = sqlite3.connect(":memory:")
        self.conversation = []
        
    def load_data(self):
        """Load all CSV files."""
        csv_files = list(Path(".").glob("*.csv"))
        
        if not csv_files:
            print("No CSV files found!")
            return False
        
        print(f"\nLoading {len(csv_files)} file(s)...")
        
        for csv_file in csv_files:
            try:
                df = pd.read_csv(csv_file)
                table_name = csv_file.stem.lower()
                df.to_sql(table_name, self.db, if_exists='replace', index=False)
                print(f"  ✓ {csv_file.name} ({len(df)} rows, {len(df.columns)} columns)")
            except Exception as e:
                print(f"  ✗ {csv_file.name}: {str(e)}")
        
        return True
    
    def get_tables(self):
        """Get all tables."""
        cursor = self.db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [row[0] for row in cursor.fetchall()]
    
    def execute_query(self, query):
        """Execute SQL query and return results."""
        try:
            df = pd.read_sql_query(query, self.db)
            return True, df
        except Exception as e:
            return False, str(e)
    
    def analyze(self, user_input):
        """Execute analysis based on user input."""
        
        tables = self.get_tables()
        
        if not tables:
            print("No data loaded!")
            return
        
        # Build context
        table_info = ""
        for table in tables:
            df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 1;", self.db)
            cols = ", ".join(df.columns.tolist())
            rows = pd.read_sql_query(f"SELECT COUNT(*) as cnt FROM {table};", self.db).iloc[0,0]
            table_info += f"\n- {table}: {rows} rows, columns: {cols}"
        
        # Create prompt
        system_msg = f"""You are a data analyst. Analyze this data and respond with ONLY SQL queries.
        
Available tables:{table_info}

User request: {user_input}

RESPOND WITH ONLY:
1. A brief explanation (2-3 lines)
2. SQL query in this format:
QUERY: SELECT ... FROM ...

DO NOT explain the SQL. Just provide the query."""
        
        self.conversation.append({"role": "user", "content": user_input})
        
        try:
            response = self.client.chat.completions.create(
                model="gemma-2-9b-it",
                max_tokens=1000,
                messages=[
                    {"role": "system", "content": system_msg},
                    *self.conversation
                ]
            )
            
            reply = response.choices[0].message.content
            self.conversation.append({"role": "assistant", "content": reply})
            
            # Extract and execute SQL
            lines = reply.split('\n')
            explanation = []
            sql_query = None
            
            for line in lines:
                if line.startswith('QUERY:'):
                    sql_query = line.replace('QUERY:', '').strip()
                elif not line.startswith('QUERY') and line.strip():
                    explanation.append(line.strip())
            
            # Show explanation
            if explanation:
                print("\n📊 Analysis Plan:")
                print("-" * 70)
                for line in explanation[:5]:  # First 5 lines only
                    print(f"   {line}")
            
            # Execute query
            if sql_query:
                print("\n📈 Results:")
                print("-" * 70)
                
                success, result = self.execute_query(sql_query)
                
                if success:
                    print(result.to_string(index=False))
                    print(f"\n   Rows returned: {len(result)}")
                else:
                    print(f"Error: {result}")
            
        except Exception as e:
            print(f"ERROR: {str(e)}")
    
    def quick_analysis(self, analysis_type):
        """Quick pre-built analyses."""
        
        tables = self.get_tables()
        
        if not tables:
            print("No data!")
            return
        
        main_table = tables[0]
        
        print("\n📈 Results:")
        print("-" * 70)
        
        if analysis_type == "summary":
            # Row counts
            for table in tables:
                count = pd.read_sql_query(f"SELECT COUNT(*) as cnt FROM {table};", self.db).iloc[0, 0]
                print(f"\n{table}: {count} rows")
                
                # Sample columns
                df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 3;", self.db)
                print(df.to_string(index=False))
        
        elif analysis_type == "stats":
            # Statistics
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            print("\nBasic Statistics:")
            print(df.describe().to_string())
        
        elif analysis_type == "duplicates":
            # Check duplicates
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table};", self.db)
                dupes = len(df) - len(df.drop_duplicates())
                print(f"\n{table}: {dupes} duplicate rows")
        
        elif analysis_type == "nulls":
            # Check nulls
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table};", self.db)
                nulls = df.isnull().sum()
                if nulls.sum() > 0:
                    print(f"\n{table} - Missing values:")
                    print(nulls[nulls > 0].to_string())
                else:
                    print(f"\n{table}: No missing values")
        
        elif analysis_type == "types":
            # Data types
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table};", self.db)
                print(f"\n{table}:")
                print(df.dtypes.to_string())
        
        elif analysis_type == "columns":
            # Show all columns
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 1;", self.db)
                print(f"\n{table} columns:")
                for i, col in enumerate(df.columns, 1):
                    print(f"  {i}. {col}")
        
        elif analysis_type == "size":
            # Data size info
            total_rows = 0
            total_cols = 0
            print("\nDataset Size:")
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table};", self.db)
                rows = len(df)
                cols = len(df.columns)
                total_rows += rows
                total_cols += cols
                print(f"  {table}: {rows} rows × {cols} columns = {rows*cols} cells")
            print(f"\nTotal: {total_rows} rows across {len(tables)} tables")
        
        elif analysis_type == "unique":
            # Unique values per column
            print("\nUnique values per column:")
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table};", self.db)
                print(f"\n{table}:")
                for col in df.columns:
                    unique_count = df[col].nunique()
                    print(f"  {col}: {unique_count} unique values")
        
        elif analysis_type == "head":
            # First rows
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            print(f"\nFirst 5 rows of {main_table}:")
            print(df.head(5).to_string(index=False))
        
        elif analysis_type == "tail":
            # Last rows
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            print(f"\nLast 5 rows of {main_table}:")
            print(df.tail(5).to_string(index=False))
        
        elif analysis_type == "rows":
            # Row counts
            print("\nRow counts:")
            for table in tables:
                count = pd.read_sql_query(f"SELECT COUNT(*) as cnt FROM {table};", self.db).iloc[0, 0]
                print(f"  {table}: {count} rows")
        
        elif analysis_type == "describe":
            # Full description
            print(f"\nDetailed Description of {main_table}:")
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            print(f"\nShape: {len(df)} rows × {len(df.columns)} columns")
            print(f"\nColumns: {', '.join(df.columns.tolist())}")
            print(f"\nData types:\n{df.dtypes.to_string()}")
            print(f"\nMissing values:\n{df.isnull().sum().to_string()}")
        
        elif analysis_type == "numeric":
            # Numeric columns only
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            numeric_df = df.select_dtypes(include=[np.number])
            if len(numeric_df.columns) > 0:
                print(f"\nNumeric columns statistics:")
                print(numeric_df.describe().to_string())
            else:
                print("No numeric columns found")
        
        elif analysis_type == "categorical":
            # Categorical columns
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            cat_cols = df.select_dtypes(include=['object']).columns
            if len(cat_cols) > 0:
                print(f"\nCategorical columns:")
                for col in cat_cols:
                    print(f"\n{col}:")
                    print(df[col].value_counts().to_string())
            else:
                print("No categorical columns found")
        
        elif analysis_type == "correlations":
            # Correlations (numeric only)
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            numeric_df = df.select_dtypes(include=[np.number])
            if len(numeric_df.columns) > 1:
                print("\nCorrelation Matrix:")
                corr = numeric_df.corr()
                print(corr.to_string())
            else:
                print("Need at least 2 numeric columns for correlation")
        
        elif analysis_type == "outliers":
            # Find outliers using IQR
            df = pd.read_sql_query(f"SELECT * FROM {main_table};", self.db)
            numeric_df = df.select_dtypes(include=[np.number])
            if len(numeric_df.columns) > 0:
                print("\nPotential outliers (IQR method):")
                for col in numeric_df.columns:
                    Q1 = numeric_df[col].quantile(0.25)
                    Q3 = numeric_df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    outliers = numeric_df[(numeric_df[col] < Q1 - 1.5*IQR) | (numeric_df[col] > Q3 + 1.5*IQR)]
                    if len(outliers) > 0:
                        print(f"  {col}: {len(outliers)} outliers")
            else:
                print("No numeric columns for outlier detection")
        
        elif analysis_type == "quality":
            # Data quality score
            print("\nData Quality Report:")
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table};", self.db)
                total_cells = len(df) * len(df.columns)
                missing_cells = df.isnull().sum().sum()
                duplicate_rows = len(df) - len(df.drop_duplicates())
                
                quality_score = ((total_cells - missing_cells) / total_cells) * 100
                
                print(f"\n{table}:")
                print(f"  Quality Score: {quality_score:.1f}%")
                print(f"  Missing values: {missing_cells} cells ({missing_cells/total_cells*100:.1f}%)")
                print(f"  Duplicate rows: {duplicate_rows}")
                print(f"  Total cells: {total_cells}")
        
        print("\n" + "-" * 70)


def main():
    """Main function."""
    
    print("\n" + "="*70)
    print("DATA ANALYTICS AGENT - REAL RESULTS VERSION")
    print("="*70)
    
    agent = DataAnalyticsAgent()
    
    # Load data
    if not agent.load_data():
        print("No data to analyze. Place CSV files in this folder.")
        return
    
    tables = agent.get_tables()
    print(f"\n✓ Ready to analyze: {', '.join(tables)}")
    
    # Interactive mode
    print("\n" + "="*70)
    print("QUICK ANALYSIS COMMANDS")
    print("="*70)
    print("""
DATA OVERVIEW:
  summary     - Show data overview with sample rows
  describe    - Detailed description of dataset
  head        - Show first 5 rows
  tail        - Show last 5 rows
  rows        - Show row counts per table
  columns     - List all columns
  size        - Show dataset size info

DATA QUALITY:
  nulls       - Find missing values
  duplicates  - Find duplicate rows
  quality     - Data quality report (%)
  types       - Show column data types
  unique      - Count unique values per column
  outliers    - Find potential outliers

STATISTICS & ANALYSIS:
  stats       - Basic statistics
  numeric     - Numeric columns stats
  categorical - Categorical columns breakdown
  correlations- Correlation matrix

OTHER:
  help        - Show this help
  quit        - Exit

Or ask anything about your data!
Example: "Show top 10 customers by order amount"
""")
    
    while True:
        user_input = input("\n>>> ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        if user_input.lower() == "help":
            print("""
DATA OVERVIEW:
  summary     - Data overview with samples
  describe    - Detailed description
  head        - First 5 rows
  tail        - Last 5 rows
  rows        - Row counts
  columns     - List all columns
  size        - Dataset size

DATA QUALITY:
  nulls       - Missing values
  duplicates  - Duplicate rows
  quality     - Quality score
  types       - Column types
  unique      - Unique counts
  outliers    - Find outliers

ANALYSIS:
  stats       - Statistics
  numeric     - Numeric stats
  categorical - Category breakdown
  correlations- Correlations

Other: help, quit""")
            continue
        
        if user_input.lower() in ["summary", "stats", "duplicates", "nulls", "types", 
                                   "columns", "size", "unique", "head", "tail", "rows",
                                   "describe", "numeric", "categorical", "correlations",
                                   "outliers", "quality"]:
            agent.quick_analysis(user_input.lower())
            continue
        
        # Regular analysis
        agent.analyze(user_input)


if __name__ == "__main__":
    main()
