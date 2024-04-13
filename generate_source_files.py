import sys
import os
import json

def create_file(project_dir, instance):
    filename = f"{project_dir}/test_{instance['task_id'].replace('/','').lower()}.py"
    with open(filename, 'w') as file:
        coverage_excluded_test = instance['test'].replace("\n"," # pragma: no cover\n",1).replace("\"__main__\":\n", "\"__main__\": # pragma: no cover\n")
        test = (
            instance['prompt'] + 
            instance['canonical_solution'] + "\n" + 
            coverage_excluded_test + "\n"
        )
        file.write(test)
    
    
    
def create_project(filename):
    with open(filename) as file:
        project_name = os.path.basename(file.name).replace(".jsonl", "")
        project_dir = f"projects/{project_name}/src"
        os.makedirs(project_dir)
        for line in file:
            instance = json.loads(line)
            create_file(project_dir, instance)
            
            
            
if __name__ == "__main__":
    create_project(sys.argv[1])