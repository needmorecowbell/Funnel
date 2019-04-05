import os
import requests
import argparse
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
        for file in files:
            print("\t"+os.path.join(root,file))
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
    message= '''
      \:.     .:/
       \:::::::/ 
        \:::::/ 
         \:::/   
          \:/    
           .  
          .:.   
    '''
    print(message+"Welcome to Funnel")
    print() 
    compiled_rules = []
    url = "http://feeds.feedburner.com/PaloAltoNetworks"
    url = "https://cooking.nytimes.com/recipes/2868-jordan-marshs-blueberry-muffins"
    url = "https://adammusciano.com/2018/11/13/coding-livestream-3-let-s-learn-about-yara/"
    rule_path = 'rules/'


    print("Loading rules")
    ruleset = compileRules(rule_path)

    print("Scanning Directory ...")
    scanTargetLink(url,ruleset)

if __name__ == "__main__":
    main()
