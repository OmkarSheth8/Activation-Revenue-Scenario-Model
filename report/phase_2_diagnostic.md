# Phase 2 Diagnostic: Intake-to-First-Visit Activation

---

## 1. Executive Answer

**What is the highest-leverage growth or operating problem Legion should fix first?**

The highest-leverage opportunity is to improve intake-to-first-visit activation by increasing trust and clarity before booking.

Legion already has a meaningful speed advantage. Users reach matched provider cards and visible appointment slots relatively early — before competitors like Talkspace and Brightside show providers in their observed flows. That advantage should be preserved.

The problem is not that the flow is too slow. The problem is that key trust moments are under-explained.

Specifically:

* Why a particular provider was matched is not made clear on the match page
* Whether the user's insurance or self-pay path covers the selected provider is not confirmed before booking
* Availability labels may be ambiguous when dates span beyond a simple calendar-day interpretation
* There is no obvious way to edit earlier answers from the provider-match page
* What happens after a slot is selected is not clearly previewed before commitment
* Medication eligibility and care-path fit could be surfaced earlier for users with specific needs like ADHD stimulant care

Users who reach the provider match but cannot answer "why this provider, what will this cost, and what happens next" may stall or abandon before booking. Internal analytics would be required to confirm the magnitude.

---

## 2. Evidence Base

This diagnostic uses four evidence sources:

**Legion funnel walkthrough.** A structured public walkthrough of the Legion intake and booking flow, logged step by step with observed fields, gates, branching, friction hypotheses, and screenshots. 7 steps documented. Branch testing was limited.

**Legion public review coding.** 18 paraphrased reviews coded by theme, funnel stage, and sentiment, drawn from Trustpilot and Zocdoc. Trustpilot: 5 reviews, 3.1 average. Zocdoc: 1,298 reviews, 4.85 average.

**Competitor workflow comparison.** Public walkthroughs of Talkspace Psychiatry, Talkiatry, and Brightside Health, logged across 24 steps total with specific observations on provider visibility, payment timing, clinical screening depth, and Legion comparison.

**Competitor review coding.** 26 paraphrased reviews coded from Trustpilot, HelpGuide, and aggregate summaries for the same three competitors.

All evidence is directional. It does not prove actual drop-off rates, conversion loss, or revenue impact. Internal funnel analytics would be required to quantify any of these effects.

---

## 3. AARRR Funnel Diagnosis

### Acquisition

Acquisition is not the best first problem to solve from this evidence base.

The observed evidence starts after users have already entered the intake flow. There is no data on traffic volume, paid or organic channel mix, or top-of-funnel awareness. Reviews do mention Legion through positive referral signals — one Zocdoc reviewer noted that Legion gave them access faster than a six-month primary-care referral wait — but this does not isolate an acquisition bottleneck.

**Diagnosis:** Legion should not treat this as a top-of-funnel traffic problem until intake-to-first-visit confidence is stronger. Improving activation makes every acquired user more valuable before adding more traffic.

---

### Activation

Activation is the primary problem area identified in this audit.

Activation means the user moves from initial intent — they have entered the intake flow — to a booked and completed first visit.

**Observed strengths in the Legion flow:**

* Conditions step is clear and supports multi-select, reducing pressure for users with overlapping needs
* Insurance step is clear; self-pay pricing appears immediately after selecting No Insurance, which is an explicit design strength
* Provider cards and appointment slots appear relatively early compared with Talkspace and Brightside in the observed flows
* Progress indicators are visible throughout
* Account creation appears to happen during the flow, enabling continuation later

**Observed activation gaps:**

* The provider match page does not explain why specific providers are recommended
* No obvious edit control was visible from the match screen to revise condition, insurance, or care-need selections
* Availability language such as "15 times in the next 3 days" appeared potentially ambiguous when visible dates included later calendar dates
* In limited branch testing, the visible top provider list appeared similar across changed insurance and care-pathway inputs; this may reduce perceived personalization if not explained, though the cause may be provider supply, session state, or location constraints rather than a matching logic problem

**What competitors show:**

* Talkspace offers clean plan-and-payment packaging but showed no visible provider list before plan checkout in the observed psychiatry flow — weaker than Legion on early provider transparency
* Talkiatry offers strong expectation-setting with a three-step process preview before intake begins and strong clinician-choice depth after screening — but only after a much heavier intake burden
* Brightside offers the strongest clinical assessment feedback, including symptom scores and severity labels, before plan selection — but provider bios are not shown until after booking per HelpGuide testing

