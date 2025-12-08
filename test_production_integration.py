"""
Simplified Production Demo Test

Tests core functionality without full agent initialization:
1. Trust Directory connectivity
2. Agent registration
3. Agent discovery

This avoids langchain dependency conflicts while demonstrating
the production integration works.
"""

import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment
load_dotenv()

TRUST_DIR_URL = os.getenv('TRUST_DIRECTORY_URL', 'https://trust.amorce.io')
ADMIN_KEY = os.getenv('DIRECTORY_ADMIN_KEY')

def test_trust_directory_connection():
    """Test 1: Can we connect to Trust Directory?"""
    print("\n" + "="*70)
    print("  TEST 1: Trust Directory Connection")
    print("="*70)
    
    try:
        response = requests.get(f"{TRUST_DIR_URL}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Connected to {TRUST_DIR_URL}")
            print(f"   Status: {data.get('message', 'OK')}")
            return True
        else:
            print(f"❌ Connection failed (HTTP {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False


def test_agent_registration():
    """Test 2: Can we register a test agent?"""
    print("\n" + "="*70)
    print("  TEST 2: Agent Registration")
    print("="*70)
    
    if not ADMIN_KEY:
        print("⚠️  DIRECTORY_ADMIN_KEY not set - skipping registration test")
        return False
    
    # Create test agent data
    test_agent_id = f"test-marketplace-demo-{int(datetime.now().timestamp())}"
    
    agent_data = {
        "agent_id": test_agent_id,
        "public_key": "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEtest\n-----END PUBLIC KEY-----",
        "endpoint": "http://localhost:8000/test",
        "metadata": {
            "name": "Test Marketplace Agent",
            "role": "Test",
            "framework": "Production Demo Test",
            "capabilities": ["test"],
            "trust_score": 5.0,
            "verified": True
        }
    }
    
    try:
        response = requests.post(
            f"{TRUST_DIR_URL}/api/v1/agents",
            json=agent_data,
            headers={"X-Admin-Key": ADMIN_KEY},
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"✅ Agent registered successfully")
            print(f"   Agent ID: {test_agent_id}")
            print(f"   URL: {TRUST_DIR_URL}/api/v1/agents/{test_agent_id}")
            return test_agent_id
        else:
            print(f"❌ Registration failed (HTTP {response.status_code})")
            print(f"   Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return None


def test_agent_discovery(test_agent_id=None):
    """Test 3: Can we discover agents?"""
    print("\n" + "="*70)
    print("  TEST 3: Agent Discovery")
    print("="*70)
    
    try:
        response = requests.get(f"{TRUST_DIR_URL}/api/v1/agents", timeout=10)
        if response.status_code == 200:
            data = response.json()
            agent_count = data.get('count', 0)
            agents = data.get('agents', [])
            
            print(f"✅ Discovery successful")
            print(f"   Total agents: {agent_count}")
            
            if test_agent_id:
                # Try to find our test agent
                found = any(a.get('agent_id') == test_agent_id for a in agents)
                if found:
                    print(f"   ✅ Test agent found in directory")
                else:
                    print(f"   ⚠️  Test agent not yet visible (may take a moment)")
            
            # Show a few sample agents
            print(f"\n   Sample agents:")
            for agent in agents[:3]:
                name = agent.get('metadata', {}).get('name', 'Unknown')
                score = agent.get('metadata', {}).get('trust_score', 'N/A')
                print(f"   - {name} ({score}★)")
            
            return True
        else:
            print(f"❌ Discovery failed (HTTP {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Discovery error: {e}")
        return False


def test_specific_agent_retrieval(test_agent_id):
    """Test 4: Can we retrieve a specific agent?"""
    print("\n" + "="*70)
    print("  TEST 4: Specific Agent Retrieval")
    print("="*70)
    
    try:
        response = requests.get(
            f"{TRUST_DIR_URL}/api/v1/agents/{test_agent_id}",
            timeout=10
        )
        
        if response.status_code == 200:
            agent_data = response.json()
            print(f"✅ Agent retrieved successfully")
            print(f"   Agent ID: {agent_data.get('agent_id')}")
            print(f"   Name: {agent_data.get('metadata', {}).get('name')}")
            print(f"   Trust Score: {agent_data.get('metadata', {}).get('trust_score')}★")
            return True
        else:
            print(f"❌ Retrieval failed (HTTP {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Retrieval error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  PRODUCTION MARKETPLACE DEMO - INTEGRATION TEST".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝")
    
    print(f"\nConfiguration:")
    print(f"  Trust Directory: {TRUST_DIR_URL}")
    print(f"  Admin Key: {'✅ Configured' if ADMIN_KEY else '❌ Not set'}")
    
    # Run tests
    results = {}
    
    results['connection'] = test_trust_directory_connection()
    results['registration'] = test_agent_registration()
    results['discovery'] = test_agent_discovery(results['registration'])
    
    if results['registration']:
        results['retrieval'] = test_specific_agent_retrieval(results['registration'])
    
    # Summary
    print("\n" + "="*70)
    print("  TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"\n✅ Passed: {passed}/{total} tests")
    print()
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {test_name}")
    
    print("\n" + "─"*70)
    if passed == total:
        print("🎉 All tests passed! Production integration is working.")
        print(f"\nThe marketplace demo can:")
        print("  ✓ Connect to trust.amorce.io")
        print("  ✓ Register new agents")
        print("  ✓ Discover registered agents")
        print("  ✓ Retrieve agent details")
        print(f"\nNote: Full agent workflow (LangChain + CrewAI) requires")
        print(f"      CLAUDE_API_KEY and compatible langchain versions.")
    else:
        print("⚠️  Some tests failed. Check configuration and try again.")
    
    print()


if __name__ == "__main__":
    main()
