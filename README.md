# 🤖 AI-Powered Outlook to Jira Triage Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT--4-green)
![Jira](https://img.shields.io/badge/Integration-Jira-blue)
![License](https://img.shields.io/badge/License-MIT-purple)

## 📋 Overview

This agent automates the IT support triage process. It monitors a designated Outlook inbox for new support emails, uses OpenAI (GPT-4) to analyze the content, determines priority, and automatically creates a structured ticket in Jira.

It replaces the manual work of reading emails and copy-pasting them into ticket tracking systems.

## 🚀 Features

* **Automated Monitoring:** Fetches unread emails via Microsoft Graph API.
* **AI Intelligence:** Uses LLMs to summarize issues, detect urgency, and assign priority (High/Medium/Low).
* **Smart Parsing:** Converts messy HTML emails into clean Markdown for Jira descriptions.
* **Duplicate Prevention:** Tracks processed email IDs to prevent creating duplicate tickets for the same email.
* **Secure:** Uses environment variables for all credentials; no hardcoded keys.

## 🛠️ Architecture

The project follows a modular **Service-Layer Architecture**:

* `main.py`: Orchestrator that manages the data flow.
* `outlook_client.py`: Handles Microsoft Graph API authentication and fetching.
* `openai_client.py`: Interface for GPT-4 analysis.
* `jira_client.py`: Handles Jira REST API issue creation.
* `triage_agent.py`: Encapsulates the business logic for analyzing requests.

## 📦 Prerequisites

* Python 3.10+
* **OpenAI API Key**
* **Jira Account** (Cloud URL, Email, and API Token)
* **Azure App Registration** (Client ID, Tenant ID, Secret) with `Mail.Read` permissions.

## ⚙️ Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/outlook-jira-ai-agent.git](https://github.com/YOUR_USERNAME/outlook-jira-ai-agent.git)
    cd outlook-jira-ai-agent
    ```

2.  **Set up Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```ini
    # OpenAI
    OPENAI_API_KEY=sk-your-key

    # Jira
    JIRA_URL=[https://your-domain.atlassian.net](https://your-domain.atlassian.net)
    JIRA_EMAIL=your-email@example.com
    JIRA_API_TOKEN=your-token
    JIRA_PROJECT_KEY=KAN

    # Microsoft Graph
    AZURE_CLIENT_ID=your-client-id
    AZURE_TENANT_ID=your-tenant-id
    AZURE_CLIENT_SECRET=your-client-secret
    ```

## 🏃‍♂️ Usage

Run the agent manually:

```bash
python3 main.py
