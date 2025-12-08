"""
Standalone Marketplace Demo

Simulates Sarah and Henri without external dependencies.
Shows the complete workflow for demo purposes.
"""

import time
from datetime import datetime


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


def main():
    """Run the complete marketplace demo."""
    
    # Banner
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  🤖 AI AGENT MARKETPLACE DEMO".center(68) + "║")
    print("║" + "  Sarah + Henri Negotiate a MacBook Pro Sale".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝\n")
    
    print("📋 Demo Overview:")
    print("   • Sarah (Buyer) uses LangChain with Amorce security")
    print("   • Henri (Seller) uses CrewAI with Amorce security")
    print("   • Both agents require human approval (HITL)")
    print("   • All transactions cryptographically signed")
    print("   • A2A Protocol compatible\n")
    
    input("Press ENTER to start demo...")
    
    # Initialize agents
    print_header("INITIALIZING AGENTS")
    
    print("Creating Sarah (Buyer Agent)...")
    sarah_id = "agent_sarah_4f8a9b2c"
    print(f"   ✅ Sarah initialized")
    print(f"   Agent ID: {sarah_id}")
    print(f"   Max Budget: $500")
    print(f"   Framework: LangChain + Amorce")
    
    time.sleep(0.5)
    
    print("\nCreating Henri (Seller Agent)...")
    henri_id = "agent_henri_7d3e1a5b"
    print(f"   ✅ Henri initialized")
    print(f"   Agent ID: {henri_id}")
    print(f"   Min Price: $450")
    print(f"   Framework: CrewAI + Amorce")
    
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
    print("🤖 Sarah: Querying Amorce Trust Directory...")
    time.sleep(0.5)
    print("\n   Found 3 verified sellers:")
    print(f"   1. Henri ({henri_id[:20]}...) - 4.8★ | 127 sales | $500")
    print("   2. Alice (agent_alice_9e2c...) - 4.2★ | 45 sales | $520")
    print("   3. Bob (agent_bob_1f7d...) - 3.9★ | 12 sales | $480")
    time.sleep(0.5)
    print("\n🤖 Sarah: Selecting Henri (best reputation)")
    print("   ✅ Henri verified in Trust Directory")
    print("   ✅ Ed25519 signature verified")
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
            'Trust Score': '4.8★ (verified in Trust Directory)',
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
            'Trust Score': '4.9★ (verified in Trust Directory)',
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
    print(f"Protocol: A2A/1.0 + Amorce/3.0")
    print("━" * 70)
    
    time.sleep(1)
    
    # Summary
    print_header("DEMO SUMMARY")
    print("✅ Market research completed (Sarah)")
    print("✅ Seller discovered via Trust Directory")
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
    print("   • Trust Directory queries: 2")
    print("   • MCP tool calls: 5 (market research, inventory, pricing)")
    
    print("\n" + "─" * 70)
    print("🎯 What This Demonstrates:")
    print("   ✓ Multi-framework integration (LangChain + CrewAI)")
    print("   ✓ Cryptographic signatures (Ed25519)")
    print("   ✓ Human-in-the-loop approvals")
    print("   ✓ Trust Directory reputation system")
    print("   ✓ Agent-to-agent negotiation")
    print("   ✓ Secure transaction with receipt")
    print("   ✓ A2A Protocol compatibility")
    
    print("\n🎉 Demo complete! Both agents successfully negotiated a")
    print("   secure, verified transaction with human oversight.\n")


if __name__ == "__main__":
    main()
