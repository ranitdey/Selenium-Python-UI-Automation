# UI-Automation-Framework

UI automation framework made with python , selenium and PTest.

## How to run on local:
1. Make sure your system has python 3.0 or > 3.0
2. Clone this project and go to the project directory
3. Create a virtual environment and activate the virtual environment
4. Install the required packages  
```
pip install -r requirements.txt 
```

5. Go to the project directory where test_ui folder is present.
6. Run the tests from terminal
```
ptest3 -t test_ui.tests.test.UITests    
```

This will run all the test cases.


## How to see test results report:

After running all the test cases it will automatically generate the reports and report path can be found in the last 
line. 
Example:
```

====================================================================================================
Test finished in 172.52s.
Total: 45, passed: 45, failed: 0, skipped: 0. Pass rate: 100.0%.

====================================================================================================
Generating xunit report...
Cleaning old xunit report...
xunit report is generated at /Users/ranit/PycharmProjects/Revolut/test-output/xunit-results.xml
Generating html report...
Cleaning old html report...
html report is generated at /Users/ranit/PycharmProjects/Revolut/test-output/html-report
   
   
```

Copy the html report path generated in your terminal and open it in browser.


## Author

[Ranit Dey](https://github.com/ranit-geek)  
