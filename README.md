# Twitter-Complaint-Bot

Here I have created this python automation project using Selenium which checks your current internet speed and then tweets a complain about the speeds, tagging your internet service provider. 

Steps included:<br>
<ol type='numeric'>
  <li> I initialized different variables which I have used in my further code, they are as follows :<br>
    <ul type='disc'>
    <li>chrome_driver_path: This variable gives the path for where the Chrome driver is stored which is used by Selenium to control the browser, for different browsers different drivers are available.</li> 
    <li>SPEEDTEST_URL: It just stores the url for speedtest webpage.</li>
    <li>TWITTER_LOGIN_URL: It stores the url for Twitter Login Page.</li>
    <li>USERNAME & PASSWORD: This two variables stores your twitter username and password which will be used in program to login into your Twitter account.</li>
   </ul>
  </li>
  <li>Fetch all the website's data in HTML tags form.</li>
  <li>Then I clicked on the go button on the webpage which will start the speedtest and extract the up/down speeds and save into my program.</li>
  <li>Next I logged into my twitter account using the appropriate variables and made the tweet using a customized msg.</li>
</ol>