**Conclusion:** Legion's activation opportunity is to keep the fast path to providers while making that path feel more trustworthy and explainable. The goal is not to copy competitors' heavier intake flows. It is to add a trust layer that resolves the key questions users have before committing to a slot.

---

### Retention

Retention depends on care quality, provider follow-through, medication continuity, support response, and trust after the first visit.

**Positive signals from reviews:**

* Many Zocdoc reviews describe providers as caring, attentive, and collaborative
* Positive Trustpilot reviews mention feeling understood, receiving prompt callbacks, and having easy access to care
* Competitor reviews across all three platforms also show strong provider care quality once patients reach the clinical relationship

**Operational concerns from reviews:**

* Negative Legion reviews raise issues around billing after cancellation, difficulty removing a card, same-day appointment cancellation due to medication eligibility that was not caught earlier, provider lateness, referral follow-through, and support escalation
* Competitor reviews across Talkspace, Talkiatry, and Brightside show a near-identical pattern: strong provider quality alongside billing transparency problems, support issues, and appointment reliability concerns

**Conclusion:** Retention risk starts before the first visit. If users are unsure what they are booking, why a provider fits, and what their cost or care-path will be, they arrive at the first appointment with lower trust and lower tolerance for operational friction. Improving activation clarity also reduces early retention risk.

---

### Revenue

Revenue is tied to completed first visits and repeat follow-up visits.

The financial model will quantify this later. The diagnostic framing is:

* Unclear insurance expectations can cause users to abandon before booking or dispute charges after
* Unclear cancellation and billing rules are the most specific negative theme in Legion's Trustpilot reviews
* Competitor reviews for Talkiatry and Talkspace include surprise charges, unexpected bills, and insurance verification failures as recurring revenue trust issues
* Brightside reviews include price and insurance-knowledge concerns

**Conclusion:** Cost transparency is a revenue trust layer, not only a billing operations issue. A user who does not understand what they will pay, or who is surprised by a charge after a cancelled first visit, is a revenue risk and a retention loss simultaneously.

---

### Referral

Referral is not the first priority.

Positive provider experiences could generate strong word-of-mouth. The Zocdoc volume of 1,298 reviews at 4.85 average suggests Legion patients do refer and review. But operational trust issues — billing, cancellation, support, medication eligibility — suppress the likelihood that patients recommend the service after a friction-heavy experience.

**Conclusion:** Referral improves naturally after activation and retention are more reliable.

---

## 4. Friction Inventory

### Friction Point 1: Provider match transparency

**What was observed:**
The provider match page shows clinician cards with name, credentials, role, specialty tags, star rating, bio preview, and appointment slots. Labels such as "Perfect match found," "Highly recommended," and "Soonest available" appear on cards. No explanation of what drove the match — condition selected, care-need pathway, insurance, or other factors — was visible in the observed flow.

**Why it matters:**
Users who do not understand why they are matched to a provider are asked to trust a recommendation without a basis. The labels "perfect match" and "highly recommended" make claims that feel meaningful but are not explained. This may reduce booking confidence, especially for users who changed answers mid-flow and saw similar providers.

**Evidence confidence:** Medium. This is a structural observation from a single walkthrough. Internal click-through or abandonment data on the match page would be needed to confirm impact.

**Competitor comparison:**
Talkiatry shows 8 matched clinicians with credential tags, specialty labels, bio links, and availability buttons — with no explicit matching rationale either, but the volume of options and the multi-select clinical intake create an implicit sense that deeper screening produced the list. Talkspace does not show providers before checkout in the observed flow. Brightside does not show provider details before booking per HelpGuide testing. None of the three clearly explains match logic, but Talkiatry's post-screening list feels more earned.

**Recommended fix direction:**
Add a brief match-rationale note to each provider card. Examples: "Specializes in ADHD and anxiety," "Accepts your insurance," "Has availability this week," "Matches your care-need selection." This is copy and product logic, not a matching-algorithm rebuild.

**Conclusion:** Provider cards are useful, but users need to understand why these providers are recommended.

---

### Friction Point 2: No obvious edit control from match page

**What was observed:**
The provider match page shows results based on earlier answers: condition, insurance, and care-need pathway. No clearly visible link, button, or control for editing those earlier answers was observed from the match screen.

