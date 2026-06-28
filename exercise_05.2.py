"""
💼 The Scenario: The Automated Cold Outreach Sanitizer
When your lead generation agent crawls a local business website, the company name often comes back with messy extra characters (like trailing spaces or symbols), or the user submits their name in all lowercase letters. If you send a cold email that says, "Hey sayandip  , I saw your clinic, KINETICSTACK LLC!!!", it looks like a robotic spam template. Your client loses trust, and the deal dies.

You need to write a script that takes raw, messy data inputs and cleans them into perfect variables ready to be injected into an email template.

TODO: 2. **The Logic to Write:**
   * Clean `raw_founder_name` so *only* the first letter of each name is capitalized (Title case), and remove all the accidental spaces at the beginning and end.
   * Clean `raw_company_name` to remove the trailing `" LLC"` and make the domain uppercase.
   * Combine these clean variables into a final string variable called `email_draft`.

TODO: 3. **The Expected Terminal Output:**
   When you run `python outreach_sanitizer.py`, your terminal must print exactly this text:
   ```text
   --- CLEANED OUTREACH DRAFT ---
   Hi Sayandip Bhattacharya, I noticed you are the founder of KINETICSTACK.AI. Are you looking to scale your artificial intelligence agency this month?

"""
# Raw Data:
raw_founder_name = "   SAYANDIP bhattacharya   "
raw_company_name = "kineticstack.ai LLC"
raw_industry = "artificial intelligence"

# Cleaned data:
clean_founder_name = raw_founder_name.strip().title()
clean_company_name = raw_company_name.replace("LLC", "").upper().strip()

# email draft:
email_draft = f"Hi {clean_founder_name}, I noticed you are the founder of {clean_company_name}. Are you looking to scale your {raw_industry} agency this month?"

print("="*45)
print(
    f" --- CLEANED OUTREACH DRAFT ---\n{email_draft}"
)
print("="*45)
