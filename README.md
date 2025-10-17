# eduardo-qa-analyst-assessment
This is my QA Analyst two-part coding assessment.

# QA Analyst Technical Assessment

**Candidate:** Eduardo Magayanes
**Language Used:** Python
**Completion Date:** 10/17/2025

## Part 1: Functional Programming
- **Time Spent:** ~30 minutes
- **Approach:** I created a function called remove_duplicates() that iterates through each element of the input list and builds a new list (new_list) by appending only the elements that haven’t been added before. This ensures that the first occurrence of each element is kept while all subsequent duplicates are ignored, preserving the original order.

## Part 2: API Testing  
- **Time Spent:** ~30 minutes
- **Approach:** I defined a Python class called TestJSONPlaceholderAPI that tests different endpoints of the JSONPlaceholder API. Inside the class, I created three test functions, each demonstrating a different type of API interaction (GET request, POST request, and GET request for a nonexistent user). Each method uses the requests library to perform the API calls and prints the status codes and responses for each of the test functions.

## How to Run
### Part 1
Go to the folder for Part 1:
```bash
cd qa-analyst-assesment/part1-functional
```
Run the Part 1 Python file:
```bash
python3 solution.py
```

### Part 2
Go to the folder for Part 2:
```bash
cd qa-analyst-assesment/part2-api-testing
```
Run the Part 2 Python file:
```bash
python3 solution.py