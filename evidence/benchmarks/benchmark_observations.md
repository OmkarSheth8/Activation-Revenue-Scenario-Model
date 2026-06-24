# Benchmark Observations

## Purpose

This benchmark evidence supports the Legion Growth Ops Audit model.

The benchmark step exists to avoid making up assumptions. The qualitative audit identifies possible friction in Legion's intake-to-first-visit workflow. The benchmarks provide external reference points for estimating how intake completion, booking, no-shows, dropout, wait time, and cost confusion may affect business outcomes.

These benchmarks are not Legion Health's internal metrics.

They should be used only for scenario modeling.

## Evidence Standard

The benchmark evidence is directional.

Internal Legion data would be required to measure actual conversion impact, including:

* Intake starts
* Provider-match reach rate
* Slot-selection rate
* Booked-first-visit rate
* Completed-first-visit rate
* First-visit no-show rate
* Follow-up visit completion
* Insurance verification failure rate
* Payment or billing-related support tickets
* Cancellation rate

The benchmarks should be used to create conservative, base, and optimistic scenarios, not firm predictions.

## Strongest Benchmarks

### 1. Psychiatry and telehealth no-show rates are material

The academic psychiatry telehealth study found overall no-shows declined from 18.1% before telehealth to 15.3% during telehealth. Telephone visits had much lower no-show rates than face-to-face or video in that setting, especially for new visits.

This supports the idea that appointment modality, friction, and access can change completion behavior.

### 2. Behavioral-health telehealth can reduce return-visit no-shows

The rural telehealth study found return behavioral-health telehealth visits had an 11.5% no-show rate versus 16.1% for in-person visits.

This is useful for modeling ongoing attendance after the first visit.

### 3. First appointment no-show risk can be high in psychiatry

The forensic psychiatry benchmark reported 24.9% no-show for initial appointments and 9.8% for follow-ups. Its literature review reported psychiatry no-show rates ranging from 10% to 40%.

This supports treating first-visit completion as a major business and operations lever.

### 4. Early telepsychiatry dropout exists even after access is created

A telepsychiatry cohort study reported 13.2% early dropout after one or two visits. It also highlighted higher patient cost and weaker therapeutic alliance as dropout factors.

This matters because the business outcome is not only booking the first visit. It is also completing care and continuing when clinically appropriate.

### 5. Digital form completion can be far below 100%

Digital and remote form completion benchmarks ranged from about 45% to 67%, with higher completion in controlled or mandatory settings.

This supports modeling intake completion as a real funnel step. It also reinforces that long or unclear intake can create activation friction.

### 6. Faster access can sharply reduce no-shows

The addiction-treatment quality-improvement study found reducing wait time from 13 days to 0 days lowered no-show rates from 52% to 18%. Across 67 organizations, no-show rates fell from 37.4% to 19.9% after best-practice changes.

This is not virtual psychiatry-specific, but it strongly supports the operating principle that fast scheduling and reduced waiting can improve completed visits.

### 7. Cost uncertainty is a trust and revenue problem

The behavioral-health balance-billing study found that among families with out-of-network behavioral-health claims, approximately half experienced balance billing. Mean balance bill was US$861.

This supports the audit's conclusion that cost clarity should be treated as a revenue trust layer, not just a billing operations issue.

## Benchmark Quality Tiers

### Strongest evidence for this audit

Use these most heavily:

* Psychiatry telehealth no-show study
* Telepsychiatry early dropout study
* Wait-time reduction and no-show impact study
* Behavioral-health balance-billing study

These connect most directly to virtual psychiatry, first-visit activation, no-shows, dropout, and cost trust.

### Useful proxy evidence

Use these carefully:

* Rural behavioral-health telehealth no-show study
* General telemedicine completion study
* Digital form completion studies
* Massachusetts mental-health wait-time report

These are useful, but not all are specific to virtual psychiatry intake.

### Weaker or contextual evidence

Use mainly for context:

* Orthopedic digital form completion benchmarks
* Cancer ePRO form completion benchmarks
* General psychotherapy dropout evidence
* Forensic psychiatry no-show benchmark

These are not useless, but they require careful caveats.

## Recommended Model Assumption Ranges

All ranges below represent estimated changes relative to Legion's unknown current baseline.

They should be used for scenario modeling, not predictions.

### Intake-to-provider-match completion improvement

Conservative: 0% to 5% increase

