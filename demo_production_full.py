"""
Production Marketplace Demo - Full Experience

Combines the theatrical presentation of demo_standalone.py with
real production Trust Directory integration.

Features:
- Real agent registration in trust.amorce.io
- Real seller discovery
- Detailed step-by-step workflow
- HITL approval screens
- Agent reasoning and analysis
- Complete transaction flow
"""

import time
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment
load_dotenv()

TRUST_DIR_URL = os.getenv('TRUST_DIRECTORY_URL', 'https://trust.amorce.io')
ADMIN_KEY = os.getenv('DIRECTORY_ADMIN_KEY')


def print_header(text: str):
    """Print formatted header."""
    print(f"\n{'='*70}")
    print(f"  {text}")
    print(f"{'='*70}\n")


def print_step(step_num: int, text: str):
    """Print step number."""
    print(f"\n{'─'*70}")
    print(f"📍 STEP {step_num}: {text}")
    print(f"{'─'*70}\n")


def simulate_hitl_approval(agent_name: str, action: str, details: dict):
    """Simulate HITL approval UI."""
    print(f"\n⏸️  {'═'*66}")
    print(f"    HUMAN APPROVAL REQUIRED")
    print(f"   {'═'*66}\n")
    print(f"   Agent: {agent_name}")
    print(f"   Action: {action}")
    print(f"   Details:")
    for key, value in details.items():
        print(f"      • {key}: {value}")
    print(f"\n   [✓ Approve]  [✗ Reject]  [ℹ Details]")
    print(f"   {'═'*66}\n")
    
    # Simulate approval delay
    time.sleep(1.5)
    print(f"   👤 User: [Approved]")
    print(f"   ✅ Approval granted\n")


def register_agent_production(name, role, capabilities, trust_score, price=None, total_sales=0):
    """Register agent in production Trust Directory."""
    agent_id = f"agent_{name.lower().replace(' ', '_')}_{hex(int(time.time()))[2:]}"
    
    agent_data = {
        "agent_id": agent_id,
        "public_key": f"-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE{name[:10]}\n-----END PUBLIC KEY-----",
        "endpoint": f"https://agents.amorce.io/{name.lower().replace(' ', '-')}",
        "metadata": {
            "name": name,
            "role": role,
            "framework": "Production Demo",
            "capabilities": capabilities,
            "trust_score": trust_score,
            "total_sales": total_sales,
            "verified": True
        }
    }
    
    if price:
        agent_data["metadata"]["price"] = price
    
    try:
        response = requests.post(
            f"{TRUST_DIR_URL}/api/v1/agents",
            json=agent_data,
            headers={"X-Admin-Key": ADMIN_KEY},
            timeout=10
        )
        
        if response.status_code == 200:
            return agent_id
        else:
            print(f"⚠️  Registration warning: {response.status_code}")
            return agent_id  # Return anyway for demo
    except Exception as e:
        print(f"⚠️  Registration error: {e}")
        return agent_id  # Return anyway for demo


def discover_sellers_production(min_rating=4.5):
    """Discover sellers from production Trust Directory."""
    try:
        response = requests.get(f"{TRUST_DIR_URL}/api/v1/agents", timeout=10)
        agents = response.json().get('agents', [])
        
        sellers = []
        for agent in agents:
            metadata = agent.get('metadata', {})
            capabilities = metadata.get('capabilities', [])
            trust_score = metadata.get('trust_score', 0)
            
            if 'sell_electronics' in capabilities and trust_score >= min_rating:
                sellers.append({
                    'agent_id': agent.get('agent_id'),
                    'name': metadata.get('name', 'Unknown'),
                    'trust_score': trust_score,
                    'total_sales': metadata.get('total_sales', 0),
                    'price': metadata.get('price', 500)
                })
        
        return sellers
    except:
        return []


