def infection_risk_alert(infection_rate):
    if infection_rate > 0.1:
        return "🔴 High infection risk – isolate suspected patients"
    elif infection_rate > 0.05:
        return "🟠 Moderate risk – increase hygiene protocols"
    else:
        return "🟢 Low infection risk"
def estimate_infection_rate(day):
    if day < 60:
        return 0.03   # low risk
    elif day < 120:
        return 0.06   # moderate
    elif day < 180:
        return 0.09   # high
    else:
        return 0.12   # very high

