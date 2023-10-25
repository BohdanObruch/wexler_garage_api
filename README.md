# Diploma project on test automation in Python + Selene. 


* UI - https://yedalms.io/
* API - https://yedalms.io/
* Mobile - https://www.booking.com/

## The following functionality is covered
* UI (college admin panel tests)- https://yedalms.io/
    * ✅ Creating an article
    * ✅ Creating a bundle
    * ✅ Creating a course
    * ✅ Creating lessons
    * ✅ Creating a questionnaire(s) 
    * ✅ Creating a feedback form(survey)
    * ✅ Creating a student
    * ✅ Creating a lecturer
    * ✅ Filling the questionnaire with content
    * ✅ Filling the bundle with content

<br>
  
* API tests (college)- https://yedalms.io/
    * ✅ Adding a message to the forum
    * ✅ Signing in
    * ✅ Checking the display of all bundles
    * ✅ Checking the display of all courses
    * ✅ Checking the display of all college lecturers
    * ✅ Checking the display of bandle information
    * ✅ Checking the display of course information
    * ✅ Changing student information
    * ✅ Checking the display of lecturer information
    * ✅ Applying for course registration

<br>

* Android tests - https://www.booking.com/
    * ✅ Creating a list of favorites
    * ✅ Adding homes to favorites
    * ✅ Authorizing in the app
    * ✅ Deleting a place from your favorites
    * ✅ Registering a student 
    * ✅ Searching for attractions
    * ✅ Searching for housing reservations
    * ✅ Search for car rental
    * ✅ Search for cab reservations
    * ✅ Search for travel articles
  
<br>


## The project was implemented using

<p  align="center">
  <code><img width="7%" title="Python" src="resources/images/logo/python.svg"></code>
  <code><img width="7%" title="Selene" src="resources/images/logo/selene.png"></code>
  <code><img width="7%" title="Pytest" src="resources/images/logo/pytest.png"></code>
  <code><img width="7%" title="PyCharm" src="resources/images/logo/pycharm.png"></code>
  <code><img width="7%" title="Requests" src="resources/images/logo/request.png"></code>
  <code><img width="7%" title="Appium" src="resources/images/logo/appium.svg"></code>
  <code><img width="7%" title="Jenkins" src="resources/images/logo/jenkins.png"></code>
  <code><img width="7%" title="Selenoid" src="resources/images/logo/selenoid.png"></code>
  <code><img width="7%" title="Allure" src="resources/images/logo/Allure.svg"></code>
  <code><img width="7%" title="GitHub" src="resources/images/logo/GitHub.svg"></code>
  <code><img width="7%" title="Docker" src="resources/images/logo/docker.svg"></code>
  <code><img width="7%" title="Allure TestOps" src="resources/images/logo/Allure_TO.svg"></code>
  <code><img width="7%" title="Browserstack" src="resources/images/logo/browserstack.svg"></code>
  <code><img width="7%" title="Slack" src="resources/images/logo/slack.svg"></code>
  <code><img width="7%" title="Telegram" src="resources/images/logo/telegram.svg"></code>
  <code><img width="7%" title="Jira" src="resources/images/logo/jira.svg"></code>
  <code><img width="7%" title="Postman" src="resources/images/logo/postman.png"></code>
</p>
<br>

<br>

# <img width="6%" title="Jenkins" src="resources/images/logo/jenkins.png"> Autotests are run on the Jenkins server

<p align="center">
<img src="resources/images/jenkins_job.JPG" alt="Jenkins"/>
</p>
<br>

##  The build parameters in Jenkins:

* TESTS_FOLDER  (Selecting the folder to run the tests)
* BROWSER_VERSION (browser version, the default is 106.0)

<p align="center">
<img src="resources/images/jenkins_params.JPG" alt="Jenkins"/>
</p>
<br>

## Running tests

Local Launch:
```
pytest .
```

Remote launch:
```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest ${TESTS_FOLDER} --browser_version=${BROWSER_VERSION}
```
<br>

# <img width="4%" title="Allure" src="resources/images/logo/Allure.svg"> Allure
> Allure Framework is an easy and flexible multi-language test report tool that not only shows a very concise representation of what have been tested in a neat web report form, but it also gives each team member a possibility to extract maximum of useful information from tests execution.

## Allure overview
> Different charts, metrics and statistics to analyze tests results easily
<p  align="left">
<code>
<img src="resources/images/allure_report.JPG" alt="Allure Report"/>
</code>
</p>

## Allure test result
> Here are the results of test execution.  
<p align="center">
<img src="resources/images/allure_report_more.JPG" alt="Allure Report"/>
</p>
<br>

## <img width="6%" title="Allure TestOps" src="resources/images/logo/Allure_TO.svg"> Allure Testops

## Dashboard 
> Dashboard with the test cases statuses on Allure TestOps
<p align="center">
<img src="resources/images/allure_testops.JPG" alt="Allure Report"/>
</p>

## Test Cases
> Dashboard with statuses of test cases on Allure TestOps
<p align="center">
<img src="resources/images/allure_testops_test_cases.JPG" alt="Allure Report"/>
</p>
<br>


## Allure video result
> An example of a short video how web tests are executed on Selenoid server
<p  align="left">
<code>
<img width="100%" title="Allure video web test" src="resources/video/video_web.gif">
</code>
</p>
<br>

> An example of a short video how mobile tests are executed on Browserstack
<p  align="left">
<code>
<img width="100%" title="Allure video web test" src="resources/video/video_mobile.gif">
</code>
</p>

## <img width="6%" title="Browserstack" src="resources/images/logo/browserstack.svg"> Browserstack
> Mobile test log with results
<p  align="left">
<code>
<img width="100%" title="Browserstack" src="resources/images/browserstack.JPG">
</code>
</p>
<br>

## <img width="6%" title="Jira" src="resources/images/logo/jira.svg"> Integration with Jira
> All tests integrated with Jira to check statuses and activity
<p  align="left">
<code>
<img width="100%" title="Mobile tests" src="resources/images/Mobile.png">
</code>
<code>
<img width="100%" title="WEB UI tests" src="resources/images/Ui.png">
</code>
<code>
<img width="100%" title="API tests" src="resources/images/API.png">
</code>
</p>
<br>

# <img width="6%" title="Browserstack" src="resources/images/logo/telegram.svg"> Telegram notification
> Test results notifications to be sent to the specific telegram channel by the telegram bot
<p align="center">
<img src="resources/images/telegram.JPG" alt="Telegram"/>
</p>

# <img width="6%" title="Browserstack" src="resources/images/logo/slack.svg"> Slack notification
> Test results notifications to be sent to the specific Slack channel by the Slack bot
<p align="center">
<img src="resources/images/slack.JPG" alt="Slack"/>
</p>





