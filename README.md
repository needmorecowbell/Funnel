# Funnel

Funnel is a lightweight yara-based feed scraper. Give a list of inputs and it will check them periodically -- if the request gets matched to the yara rule, it will be put into the database. All matched results get put into an sqlite database, with the rule it flagged. 

Inspired by ThreatIngestor from InQuest
