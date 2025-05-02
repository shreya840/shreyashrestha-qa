WEB UI Testing for Katalon Demo Cura Healthcare
I created automated tests for the Cura Healthcare website I did some manual testing and created some test cases before automation testing. I used Selenium WebDriver with Python to check different parts of the website, like logging in, viewing products, and the checkout process. This helped me learn how to use Selenium to test websites and ensure they work correctly
I used the following tools such as 
Python: The programming language used to write the test scripts.
Selenium WebDriver: The library used to interact with the web browser.
PyCharm: The Integrated Development Environment (IDE) used for writing and running the Python scripts.
Microsoft Edge: The web browser used for executing the automated tests.
XPaths Used:
1.	//a[text()='Login'] - This XPath locates the link (<a> tag) whose visible text content is exactly "Login". 
2.	//input[@id='txt-username'] - This XPath locates the input element (<input>) that has an attribute id with the value "txt-username". 
3.	//input[@name='password'] - This XPath locates the input element (<input>) that has an attribute name with the value "password". 
4.	//button[@id= 'btn-login'] - This XPath locates the button element (<button>) that has an attribute id with the value "btn-login". 
5.	//select[@id='combo_facility'] - This XPath locates the select element (<select>), which is typically a dropdown list, that has an attribute id with the value "combo_facility". 
6.	//input[@id='chk_hospotal_readmission'] - This XPath locates the input element (<input>) that has an attribute id with the value "chk_hospotal_readmission" (likely a checkbox). 
7.	//input[@id='radio_program_medicaid'] - This XPath locates the input element (<input>) that has an attribute id with the value "radio_program_medicaid" (likely a radio button). 
8.	//input[@id='txt_visit_date'] - This XPath locates the input element (<input>) that has an attribute id with the value "txt_visit_date". 
9.	//textarea[@id='txt_comment'] - This XPath locates the textarea element (<textarea>) that has an attribute id with the value "txt_comment". 
10.	//button[@id='btn-book-appointment'] - This XPath locates the button element (<button>) that has an attribute id with the value "btn-book-appointment". 
11.	//a[@class='btn btn-default'] - This XPath locates the link (<a> tag) that has an attribute class with the value "btn btn-default".
