\# Lab 5: Static Code Analysis — Blood Donation System



\## 1. Tools Used



\- \*\*Pylint:\*\* Checks Python code quality, naming conventions, documentation, and potential programming errors.

\- \*\*Bandit:\*\* Detects potential security vulnerabilities in Python code.

\- \*\*Flake8:\*\* Checks Python style and formatting.



\## 2. Before-and-After Results



| Tool | Before | After |

|---|---|---|

| Pylint | 4.81/10 | 10.00/10 |

| Bandit | 4 findings: 2 Low, 1 Medium, 1 High | 0 findings |

| Flake8 | 4 style violations | 0 violations |



\## 3. Issues Identified and Fixes



| Issue | Tool | Fix Applied |

|---|---|---|

| Hardcoded officer password | Bandit | Removed the hardcoded credential. |

| Use of `assert` for input validation | Bandit | Replaced it with explicit validation and an exception. |

| Unsafe temporary filename generation using `tempfile.mktemp()` | Bandit | Replaced it with `NamedTemporaryFile`. |

| Shell command execution using `os.system()` | Bandit | Removed shell execution and replaced it with a safer approach. |

| Mutable default argument `notes=\[]` | Pylint | Changed the default to `None` and initialized the list inside the function. |

| Broad exception handling | Pylint | Replaced broad exception handling with explicit validation. |

| Naming convention violations | Pylint | Changed function and variable names to snake\_case. |

| Missing docstrings | Pylint | Added documentation to modules and functions. |

| Line length and spacing violations | Flake8 | Corrected formatting and spacing. |



\## 4. Reflection



\### Q1. Why is static code analysis important?



Static code analysis helps identify code quality issues, style violations, and potential security vulnerabilities without requiring the program to execute. It improves maintainability, readability, and reliability.



\### Q2. What is the difference between Pylint, Bandit, and Flake8?



Pylint checks code quality and programming practices. Bandit focuses on potential security vulnerabilities. Flake8 checks coding style and common formatting violations.



\### Q3. What were the major security issues identified?



The initial analysis identified a hardcoded password, use of `assert` for validation, unsafe temporary file creation using `tempfile.mktemp()`, and shell command execution using `os.system()`.



\### Q4. How were the issues resolved?



The code was modified to use explicit validation, safer temporary file creation, safer notification handling, improved exception handling, better naming conventions, and appropriate documentation. Formatting violations were also corrected.



\### Q5. What were the final results?



Pylint achieved a score of 10.00/10, Bandit reported zero issues, and Flake8 reported zero style violations.



\### Q6. What did you learn from this lab?



I learned how static analysis tools identify different categories of problems, how to interpret their reports, and how to improve code quality and security through systematic fixes and before-and-after verification.



\## 5. Conclusion



Static analysis was performed on the Blood Donation System using Pylint, Bandit, and Flake8. The identified issues were addressed, and the final reports showed improved code quality, no Bandit findings, and no Flake8 violations.

## 6. Viva Preparation

### Q1. What is static code analysis?

Static code analysis is the process of examining source code without executing it to identify potential bugs, security vulnerabilities, and coding-style issues.

### Q2. Why did you use Pylint, Bandit, and Flake8?

- **Pylint:** Checks code quality, naming conventions, and programming practices.
- **Bandit:** Identifies potential security vulnerabilities in Python code.
- **Flake8:** Checks Python formatting and style violations.

### Q3. What is the objective of your project?

The objective was to analyze and improve the quality, security, and maintainability of the Blood Donation Management System using static code analysis tools.

### Q4. What were your final results?

Pylint achieved a score of 10.00/10, Bandit reported zero issues, and Flake8 reported zero formatting errors.

### Q5. What was the hardcoded password issue?

The original program contained a password directly in the source code. Hardcoded credentials can expose sensitive information if the source code is shared. The credential was removed from the source and replaced with environment-variable access.

### Q6. What is a mutable default argument?

A mutable default argument, such as `notes=[]`, can be shared across multiple function calls. This can cause unexpected behavior. Using `None` as the default and creating a new list inside the function avoids this problem.

### Q7. Why is `os.system()` potentially dangerous?

Executing shell commands with user-controlled input can introduce command-injection vulnerabilities. A safer approach avoids constructing and executing shell commands from input.

### Q8. Why is `tempfile.mktemp()` unsafe?

It generates a temporary filename without securely creating the file, creating a risk that another process could use that filename before the program does. `NamedTemporaryFile` provides a safer alternative.

### Q9. What did you learn from this lab?

I learned how to use static analysis tools, interpret their reports, fix security and code-quality issues, and verify improvements by comparing before-and-after results.

### Q10. Why did you create three Git commits?

The lab requires three commits documenting the work. My commits organize the cleaned code, before-and-after analysis reports, and lab documentation.
