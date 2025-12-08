"""
Henri - The Professional Reseller (Seller Agent)

Uses CrewAI with Amorce security to manage inventory
and negotiate sales while maintaining 4.8★ reputation.

PRODUCTION VERSION - Uses PyPI packages and real Trust Directory.
"""

import os
import requests
from crewai_amorce import SecureAgent
from crewai import Tool
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
TRUST_DIR_URL = os.getenv('TRUST_DIRECTORY_URL', 'https://trust.amorce.io')
DIRECTORY_ADMIN_KEY = os.getenv('DIRECTORY_ADMIN_KEY')


class HenriSellerAgent:
    """
    Henri - Autonomous seller agent powered by CrewAI + Amorce.
    
    Goals:
    - Maximize profit on each sale
    - Maintain 4.8★ trust rating
    - Provide excellent customer service
    - Get human approval for major sales
    """
    
    def __init__(self, min_price: int = 450):
        """
        Initialize Henri.
        
        Args:
            min_price: Minimum acceptable price in USD
        """
        self.min_price = min_price
        self.cost_basis = 350  # What Henri paid for the MacBook
        
        # Create tools
        self.tools = self._create_tools()
        
        # Create CrewAI agent with Amorce security + Claude
        # Note: CrewAI uses environment ANTHROPIC_API_KEY by default
        self.agent = SecureAgent(
            role="Electronics Reseller",
            goal="Maximize profit while maintaining 4.8★ rating",
            backstory="Professional refurbisher with 127+ sales. Known for quality products and fair pricing.",
            tools=self.tools,
            hitl_required=['confirm_sale', 'issue_refund'],
            verbose=True,
            llm_model="claude-3-5-sonnet-20241022",
            trust_directory_url=TRUST_DIR_URL
        )
        
        print(f"🤖 Henri initialized")
        print(f"   Agent ID: {self.agent.agent_id}")
        print(f"   Min Price: ${min_price}")
        print(f"   Cost Basis: ${self.cost_basis}")
        print(f"   Trust Directory: {TRUST_DIR_URL}")
        print(f"   HITL required for: sales, refunds")
    
    def _create_tools(self):
        """Create Henri's tools."""
        
        # Inventory database
        def check_inventory(product_id: str) -> Dict[str, Any]:
            """Check product availability and condition."""
            print(f"\n📦 Checking inventory for: {product_id}")
            return {
                'product_id': product_id,
                'name': 'MacBook Pro 2020',
                'specs': '16GB RAM, 512GB SSD',
                'condition': 'Excellent',
                'in_stock': True,
                'cost_basis': self.cost_basis,
                'photos': ['photo1.jpg', 'photo2.jpg'],
                'warranty': '30 days'
            }
        
        # Pricing API
        def get_market_pricing(product: str) -> Dict[str, Any]:
            """Get real-time market pricing."""
            print(f"\n💹 Getting market pricing for: {product}")
            return {
                'current_market': 515,
                'competitor_prices': [480, 500, 520, 550],
                'recommended_price': 500,
                'price_trend': 'stable'
            }
        
        # Profit calculator
        def calculate_profit(sale_price: float) -> Dict[str, Any]:
            """Calculate profit margin."""
            profit = sale_price - self.cost_basis
            margin = (profit / sale_price) * 100
            
            print(f"\n💰 Profit Analysis:")
            print(f"   Sale Price: ${sale_price}")
            print(f"   Cost Basis: ${self.cost_basis}")
            print(f"   Profit: ${profit} ({margin:.1f}%)")
            
            return {
                'sale_price': sale_price,
                'cost_basis': self.cost_basis,
                'profit': profit,
                'margin_percent': margin,
                'acceptable': profit >= 100  # Minimum $100 profit
            }
        
        return [
            Tool(
                name="check_inventory",
                description="Check inventory for product availability and condition",
                func=check_inventory
            ),
            Tool(
                name="get_market_pricing",
                description="Get real-time market pricing data",
                func=get_market_pricing
            ),
            Tool(
                name="calculate_profit",
                description="Calculate profit margin for a sale price",
                func=calculate_profit
            )
        ]
    
    def register_with_trust_directory(self):
        """Register Henri in the production Trust Directory."""
        if not DIRECTORY_ADMIN_KEY:
            print("⚠️  DIRECTORY_ADMIN_KEY not set - skipping registration")
            return False
        
        try:
            registration_data = {
                "agent_id": self.agent.agent_id,
                "public_key": self.agent.get_public_key(),
                "endpoint": "http://localhost:8002/agent/henri",
                "metadata": {
                    "name": "Henri - Professional Reseller",
                    "role": "Seller",
                    "framework": "CrewAI",
                    "capabilities": ["sell_electronics", "price_negotiation", "inventory_management"],
                    "trust_score": 4.8,
                    "total_sales": 127,
                    "verified": True,
                    "price": 500,
                    "product": "MacBook Pro 2020"
                }
            }
            
            response = requests.post(
                f"{TRUST_DIR_URL}/api/v1/agents",
                json=registration_data,
                headers={"X-Admin-Key": DIRECTORY_ADMIN_KEY},
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"\n✅ Henri registered in Trust Directory")
                print(f"   URL: {TRUST_DIR_URL}/api/v1/agents/{self.agent.agent_id}")
                return True
            else:
                print(f"\n❌ Registration failed: {response.text}")
                return False
        except Exception as e:
            print(f"\n❌ Registration error: {e}")
            return False
    
    def receive_offer(self, buyer_id: str, offer_price: float) -> Dict[str, Any]:
        """
        Receive and evaluate buyer offer.
        
        Args:
            buyer_id: Buyer's agent ID
            offer_price: Offered price
            
        Returns:
            Evaluation and response
        """
        print(f"\n{'='*50}")
        print(f"🤖 Henri: Received offer from {buyer_id}")
        print(f"   Offered: ${offer_price}")
        print(f"{'='*50}\n")
        
        # Check buyer reputation from Trust Directory
        try:
            response = requests.get(f"{TRUST_DIR_URL}/api/v1/agents/{buyer_id}", timeout=10)
            if response.status_code == 200:
                buyer_data = response.json()
                reputation = buyer_data.get('metadata', {}).get('trust_score', 0)
                print(f"\n   Buyer trust score: {reputation}★")
            else:
                reputation = 0
                print(f"\n   ⚠️  Could not verify buyer")
        except:
            reputation = 0
        
        # Calculate profit
        profit_analysis = calculate_profit(offer_price)
        
        # Determine response
        if offer_price < self.min_price:
            response = "too_low"
            counter_price = self.min_price + 50
        elif profit_analysis['profit'] < 100:
            response = "counter"
            counter_price = self.cost_basis + 150
        else:
            response = "accept"
            counter_price = offer_price
        
        return {
            'response': response,
            'counter_price': counter_price,
            'profit': profit_analysis['profit'],
            'buyer_reputation': reputation
        }
    
    def make_counter_offer(self, price: float, reasoning: str = ""):
        """
        Make counter-offer to buyer.
        
        Args:
            price: Counter-offer price
            reasoning: Explanation for price
        """
        print(f"\n{'='*50}")
        print(f"🤖 Henri: Making counter-offer")
        print(f"{'='*50}\n")
        
        print(f"   Price: ${price}")
        print(f"   Reasoning: {reasoning or 'Fair market value based on condition'}")
        
        return {
            'price': price,
            'reasoning': reasoning,
            'signed': True
        }


def main():
    """Run Henri production demo."""
    print("\n" + "="*60)
    print("  HENRI - THE PROFESSIONAL RESELLER (Seller Agent)")
    print("  Powered by CrewAI + Amorce + Claude")
    print("  PRODUCTION MODE")
    print("="*60 + "\n")
    
    # Create Henri
    henri = HenriSellerAgent(min_price=int(os.getenv('HENRI_MIN_PRICE', 450)))
    
    # Register in Trust Directory
    print("\n--- REGISTERING IN TRUST DIRECTORY ---\n")
    henri.register_with_trust_directory()
    
    # Demo workflow
    print("\n--- DEMO WORKFLOW ---\n")
    
    # 1. Receive offer
    offer_response = henri.receive_offer(
        buyer_id="agent_sarah_123",
        offer_price=450
    )
    
    # 2. Counter-offer
    if offer_response['response'] == 'counter':
        henri.make_counter_offer(
            price=500,
            reasoning="Fair market value, excellent condition, 30-day warranty"
        )
    
    print("\n" + "="*60)
    print("  DEMO COMPLETE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
