"""
Henri - The Professional Reseller (Seller Agent)

Uses CrewAI with Amorce security to manage inventory
and negotiate sales while maintaining 4.8★ reputation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

from crewai_amorce import SecureAgent
from crewai import Tool
from typing import Dict, Any


class HenriSellerAgent:
    """
    Henri - Autonomous seller agent powered by CrewAI.
    
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
        
        # Create CrewAI agent with Amorce security
        self.agent = SecureAgent(
            role="Electronics Reseller",
            goal="Maximize profit while maintaining 4.8★ rating",
            backstory="Professional refurbisher with 500+ sales. Known for quality products and fair pricing.",
            tools=self.tools,
            hitl_required=['confirm_sale', 'issue_refund'],
            verbose=True
        )
        
        print(f"🤖 Henri initialized")
        print(f"   Agent ID: {self.agent.agent_id}")
        print(f"   Min Price: ${min_price}")
        print(f"   Cost Basis: ${self.cost_basis}")
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
        
        # Check buyer reputation
        reputation = self.agent.check_buyer_reputation(buyer_id)
        print(f"\n   Buyer trust score: {reputation.get('trust_score', 'N/A')}★")
        
        # Calculate profit
        profit_analysis = self.agent.calculate_margin(offer_price)
        
        # Determine response
        if offer_price < self.min_price:
            response = "too_low"
            counter_price = self.min_price + 50
        elif profit_analysis < 100:
            response = "counter"
            counter_price = self.cost_basis + 150
        else:
            response = "accept"
            counter_price = offer_price
        
        return {
            'response': response,
            'counter_price': counter_price,
            'profit': profit_analysis,
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
        
        counter = self.agent.counter_offer(
            price=price,
            reasoning=reasoning or f"Fair market value based on condition and current demand"
        )
        
        print(f"   Price: ${counter['price']}")
        print(f"   Reasoning: {counter['reasoning']}")
        print(f"   Signature: {counter['signature'][:50]}...")
        
        return counter
    
    def finalize_sale(self, buyer_id: str, final_price: float):
        """
        Finalize sale with human approval.
        
        Args:
            buyer_id: Buyer's agent ID
            final_price: Final agreed price
        """
        print(f"\n{'='*50}")
        print(f"🤖 Henri: Finalizing sale to {buyer_id}")
        print(f"   Final price: ${final_price}")
        print(f"{'='*50}\n")
        
        try:
            # Request human approval
            self.agent.request_human_approval_for_sale()
            
            # Generate receipt
            receipt = self.agent.generate_signed_receipt()
            
            print(f"\n✅ Sale complete!")
            print(f"   Receipt ID: {receipt['timestamp']}")
            print(f"   Signature: {receipt['signature'][:50]}...")
            
            return receipt
            
        except (PermissionError, TimeoutError) as e:
            print(f"\n❌ Sale cancelled: {e}")
            return None


def main():
    """Run Henri demo."""
    print("\n" + "="*60)
    print("  HENRI - THE PROFESSIONAL RESELLER (Seller Agent)")
    print("  Powered by CrewAI + Amorce")
    print("="*60 + "\n")
    
    # Create Henri
    henri = HenriSellerAgent(min_price=450)
    
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
            reasoning="Fair market value, excellent condition"
        )
    
    # 3. Finalize (after agreement)
    # henri.finalize_sale("agent_sarah_123", 500)
    
    print("\n" + "="*60)
    print("  DEMO COMPLETE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
