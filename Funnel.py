import os
import json
import requests
import argparse
from pprint import pprint
import feedparser
import yara




def isMatch(rule, target_path):
    #rule = compiled yara rules
    m = rule.match(target_path)
    if m:
        return True
    else:
        return False

def compileRules(rule_path):
    ruleSet=[]
    for root, sub, files in os.walk(rule_path):
        #print("Compiling Rules")
        for file in files:
            #print("\t"+os.path.join(root,file))
            rule = yara.compile(os.path.join(root,file))
            ruleSet.append(rule)
    return ruleSet


def scanTargetDirectory(target_path, ruleSet ):
    for root, sub, files in os.walk(target_path):
        for file in files: #check each file for rules
            print("\t"+os.path.join(root,file))
            for rule in ruleSet:
                if(isMatch(rule,os.path.join(root,file))):
                    matches = rule.match(os.path.join(root,file))
                    if(matches):
                        for match in matches:
                            print("\t\tYARA MATCH: "+ os.path.join(root,file)+"\t"+match.rule)


def scanTargetLink(target_path, ruleSet ):
    response = requests.get(target_path)
    with open("tmp", "w") as f:
        f.write(str(response.content))

    for rule in ruleSet:
        matches = rule.match("tmp")
        if(matches):
            for match in matches:
                print("Match: "+ str(match))

    # remove tmp file
    os.remove("tmp")

def main():
    art= '''
      \:.     .:/
       \:::::::/ 
        \:::::/ 
         \:::/   
          \:/    
           .  
          .:.   
    '''
    print(art+"Welcome to Funnel\n")

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-u", "--url", help="scan one url instead of using sources list", action="store_true")
    parser.add_argument("rule_path", help="path to directory of rules used on list of feeds")
    parser.add_argument("target_path", help="path to sources list or url")
    args = parser.parse_args()


    #url = "http://feeds.feedburner.com/PaloAltoNetworks"
    url = "https://cooking.nytimes.com/recipes/2868-jordan-marshs-blueberry-muffins"
    #url = "https://adammusciano.com/2018/11/13/coding-livestream-3-let-s-learn-about-yara/"

    


    if(args.verbose): print("Loading rules")
    ruleset = compileRules(args.rule_path)

    if(args.url):
        if(args.verbose): print("Scanning URL...")
        scanTargetLink(args.target_path,ruleset)
    else:
        if(args.verbose): print("Reading from Sources list...")
        with open(args.target_path, "r") as f:
            sources = json.load(f)
            for source in sources["sources-rss"]:
                #print("Feed: "+source["title"])
                #print("\turl: "+source["url"])
                feed = feedparser.parse(source["url"])

                for post in feed.entries:
                    print(post.link)

if __name__ == "__main__":
    main()
