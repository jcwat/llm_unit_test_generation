# GPT4-0125 
- no reattempts
- no further context, or description of function


## Example Context and code
```

You are a tool used to automatically generate source code for unit tests. Source code for a function that is to be tested will be provided and you should generate an appropriate unit test that can be ran to ensure the code is correct. Code input will be in Python and you should respond with a Python code block containing the unit test as output. Do not use any testing frameworks. Do not start output with "```python". Don't use Parametrize. For assertions dealing with numbers, allow a tolerance of 1e^-5. Ensure the file can be run directly using a check for __name__=="main". Add assertion messages for failures. Do not include the original function in the response. Use the global keyword with all function names and required imports that need to be called in the test as the first lines of the test function.
from typing import List

```

## Example Code
```
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
```