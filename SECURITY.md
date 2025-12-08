# Security Guidelines - Marketplace Demo

## Security Checklist ✅

### Environment Variables
- ✅ All secrets stored in `.env` (gitignored)
- ✅ `.env.example` contains NO real credentials
- ✅ Admin keys loaded from environment only
- ✅ API keys loaded from environment only

### Credentials Management
**NEVER commit these to version control:**
- `CLAUDE_API_KEY` - Get from Anthropic console
- `DIRECTORY_ADMIN_KEY` - Get from Amorce deployment secrets
- `.env` file - Contains actual credentials

### Public Keys in Code
The demo uses **mock/test public keys** for demonstration purposes:
```
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEtest
-----END PUBLIC KEY-----
```

**These are NOT real keys and are safe to include in code.**

In production, agents would:
1. Generate their own Ed25519 keypairs
2. Store private keys securely (never in code)
3. Register only public keys with Trust Directory

---

## Setup Instructions

### 1. Create `.env` file
```bash
cp .env.example .env
```

### 2. Add Real Credentials
Edit `.env` and replace placeholders:

```bash
# Get from https://console.anthropic.com/
CLAUDE_API_KEY=sk-ant-api-xxx...

# Get from your Amorce deployment
# NEVER commit this!
DIRECTORY_ADMIN_KEY=sk-admin-xxx...
```

### 3. Verify `.gitignore`
Ensure `.env` is in `.gitignore`:
```bash
grep ".env" .gitignore
```

---

## Security Best Practices

### ✅ DO:
- Store all secrets in `.env`
- Use environment variables in code
- Add `.env` to `.gitignore`
- Use separate keys for dev/staging/prod
- Rotate admin keys periodically
- Use principle of least privilege

### ❌ DON'T:
- Hardcode API keys in code
- Commit `.env` files
- Share admin keys in chat/email
- Use production keys in demos
- Expose keys in logs/error messages

---

## Credential Locations

### Where Secrets Are Used:
1. **demo_production_*.py**
   - `CLAUDE_API_KEY` - Optional (Claude API)
   - `DIRECTORY_ADMIN_KEY` - Required (agent registration)

2. **test_production_integration.py**
   - `DIRECTORY_ADMIN_KEY` - Required

3. **agents/sarah/buyer_agent.py**
   - `CLAUDE_API_KEY` - Required
   - `DIRECTORY_ADMIN_KEY` - Required

4. **agents/henri/seller_agent.py**
   - `CLAUDE_API_KEY` - Required
   - `DIRECTORY_ADMIN_KEY` - Required

### All loaded via:
```python
from dotenv import load_dotenv
load_dotenv()

ADMIN_KEY = os.getenv('DIRECTORY_ADMIN_KEY')
CLAUDE_KEY = os.getenv('CLAUDE_API_KEY')
```

---

## Audit Results

**Files Audited:** All `.py` files  
**Last Audit:** 2025-12-08  
**Status:** ✅ SECURE

**Findings:**
- ✅ No hardcoded API keys
- ✅ No hardcoded admin keys  
- ✅ All secrets from environment
- ✅ `.env` in `.gitignore`
- ✅ Mock keys clearly labeled

---

## Incident Response

If credentials are exposed:

1. **Immediately rotate the key**
   - Anthropic: Revoke in console
   - Admin key: Update in Google Secret Manager

2. **Update `.env` locally**

3. **Verify no commits contain secrets:**
   ```bash
   git log -p | grep -i "sk-admin\|sk-ant"
   ```

4. **If found in git history:**
   ```bash
   # Remove from history (destructive)
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch .env" HEAD
   ```

---

## Production Deployment

For production deployments:

1. **Use Google Secret Manager:**
   ```bash
   gcloud secrets create DIRECTORY_ADMIN_KEY \
     --data-file=-
   ```

2. **Grant service account access:**
   ```bash
   gcloud secrets add-iam-policy-binding DIRECTORY_ADMIN_KEY \
     --member="serviceAccount:xxx@xxx.iam.gserviceaccount.com" \
     --role="roles/secretmanager.secretAccessor"
   ```

3. **Access in Cloud Run:**
   ```python
   from google.cloud import secretmanager
   
   client = secretmanager.SecretManagerServiceClient()
   response = client.access_secret_version(
       name="projects/PROJECT_ID/secrets/DIRECTORY_ADMIN_KEY/versions/latest"
   )
   admin_key = response.payload.data.decode('UTF-8')
   ```

---

## Questions?

Contact: team@amorce.io  
Security: security@amorce.io
