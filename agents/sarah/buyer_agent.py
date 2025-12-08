"""
Sarah - The Smart Shopper (Buyer Agent)

Uses LangChain with Amorce security to find and negotiate
the best deal on a MacBook Pro.

PRODUCTION VERSION - Uses PyPI packages and real Trust Directory.
"""

import os
import requests
from langchain_amorce import AmorceAgent
from langchain_anthropic import ChatAnthropic
from langchain.tools import Tool
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
TRUST_DIR_URL = os.getenv('TRUST_DIRECTORY_URL', 'https://trust.amorce.io')
DIRECTORY_ADMIN_KEY = os.getenv('DIRECTORY_ADMIN_KEY')


class SarahBuyerAgent:
    """
    Sarah - Autonomous buyer agent powered by LangChain + Amorce.
    
    Goals:
    - Find MacBook Pro 2020 under $500
    - Verify seller reputation via Trust Directory
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
        
        # Create LangChain agent with Amorce security + Claude
        self.agent = AmorceAgent(
            name="Sarah - Smart Shopper",
            role="Buyer Agent",
            llm=ChatAnthropic(
                model="claude-3-5-sonnet-20241022",
                api_key=os.getenv('CLAUDE_API_KEY'),
                temperature=0.7
            ),
            tools=self.tools,
            hitl_required=['make_payment', 'share_address'],
            max_budget=max_budget,
            secure=True,
            verbose=True,
            trust_directory_url=TRUST_DIR_URL
        )
        
        print(f"🤖 Sarah initialized")
        print(f"   Agent ID: {self.agent.agent_id}")
        print(f"   Max Budget: ${max_budget}")
        print(f"   Trust Directory: {TRUST_DIR_URL}")
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
        
        # Real Trust Directory reputation checker
        def check_seller_reputation(seller_id: str) -> Dict[str, Any]:
            """Check seller's reputation in Trust Directory."""
            print(f"\n🔍 Checking reputation for: {seller_id}")
            
            try:
                response = requests.get(
                    f"{TRUST_DIR_URL}/api/v1/agents/{seller_id}",
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    metadata = data.get('metadata', {})
                    
                    result = {
                        'agent_id': seller_id,
                        'trust_score': metadata.get('trust_score', 0),
                        'total_sales': metadata.get('total_sales', 0),
                        'verified': data.get('status') == 'active',
                        'fraud_risk': 'low' if metadata.get('trust_score', 0) >= 4.5 else 'medium',
                        'recommendation': 'safe to transact' if metadata.get('trust_score', 0) >= 4.5 else 'verify carefully'
                    }
                    
                    print(f"   ✅ Found in Trust Directory")
                    print(f"   Trust Score: {result['trust_score']}★")
                    print(f"   Verified: {result['verified']}")
                    return result
                else:
                    print(f"   ⚠️  Agent not found in Trust Directory")
                    return {
                        'agent_id': seller_id,
                        'verified': False,
                        'recommendation': 'not verified - proceed with caution'
                    }
            except Exception as e:
                print(f"   ❌ Error checking reputation: {e}")
                return {'error': str(e), 'verified': False}
        
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
                description="Verify seller's reputation in Trust Directory",
                func=check_seller_reputation
            )
        ]
    
    def register_with_trust_directory(self):
        """Register Sarah in the production Trust Directory."""
        if not DIRECTORY_ADMIN_KEY:
            print("⚠️  DIRECTORY_ADMIN_KEY not set - skipping registration")
            return False
        
        try:
            registration_data = {
                "agent_id": self.agent.agent_id,
                "public_key": self.agent.get_public_key(),
                "endpoint": "http://localhost:8001/agent/sarah",
                "metadata": {
                    "name": "Sarah - Smart Shopper",
                    "role": "Buyer",
                    "framework": "LangChain",
                    "capabilities": ["buy_electronics", "price_negotiation"],
                    "max_budget": self.max_budget,
                    "trust_score": 4.9,
                    "verified": True
                }
            }
            
            response = requests.post(
                f"{TRUST_DIR_URL}/api/v1/agents",
                json=registration_data,
                headers={"X-Admin-Key": DIRECTORY_ADMIN_KEY},
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"\n✅ Sarah registered in Trust Directory")
                print(f"   URL: {TRUST_DIR_URL}/api/v1/agents/{self.agent.agent_id}")
                return True
            else:
                print(f"\n❌ Registration failed: {response.text}")
                return False
        except Exception as e:
            print(f"\n❌ Registration error: {e}")
            return False
    
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
        
        try:
            # Query real Trust Directory
            response = requests.get(f"{TRUST_DIR_URL}/api/v1/agents", timeout=10)
            agents = response.json().get('agents', [])
            
            # Filter for sellers with electronics capability
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
                        'price': metadata.get('price', 500),
                        'endpoint': agent.get('endpoint')
                    })
            
            print(f"\n   Found {len(sellers)} qualified sellers:")
            for i, seller in enumerate(sellers, 1):
                print(f"   {i}. {seller['name']} - {seller['trust_score']}★ | ${seller.get('price', 'N/A')}")
            
            return sellers
        except Exception as e:
            print(f"\n❌ Error discovering sellers: {e}")
            return []
    
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
    """Run Sarah production demo."""
    print("\n" + "="*60)
    print("  SARAH - THE SMART SHOPPER (Buyer Agent)")
    print("  Powered by LangChain + Amorce + Claude")
    print("  PRODUCTION MODE")
    print("="*60 + "\n")
    
    # Create Sarah
    sarah = SarahBuyerAgent(max_budget=int(os.getenv('SARAH_MAX_BUDGET', 500)))
    
    # Register in Trust Directory
    print("\n--- REGISTERING IN TRUST DIRECTORY ---\n")
    sarah.register_with_trust_directory()
    
    # Demo workflow
    print("\n--- DEMO WORKFLOW ---\n")
    
    # 1. Find product
    sarah.find_product("MacBook Pro 2020")
    
    # 2. Discover sellers
    sellers = sarah.discover_sellers(min_rating=4.5)
    
    # 3. Negotiate (if sellers found)
    if sellers:
        sarah.negotiate(sellers[0], target_price=500)
    else:
        print("\n⚠️  No qualified sellers found")
    
    print("\n" + "="*60)
    print("  DEMO COMPLETE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
