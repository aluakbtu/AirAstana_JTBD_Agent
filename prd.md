# PRD: AI Procurement Risk & Workflow Assistant
Company: Air Astana Group

## 1. Problem Statement
Procurement at Air Astana involves complex cross-functional coordination between Legal, Finance, Operations, and external vendors. Contracts are reviewed manually across disconnected tools (email, Word, PDF, Excel), leading to long cycle times, high cognitive load on procurement officers, approval bottlenecks, and elevated risk of missing critical contractual clauses. The current workflow prioritizes perceived safety over efficiency, making slow, manual processes the default.

## 2. User Persona
**Primary User:** Procurement Officer (Mid-level)

- Handles 20–30 procurement cases in parallel
- Coordinates contract reviews with Legal, Finance, and Ops
- Personally accountable for errors or delays
- Operates in a safety-first, compliance-heavy environment
- Avoids tools that introduce untraceable changes or unclear audit trails

## 3. Job To Be Done (JTBD)
When managing complex procurement contracts involving multiple stakeholders,
I want to identify contractual risks, approval dependencies, and blockers early and transparently,
so I can complete procurements on time without introducing compliance, safety, or career risk.

## 4. Proposed Solution (Product Overview)
An internal AI-powered Procurement Assistant that supports contract review, dependency tracking, and approval visibility. The agent operates within Air Astana’s secure environment and augments—not replaces—existing Legal and Finance approval processes by highlighting risks, inconsistencies, and workflow bottlenecks.

## 5. Key Use Cases
- Detect inconsistent clauses between contract drafts and operational specifications
- Flag high-risk clauses (e.g., force majeure, liability, penalties)
- Track approval dependencies and identify workflow bottlenecks
- Provide real-time visibility into contract status for stakeholders
- Reduce manual reconciliation across document versions

## 6. Functional Requirements
FR1: The agent shall analyze uploaded contract documents and highlight clause inconsistencies across versions.  
FR2: The agent shall flag predefined high-risk contractual clauses for review.  
FR3: The agent shall map approval dependencies across Legal, Finance, and Operations.  
FR4: The agent shall display contract status (e.g., In Review, Blocked, Approved).  
FR5: The agent shall provide an auditable explanation for every risk flag or recommendation.

## 7. Non-Functional Requirements
- **Security:** All data processed within Air Astana’s secure infrastructure.
- **Auditability:** Full traceability of document versions and agent outputs.
- **Human-in-the-loop:** Final decisions remain with Legal and Finance.
- **Accuracy:** The agent must cite document sections when flagging risks.
- **Access Control:** Role-based access aligned with existing policies.

## 8. Out of Scope
- Aut
