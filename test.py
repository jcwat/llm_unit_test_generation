import json

with open("test.json") as file:
    for line in file:
        instance = json.loads(line)
        test = (
                    instance['prompt'] + 
                    instance['canonical_solution'] + "\n" + 
                    instance['test'] + "\n"
                )
        compiled_code = compile(test, "<string>", "exec")
        exec(test)