**Why it matters:**
A user who selected the wrong condition, changed their mind about their care need, or wants to try a different insurance option has no obvious path to revise. If the user cannot easily adjust prior answers, they may either accept a suboptimal match or abandon the flow entirely.

**Evidence confidence:** Medium. This was observed in a single walkthrough. Mobile versus desktop behavior, or logged-in versus new-user behavior, may differ.

**Competitor comparison:**
Talkiatry's match page similarly does not show an in-page edit control, but the extensive intake gives users confidence that their answers were captured deeply. Brightside's assessment result screen shows next steps without a visible edit path in the observed flow. No competitor handles this obviously well in the observed flows.

**Recommended fix direction:**
Add a visible "Edit your answers" or "Change preferences" control on the match page. This is a trust signal as much as a functional feature. Users who know they can change answers are more likely to continue with confidence.

**Conclusion:** If earlier answers drive matching, the user should be able to review or edit those answers before booking.

---

### Friction Point 3: Availability copy ambiguity

**What was observed:**
Provider cards display availability language such as "4 times in the next 2 days" and "15 times in the next 3 days." In one observed case, visible appointment dates appeared to extend beyond a simple consecutive-calendar-day interpretation of the label.

**Why it matters:**
Availability language is a trust signal. If a user reads "3 days" but sees dates that appear to span more than three days, they may question the accuracy of other information on the page.

**Evidence confidence:** Low to medium. This was a limited observation and may reflect non-consecutive available booking days, timezone interpretation, or session timing. It should be treated as a hypothesis, not a confirmed bug.

**Competitor comparison:**
Talkiatry shows appointment slots in a calendar modal after selecting a clinician, which makes the date count implicit rather than labeled. Talkspace and Brightside did not show specific slot availability in the observed flows before the stopping point.

**Recommended fix direction:**
Change "times in the next X days" to "times in the next X available days" if the count reflects booking-day availability. Alternatively, show a date range explicitly: "4 slots between Jun 23 and Jun 25."

**Conclusion:** Availability copy should distinguish between calendar days and available booking days.

---

### Friction Point 4: Insurance and cost expectation clarity

**What was observed:**
The insurance step asks users to select a plan from a list that includes major insurers, Other Insurance, and No Insurance. Selecting No Insurance shows self-pay pricing immediately: $250 for new patient intakes and $150 for follow-ups. This is a genuine design strength.

The gap is what happens for users with insurance. After selecting an insurer, the flow proceeds to provider match without a clear statement of expected copay, deductible exposure, or what happens if the selected plan does not cover a specific provider.

The most specific negative Legion review described a same-day cancellation and an unexpected charge, with difficulty removing a card.

**Why it matters:**
Cost uncertainty before booking creates hesitation. Cost surprise after care creates churn, billing disputes, and review-level complaints. Both are revenue and trust problems.

**Evidence confidence:** Medium-high. The billing and cancellation theme in negative Legion reviews is the strongest operational signal in the review evidence.

**Competitor comparison:**
Talkspace shows a "not charged until matched" message at plan checkout, which partially addresses timing uncertainty. Talkiatry's fallback message says coverage is being verified and the user can still book — strong for availability but leaves cost uncertainty open. Brightside accepts major insurance and shows pricing, but does not prescribe controlled substances, which limits its ADHD comparison. Across all three, billing and surprise charges are a shared review complaint.

**Recommended fix direction:**
After insurance selection and before slot confirmation, add a brief cost-expectation note: "Your insurance is accepted. Final cost depends on your plan. Most patients pay $X–$Y per visit." Include a one-line note on cancellation policy before the booking button is clicked.

**Conclusion:** Legion already shows self-pay pricing after No Insurance, which is good. The next opportunity is clearer expectation-setting around coverage, final cost, cancellation, and what happens if insurance cannot be verified.

---

### Friction Point 5: Clinical explanation before booking

**What was observed:**
The Legion flow asks users to select conditions and a care-need pathway. The intake does not appear to return clinical feedback — no score, no explanation of how selected answers map to the recommended providers or care path.

**Why it matters:**
Users who do not receive feedback on their selections may not understand whether they are in the right place. This matters most for users with complex or overlapping needs — for example, someone who selected both depression and anxiety but primarily needs ADHD evaluation.

**Evidence confidence:** Medium. This is a gap observation, not a confirmed drop-off point.

**Competitor comparison:**
Brightside gives users depression and anxiety symptom scores with severity labels and then shows available appointment times before plan selection. This is the strongest clinical-explanation experience among the competitors observed. The cost is questionnaire length: Brightside's intake is the longest of the three competitors observed.

