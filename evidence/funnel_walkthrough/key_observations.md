# Key Observations

## Evidence Standard

These observations come from a public walkthrough of the intake and booking flow. They should be treated as product and UX hypotheses, not proof of actual user drop-off. Internal analytics would be needed to confirm conversion impact.

## Strongest Findings

### 1. Provider match transparency gap

During limited branch testing, the visible provider list appeared similar after changing insurance and care-pathway inputs. This does not prove that the matching logic is static. The result may be caused by provider overlap, session state, location, account caching, or limited available supply.

The stronger point is a transparency gap: the interface does not explain why the same providers remain recommended after different inputs.

Recommended wording:

The provider match page is useful and confidence-building, but the matching logic could be more transparent. If the same providers remain recommended after changed inputs, the interface should explain why they are still a strong fit.

### 2. No obvious edit control on provider match page

The match page depends on earlier inputs like condition, insurance, and care need. However, there is no clearly visible way to edit those prior answers from the provider match screen.

Recommended wording:

At the provider-match stage, the user does not appear to have a clear, visible way to edit earlier inputs. Since provider recommendations depend on those answers, this creates a control and trust gap.

### 3. Availability copy ambiguity

Availability labels like "times in the next X days" may be ambiguous. In one observed case, visible appointment dates appeared to span beyond a simple calendar-day interpretation.

Recommended wording:

Clearer wording such as "next 3 available days" could reduce confusion when provider availability spans non-consecutive dates.

### 4. Insurance uncertainty

The insurance step is visually clear and includes a No Insurance option. Selecting No Insurance shows self-pay pricing, which is a strength.

The friction is not that insurance is asked early. In healthcare, insurance is operationally necessary. The actual friction is that users may still be unsure whether their exact plan is accepted before they see provider availability and final cost.

Recommended wording:

The insurance step is clear, but users who do not know whether their exact plan is accepted may still feel uncertainty before seeing provider match, appointment availability, or final cost.

### 5. Medication and diagnosis pathway wording

The "How can we help you?" screen routes users into diagnosis or medication-support paths. This fits a psychiatry and medication-management product. Do not position this as a major weakness.

Better framing:

Users looking for broad mental health support may not immediately understand whether the service is best for therapy-only care, psychiatric evaluation, medication management, or all of the above.

## Strengths Observed

* The fit check screens show strong clinical and safety discipline.
* The flow uses progress indicators.
* The Conditions screen allows multi-select.
* The "I'm not sure" option reduces user pressure.
* The Insurance screen includes a No Insurance path.
* Self-pay pricing is shown clearly after selecting No Insurance.
* Account creation appears to happen before full intake completion, which may help recover partially completed users.
* Provider cards include ratings, specialties, bios, availability, and appointment slots.
* Selecting a time slot creates a clear booking CTA.

## Weak or Risky Claims to Avoid

Do not say:

* The matching algorithm is broken.
* Users definitely drop off at insurance.
* The provider list is fake or not personalized.
* The availability copy is definitely wrong.
* Medication-centered language is automatically bad.

Use safer wording:

* "May create uncertainty."
* "Appeared similar in limited branch testing."
* "Could reduce perceived personalization."
* "May be ambiguous."
* "Would require internal analytics to confirm."

## Recommended Next Research Step

Collect patient reviews from public sources and code them by funnel stage:

* Intake
* Insurance
* Provider match
* Booking
* Billing
* Follow-up
* Support

The goal is to see whether public patient reviews mention the same themes observed in the walkthrough.