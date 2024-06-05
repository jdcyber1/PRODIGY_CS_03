# PRODIGY_CS_03
Password Complexity Checker in Python
Overview
The Password Complexity Checker is a Python script designed to assess the strength of a password based on predefined criteria. It evaluates passwords on several factors, including length, presence of uppercase and lowercase letters, numbers, and special characters. The script provides feedback to help users understand how they can improve the strength of their passwords.

Features
Length Check: Ensures the password is at least 8 characters long.
Uppercase Letter Check: Ensures the password contains at least one uppercase letter.
Lowercase Letter Check: Ensures the password contains at least one lowercase letter.
Number Check: Ensures the password contains at least one numeric character.
Special Character Check: Ensures the password contains at least one special character (non-alphanumeric).
How It Works
Criteria Definition: The script defines the necessary criteria for a strong password.
Regex Utilization: Regular expressions are used to check for uppercase letters, lowercase letters, numbers, and special characters.
Strength Calculation: The script calculates the strength of the password based on how many criteria are met.
Feedback Generation: Feedback messages are generated for any criteria that are not met.
Strength Level Determination: Based on the number of criteria met, the script assigns a strength level from "Very Weak" to "Very Strong".
