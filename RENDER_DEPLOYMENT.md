# Render Deployment Guide for VishwaGuru Backend

This guide explains how to properly deploy the VishwaGuru backend on Render.

## Overview

The VishwaGuru backend is a FastAPI application that includes:
- RESTful API endpoints for issue reporting
- Integrated Telegram bot (runs automatically with the FastAPI app)
- Database connectivity (PostgreSQL for production, SQLite for local dev)
- AI-powered action plan generation using Google Gemini

## Deployment Configuration

### Option 1: Using render.yaml (Recommended)

If you have a `render.yaml` file in your repository, Render will automatically detect and use it. The configuration includes:

- **Build Command**: `./render-build.sh` (installs Python dependencies and builds frontend)
- **Start Command**: `cd backend && python __main__.py` (starts FastAPI app with Telegram bot)

### Option 2: Manual Configuration via Render Dashboard

If configuring manually in the Render dashboard:

#### Build Command
```bash
pip install -r backend/requirements.txt
```

**Note**: If you also want to serve the frontend from the backend (as configured in `main.py`), use the full build script:
```bash
./render-build.sh
```

#### Pre-Deploy Command (Optional)
Leave empty or use for database migrations if needed in the future:
```bash
# Leave empty for now
```

#### Start Command
```bash
cd backend && python __main__.py
```

**Alternative Start Commands** (both work):
```bash
cd backend && python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

or from the root directory:
```bash
python -m backend
```

### ❌ INCORRECT Start Commands

**DO NOT USE** these commands:
- ❌ `python -m bot` - This only starts the Telegram bot without the FastAPI server
- ❌ `python bot.py` - Same issue, bot only, no web API
- ❌ `uvicorn backend.main:app` (from root without cd) - Import path issues

## Environment Variables

Set these in the Render dashboard under "Environment Variables":

### Required Variables

1. **TELEGRAM_BOT_TOKEN**
   - Get from [@BotFather](https://t.me/botfather) on Telegram
   - Example: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

2. **GEMINI_API_KEY**
   - Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Example: `AIzaSyABcDEfGhIjKlMnOpQrStUvWxYz`

3. **DATABASE_URL**
   - Automatically set by Render when you attach a PostgreSQL database
   - Format: `postgresql://user:password@host:port/database`
   - The app automatically converts `postgres://` to `postgresql://` for SQLAlchemy

### Optional Variables

4. **PORT**
   - Automatically set by Render (usually 10000)
   - Don't manually set this

5. **HOST**
   - Default: `0.0.0.0`
   - Don't change this on Render

## Database Setup

1. Create a PostgreSQL database in Render
2. Link it to your web service
3. Render will automatically set the `DATABASE_URL` environment variable
4. Database tables are automatically created on first startup

## How It Works

### Application Structure

```
backend/
├── __init__.py           # Makes backend a Python package
├── __main__.py          # Entry point for python -m backend or python __main__.py
├── main.py              # FastAPI application with bot integration
├── bot.py               # Telegram bot logic
├── database.py          # Database configuration
├── models.py            # SQLAlchemy models
├── ai_service.py        # AI service for action plans
└── requirements.txt     # Python dependencies
```

### Startup Flow

1. **Build Phase**: 
   - Render runs the build command
   - Installs Python dependencies from `requirements.txt`
   - (Optional) Builds frontend if using `render-build.sh`

2. **Start Phase**:
   - Runs `cd backend && python __main__.py`
   - This starts uvicorn with the FastAPI app
   - FastAPI's lifespan manager automatically starts the Telegram bot
   - The bot runs in the background alongside the API

3. **Runtime**:
   - API is available at `https://your-app.onrender.com/`
   - Health check endpoint: `https://your-app.onrender.com/health`
   - Telegram bot is active and responding to messages

## Troubleshooting

### "Module not found" errors
- Make sure you're using `cd backend && python __main__.py` as the start command
- Don't try to import backend modules from the root directory without proper PYTHONPATH

### Bot not responding
- Check that `TELEGRAM_BOT_TOKEN` is correctly set
- Verify the token is active in BotFather
- Check the logs for bot-specific errors

### Database connection errors
- Ensure PostgreSQL database is created and linked
- Check that `DATABASE_URL` is automatically set by Render
- The app converts `postgres://` to `postgresql://` automatically

### Port binding issues
- Don't hardcode the port - use `$PORT` environment variable
- The `__main__.py` file automatically reads from `os.environ.get("PORT", 8000)`

### Frontend not loading
- Make sure you ran `./render-build.sh` as the build command
- Check that the frontend was built successfully
- Verify `frontend/dist` directory exists after build

## Local Testing

Test the deployment configuration locally:

```bash
# From project root
cd backend
export TELEGRAM_BOT_TOKEN="your_token"
export GEMINI_API_KEY="your_key"
export PORT=8000
python __main__.py
```

Or:

```bash
# From project root
export TELEGRAM_BOT_TOKEN="your_token"
export GEMINI_API_KEY="your_key"
export PORT=8000
python -m backend
```

Visit `http://localhost:8000/health` to verify it's running.

## Summary

✅ **Correct Render Configuration**:
- **Build Command**: `pip install -r backend/requirements.txt` (or `./render-build.sh` for full stack)
- **Start Command**: `cd backend && python __main__.py`
- **Environment Variables**: Set `TELEGRAM_BOT_TOKEN`, `GEMINI_API_KEY`, and attach PostgreSQL database

❌ **DO NOT USE**:
- Start Command: `python -m bot` (This won't start the web server!)

The key insight is that the Telegram bot is integrated into the FastAPI application via the lifespan context manager, so starting the FastAPI app automatically starts the bot. You should NOT run the bot separately.