Talkiatry's deep clinical screening accomplishes a similar goal through extensive input rather than output feedback. Talkspace's flow does not include assessment feedback in the observed steps.

**Recommended fix direction:**
After condition and care-need selection, add a brief one- or two-line summary before the match page: "Based on your selections, we've matched you with providers who specialize in ADHD evaluation and medication management in Texas." This connects the user's answers to the match result without requiring a full clinical assessment.

**Conclusion:** Brightside gives users assessment scores and clinical feedback. Legion does not need to copy the long questionnaire, but it should explain how the user's answers translate into the recommended care path and matched providers.

---

## 5. ICE Ranking

ICE scores use Impact (1–10), Confidence (1–10), and Ease (1–10). Higher scores are better. ICE Score = (Impact × Confidence × Ease) / 10.

| Opportunity | Impact | Confidence | Ease | ICE Score | Why it ranks here |
|---|---|---|---|---|---|
| Explain provider match logic on match page | 9 | 8 | 3 | 21.6 | Directly addresses the primary trust gap. Moderate engineering lift — mostly copy and product logic, not an algorithm rebuild. |
| Clarify availability language | 6 | 7 | 2 | 8.4 | Low-effort copy fix. High confidence because ambiguity was directly observed. Lower impact because it is one label, not a core trust moment. |
| Add review/edit answers control before booking | 8 | 8 | 4 | 25.6 | High trust and control signal. Engineering lift is real but contained — a back-navigation or edit modal on the match page. |
| Add insurance/self-pay expectation module before slot confirmation | 8 | 7 | 5 | 28.0 | High confidence because billing complaints are the strongest operational signal in Legion reviews. Moderate effort — requires coordination with billing and insurance logic. |
| Add lightweight clinical rationale after intake | 8 | 6 | 6 | 28.8 | Strong strategic value. Confidence lower because the connection from intake selections to match rationale requires product and clinical logic. |
| Add more provider cards or provider filters | 6 | 5 | 7 | 21.0 | May help later, but the first problem is explanation and confidence, not provider count or filter controls. |
| Shorten the intake flow | 5 | 5 | 7 | 17.5 | Legion's intake is already shorter than Talkiatry and Brightside. A shorter intake is not the leverage point. |

**ICE score note:** The raw ICE score is not the sole decision input. The insurance/expectation module and lightweight clinical rationale rank high because their strategic trust value is high. The availability copy fix ranks lower on ICE but is the easiest item to ship and should be done quickly regardless. The recommended 30-day focus should combine the highest strategic trust improvements, not chase only the easiest copy changes.

---

## 6. Recommended First Problem

**Problem statement:**

Legion should improve intake-to-first-visit activation by making the provider match, cost path, eligibility path, and appointment path more transparent before booking, while preserving the current speed to provider cards.

This is better than "increase signups" because:

* The walkthrough shows Legion already gets users to provider cards relatively quickly. The problem is not reach — it is confidence at the match and booking moment.

This is better than "reduce form length" because:

* Legion's intake is already shorter than Talkiatry and Brightside in the observed flows. Shortening further may remove useful routing information without resolving the trust gap.

This is better than "add more providers or filters" because:

* The primary observed issue is not that users lack choices. It is that users cannot interpret the choices they see.

The competitive evidence makes the opportunity clear:

* Talkspace is weaker on provider transparency before checkout — Legion should not copy that model
* Talkiatry is stronger on expectation-setting and clinician choice — Legion should add the explanation without adding the intake burden
* Brightside is stronger on clinical feedback — Legion should add the rationale without copying the long questionnaire

Reviews suggest care quality can be strong when care is reached. The trust gap lives between "I started intake" and "I booked my first visit."

---

## 7. What Not To Solve First

### Do not solve acquisition first

The evidence does not show a traffic problem. Improving intake conversion makes every acquired user more valuable before adding more acquisition cost.

### Do not solve full intake redesign first

A full intake redesign is too broad and risks breaking Legion's current speed advantage to provider cards. The target is a trust layer on the existing flow, not a structural rebuild.

### Do not copy Brightside's long assessment

Brightside's clinical explanation is the strongest competitor feature observed. But the long questionnaire creates activation burden. Most Brightside surveyed users wanted a shorter sign-up. Legion should add lightweight rationale, not clinical assessment depth.

### Do not copy Talkspace's checkout-before-provider path

