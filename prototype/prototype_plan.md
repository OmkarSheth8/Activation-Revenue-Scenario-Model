# Prototype Plan

The prototype will be an AI-assisted pre-intake workflow.

## Intended Function

A prospective patient provides a short free-text description. The workflow extracts structured information and returns a safe administrative routing summary.

## Example Inputs

* State
* Condition interest
* Insurance status
* Urgency indicators
* Questions or confusion points

## Example Outputs

* Condition interest
* Eligibility or routing notes
* Possible friction point
* Patient-friendly next step
* Internal operations summary
* Escalation flag if needed

## Guardrails

* No diagnosis
* No medication recommendation
* No clinical decision-making
* Synthetic sample data only
* Human review for any safety-sensitive output