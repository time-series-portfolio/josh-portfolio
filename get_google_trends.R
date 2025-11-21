# Script to download Google Trends data for sports betting terms
# Time period: 2020-01-01 to 2024-12-31
# Geographic focus: United States

library(gtrendsR)
library(tidyverse)
library(lubridate)

# Define search terms
terms <- c(
    "sports betting",
    "draftkings",
    "online betting",
    "nba betting"
)

# Download data for each term (Google Trends allows max 5 terms at once)
# We'll do them separately to ensure daily granularity
all_trends <- list()

for (term in terms) {
    cat("Downloading:", term, "\n")

    # Get trends data
    trends <- gtrends(
        keyword = term,
        geo = "US",
        time = "2020-01-01 2024-12-31",
        onlyInterest = TRUE
    )

    # Extract interest over time
    if (!is.null(trends$interest_over_time)) {
        df <- trends$interest_over_time %>%
            select(date, hits, keyword) %>%
            mutate(
                date = as.Date(date),
                hits = ifelse(hits == "<1", "0", hits),
                hits = as.numeric(hits)
            )

        all_trends[[term]] <- df
    }

    Sys.sleep(2)  # Pause to avoid rate limiting
}

# Combine all trends
combined_trends <- bind_rows(all_trends)

# Save to CSV
write_csv(combined_trends, "data/google_trends/sports_betting_trends.csv")

cat("\n✓ Successfully downloaded Google Trends data\n")
cat("  Saved to: data/google_trends/sports_betting_trends.csv\n")
cat("  Terms:", paste(terms, collapse = ", "), "\n")
cat("  Date range:", min(combined_trends$date), "to", max(combined_trends$date), "\n")
cat("  Total rows:", nrow(combined_trends), "\n")

# Preview the data
head(combined_trends, 20)
