# 🌍 VishwaGuru --- Project Overview

Empowering India's youth to engage with democracy through AI-powered
civic action.

VishwaGuru is an open-source civic-tech platform designed to simplify
how citizens interact with government systems. It enables people to
report civic issues, contact public representatives, and organize
community action using artificial intelligence, automation, and modern
web technologies.

Built specifically for India's governance structure and linguistic
diversity, VishwaGuru transforms everyday photos, videos, and voice
messages into structured civic reports that can be shared with the right
authorities in seconds.

## 🎯 Vision & Mission

### Vision

To create a transparent, inclusive, and technology-driven civic
ecosystem where every citizen can raise their voice easily and
effectively.

### Mission

Make democracy accessible to every Indian citizen through technology,
automation, and AI-powered civic tools.

## ✨ Core Capabilities

  -----------------------------------------------------------------------
  Feature                     Description
  --------------------------- -------------------------------------------
  🤖 AI Action Plans          Automatically generates complaint messages,
                              WhatsApp texts, and email drafts using
                              Google Gemini.

  📸 Civic Eye                Detects civic issues from uploaded images
                              and videos.

  ♻️ Waste Sorter             Classifies waste type using local
                              machine-learning models.

  🔊 Audio Transcription      Converts voice complaints into structured
                              text reports.

  📍 Spatial Deduplication    Prevents duplicate issue reports from the
                              same geographic location.

  📊 Impact Analytics         Displays civic engagement metrics and user
                              activity stats.

  🤝 Multi-Platform Access    Available via Web UI and Telegram bot.

  🌏 India-Centric Design     Supports Indian governance structure,
                              languages, and civic workflows.
  -----------------------------------------------------------------------

## 🏗️ System Architecture

VishwaGuru follows a unified service architecture where a single FastAPI
backend powers:

-   The web frontend
-   AI services
-   Database operations
-   Telegram bot communication

### Major Components

  -----------------------------------------------------------------------
  Component              Technology                   Purpose
  ---------------------- ---------------------------- -------------------
  🎨 Frontend            React, Vite, Tailwind        User interface and
                                                      interaction

  ⚙️ Backend             FastAPI, Python              API logic,
                                                      validation,
                                                      orchestration

  🗄️ Database            SQLite (dev), PostgreSQL     Persistent storage
                         (prod)                       

  🤖 AI Engine           Google Gemini API + local ML Issue analysis &
                                                      action generation

  📱 Bot                 python-telegram-bot          Alternate user
                                                      interface

  ☁️ Deployment          Firebase, Render, Netlify    Hosting and
                                                      scalability
  -----------------------------------------------------------------------

## 🔄 High-Level Data Flow

1.  User uploads photo/video/audio or text\
2.  AI engine analyzes and classifies the issue\
3.  Local ML models validate and tag the content\
4.  Gemini generates a civic action plan\
5.  User sends message via WhatsApp, Email, or Telegram\
6.  Data is stored in the database\
7.  Analytics and impact widgets update in real time

## 🧪 Quality Assurance

-   Automated backend tests with PyTest\
-   Frontend unit tests with Jest\
-   Verification scripts for UI, stats, and features\
-   Thread safety, caching, and deduplication testing

## ☁️ Deployment Options

  Platform           Frontend   Backend           Database
  ------------------ ---------- ----------------- ------------
  Firebase           Hosting    Cloud Functions   Firestore
  Netlify + Render   Netlify    Render            PostgreSQL
  Railway            Built-in   Built-in          Built-in
  Vercel + Railway   Vercel     Railway           Railway

## 🛠️ Technology Stack

Frontend: React 18, Vite, Tailwind CSS\
Backend: FastAPI, Python 3.12+, SQLAlchemy\
Database: SQLite, PostgreSQL\
AI/ML: Google Gemini API, local ML models\
Bot: python-telegram-bot\
Deployment: Firebase, Render, Netlify, Railway

## 🌟 Open Source & Community

VishwaGuru is licensed under the GNU Affero General Public License v3.0
(AGPL-3.0) and is built by a growing open-source community.
