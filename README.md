# Automation project according to the Api documentation in swagger in Python and the **request** library. 


## The following functionality is covered by autotests:

### API tests

* Administration 
    * ✅ Administration

* Car Engines
  * ✅ List car engines 
  * ✅ Create car engines post 
  * ✅ Create car engines put 
  * ✅ Details by random engine number 
  * ✅ Update car engines 
  * ✅ Partial update car engines 
  * ✅ Delete car engines 
  
* Cars
  * ✅ List cars 
  * ✅ Create cars post 
  * ✅ Create cars put 
  * ✅ Details by random car 
  * ✅ Update cars 
  * ✅ Partial update cars 
  * ✅ Delete cars
  
* Customers
  * ✅ List customers 
  * ✅ Create customers post 
  * ✅ Create customers put 
  * ✅ Details by random customer 
  * ✅ Update customer 
  * ✅ Partial update customer 
  * ✅ Delete customer 
  
* Kitchen
  * ✅ Brew coffee in coffee maker list 

* Operations
  * ✅ Operations list 
  * ✅ Create operations 
  * ✅ Init operations 
  * ✅ Details by random operations 
  * ✅ Update operations 
  * ✅ Partial update operations 
  * ✅ Delete operations 
  * ✅ Finished operations 
  * ✅ Operations in progress 
  * ✅ Stop operations 

* Payments
  * ✅ Payments list 
  * ✅ Create payments post 
  * ✅ Create payments put 
  * ✅ Payments success 
  * ✅ Read payments 
  * ✅ Update payments 
  * ✅ Partial update payments 
  * ✅ Delete payments 

* Root
  * ✅ Root list

* Services
  * ✅ Services list 
  * ✅ Create services post 
  * ✅ Apply discounts v2 services 
  * ✅ Create services put 
  * ✅ Details by random service id 
  * ✅ Update services 
  * ✅ Partial update services 
  * ✅ Delete services 
  * ✅ Apply discounts services 
  * ✅ Apply discounts for all services 

* User
  * ✅ User login 
  * ✅ Login refreh 


<br>


## The project was implemented using

<p  align="center">
  <code><img width="7%" title="Python" src="resources/images/logo/python.svg"></code>
  <code><img width="7%" title="Pytest" src="resources/images/logo/pytest.png"></code>
  <code><img width="7%" title="PyCharm" src="resources/images/logo/pycharm.png"></code>
  <code><img width="7%" title="Requests" src="resources/images/logo/request.png"></code>
  <code><img width="7%" title="Jenkins" src="resources/images/logo/jenkins.png"></code>
  <code><img width="7%" title="GitHub" src="resources/images/logo/GitHub.svg"></code>
  <code><img width="7%" title="Postman" src="resources/images/logo/postman.png"></code>
</p>
<br>

<br>

# <img width="20%" title="Jenkins" src="resources/images/logo/swagger_logo.svg"> Documentation for APIs and endpoints

<p align="center">
<img src="resources/images/swagger.png" alt="Swagger"/>
</p>
<br>


# <img width="6%" title="Jenkins" src="resources/images/logo/jenkins.png"> Autotests are run on the Jenkins server

<p align="center">
<img src="resources/images/pipeline.JPG" alt="Jenkins"/>
</p>
<br>


## Running tests

Local Launch:
```
pytest .
```
If you uses TMS Testomat:

Add the Testomat variable to the environment variables of the PC
```
set TESTOMATIO=api_key 

pytest --analyzer add 
pytest --analyzer sync
```
Remote launch:
```
python3 -m venv .venv
. .venv/bin/activate
pip install poetry
poetry install
poetry run pytest
```
If you uses TMS Testomat:
```
python3 -m venv .venv
. .venv/bin/activate
pip install poetry
poetry install
TESTOMATIO=api_key pytest --analyzer sync
```
<br>

## Testomat overview
> Here are the results of test execution.  
<p align="center">
<img src="resources/images/test_runs.JPG" alt="Testomat Report"/>
</p>
<br>

## Testomat test result
> Results of running tests with added Report Notifications to email
<p align="center">
<img src="resources/images/screencapture-mail.png" alt="Testomat Report"/>
</p>

## Dashboard 
> Dashboard with the tests on Testomat.io
<p align="center">
<img src="resources/images/dashboard.JPG" alt="Testomat project dashbord"/>
</p>

<br>







