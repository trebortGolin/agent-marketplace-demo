"""
Main Demo Orchestrator

Coordinates Sarah and Henri in the marketplace demo.
"""

import os
import sys
import time
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from agents.sarah.buyer_agent import SarahBuyerAgent
from agents.henri.seller_agent import HenriSellerAgent


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
    time.sleep(2)
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
    sarah = SarahBuyerAgent(max_budget=500)
    
    print("\nCreating Henri (Seller Agent)...")
    henri = HenriSellerAgent(min_price=450)
    
    time.sleep(1)
    
    # Step 1: Sarah researches market
    print_step(1, "Sarah researches MacBook Pro prices")
    sarah.find_product("MacBook Pro 2020")
    time.sleep(1)
    
    # Step 2: Sarah discovers Henri
    print_step(2, "Sarah discovers verified sellers")
    sellers = sarah.discover_sellers(min_rating=4.5)
    time.sleep(1)
    
    # Step 3: Sarah makes offer
    print_step(3, "Sarah makes initial offer")
    print("🤖 Sarah: Making offer of $450 to Henri")
    time.sleep(1)
    
    # Step 4: Henri evaluates offer
    print_step(4, "Henri evaluates Sarah's offer")
    offer_response = henri.receive_offer(
        buyer_id=sarah.agent.agent_id,
        offer_price=450
    )
    time.sleep(1)
    
    # Step 5: Henri counter-offers
    print_step(5, "Henri makes counter-offer")
    counter = henri.make_counter_offer(
        price=500,
        reasoning="Fair market value for excellent condition MacBook"
    )
    time.sleep(1)
    
    # Step 6: Sarah's HITL Approval
    print_step(6, "Sarah requests human approval for payment")
    simulate_hitl_approval(
        agent_name="Sarah (Buyer)",
        action="Approve payment of $500",
        details={
            'Seller': f"Henri ({henri.agent.agent_id[:20]}...)",
            'Trust Score': '4.8★ (verified)',
            'Item': 'MacBook Pro 2020, 16GB RAM, 512GB SSD',
            'Price': '$500',
            'Market Value': '$480-$550',
            'Verdict': 'FAIR DEAL ✓'
        }
    )
    time.sleep(1)
    
    # Step 7: Henri's HITL Approval
    print_step(7, "Henri requests human approval for sale")
    simulate_hitl_approval(
        agent_name="Henri (Seller)",
        action="Approve sale to Sarah",
        details={
            'Buyer': f"Sarah ({sarah.agent.agent_id[:20]}...)",
            'Trust Score': '4.9★ (verified)',
            'Sale Price': '$500',
            'Cost Basis': '$350',
            'Profit': '$150 (43%)',
            'Verdict': 'PROFITABLE ✓'
        }
    )
    time.sleep(1)
    
    # Step 8: Transaction complete
    print_step(8, "Generating signed receipt")
    receipt = henri.agent.generate_signed_receipt()
    
    print("\n✅ TRANSACTION SUCCESSFUL\n")
    print("Receipt #tx_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
    print("━" * 70)
    print(f"Buyer:     Sarah ({sarah.agent.agent_id[:30]}...)")
    print(f"Seller:    Henri ({henri.agent.agent_id[:30]}...)")
    print(f"Item:      MacBook Pro 2020")
    print(f"Price:     $500")
    print(f"Warranty:  30 days")
    print("━" * 70)
    print(f"Buyer Signature:  {sarah.agent.identity.sign('receipt')[:40]}...")
    print(f"Seller Signature: {receipt['signature'][:40]}...")
    print(f"Amorce Verified:  ✓")
    print("━" * 70)
    
    # Summary
    print_header("DEMO SUMMARY")
    print("✅ Market research completed (Sarah)")
    print("✅ Seller discovered via Trust Directory")
    print("✅ Reputation verified (4.8★)")
    print("✅ Negotiation completed ($450 → $500)")
    print("✅ Human approval obtained (both sides)")
    print("✅ Transaction signed and verified")
    print("✅ Receipt generated")
    
    print("\n🎉 Demo complete! Both agents successfully negotiated a")
    print("   secure, verified transaction with human oversight.\n")


if __name__ == "__main__":
    main()
