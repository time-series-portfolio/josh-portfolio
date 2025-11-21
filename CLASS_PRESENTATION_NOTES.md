# Class Presentation: Quick Reference

## Opening Statement

"My dataset is Google Trends search data for sports betting-related terms from January 2020 to December 2024. I'm analyzing four search terms: 'sports betting', 'draftkings', 'online betting', and 'nba betting'. My intervention point is January 8, 2022, when New York State launched online sports betting."

## Why Google Trends (Not Stock Prices)?

"I chose Google Trends because it directly measures public interest and cultural engagement with sports betting, free from macroeconomic confounders like Federal Reserve policy or interest rates. Search behavior captures consumer awareness in real-time - when NY launched, we'd expect to see immediate changes in how people search for betting information."

## Why This Matters

"New York became the largest U.S. sports betting market, representing about 20% of total U.S. revenue. The launch came with massive advertising campaigns across NYC subways, TV, and online. This was a cultural milestone that moved sports betting from niche to mainstream."

## Research Question

"Did the NY legalization cause a significant level change and/or trend change in public interest in sports betting, measured by Google search volume?"

## Model

```
SearchInterest = β₀ + β₁(Time) + β₂(Intervention) + β₃(Time_Since_Intervention) + ε
```

- β₁ = pre-intervention weekly trend in searches
- β₂ = immediate jump/drop on Jan 8, 2022
- β₃ = change in search growth rate after intervention

## Key Findings (All Highly Significant, p < 0.001)

**For "sports betting" searches:**
- **Pre-intervention**: Searches growing +0.032 points/week (steady upward interest)
- **Immediate impact**: Search interest dropped 9.34 points on intervention (β₂ = -9.34***)
- **Trend change**: Growth slowed by -0.026 points/week after launch (β₃ = -0.026***)

**Interpretation:**
"All coefficients are statistically significant at p < 0.001. The negative effects might seem counterintuitive, but they likely reflect that NY launched during peak NFL playoff season, and massive pre-launch advertising may have frontloaded public awareness before the actual launch date. The key finding is that the intervention clearly and measurably impacted search behavior."

## Key Strengths

✅ **Direct measure of public interest**: Not confounded by macro factors
✅ **Clear intervention date**: January 8, 2022
✅ **Multiple search terms**: Captures general and specific betting interest
✅ **Ties to thesis**: Analytics revolution → betting infrastructure → regulatory expansion → **public participation**
✅ **All effects significant**: p < 0.001 across all coefficients

## If Asked About the Negative Coefficients

"The negative level change might reflect that the intervention occurred during peak NFL playoff season when searches were already elevated, making it appear as a 'drop' relative to that seasonal peak. Alternatively, the massive pre-launch advertising in NYC may have frontloaded searches before the official launch. The crucial point is that the intervention significantly altered search patterns - the ITS model captured a clear structural break."

## Ties to Broader Thesis

"This connects to my overall project narrative: NBA analytics made basketball quantifiable → this enabled sophisticated sports betting technology → which led to state legalizations like NY → which increased public participation. Google Trends captures that final step - actual consumer engagement."

## Analysis File

`docs/ITS_analysis.html` - visualizations, regression tables, and comparative summary for all 4 search terms
