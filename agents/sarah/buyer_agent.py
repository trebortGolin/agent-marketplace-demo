"""
Sarah - The Smart Shopper (Buyer Agent)

Uses LangChain with Amorce security to find and negotiate
the best deal on a MacBook Pro.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

from langchain_amorce import AmorceAgent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from typing import Dict, Any


class SarahBuyerAgent:
    """
    Sarah - Autonomous buyer agent powered by LangChain.
    
    Goals:
    - Find MacBook Pro 2020 under $500
    - Verify seller reputation
    - Negotiate best price
    - Get human approval before payment
    """
    
    def __init__(self, max_budget: int = 500):
        """
        Initialize Sarah.
        
        Args:
            max_budget: Maximum budget in USD
        """
        self.max_budget = max_budget
        
        # Create tools
        self.tools = self._create_tools()
        
        # Create LangChain agent with Amorce security
        self.agent = AmorceAgent(
            name="Sarah",
            role="Smart Shopper",
            llm=ChatOpenAI(model="gpt-4", temperature=0.7),
            tools=self.tools,
            hitl_required=['make_payment', 'share_address'],
            max_budget=max_budget,
            secure=True,
            verbose=True
        )
        
        print(f"🤖 Sarah initialized")
        print(f"   Agent ID: {self.agent.agent_id}")
        print(f"   Max Budget: ${max_budget}")
        print(f"   HITL required for: payment, sharing address")
    
    def _create_tools(self):
        """Create Sarah's tools."""
        
        # Market research tool (simulated Brave Search)
        def search_market_prices(product: str) -> Dict[str, Any]:
            """Search market for product prices."""
            print(f"\n🔍 Searching market for: {product}")
            # Simulated results
            return {
                'ebay': {'min': 480, 'max': 550, 'avg': 515},
                'craigslist': {'min': 450, 'max': 520, 'avg': 485},
                'facebook': {'min': 470, 'max': 530, 'avg': 500},
                'recommended_price': 500,
                'fair_deal_threshold': 520
            }
        
        # Budget checker
        def check_budget(price: float) -> bool:
            """Check if price is within budget."""
            affordable = price <= self.max_budget
            print(f"\n💰 Budget check: ${price}")
            print(f"   Max budget: ${self.max_budget}")
            print(f"   Affordable: {'✅ Yes' if affordable else '❌ No'}")
            return affordable
        
        # Fraud detector (checks Trust Directory)
        def check_seller_reputation(seller_id: str) -> Dict[str, Any]:
            """Check seller's reputation in Trust Directory."""
            print(f"\n🔍 Checking reputation for: {seller_id}")
            # Simulated Trust Directory lookup
            return {
                'agent_id': seller_id,
                'trust_score': 4.8,
                'total_sales': 127,
                'verified': True,
                'fraud_risk': 'low',
                'recommendation': 'safe to transact'
            }
        
        return [
            Tool(
                name="search_market_prices",
                description="Search eBay, Craigslist, and other marketplaces for prices",
                func=search_market_prices
            ),
            Tool(
                name="check_budget",
                description="Check if a price is within budget",
                func=check_budget
            ),
            Tool(
                name="check_seller_reputation",
                description="Verify seller's reputation and trustworthiness",
                func=check_seller_reputation
            )
        ]
    
    def find_product(self, product: str) -> Dict[str, Any]:
        """
        Find product and research prices.
        
        Args:
            product: Product to search for
            
        Returns:
            Market research data
        """
        print(f"\n{'='*50}")
        print(f"🤖 Sarah: Starting search for {product}")
        print(f"{'='*50}\n")
        
        query = f"Search the market for '{product}' and tell me the price range"
        result = self.agent.run(query)
        
        return result
    
    def discover_sellers(self, min_rating: float = 4.5) -> list:
        """
        Discover verified sellers in Trust Directory.
        
        Args:
            min_rating: Minimum trust score required
            
        Returns:
            List of verified sellers
        """
        print(f"\n{'='*50}")
        print(f"🤖 Sarah: Discovering sellers (min rating: {min_rating}★)")
        print(f"{'='*50}\n")
        
        # Query Trust Directory through Amorce client
        sellers = self.agent.discover_agents(capability='sell_electronics')
        
        # Filter by rating
        qualified = [s for s in sellers if s.get('trust_score', 0) >= min_rating]
        
        print(f"\n   Found {len(qualified)} qualified sellers:")
        for i, seller in enumerate(qualified, 1):
            print(f"   {i}. {seller['name']} - {seller['trust_score']}★ | ${seller.get('price', 'N/A')}")
        
        return qualified
    
    def negotiate(self, seller: Dict[str, Any], target_price: float):
        """
        Negotiate with seller.
        
        Args:
            seller: Seller information
            target_price: Target price to negotiate to
        """
        print(f"\n{'='*50}")
        print(f"🤖 Sarah: Negotiating with {seller['name']}")
        print(f"   Target price: ${target_price}")
        print(f"{'='*50}\n")
        
        # This would use agent.negotiate_with() in full implementation
        print(f"   Making initial offer: ${target_price - 50}")
        print(f"   Waiting for counter-offer...")


def main():
    """Run Sarah demo."""
    print("\n" + "="*60)
    print("  SARAH - THE SMART SHOPPER (Buyer Agent)")
    print("  Powered by LangChain + Amorce")
    print("="*60 + "\n")
    
    # Create Sarah
    sarah = SarahBuyerAgent(max_budget=500)
    
    # Demo workflow
    print("\n--- DEMO WORKFLOW ---\n")
    
    # 1. Find product
    sarah.find_product("MacBook Pro 2020")
    
    # 2. Discover sellers
    sellers = sarah.discover_sellers(min_rating=4.5)
    
    # 3. Negotiate (if sellers found)
    if sellers:
        sarah.negotiate(sellers[0], target_price=500)
    
    print("\n" + "="*60)
    print("  DEMO COMPLETE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
