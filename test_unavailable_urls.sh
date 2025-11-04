#!/bin/bash

# Test all blog posts marked as "no longer available online"

echo "Testing allegedly unavailable blog post URLs..."
echo ""

urls=(
    "https://netstrata.com.au/how-we-can-help-strata-schemes-prepare-for-the-2024-insurance-renewal-season/"
    "https://netstrata.com.au/preparing-for-2025-strata-insurance-renewals/"
    "https://netstrata.com.au/revolutionising-strata-management-introducing-drill-down/"
    "https://netstrata.com.au/independent-review-of-netstrata-setting-the-record-straight/"
    "https://netstrata.com.au/new-options-for-virtual-and-hybrid-agms/"
)

titles=(
    "How We Can Help Strata Schemes Prepare for the 2024 Insurance Renewal Season (Dec 6, 2023)"
    "Preparing for 2025 Strata Insurance Renewals (Oct 30, 2024)"
    "Revolutionising Strata Management – Introducing Drill Down (May 22, 2025)"
    "Independent Review of Netstrata: Setting the Record Straight (Feb 26, 2025)"
    "New Options for Virtual and Hybrid AGMs (Dec 8, 2021)"
)

for i in "${!urls[@]}"; do
    url="${urls[$i]}"
    title="${titles[$i]}"

    echo "[$((i+1))/5] Testing: $title"
    echo "URL: $url"

    status=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    if [ "$status" = "200" ]; then
        echo "✅ STATUS: $status (FOUND - We made an error!)"
    elif [ "$status" = "404" ]; then
        echo "❌ STATUS: $status (Confirmed unavailable)"
    else
        echo "⚠️  STATUS: $status (Unexpected status)"
    fi

    echo ""
done

echo "Testing complete."
