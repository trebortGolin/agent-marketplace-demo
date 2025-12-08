# 🤖 Amorce Marketplace Demo

> **Production-ready AI agent marketplace demo showcasing secure agent-to-agent transactions**

Watch Sarah (buyer) and Henri (seller) negotiate a MacBook Pro sale with real Trust Directory integration, cryptographic signatures, and human-in-the-loop approvals.

[![Trust Directory](https://img.shields.io/badge/Trust%20Directory-trust.amorce.io-blue)](https://trust.amorce.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

---

## 🎬 Demo Preview

```
🤖 Sarah: Searching for MacBook Pro 2020...
   Found 3 verified sellers in trust.amorce.io

🤖 Sarah: Selecting Henri (4.8★ rating)
   ✅ Signature verified
   Initial offer: $450

🤖 Henri: Evaluating offer...
   Profit margin: 28% (below threshold)
   Counter-offer: $500

⏸️  HUMAN APPROVAL REQUIRED
   Agent: Sarah (Buyer)
   Action: Approve payment of $500
   [✓ Approve]

✅ TRANSACTION SUCCESSFUL
   Receipt #tx_20251208_094740
   Both signatures verified ✓
```

---

## ✨ Features

- 🔐 **Production Trust Directory** - Real agent registration at `trust.amorce.io`
- 🤝 **Multi-Framework** - LangChain (Sarah) + CrewAI (Henri)
- 🔑 **Cryptographic Security** - Ed25519 signatures on all transactions
- 👤 **Human-in-the-Loop** - Interactive approval screens for critical actions
- 🤖 **Claude AI** - Powered by Anthropic's Claude API
- 📊 **Detailed Reasoning** - Market research, profit analysis, risk assessment
- 🎯 **A2A Protocol** - Agent-to-agent communication standard

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Claude API key ([get one here](https://console.anthropic.com/))
- Trust Directory admin key (from Amorce deployment)

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/marketplace-demo.git
cd marketplace-demo

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (from PyPI)
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Run the Demo

**Full theatrical demo (recommended):**
```bash
python demo_production_full.py
```

**Simple version:**
```bash
python demo_production_simple.py
```

**Integration tests:**
```bash
python test_production_integration.py
```

---

## 📋 What Happens

### Step-by-Step Workflow

1. **🔧 Initialize Agents**
   - Sarah (Buyer) registers with Trust Directory
   - Henri (Seller) registers with Trust Directory
   - Both receive unique agent IDs

2. **🔍 Market Research**
   - Sarah analyzes prices across marketplaces
   - Determines fair market value: $500

3. **🌐 Seller Discovery**
   - Sarah queries `trust.amorce.io`
   - Finds Henri (4.8★, 127 sales)
   - Verifies cryptographic signature

4. **💬 Negotiation**
   - Sarah offers $450
   - Henri counter-offers $500
   - Both offers cryptographically signed

5. **⏸️ HITL Approval #1** - Sarah's Payment
   ```
   Agent: Sarah (Buyer)
   Action: Approve payment of $500
   Details:
     • Seller: Henri (4.8★)
     • Item: MacBook Pro 2020
     • Price: $500 (Fair ✓)
     • Fraud Risk: LOW
   [✓ Approve]
   ```

6. **⏸️ HITL Approval #2** - Henri's Sale
   ```
   Agent: Henri (Seller)
   Action: Approve sale to Sarah
   Details:
     • Buyer: Sarah (4.9★)
     • Profit: $150 (43% margin)
     • Risk: LOW
   [✓ Approve]
   ```

7. **📝 Transaction Complete**
   - Signed receipt generated
   - Both signatures verified
   - Transaction recorded

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│     Marketplace Demo (Production)       │
├─────────────────────────────────────────┤
│                                         │
│  ┌────────────┐      ┌──────────────┐ │
│  │   Sarah    │      │    Henri     │ │
│  │ (LangChain)│      │  (CrewAI)    │ │
│  │ + Claude   │      │  + Claude    │ │
│  └─────┬──────┘      └──────┬───────┘ │
│        │                    │         │
│        └────────┬───────────┘         │
│                 │                     │
└─────────────────┼─────────────────────┘
                  │
                  ▼
        ┌─────────────────────┐
        │  trust.amorce.io    │
        │  (Trust Directory)  │
        │                     │
        │  • Agent Registry   │
        │  • Reputation       │
        │  • Discovery        │
        └─────────────────────┘
```

---

## 📦 Production Components

All packages installed from PyPI:

- **[langchain-amorce](https://pypi.org/project/langchain-amorce/)** `>=0.1.0` - LangChain integration
- **[crewai-amorce](https://pypi.org/project/crewai-amorce/)** `>=0.1.0` - CrewAI integration
- **[amorce-sdk](https://pypi.org/project/amorce-sdk/)** `>=0.2.1` - Core SDK
- **[anthropic](https://pypi.org/project/anthropic/)** - Claude API

---

## 🔒 Security

**This demo follows security best practices:**

- ✅ No hardcoded secrets
- ✅ All credentials in `.env` (gitignored)
- ✅ Comprehensive `.gitignore`
- ✅ Security documentation ([SECURITY.md](SECURITY.md))

**See [SECURITY.md](SECURITY.md) for complete security guidelines.**

---

## 🎯 Use Cases

This demo showcases how to build:

- **🛒 AI Marketplaces** - Autonomous buying and selling agents
- **🤝 Agent Negotiation** - Multi-agent price negotiation
- **🔐 Secure Transactions** - Cryptographically signed agreements
- **👥 Multi-Framework Integration** - LangChain + CrewAI working together
- **⚡ Trust-Based Systems** - Reputation and verification

---

## 📁 Repository Structure

```
marketplace-demo/
├── agents/
│   ├── sarah/
│   │   └── buyer_agent.py       # LangChain buyer agent
│   └── henri/
│       └── seller_agent.py      # CrewAI seller agent
├── demo_production_full.py      # Full theatrical demo
├── demo_production_simple.py    # Simplified version
├── demo_standalone.py           # Mock version (no network)
├── test_production_integration.py
├── requirements.txt             # PyPI dependencies
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
├── SECURITY.md                  # Security guidelines
└── README.md                    # This file
```

---

## 🧪 Testing

**Integration Tests:**
```bash
python test_production_integration.py
```

Tests verify:
- ✅ Trust Directory connectivity
- ✅ Agent registration
- ✅ Agent discovery
- ✅ Specific agent retrieval

---

## 🌐 Live Demo

Both agents are registered in the production Trust Directory:

- **Trust Directory:** https://trust.amorce.io
- **API:** https://trust.amorce.io/api/v1/agents
- **Agent Count:** 139+ verified agents

**Verify registration:**
```bash
curl https://trust.amorce.io/api/v1/agents | jq '.count'
```

---

## 📚 Learn More

- **Documentation:** [amorce.io/docs](https://amorce.io/docs)
- **Trust Directory:** [trust.amorce.io](https://trust.amorce.io)
- **Main Repository:** [github.com/amorce/amorce](https://github.com/amorce/amorce)
- **LangChain Integration:** [github.com/amorce/langchain-amorce](https://github.com/amorce/langchain-amorce)
- **CrewAI Integration:** [github.com/amorce/crewai-amorce](https://github.com/amorce/crewai-amorce)

---

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Built with [Amorce](https://amorce.io) - Secure AI agent infrastructure
- Powered by [Claude](https://anthropic.com) - Anthropic's AI assistant
- Integrated with [LangChain](https://langchain.com) and [CrewAI](https://crewai.com)

---

## 📧 Contact

- **Website:** [amorce.io](https://amorce.io)
- **Email:** team@amorce.io
- **Twitter:** [@amorce_ai](https://twitter.com/amorce_ai)

---

<div align="center">
  <p>Made with ❤️ by the Amorce team</p>
  <p>
    <a href="https://amorce.io">Website</a> •
    <a href="https://amorce.io/docs">Docs</a> •
    <a href="https://trust.amorce.io">Trust Directory</a>
  </p>
</div>
