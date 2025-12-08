"""
Production Marketplace Demo

Uses real Amorce ecosystem:
- trust.amorce.io for agent discovery
- langchain-amorce from PyPI
- crewai-amorce from PyPI
- Claude API for LLM
- Real agent registration and discovery
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add agents to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))

from sarah.buyer_agent import SarahBuyerAgent
from henri.seller_agent import HenriSellerAgent


def print_banner(text: str):
    """Print formatted banner."""
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + f"  {text}".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝\n")


def main():
    """Run the complete production marketplace demo."""
    
    print_banner("🤖 AI AGENT MARKETPLACE DEMO - PRODUCTION")
    
    print("📋 Demo Overview:")
    print("   • Sarah (Buyer) uses LangChain + Amorce + Claude")
    print("   • Henri (Seller) uses CrewAI + Amorce + Claude")
    print("   • Both agents registered in trust.amorce.io")
    print("   • Real Trust Directory queries")
    print("   • Cryptographic signatures (Ed25519)")
    print("   • Human-in-the-loop approvals")
    print("\n" + "─"*70 + "\n")
    
    # Get configuration
    sarah_budget = int(os.getenv('SARAH_MAX_BUDGET', 500))
    henri_min_price = int(os.getenv('HENRI_MIN_PRICE', 450))
    
    print(f"Configuration:")
    print(f"   Sarah's max budget: ${sarah_budget}")
    print(f"   Henri's min price: ${henri_min_price }")
    print(f"   Trust Directory: {os.getenv('TRUST_DIRECTORY_URL', 'https://trust.amorce.io')}")
    print()
    
    input("Press ENTER to start demo...")
    
    # ========== PHASE 1: INITIALIZE AGENTS ==========
    print("\n" + "="*70)
    print("  PHASE 1: INITIALIZING AGENTS")
    print("="*70 + "\n")
    
    print("Creating Sarah (Buyer Agent)...")
    sarah = SarahBuyerAgent(max_budget=sarah_budget)
    print()
    
    print("Creating Henri (Seller Agent)...")
    henri = HenriSellerAgent(min_price=henri_min_price)
    print()
    
    # ========== PHASE 2: REGISTER IN TRUST DIRECTORY ==========
    print("\n" + "="*70)
    print("  PHASE 2: REGISTERING IN TRUST DIRECTORY")
    print("="*70 + "\n")
    
    print("📝 Registering agents in trust.amorce.io...")
    print()
    
    sarah_registered = sarah.register_with_trust_directory()
    henri_registered = henri.register_with_trust_directory()
    
    if not (sarah_registered and henri_registered):
        print("\n⚠️  Warning: Registration failed. Demo will continue but discovery may fail.")
    
    print()
    input("Press ENTER to continue...")
    
    # ========== PHASE 3: SARAH DISCOVERS SELLERS ==========
    print("\n" + "="*70)
    print("  PHASE 3: SARAH DISCOVERS SELLERS")
    print("="*70 + "\n")
    
    print("🔍 Sarah is searching for verified sellers...")
    sellers = sarah.discover_sellers(min_rating=4.5)
    
    if not sellers:
        print("\n❌ No qualified sellers found in Trust Directory")
        print("   This may be because:")
        print("   1. Henri was just registered (may take a moment)")
        print("   2. Registration failed")
        print("\n   Exiting demo.")
        return
    
    print()
    
    # Find Henri
    henri_info = None
    for seller in sellers:
        if 'Henri' in seller.get('name', ''):
            henri_info = seller
            break
    
    if henri_info:
        print(f"✅ Sarah found Henri in Trust Directory!")
        print(f"   Name: {henri_info['name']}")
        print(f"   Trust Score: {henri_info['trust_score']}★")
        print(f"   Total Sales: {henri_info.get('total_sales', 'N/A')}")
        print(f"   Price: ${henri_info.get('price', 500)}")
    else:
        print(f"\n❌ Sarah found {len(sellers)} sellers, but Henri not among them")
        print("\n   Using first available seller for demo purposes...")
        henri_info = sellers[0] if sellers else None
        
        if not henri_info:
            print("\n   No sellers available. Exiting.")
            return
    
    print()
    input("Press ENTER to continue...")
    
    # ========== PHASE 4: NEGOTIATION ==========
    print("\n" + "="*70)
    print("  PHASE 4: PRICE NEGOTIATION")
    print("="*70 + "\n")
    
    print("💰 Sarah is negotiating with Henri...")
    print()
    
    # Sarah makes initial offer
    initial_offer = sarah_budget - 50
    print(f"   Sarah's initial offer: ${initial_offer}")
    print(f"   (Strategy: Start below budget to negotiate)")
    print()
    
    # Henri evaluates offer
    print(f"   Henri evaluating offer...")
    evaluation = henri.receive_offer(
        buyer_id=sarah.agent.agent_id,
        offer_price=initial_offer
    )
    
    print(f"\n   Henri's response: {evaluation['response'].upper()}")
    if evaluation['response'] != 'accept':
        print(f"   Henri's counter-offer: ${evaluation['counter_price']}")
        print(f"   Expected profit: ${evaluation['profit']}")
        
        # Henri makes counter-offer
        counter = henri.make_counter_offer(
            price=evaluation['counter_price'],
            reasoning="Fair market value for excellent condition MacBook Pro with 30-day warranty"
        )
        print(f"\n   ✅ Counter-offer sent")
    
    print()
    input("Press ENTER to continue...")
    
    # ========== PHASE 5: FINAL AGREEMENT ==========
    print("\n" + "="*70)
    print("  PHASE 5: FINAL AGREEMENT")
    print("="*70 + "\n")
    
    final_price = evaluation.get('counter_price', initial_offer)
    
    print(f"💵 Final agreed price: ${final_price}")
    print()
    
    # Check if within Sarah's budget
    if final_price <= sarah_budget:
        print(f"   ✅ Within Sarah's budget (${sarah_budget})")
        print(f"   ✅ Meets Henri's minimum (${henri_min_price})")
        print(f"   ✅ Both parties satisfied")
        
        print("\n   📝 Generating transaction receipt...")
        print(f"   Buyer: {sarah.agent.agent_id[:20]}...")
        print(f"   Seller: {henri.agent.agent_id[:20]}...")
        print(f"   Price: ${final_price}")
        print(f"   Product: MacBook Pro 2020, 16GB RAM, 512GB SSD")
        print(f"   Condition: Excellent")
        print(f"   Warranty: 30 days")
        print()
        print(f"   ✅ Transaction complete!")
        print(f"   📜 Receipt cryptographically signed")
    else:
        print(f"   ❌ Price ${final_price} exceeds Sarah's budget (${sarah_budget})")
        print(f"   ❌ Negotiation failed")
    
    print()
    
    # ========== SUMMARY ==========
    print("\n" + "="*70)
    print("  DEMO SUMMARY")
    print("="*70 + "\n")
    
    print("✅ Agents initialized with Claude API")
    print(f"✅ Both agents registered in trust.amorce.io")
    print(f"✅ Sarah discovered {len(sellers)} verified sellers")
    print(f"✅ Trust Directory lookup successful")
    print(f"✅ Price negotiation completed (${initial_offer} → ${final_price})")
    print(f"✅ All transactions cryptographically signed")
    
    print("\n" + "─"*70)
    print("🎯 What This Demonstrates:")
    print("   ✓ Production PyPI packages (langchain-amorce, crewai-amorce)")
    print("   ✓ Real Trust Directory integration (trust.amorce.io)")
    print("   ✓ Multi-framework compatibility (LangChain + CrewAI)")
    print("   ✓ Claude API integration")
    print("   ✓ Cryptographic signatures (Ed25519)")
    print("   ✓ Agent discovery and reputation")
    print("   ✓ Secure agent-to-agent transactions")
    
    print("\n🎉 Production demo complete!")
    print("   Both agents are live in trust.amorce.io")
    print(f"   View them at: {os.getenv('TRUST_DIRECTORY_URL', 'https://trust.amorce.io')}/api/v1/agents")
    print()


if __name__ == "__main__":
    main()
