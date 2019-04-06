# Funnel

**THIS REPO IS IN DEVELOPMENT**

Funnel is a lightweight yara-based feed scraper. Give a list of inputs and it will check them periodically -- if the request gets matched to the yara rule, it will be put into the database. All matched results get put into an sqlite database, with the rule it flagged. 

Inspired by ThreatIngestor from InQuest

**Usage:**

Funnel.py [-h] [-v] [-u] rule_path target_path

positional arguments:
  rule_path      path to directory of rules used on list of feeds
  target_path    path to sources list or url

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
  -u, --url      scan one url instead of using sources list


