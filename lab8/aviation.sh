#!/bin/bash

# Fetch the METAR data and save it to a JSON file
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# Parse the JSON to extract `receiptTime` values
receipt_times=$(jq -r '.[].receiptTime' aviation.json)

# Print the first six `receiptTime` values
echo "$receipt_times" | head -n 6