Talkspace moves users into plan selection and checkout before showing a provider list in the observed psychiatry flow. Legion's early provider visibility is a genuine competitive advantage. Do not trade it for payment packaging clarity alone.

### Do not overbuild provider filtering first

Provider filters are a reasonable future feature. They are not the first leverage point. The issue is not that users cannot filter — it is that users cannot interpret the matches they already see.

---

## 8. 30-Day Execution Direction

The full 30-day plan will be written separately. This section previews the three workstreams that plan should focus on.

### Workstream 1: Match transparency

Make it clear why a user was matched to a specific provider.

Examples:
* "Why this provider?" callout on each provider card
* Match factors drawn from earlier answers: condition specialty, insurance fit, care-need alignment, availability
* Insurance fit indicator — "Accepts your plan" or "In-network pending verification"
* Specialty fit indicator — "Specializes in ADHD evaluation"
* Availability fit indicator — "Has openings this week"

### Workstream 2: Booking confidence

Make the moment after slot selection feel less ambiguous.

Examples:
* "Edit your answers" control visible from the match page
* Clarified availability labels — "next X available booking days"
* A brief "What happens next" note before the booking button: "You'll confirm your details and insurance. No charge until your visit is complete."
* Cancellation and support expectations surfaced before commitment

### Workstream 3: Cost and care-path clarity

Resolve cost and eligibility uncertainty before the user reaches the booking confirmation.

Examples:
* Insurance/self-pay expectation module: expected cost range or pending verification note shown after insurance selection
* Medication eligibility note where relevant: "Legion can evaluate and prescribe for ADHD, including stimulant medications where clinically appropriate"
* Lightweight clinical rationale connecting condition and care-need selection to the match result: "Based on your selections, we matched you with providers who specialize in ADHD and anxiety in Texas"

---

## 9. Model Implications

The financial model will be built separately.

The model should estimate the revenue impact of improving activation from intake start to completed first visit.

**Planned model inputs:**

* Monthly intake starts (assumption — internal volume is not public)
* Current estimated provider-match reach rate
* Current estimated slot-selection rate
* Current estimated booked-first-visit rate
* Current estimated completed-first-visit rate
* Improvement scenarios: conservative, base, and optimistic
* Estimated incremental completed visits gained per scenario
* Estimated incremental revenue per scenario

**External benchmarks still needed before finalizing assumptions:**

* Telehealth digital intake abandonment rates
* Behavioral health appointment no-show rates
* First-visit conversion rates for virtual psychiatry
* Behavioral health retention after first visit

These should be sourced from PubMed, JMIR, Psychiatric Services, and industry reports and placed in the benchmarks evidence folder before the model is finalized.

---

## 10. Prototype Implications

The prototype will be built separately.

Two options are viable given the diagnostic:

**Option A: Provider-match trust panel**

A lightweight UI or workflow that:
* Explains why each provider was matched using factors from earlier answers
* Shows insurance or self-pay expectation relevant to that provider
* Clarifies availability using unambiguous language
* Lets the user review and edit prior answers before committing to a slot

This directly addresses the activation trust gap visible in the walkthrough and confirmed by competitive context.

**Option B: Intake-to-booking funnel dashboard**

A simple dashboard or workflow that shows where users drop from condition selection to provider match to slot selection to booked visit, using synthetic data to simulate the funnel.

This addresses an operational analytics gap but does not directly fix the trust problem.

**Recommendation:** Option A is the stronger prototype. It demonstrates the specific trust intervention the diagnostic recommends and can be shown end-to-end with synthetic inputs. Option B is useful for internal ops but less compelling as a standalone demonstration of the activation opportunity.

---

## 11. Final Diagnostic Summary

Legion's observed advantage is speed to provider visibility. Users reach matched provider cards and appointment slots before they encounter checkout, insurance verification forms, or clinical questionnaire burdens — a meaningful contrast with all three competitors in the observed flows.

The weakness is trust clarity around the match, cost, eligibility, and booking path. Users who reach the provider match page but cannot interpret why a provider is recommended, what their insurance or self-pay path means, what availability labels represent, or what happens after clicking a slot may stall or abandon before booking.

The next 30 days should not focus on a full funnel rebuild. They should focus on adding a lightweight trust layer that answers four questions before a user clicks book: Why this provider? What will this cost or require? When is the appointment, exactly? And what happens next?

Those four answers — built into the existing flow without replacing it — are the highest-leverage activation improvement available from the current evidence base.
