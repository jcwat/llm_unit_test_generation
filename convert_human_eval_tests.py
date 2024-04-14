import json
import re

    
def convert():
    with open("HumanEval.jsonl") as file:
        for line in file:
            instance = json.loads(line)
            filename = "results/humaneval_processed.jsonl"
            with open(filename, 'a') as file:
                instance['test'] = re.sub(r'^.*def check\(candidate\)\:', f"def test_{instance['entry_point']}():", instance['test'], 1, re.DOTALL)
                instance['test'] = instance['test'].replace("candidate(", f" {instance['entry_point']}(")
                file.write(json.dumps(instance))
                file.write("\n")
            
            
            
if __name__ == "__main__":
    convert()