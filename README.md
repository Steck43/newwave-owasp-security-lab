# CSEN 296A-1 Security in AI Project — Spring 2026

## NewWave Deal Assistant LLM Security Demo

This project is a local Streamlit web demo for OWASP-style LLM security risks in an investment banking AI assistant. It compares the same attack prompt under two configurations:

- An unsafe assistant configuration for classroom simulation
- A safer assistant configuration with stronger controls

The app can call a real OpenAI model through the official OpenAI Python SDK and the Responses API, a real Gemini model through Google's Gen AI Python SDK, or an OpenRouter model through OpenRouter's OpenAI-compatible Chat Completions endpoint. LLM outputs are not hardcoded.

## Safety Scope

NewWave is a fictional Bay Area investment bank. All clients, deal names, buyer lists, financial figures, documents, and risks in this demo are fictional.

The app does not send emails, modify files, connect to external systems, call financial APIs, or perform real financial actions. Any email or tool behavior is simulated text only.

## Scenarios

1. **Prompt Injection**  
   A malicious due diligence document contains hidden instructions that try to override the assistant's rules.

2. **Sensitive Information Disclosure**  
   A user tries to make the assistant reveal cross-client confidential data.

3. **System Prompt Leakage**  
   A user tries to extract hidden system instructions and internal compliance rules.

4. **Excessive Agency**  
   A user tries to make the assistant perform an external client action without human approval.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configure API Keys

For OpenAI, set `OPENAI_API_KEY` in your shell:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

For Gemini, set `GEMINI_API_KEY`:

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

`GOOGLE_API_KEY` is also supported for Gemini.

For OpenRouter, set `OPENROUTER_API_KEY`:

```bash
export OPENROUTER_API_KEY="your_openrouter_api_key_here"
```

Or create a local `.env` file:

```bash
cp .env.example .env
```

Then edit `.env` and replace the placeholder value.

Streamlit secrets are also supported. You can set:

```toml
OPENAI_API_KEY = "your_api_key_here"
GEMINI_API_KEY = "your_gemini_api_key_here"
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```

in `.streamlit/secrets.toml`.

## Run

```bash
streamlit run app.py
```

By default, the app uses Gemini with:

```text
gemini-3.5-flash
```

You can change the provider and model name in the Streamlit sidebar. OpenAI defaults to:

```text
gpt-5.5
```

OpenRouter defaults to DeepSeek:

```text
deepseek/deepseek-v4-flash
```

You can also set `DEFAULT_PROVIDER`, `DEFAULT_MODEL`, `DEFAULT_OPENAI_MODEL`, `DEFAULT_GEMINI_MODEL`, or `DEFAULT_OPENROUTER_MODEL` in your environment or `.env` file.

## What the Demo Shows

The demo sends the same fictional context and user attack prompt to two different instruction sets:

- The unsafe configuration is intentionally vulnerable and demonstrates what can go wrong.
- The safe configuration treats retrieved documents and user prompts as untrusted, blocks unsafe disclosures or actions, and requires human review for high-risk banking outputs.
- The unsafe and safe responses stream side by side so students can watch both configurations run in parallel.

Because responses come from a real selected model provider, exact wording may vary between runs.
