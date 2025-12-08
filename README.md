# AI Agent Marketplace Demo
[![GitHub](https://img.shields.io/github/stars/amorce/agent-marketplace-demo?style=social)](https://github.com/amorce/agent-marketplace-demo)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Demo](https://img.shields.io/badge/demo-live-success.svg)](https://github.com/amorce/agent-marketplace-demo)

---

## 🎯 What This Demo Shows

**Sarah (Buyer Agent)** negotiates with **Henri (Seller Agent)** to purchase a used MacBook Pro for $500, demonstrating:

- ✅ **LangChain + CrewAI Integration** - Multi-framework interoperability
- ✅ **Ed25519 Signatures** - Every message cryptographically signed
- ✅ **HITL Approvals** - Human oversight for payments and sales
- ✅ **Trust Directory** - Agent discovery and reputation
- ✅ **MCP Integration** - Tools for price research and inventory
- ✅ **A2A Protocol** - Compatible message format

---

## 🚀 Quick Start

### Prerequisites

```bash
# Install dependencies
pip install amorce-sdk langchain-amorce crewai-amorce openai
```

### Run the Demo

```bash
# Option 1: One-command demo
docker-compose up

# Option 2: Manual run
python orchestrator/run_demo.py
```

**Demo runs in ~2 minutes** and shows:
1. Sarah searches for MacBook prices
2. Sarah finds Henri in Trust Directory
3. Sarah makes offer ($450)
4. Henri counter-offers ($500)
5. **HITL**: Sarah approves payment
6. **HITL**: Henri approves sale
7. Signed receipt generated

---

## 🏗️ Architecture

```
Sarah (Buyer)              Amorce Protocol              Henri (Seller)
[LangChain + GPT-4]                                     [CrewAI + GPT-4]
       │                                                        │
       ├─► Brave Search (MCP) ────────────────────────►        │
       │   Research market prices                              │
       │                                                        │
       ├─► Trust Directory ────────────────────────────►        │
       │   Find Henri (4.8★ seller)                           │
       │                                                        │
       ├─► Budget Check ───────────────────────────────►        │
       │   Confirm $500 affordable                             │
       │                                                        │
       ├─► Offer: $450 ────────────────────────────────► Inventory DB (MCP)
       │   💳 HITL: Approve offer                       Check stock/condition
       │                                                        │
       │◄──── Counter: $500 ◄────────────────────────────      │
       │   Market analysis                             Pricing API (MCP)
       │                                               Calculate margin
       │                                                        │
       ├─► Accept $500 ────────────────────────────────► 🔐 HITL: Approve
       │   💳 HITL: Approve payment                      sale to Sarah
       │                                                        │
       │◄──── Signed Receipt ◄───────────────────────────      │
       │   Ed25519 signature                           Receipt generator
       └────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
marketplace-demo/
├── README.md                    # This file
├── docker-compose.yml           # One-command setup
├── requirements.txt             # Python dependencies
├── .env.example                 # Configuration template
│
├── agents/
│   ├── sarah/                  # Buyer agent (LangChain)
│   │   ├── buyer_agent.py     # Main agent logic
│   │   ├── tools/             # Sarah's tools
│   │   │   ├── market_research.py
│   │   │   ├── budget_checker.py
│   │   │   └── fraud_detector.py
│   │   └── prompts/
│   │       └── negotiation.txt
│   │
│   └── henri/                  # Seller agent (CrewAI)
│       ├── seller_agent.py    # Main agent logic
│       ├── tools/             # Henri's tools
│       │   ├── inventory.py
│       │   ├── pricing.py
│       │   └── receipt.py
│       └── prompts/
│           └── sales_strategy.txt
│
├── mcp_servers/               # MCP tool servers
│   ├── brave_search/         # Price comparison
│   └── inventory_db/         # Product catalog
│
├── orchestrator/
│   ├── run_demo.py           # Main demo script
│   ├── hitl_ui.py            # Terminal approval UI
│   └── logger.py             # Transaction logging
│
└── docs/
    ├── ARCHITECTURE.md       # Design decisions
    ├── DEMO_SCRIPT.md        # What happens step-by-step
    └── screenshots/          # Demo screenshots
```

---

## 🎬 Demo Flow

### 1. Sarah Starts Research

```
🤖 Sarah: Starting search for MacBook Pro 2020...
🔍 Searching eBay, Craigslist, marketplace...
   
   Market Analysis:
   • eBay: $480-550
   • Craigslist: $450-520
   • Average: $500
   
✅ Market research complete
```

### 2. Sarah Discovers Henri

```
🤖 Sarah: Discovering verified sellers...
🔍 Querying Trust Directory...

   Found 3 sellers:
   1. Henri (agent_abc123) - 4.8★ | 127 sales | $500
   2. Alice (agent_def456) - 4.2★ | 45 sales | $520
   3. Bob (agent_ghi789) - 3.9★ | 12 sales | $480

🤖 Sarah: Selecting Henri (best reputation)
✅ Henri verified in Trust Directory
```

### 3. HITL Approval (Sarah)

```
⏸️  ═══════════════════════════════════════════
    HUMAN APPROVAL REQUIRED
   ═══════════════════════════════════════════
   
   💳 Approve payment of $500?
   
   Seller: Henri (agent_abc123)
   Trust Score: 4.8★ (verified)
   Item: MacBook Pro 2020, 16GB RAM, 512GB SSD
   Condition: Excellent
   Price: $500 (fair market value)
   Warranty: 30 days
   
   [✓ Approve]  [✗ Reject]  [ℹ Request Info]
   ═══════════════════════════════════════════

👤 User: [Approved]
✅ Payment approved by user@example.com
```

### 4. HITL Approval (Henri)

```
⏸️  ═══════════════════════════════════════════
    HUMAN APPROVAL REQUIRED
   ═══════════════════════════════════════════
   
   🔐 Approve sale to Sarah?
   
   Buyer: Sarah (agent_xyz789)
   Trust Score: 4.9★ (verified)
   Item: MacBook Pro 2020 (#INV-12345)
   Offer: $500 (above minimum $480)
   Profit: $150 (43% margin)
   Buyer history: Excellent
   
   [✓ Approve]  [💬 Counter]  [✗ Reject]
   ═══════════════════════════════════════════

👤 Seller: [Approved]
✅ Sale approved by seller@example.com
```

### 5. Transaction Complete

```
✅ TRANSACTION SUCCESSFUL

Receipt #tx_20251207_001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buyer:     Sarah (agent_xyz789)
Seller:    Henri (agent_abc123)
Item:      MacBook Pro 2020
Price:     $500
Warranty:  30 days
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buyer Signature:  ed25519:abc...
Seller Signature: ed25519:def...
Amorce Verified:  ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️  Total time: 2m 15s
```

---

## ⚙️ Configuration

### Environment Variables

Copy `.env.example` to `.env`:

```bash
# OpenAI API Key (required)
OPENAI_API_KEY=sk-...

# Amorce Configuration
AMORCE_DIRECTORY_URL=https://directory.amorce.io
AMORCE_ORCHESTRATOR_URL=https://api.amorce.io

# Agent Settings
SARAH_MAX_BUDGET=500
HENRI_MIN_PRICE=450

# Demo Options
DEMO_AUTO_APPROVE=false  # Set true to skip HITL
DEMO_VERBOSE=true        # Show all agent reasoning
```

---

## 🎥 Recording a Demo Video

```bash
# Install asciinema for terminal recording
brew install asciinema

# Record demo
asciinema rec marketplace_demo.cast

# Run demo
python orchestrator/run_demo.py

# Stop recording (Ctrl+D)

# Convert to GIF
agg marketplace_demo.cast marketplace_demo.gif
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Test individual agents
python -m agents.sarah.buyer_agent --test
python -m agents.henri.seller_agent --test

# Test MCP servers
pytest mcp_servers/tests/
```

---

## 📚 Learn More

- [Amorce Documentation](https://amorce.io/docs)
- [LangChain-Amorce](../langchain-amorce)
- [CrewAI-Amorce](../crewai-amorce)
- [A2A Protocol](https://a2a-protocol.org/)

---

## 🤝 Contributing

Found a bug? Have ideas? Open an issue!

---

## 📄 License

MIT License

---

**Built with ❤️ by the Amorce team to show the future of agent commerce**
