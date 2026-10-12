Simulated Device Monitoring and Alert System
Student Name: Leopardas, Cyrel J.
Student Number: 2601169
Section: 1 CpE-A
Project Description
This Python program monitors simulated device temperature readings using a stored list of values. It classifies each reading as NORMAL, WARNING, or CRITICAL according to the project's temperature rules. It can also accept new valid readings, calculate a numerical summary, and determine the overall monitoring status.
Features
- View all stored temperature readings.
- Add a new temperature reading using whole numbers from 0 to 100.
- Classify each reading as NORMAL, WARNING, or CRITICAL.
- Generate a summary showing the number of readings, total, average, minimum, maximum, category counts, and percentages.
- Determine the overall status as NORMAL, MONITOR, or ATTENTION REQUIRED.
- Reject invalid menu choices and invalid readings.
Requirements
- Python 3
- No external packages are required.
How to Run
1. Open a terminal inside the Week17 folder.
2. Run the program with:
   python device_monitor.py
   On macOS or Linux, use:
   python3 device_monitor.py
Sample Output
The following is the expected output when the program generates a summary using the initial readings [28, 31, 35, 37, 29]:
MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
Test Cases
The project requires 10 tests covering viewing readings, adding a valid reading, rejecting non-numeric and out-of-range inputs, checking the 30°C and 35°C boundaries, generating the summary, rejecting an invalid menu choice, and exiting the program.
Testing result: Enter the number of tests passed and failed after running the program and recording the actual results in test_cases.md. These counts should reflect the tests you really performed.
Full details: see [`test_cases.md`](test_cases.md).
Known Limitations
- The program uses simulated temperature readings; it does not connect to a real sensor or device.
- Readings added during a session are stored only in memory and are lost when the program exits.
- Only whole-number readings from 0 to 100 are accepted.
- The temperature categories are classroom simulation rules and are not real device-safety standards.
Reflection
While completing this project, I learned how to combine lists, loops, conditional statements, functions, and input validation in one program. I learned that checking input before adding it to a list helps prevent errors and incorrect calculations. The most challenging part was handling boundary values correctly, especially 30°C and 35°C, and making sure the overall status prioritizes critical readings. This project also helped me understand why testing and clear documentation are important in programming.