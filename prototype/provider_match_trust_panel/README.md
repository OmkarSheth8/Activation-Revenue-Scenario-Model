# Activation Revenue Scenario Model

**[Live app →](https://omkarsheth8-activ-prototypeprovider-match-trust-panelapp-5qfhst.streamlit.app/)**
&nbsp;&nbsp;|&nbsp;&nbsp;
**[Excel model →](https://docs.google.com/spreadsheets/d/1xmVXqEkXylYkrhmxIgWt_Gx_yoVZuRyF/edit?usp=sharing&ouid=107052654186129163053&rtpof=true&sd=true)**

## What this is

A one-scroll Streamlit dashboard that turns the Excel activation revenue model into an interactive scenario tool.

## Why it exists

Instead of editing assumptions directly in Excel, a reviewer can change intake volume, funnel rates, revenue assumptions, and improvement scenarios in the dashboard and immediately see the impact on completed visits and revenue.

## What it shows

* Funnel stage counts
* Completed first visits
* Follow-up retained visits
* Scenario-based visit impact
* Monthly revenue impact
* Annualized revenue impact

## How to run

```
cd prototype/provider_match_trust_panel
```

```
python -m venv .venv
```

Windows:
```
.venv\Scripts\activate
```

Mac/Linux:
```
source .venv/bin/activate
```

```
pip install -r requirements.txt
streamlit run app.py
```

## Default output at Base scenario (10%)

* Current completed first visits: 360
* Change in completed visits: +36
* Monthly revenue impact: +$9,792
* Annualized revenue impact: +$117,504

## Caveats

* Uses sample assumptions
* Not Legion internal data
* Not a financial forecast
* Not medical advice
* No PHI should be entered
