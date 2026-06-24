import streamlit as st

st.set_page_config(
    page_title="Activation Revenue Scenario Model",
    page_icon="📈",
    layout="wide"
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #f0f2f6; }

.card {
    background: #ffffff;
    border: 1px solid #dde1e7;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 14px;
}
.card-title {
    font-size: 0.73rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #888;
    margin-bottom: 6px;
}
.helper {
    font-size: 0.82rem;
    color: #888;
    margin-bottom: 0;
}
.section-label {
    font-size: 0.73rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #888;
    margin-bottom: 8px;
    margin-top: 2px;
}
.funnel-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.84rem;
}
.funnel-table th {
    text-align: left;
    color: #aaa;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    padding: 2px 0 8px 0;
    border-bottom: 2px solid #eeeff2;
}
.funnel-table th:nth-child(2),
.funnel-table th:nth-child(3) { text-align: right; }
.funnel-table td {
    padding: 6px 0;
    color: #333;
    border-bottom: 1px solid #f4f4f6;
    vertical-align: middle;
}
.funnel-table td:nth-child(2) {
    text-align: right;
    color: #bbb;
    font-size: 0.82rem;
}
.funnel-table td:nth-child(3) {
    text-align: right;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
    font-family: ui-monospace, monospace;
}
.hl td {
    background: #eff6ff;
    color: #1e40af;
    font-weight: 700;
}
.hl td:nth-child(2) { color: #93c5fd; }
.caveat {
    background: #f8f9fa;
    border: 1px solid #e2e6ea;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 0.78rem;
    color: #888;
    margin-top: 6px;
}
.interp {
    font-size: 0.82rem;
    color: #444;
    margin-top: 10px;
    padding: 8px 12px;
    background: #f0f4ff;
    border-radius: 6px;
    border-left: 3px solid #4f80e1;
}
</style>
""", unsafe_allow_html=True)

# ── Helper functions ──────────────────────────────────────────────────────────
def pct(v):
    return v / 100.0

def fmt_count(n):
    return f"{round(n):,}"

def fmt_pct_label(v):
    return f"{v:.0f}%"

def fmt_signed_count(n):
    n = round(n)
    if n > 0:
        return f"+{n:,}"
    if n < 0:
        return f"{n:,}"
    return "0"

def fmt_signed_currency(n):
    n = round(n)
    if n > 0:
        return f"+${n:,}"
    if n < 0:
        return f"-${abs(n):,}"
    return "$0"

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown(
    "<h2 style='margin-bottom:2px;'>📈 Activation Revenue Scenario Model</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:0.92rem;color:#555;'>"
    "Interactive version of the Excel model estimating how intake-to-first-visit activation "
    "changes completed visits and revenue impact."
    "</span>&nbsp;&nbsp;"
    "<span style='font-size:0.76rem;color:#bbb;'>"
    "Sample assumptions only. Not Legion internal data. Not a financial forecast."
    "</span>",
    unsafe_allow_html=True
)
st.markdown("<div style='margin-bottom:4px;'></div>", unsafe_allow_html=True)

# ── MAIN LAYOUT ───────────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1.4])

# ══ LEFT COLUMN: Editable Assumptions ════════════════════════════════════════
with left_col:

    # Card header
    st.markdown("""
<div class="card" style="margin-bottom:10px;">
<div class="card-title">Model assumptions</div>
<div class="helper">Change the assumptions below to see how the funnel and revenue impact update.</div>
</div>
""", unsafe_allow_html=True)

    # Funnel volume
    monthly_intake_starts = st.number_input(
        "Monthly intake starts",
        min_value=100, max_value=10000, value=1000, step=100
    )

    # Funnel rates
    st.markdown("<div class='section-label' style='margin-top:6px;'>Funnel rates</div>",
                unsafe_allow_html=True)

    provider_match_rate_pct = st.slider(
        "Provider match reached (%)", 0, 100, 70, 1
    )
    slot_selected_rate_pct = st.slider(
        "Slot selected (%)", 0, 100, 55, 1
    )
    first_visit_booked_rate_pct = st.slider(
        "First visit booked (%)", 0, 100, 45, 1
    )
    first_visit_completed_rate_pct = st.slider(
        "First visit completed (%)", 0, 100, 36, 1
    )
    follow_up_retained_rate_pct = st.slider(
        "Follow-up retained (%)", 0, 100, 60, 1
    )

    # Revenue assumptions
    st.markdown("<div class='section-label' style='margin-top:6px;'>Revenue assumptions</div>",
                unsafe_allow_html=True)

    avg_first_visit_revenue = st.number_input(
        "Average first visit revenue ($)",
        min_value=0, max_value=2000, value=200, step=10
    )
    avg_follow_up_revenue = st.number_input(
        "Average follow-up visit revenue ($)",
        min_value=0, max_value=2000, value=120, step=10
    )

    # Scenario
    st.markdown("<div class='section-label' style='margin-top:6px;'>Improvement scenario</div>",
                unsafe_allow_html=True)

    scenario_label = st.selectbox(
        "Scenario",
        options=[
            "Decline: -10%",
            "Current: 0%",
            "Conservative: 5%",
            "Base: 10%",
            "Optimistic: 15%",
            "Aggressive: 20%",
        ],
        index=3,
        label_visibility="collapsed"
    )

# ── Derived rates (convert sliders to decimals) ───────────────────────────────
provider_match_rate   = pct(provider_match_rate_pct)
slot_selected_rate    = pct(slot_selected_rate_pct)
first_visit_booked_rate    = pct(first_visit_booked_rate_pct)
first_visit_completed_rate = pct(first_visit_completed_rate_pct)
follow_up_retained_rate    = pct(follow_up_retained_rate_pct)

# ── Funnel counts ─────────────────────────────────────────────────────────────
provider_match_count  = monthly_intake_starts * provider_match_rate
slot_selected_count   = monthly_intake_starts * slot_selected_rate
first_visit_booked_count    = monthly_intake_starts * first_visit_booked_rate
first_visit_completed_count = monthly_intake_starts * first_visit_completed_rate
follow_up_retained_count    = first_visit_completed_count * follow_up_retained_rate

# ── Scenario mapping ──────────────────────────────────────────────────────────
scenario_map = {
    "Decline: -10%":    -0.10,
    "Current: 0%":       0.00,
    "Conservative: 5%":  0.05,
    "Base: 10%":         0.10,
    "Optimistic: 15%":   0.15,
    "Aggressive: 20%":   0.20,
}
improvement_rate = scenario_map[scenario_label]

# ── Scenario calculations ─────────────────────────────────────────────────────
current_completed_visits  = first_visit_completed_count
improved_completed_visits = current_completed_visits * (1 + improvement_rate)
change_in_completed       = improved_completed_visits - current_completed_visits
first_visit_revenue_lift  = change_in_completed * avg_first_visit_revenue
follow_up_revenue_lift    = change_in_completed * follow_up_retained_rate * avg_follow_up_revenue
total_monthly_lift        = first_visit_revenue_lift + follow_up_revenue_lift
annualized_lift           = total_monthly_lift * 12

# ══ RIGHT COLUMN: Outputs ════════════════════════════════════════════════════
with right_col:

    # ── CARD 1: Funnel output ─────────────────────────────────────────────────
    st.markdown(f"""
<div class="card">
<div class="card-title">Funnel output</div>
<table class="funnel-table">
  <thead>
    <tr><th>Stage</th><th>Rate</th><th>Count</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Intake starts</td>
      <td>—</td>
      <td>{fmt_count(monthly_intake_starts)}</td>
    </tr>
    <tr>
      <td>Provider match reached</td>
      <td>{fmt_pct_label(provider_match_rate_pct)}</td>
      <td>{fmt_count(provider_match_count)}</td>
    </tr>
    <tr>
      <td>Slot selected</td>
      <td>{fmt_pct_label(slot_selected_rate_pct)}</td>
      <td>{fmt_count(slot_selected_count)}</td>
    </tr>
    <tr>
      <td>First visit booked</td>
      <td>{fmt_pct_label(first_visit_booked_rate_pct)}</td>
      <td>{fmt_count(first_visit_booked_count)}</td>
    </tr>
    <tr class="hl">
      <td>First visit completed</td>
      <td>{fmt_pct_label(first_visit_completed_rate_pct)}</td>
      <td>{fmt_count(first_visit_completed_count)}</td>
    </tr>
    <tr>
      <td>Follow-up retained</td>
      <td>{fmt_pct_label(follow_up_retained_rate_pct)}</td>
      <td>{fmt_count(follow_up_retained_count)}</td>
    </tr>
  </tbody>
</table>
</div>
""", unsafe_allow_html=True)

    # ── CARD 2: Scenario impact ───────────────────────────────────────────────
    st.markdown(
        f'<div class="card"><div class="card-title">Scenario impact — {scenario_label}</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Current completed visits", fmt_count(current_completed_visits))
    with m2:
        st.metric("Change in completed visits", fmt_signed_count(change_in_completed))
    with m3:
        st.metric("Monthly revenue impact", fmt_signed_currency(total_monthly_lift))
    with m4:
        st.metric("Annualized revenue impact", fmt_signed_currency(annualized_lift))

    # Interpretation line
    if improvement_rate > 0:
        interp = "This scenario estimates the upside from improving completed-first-visit activation."
    elif improvement_rate == 0:
        interp = "This scenario shows the current baseline with no assumed activation change."
    else:
        interp = "This scenario shows downside sensitivity if completed-first-visit activation declines."

    st.markdown(
        f'<div class="interp">{interp}</div></div>',
        unsafe_allow_html=True
    )

# ── BOTTOM CAVEAT ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="caveat">
<strong>Caveat:</strong> This dashboard uses sample assumptions from the Excel scenario model.
It is designed for sensitivity analysis, not as a claim about Legion Health's actual performance.
Replace assumptions with internal funnel and revenue data to validate real impact.
</div>
""", unsafe_allow_html=True)
