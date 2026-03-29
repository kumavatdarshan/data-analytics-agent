# HOW TO SET YOUR GROQ API KEY - Simple Guide

## 🔑 STEP 1: Get Your API Key

1. Go to: https://console.groq.com
2. Sign in (or create free account)
3. Click "API Keys" 
4. Click "Create New API Key"
5. **Copy the key** (looks like: `gsk_xxxxxxxxxxxxx`)

---

## 📁 STEP 2: Create .env File

In your project folder, create a new file named:
```
.env
```

Open it and paste:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxx
```

**Replace** `gsk_xxxxxxxxxxxxx` with your actual key!

---

## 📦 STEP 3: Install dotenv (One Time Only)

Run this command once:
```bash
pip install python-dotenv
```

---

## ▶️ STEP 4: Run the Agent

```bash
python analytics_agent_v2.py
```

Done! The agent will automatically load your API key from the .env file! ✅

---

## 🎯 Folder Structure Should Look Like:

```
your_project/
├── analytics_agent_v2.py
├── sample_customers_new.csv
├── sample_orders_new.csv
├── .env                          ← Your API key here
└── requirements_new.txt
```

---

## ✅ Verify It Works

When you run the agent, you should see:

```
PROFESSIONAL DATA ANALYTICS AGENT
==================================

Detecting available models...
✓ Using model: gemma-2-9b-it

LOADING DATA
============
```

If you see errors about API key, make sure:
1. ✓ .env file is created
2. ✓ File is named `.env` (exactly)
3. ✓ Contains: `GROQ_API_KEY=your-actual-key`
4. ✓ python-dotenv is installed: `pip install python-dotenv`

---

## 🆘 If Still Having Issues

Try this direct method instead:

### Windows - Create RUN.bat file:

Create a file named `RUN.bat` with this content:

```batch
@echo off
set GROQ_API_KEY=gsk_xxxxxxxxxxxxx
python analytics_agent_v2.py
pause
```

Then double-click `RUN.bat` to run!

---

## 🎉 That's It!

Your agent is ready to use. Just run:

```bash
python analytics_agent_v2.py
```

And start asking questions about your data! 📊
