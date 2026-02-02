# JTBD Interview Log
Persona: Procurement Officer, Air Astana
Method: 5 Whys

## Context question: Describe the last procurement case that was especially difficult or slow.

**Answer:**
"The most difficult recent case was the renewal of our **Ground Handling Services contract for Frankfurt**. 

It should have been a standard renewal, but it turned into a **six-week nightmare**. Here’s why:

1.  **Version Control Chaos**: The vendor introduced a new dynamic pricing model. I spent weeks just chasing the 'source of truth'. Legal marked up v3 in Word, the vendor replied to v2 by email, and the operational technical specs were in a separate PDF that didn't match the new contract definitions. I was literally printing them out and highlighting differences on my desk.
2.  **The 'Hidden Clause' Fear**: The vendor slipped in a subtle change to the 'force majeure' clause regarding strikes. Because I was manually reviewing these 40-page documents late at night, I was terrified I’d miss it. If I had, and there was a strike (which is common there), we would have been liable for cancellation fees. I caught it by pure luck, but the stress was immense.
3.  **Approval Bottlenecks**: Once we finally agreed, the internal sign-off took another 12 days. The approval request got buried in the VP of Operations' inbox, and I had to physically walk to his office three times to remind him, feeling like a pest, while the vendor threatened to suspend services."

## Why 1: Why did this situation escalate into such a long delay instead of being resolved early?

**Answer:**
"Because each department was working in a silo, and we lacked a **single source of truth**.

The escalation happened because:
1.  **Manual Reconciliation Delay**: Every time Legal made a change to the liability clause, I had to manually check if it conflicted with the operational SLAs in the PDF. I missed one conflict for 4 days because I was swamped with 20 other contracts. That 4-day delay effectively paused the whole deal because the vendor wouldn't sign until it was resolved.
2.  **Sequential, Not Parallel Work**: Finance wouldn't approve the budget until Legal signed off. Legal wouldn't sign off until Ops confirmed the specs. Ops was waiting for the vendor. If we could have flagged these dependencies instantly, we could have worked in parallel. Instead, we worked in a slow, linear chain.
3.  **Lack of Visibility**: No one else knew the contract was stuck on *my* desk waiting for that manual check. If the VP of Ops could see a dashboard saying 'Blocked: Awaiting Clause Verification', he might have stepped in. But to him, it was just 'in progress'."

## Why 2: Why do these silos and sequential approvals exist instead of a shared, transparent process?

**Answer:**
"Because **we are trying to manage complex collaboration using tools designed for personal productivity**: Email and Excel.

1.  **The 'Email Attachment' Trap**: There is no central platform where Legal, Ops, and I can look at the *same* live document. I have to email a file to Legal. They lock it, edit it, and email it back. Until they send it back, nobody else can touch it. That forces the sequential process. I can't let Ops work on the specs while Legal works on the liability, because merging their two versions later is a manual nightmare (and legally risky).
2.  **Lack of Trust in 'Live' Editing**: Legal refuses to use things like Google Docs or shared drives for contracts because they are terrified of 'ghost edits'—someone changing a clause without track changes. They rely on email because it provides a clear audit trail of *who sent what when*, even though it slows everything down.
3.  **The 'Integration Gap'**: Our ERP (SAP) is great for paying invoices, but it’s terrible for *negotiating* them. It doesn't handle back-and-forth redlines or comments. So we revert to email, which creates the silos."

## Why 3: Why hasn’t this process been fixed already, even though everyone knows it causes delays and stress?

**Answer:**
"Because every time we try to fix it, we hit a wall of **Compliance vs. Agility**.

1.  **The 'Enterprise' Deadlock**: We asked IT for a better contract management system. They quoted us a 9-month implementation plan for an SAP module that costs a fortune. Management won't approve that budget for a 'back-office improvement' unless we prove massive ROI, which is hard to quantify.
2.  **Shadow IT Protocols**: We could use lighter tools (like Trello or Monday.com) to track this, but InfoSec blocks them. They say contract data is 'highly sensitive' and can't leave our secure perimeter. So we are forced back to the only 'secure' tool we have: Outlook.
3.  **Process Ownership Vacuum**: Legal says 'We just review.' Finance says 'We just approve.' I’m the only one who sees the *whole* broken chain, but I don't have the authority to tell the Legal VP to change how her team works. Everyone agrees it's broken, but nobody has the mandate to fix the cross-functional workflow."

## Why 4: Why is there no single owner accountable for fixing this end-to-end procurement workflow?

**Answer:**
"Because **Air Astana (and most airlines) views procurement as a 'Support Function', not a 'Strategic Partner'**. 

The root cause is structural:
1.  **Conflicting KPIs**: My goal is **Speed** (Cycle Time). Legal's goal is **Risk Zero** (Protection). Finance's goal is **Control** (Audit). These goals are mutually exclusive. Without a 'Chief Supply Chain Officer' (CSCO) who forces these departments to compromise for the greater good, the department with the 'hardest' power wins. Usually, that's Legal or Finance, not Procurement.
2.  **The 'Cost Center' Mindset**: The business sees us as people who *spend* money, not people who *make* money. Therefore, fixing our internal headaches isn't a priority compared to fixing a passenger-facing app or a flight operations system. 
3.  **No Consequence for Delay**: If a contract is late, I get blamed, but nobody calculates the *cost* of that delay (e.g., higher temporary pricing, lost opportunities). Since the cost of the inefficiency is invisible/unquantified, there feels like there is no urgent 'burning platform' to fix it."

## Why 5: Why is this misalignment between speed, risk, and cost accepted as “normal” by the organization instead of being treated as a strategic problem to solve?

**Answer:**
"Because, in an airline, **'Process' is synonymous with 'Safety'**, and changing a known process feels like introducing unknown risk.

1.  **The Safety Culture Hangover**: In Flight Ops, sticking to the checklist keeps planes in the sky. Innovation is viewed with suspicion. This mindset bleeds into the back office. We treat a procurement policy like a flight manual—deviating from it or rewriting it feels reckless, even if it's just administrative. 'Better safe and slow than fast and sorry.'
2.  **Survival Mode**: We are always fighting the next crisis—engine issues, fuel price spikes, geopolitical airspace bans. Management’s bandwidth is consumed by *operational survival*. Improving the procurement workflow is a 'nice to have' that never makes it to the top of the 'must do' list because the planes are still flying.
3.  **Learned Helplessness**: The veterans here have seen three 'Digital Transformation' initiatives fail in the last decade. They’ve learned that keeping your head down and following the slow legacy process is safer for your career than trying to be the hero who pushes for change and fails."