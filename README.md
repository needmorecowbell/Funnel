
# Funnel

<p align="center">
    <img src="https://user-images.githubusercontent.com/7833164/55665412-1ca67180-580d-11e9-8e63-c09f83d919da.png" height="150"  width="150"></img>
</p>


Funnel is a lightweight yara-based feed scraper. Give a list of inputs and it will check them periodically. If the article gets matched to the yara rule, it will be put into the database. All matched results get put into an sqlite database, with the rule it flagged. 


## Usage:

```bash
Funnel.py [-h] [-v] [-u] rule_path target_path

positional arguments:
  rule_path      path to directory of rules used on list of feeds
  target_path    path to sources list or url

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
  -u, --url      scan one url instead of using sources list
```


## Contribute

Feel free to add your suggestions for what to add to this project, even better if you give me a pull request!


Inspired by ThreatIngestor from InQuest

