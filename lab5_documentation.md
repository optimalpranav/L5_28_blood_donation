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