Base: 5% to 10% increase

Optimistic: 10% to 20% increase

Rationale:
Digital intake completion benchmarks range from 45% to 67% in remote or mixed settings and can reach 84% or higher in controlled settings. Legion's current intake likely already captures some users well because the observed flow reaches provider cards relatively quickly. Improvements should therefore be modeled conservatively unless internal data shows major drop-off.

### Provider-match-to-booked-visit improvement

Conservative: 2% to 5% increase

Base: 5% to 10% increase

Optimistic: 10% to 15% increase

Rationale:
Provider-match trust improvements may help more users move from seeing providers to selecting a slot. Benchmarks on telehealth completion and no-show rates support the broader idea that reducing friction and improving access can improve completion. However, there is limited public evidence specifically on provider-card-to-booked-visit conversion, so assumptions should stay conservative.

### Booked-visit-to-completed-visit improvement

Conservative: 3% to 7% increase

Base: 7% to 12% increase

Optimistic: 12% to 20% increase

Rationale:
Psychiatry no-show rates can range from 10% to 40%, and first-appointment no-shows may be materially higher than follow-ups. Telehealth and reduced wait time can lower no-shows. A trust and booking-confidence layer may reduce first-visit non-completion, but internal no-show data is needed before claiming a precise lift.

### No-show reduction after first visit

Conservative: 2% to 5% decrease

Base: 5% to 10% decrease

Optimistic: 10% to 20% decrease

Rationale:
Return behavioral-health telehealth visits showed lower no-shows than in-person visits in one rural study. Follow-up psychiatry no-shows may be lower than first-visit no-shows. Ongoing scheduling clarity, reminders, and modality flexibility may reduce missed follow-ups.

### Revenue sensitivity to cost transparency

Conservative: Modest impact

Base: Moderate impact

Optimistic: High impact

Rationale:
Behavioral-health balance billing and telepsychiatry dropout evidence both suggest patient cost burden can affect trust and continuation. However, direct public evidence linking a specific cost-transparency module to virtual psychiatry revenue lift is limited. The model should use scenario sensitivity rather than a fixed assumption.

## How These Benchmarks Support the Audit

The Phase 2 diagnostic concluded that Legion should improve intake-to-first-visit activation by making provider matching, cost path, eligibility path, and appointment path more transparent before booking.

The benchmarks support that conclusion in four ways:

1. Digital intake completion is not automatic.
2. First-visit no-show risk is meaningful in psychiatry and behavioral health.
3. Faster scheduling and reduced wait times can materially affect appointment completion.
4. Cost uncertainty can damage trust and contribute to dropout or dissatisfaction.

Together, these support building a simple activation model around the following funnel:

* Intake starts
* Provider match reached
* Slot selected
* First visit booked
* First visit completed
* Follow-up visit retained

## Recommended Model Structure

The spreadsheet model should include:

### Baseline inputs

* Monthly intake starts
* Percent reaching provider match
* Percent selecting a slot
* Percent booking first visit
* Percent completing first visit
* Average revenue per completed first visit
* Average revenue per follow-up visit
* Follow-up retention rate

### Scenario inputs

* Conservative activation lift
* Base activation lift
* Optimistic activation lift
* No-show reduction
* Cost-transparency retention effect

### Outputs

* Additional provider matches
* Additional booked first visits
* Additional completed first visits
* Estimated first-visit revenue lift
* Estimated follow-up revenue lift
* Total estimated monthly impact
* Total estimated annualized impact

## Important Caveats

Do not claim:

* Legion has a specific no-show rate.
* Legion has a specific intake abandonment rate.
* Legion loses a specific amount of revenue today.
* Any benchmark proves Legion's internal performance.
* Any benchmark proves a prototype will create a specific lift.

Use safer wording:

* External benchmarks suggest this is a material operating lever.
* Internal analytics would be required to validate actual drop-off.
* The model uses scenario ranges, not firm predictions.
* The goal is to show sensitivity of completed visits to small activation improvements.

## Final Benchmark Interpretation

The benchmark evidence makes the project stronger because it connects the qualitative friction findings to measurable business logic.

Legion's observed flow already gets users to provider cards relatively quickly. The question is not whether the whole flow needs a full rebuild. The question is whether a trust layer around provider matching, cost expectations, eligibility, availability, and booking could create a small but meaningful increase in completed first visits.

The model should test that question using conservative, base, and optimistic scenarios.