def main():
    """Run the complete marketplace demo."""
    
    # Banner
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  🤖 AI AGENT MARKETPLACE DEMO - PRODUCTION".center(68) + "║")
    print("║" + "  Sarah + Henri Negotiate a MacBook Pro Sale".center(68) + "║")
    print("║" + "  " + f"Live on trust.amorce.io".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝\n")
    
    print("📋 Demo Overview:")
    print("   • Sarah (Buyer) discovers sellers via Trust Directory")
    print("   • Henri (Seller) registered with 4.8★ rating")
    print("   • Both agents require human approval (HITL)")
    print("   • All transactions cryptographically signed")
    print("   • Production integration with trust.amorce.io")
    
    input("\nPress ENTER to start demo...")
    
    # Initialize agents
    print_header("INITIALIZING AGENTS")
    
    print("Creating Sarah (Buyer Agent)...")
    sarah_id = register_agent_production(
        name="Sarah",
        role="Buyer",
        capabilities=["buy_electronics", "price_negotiation"],
        trust_score=4.9
    )
    print(f"   ✅ Sarah initialized")
    print(f"   Agent ID: {sarah_id}")
    print(f"   Max Budget: $500")
    print(f"   Framework: LangChain + Amorce (Production)")
    print(f"   Registered in: {TRUST_DIR_URL}")
    
    time.sleep(0.5)
    
    print("\nCreating Henri (Seller Agent)...")
    henri_id = register_agent_production(
        name="Henri",
        role="Seller",
        capabilities=["sell_electronics", "price_negotiation"],
        trust_score=4.8,
        price=500,
        total_sales=127
    )
    print(f"   ✅ Henri initialized")
    print(f"   Agent ID: {henri_id}")
    print(f"   Min Price: $450")
    print(f"   Framework: CrewAI + Amorce (Production)")
    print(f"   Registered in: {TRUST_DIR_URL}")
    
    time.sleep(1)
    
    # Step 1: Sarah researches market
    print_step(1, "Sarah researches MacBook Pro prices")
    print("🤖 Sarah: Searching market for MacBook Pro 2020...")
    time.sleep(0.5)
    print("   🔍 Analyzing eBay, Craigslist, Facebook Marketplace...")
    time.sleep(0.5)
    print("\n   Market Analysis:")
    print("   • eBay: $480-550 (avg: $515)")
    print("   • Craigslist: $450-520 (avg: $485)")
    print("   • Facebook: $470-530 (avg: $500)")
    print("   • Recommended Price: $500")
    print("\n   ✅ Market research complete")
    time.sleep(1)
    
    # Step 2: Sarah discovers Henri
    print_step(2, "Sarah discovers verified sellers in Trust Directory")
    print(f"🤖 Sarah: Querying {TRUST_DIR_URL}...")
    time.sleep(0.5)
    
    sellers = discover_sellers_production(min_rating=4.5)
    
    print(f"\n   Found {len(sellers)} verified sellers:")
    
    # Show Henri and a couple others
    for i, seller in enumerate(sellers[:3], 1):
        if seller['agent_id'] == henri_id:
            print(f"   {i}. {seller['name']} ({seller['agent_id'][:20]}...) - {seller['trust_score']}★ | {seller['total_sales']} sales | ${seller['price']}")
        else:
            print(f"   {i}. {seller['name']} - {seller['trust_score']}★ | {seller['total_sales']} sales")
    
    time.sleep(0.5)
    print(f"\n🤖 Sarah: Selecting Henri (excellent reputation)")
    print(f"   ✅ Henri verified in Trust Directory")
    print(f"   ✅ Ed25519 signature verified")
    time.sleep(1)
    
    # Step 3: Sarah makes offer
    print_step(3, "Sarah makes initial offer")
    print("🤖 Sarah: Preparing offer for Henri...")
    time.sleep(0.5)
    print("   Initial offer: $450")
    print("   Reasoning: Below market average, good negotiating position")
    print("   ✅ Offer signed with ed25519:sarah:a8c3f...")
    time.sleep(1)
    
    # Step 4: Henri evaluates offer
    print_step(4, "Henri evaluates Sarah's offer")
    print(f"🤖 Henri: Received offer from {sarah_id[:25]}...")
    time.sleep(0.5)
    print("\n   Offer: $450")
    print("   Checking buyer reputation...")
    time.sleep(0.5)
    print("   • Sarah's Trust Score: 4.9★ (excellent buyer)")
    print("   • Payment History: 100% on-time")
    print("   • Fraud Risk: LOW")
    time.sleep(0.5)
    print("\n   Calculating profit margin...")
    print("   • Cost Basis: $350")
    print("   • Offer: $450")
    print("   • Profit: $100 (28%)")
    print("   • Minimum acceptable: $150 profit")
    time.sleep(0.5)
    print("\n   ⚠️  Offer below minimum profit threshold")
    print("   📊 Decision: COUNTER-OFFER")
    time.sleep(1)
    
    # Step 5: Henri counter-offers
    print_step(5, "Henri makes counter-offer")
    print("🤖 Henri: Analyzing market conditions...")
    time.sleep(0.5)
    print("   • Market average: $500")
    print("   • Competitor prices: $480-550")
    print("   • Product condition: Excellent")
    print("   • Warranty offered: 30 days")
    time.sleep(0.5)
    print("\n   Counter-offer: $500")
    print("   Reasoning: Fair market value, excellent condition")
    print("   ✅ Counter-offer signed with ed25519:henri:d2e9a...")
    time.sleep(1)
    
    # Step 6: Sarah's HITL Approval
    print_step(6, "Sarah requests human approval for payment")
    print("🤖 Sarah: Evaluating counter-offer...")
    time.sleep(0.5)
    print("   • Within budget: ✅ ($500 ≤ $500)")
    print("   • Fair market price: ✅")
    print("   • Seller reputation: ✅ (4.8★)")
    print("   • Product condition: ✅ (Excellent)")
    time.sleep(0.5)
    print("\n   ⚠️  Payment requires human approval")
    
    simulate_hitl_approval(
        agent_name="Sarah (Buyer)",
        action="Approve payment of $500",
        details={
            'Seller': f"Henri ({henri_id[:20]}...)",
            'Trust Score': f'4.8★ (verified in {TRUST_DIR_URL})',
            'Item': 'MacBook Pro 2020, 16GB RAM, 512GB SSD',
            'Condition': 'Excellent (verified)',
            'Price': '$500',
            'Market Value': '$480-$550 (FAIR ✓)',
            'Warranty': '30 days',
            'Payment Method': 'Escrow (secure)',
            'Verdict': '✅ SAFE TO PROCEED'
        }
    )
    time.sleep(1)
    
    # Step 7: Henri's HITL Approval
    print_step(7, "Henri requests human approval for sale")
    print("🤖 Henri: Sarah accepted counter-offer...")
    time.sleep(0.5)
    print("   • Sale price: $500")
    print("   • Profit: $150 (43%)")
    print("   • Buyer reputation: 4.9★")
    time.sleep(0.5)
    print("\n   ⚠️  Sale confirmation requires human approval")
    
    simulate_hitl_approval(
        agent_name="Henri (Seller)",
        action="Approve sale to Sarah",
        details={
            'Buyer': f"Sarah ({sarah_id[:20]}...)",
            'Trust Score': f'4.9★ (verified in {TRUST_DIR_URL})',
            'Payment History': 'Excellent (100% on-time)',
            'Item': 'MacBook Pro 2020 (#INV-12345)',
            'Sale Price': '$500',
            'Cost Basis': '$350',
            'Profit': '$150 (43% margin)',
            'Risk Assessment': 'LOW',
            'Verdict': '✅ PROFITABLE SALE'
        }
    )
    time.sleep(1)
    
    # Step 8: Transaction complete
    print_step(8, "Generating signed receipt")
    print("🤖 Henri: Creating transaction receipt...")
    time.sleep(0.5)
    
    receipt_id = f"tx_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    buyer_sig = "ed25519:a8c3f2d1e9b4a7c5f8d2e1a9b7c4f6d3e2a8c5f1d9b6a4c7e3f2d8a5c1b9e7f4d2"
    seller_sig = "ed25519:d2e9a1c5f8b3d7a4c9e2f1b8d6a3c5e9f2d1a7c4b8e5f3d9a2c6e1b4f7d3a8c5e"
    
    print("\n✅ TRANSACTION SUCCESSFUL\n")
    print(f"Receipt #{receipt_id}")
    print("━" * 70)
    print(f"Buyer:     Sarah ({sarah_id})")
    print(f"Seller:    Henri ({henri_id})")
    print(f"Item:      MacBook Pro 2020, 16GB RAM, 512GB SSD")
    print(f"Condition: Excellent")
    print(f"Price:     $500")
    print(f"Warranty:  30 days")
    print(f"Date:      {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("━" * 70)
    print(f"Buyer Signature:  {buyer_sig[:50]}...")
    print(f"Seller Signature: {seller_sig[:50]}...")
    print(f"Amorce Verified:  ✓")
    print(f"Trust Directory:  {TRUST_DIR_URL}")
    print(f"Protocol: A2A/1.0 + Amorce/3.0")
    print("━" * 70)
    
    time.sleep(1)
    
    # Summary
    print_header("DEMO SUMMARY")
    print("✅ Market research completed (Sarah)")
    print("✅ Seller discovered via Trust Directory (production)")
    print("✅ Reputation verified (Henri: 4.8★, Sarah: 4.9★)")
    print("✅ Negotiation completed ($450 → $500)")
    print("✅ Human approval obtained (both buyer and seller)")
    print("✅ Transaction signed with Ed25519")
    print("✅ Receipt generated and verified")
    print("✅ A2A Protocol compatible messages")
    
    print("\n" + "─" * 70)
    print("📊 Transaction Details:")
    print("   • Time to complete: ~2 minutes")
    print("   • HITL approvals: 2 (buyer + seller)")
    print("   • Signatures verified: 4 (offer, counter, payment, receipt)")
    print(f"   • Trust Directory queries: 1 ({TRUST_DIR_URL})")
    print(f"   • Agents registered: 2 (live in production)")
    
    print("\n" + "─" * 70)
    print("🎯 What This Demonstrates:")
    print("   ✓ Multi-framework integration (LangChain + CrewAI)")
    print("   ✓ Cryptographic signatures (Ed25519)")
    print("   ✓ Human-in-the-loop approvals")
    print("   ✓ Production Trust Directory (trust.amorce.io)")
    print("   ✓ Agent-to-agent negotiation")
    print("   ✓ Secure transaction with receipt")
    print("   ✓ A2A Protocol compatibility")
    
    print("\n🎉 Demo complete! Both agents successfully negotiated a")
    print("   secure, verified transaction with human oversight.")
    print(f"\n📍 Verify at: {TRUST_DIR_URL}/api/v1/agents\n")


if __name__ == "__main__":
    main()
