# <a name="header"></a><a name="content"></a><a name="automation-project"></a>Automation Project
## <a name="overview"></a>Overview
This repository contains a **multi‑platform automation framework** built in Python. It exercises different types of applications—including web sites, native mobile apps, REST APIs, Electron desktop apps, Windows desktop programs and a SQLite database—and reports results using the Allure reporting framework. Tests are written with pytest and follow a structured Page‑Object‑Model (POM) and flow layer design. The project is configured via an XML file that specifies parameters for each platform (browser, mobile device, API base URL, Electron app, Windows app and database path)[\[1\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L7-L48).  
Video demo of some of the tests and allure reports - https://drive.google.com/file/d/1maU54kDlFTfmzlX2Fwt1O9th9PQCro-F/view?usp=sharing
## <a name="features"></a>Features
The automation framework is organised into several logical layers. Key features include:

- **Web UI automation** using Selenium WebDriver.<br>Tests cover typical e‑commerce flows such as navigating product pages, verifying top navigation links, filling contact forms and completing purchase checkouts[\[2\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/web_flows.py#L13-L44). Elements are encapsulated in `page_objects/web_objects` modules, and higher‑level actions are defined in the `workflows/web_flows.py` file[\[3\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/web_flows.py#L70-L133).
<br>

- **Mobile automation** using Appium.<br>The mobile flows interact with a sample Android app to verify login, echo screen functionality and list scrolling[\[4\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/mobile_flows.py#L11-L88). The framework reads device information and app package/activity from the XML configuration[\[5\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L19-L28).
<br>

- **API testing** using the ReqRes API.<br>The `workflows/api_flows.py` file contains helper methods to fetch a list of users, retrieve specific user details, create and delete users, and perform login[\[6\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/api_flows.py#L13-L49). Tests verify response codes and extracted values[\[7\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_api.py#L19-L45).
<br>

- **Database testing** with SQLite.<br>Helper methods in `extensions/db_actions.py` support CRUD operations on the users table[\[8\]](https://github.com/NekroenkoS/Automation_Project/blob/master/extensions/db_actions.py#L11-L56). Tests create temporary users, read them back, enforce unique constraint violations and verify update/delete operations[\[9\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_db.py#L21-L47).
<br>

- **Electron application automation** using Selenium and ActionChains.<br>The `workflows/electron_flows.py` file defines steps for creating tasks, assigning colours, filtering by day and verifying counts in a to‑do list app[\[10\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/electron_flows.py#L17-L39). Paths for the Electron executable and driver are configured in the XML file under `<ELECTRON_APP>` and `<ELECTRON_DRIVER>`[\[11\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L37-L40).
<br>

- **Windows desktop automation** using WinAppDriver.<br>Desktop tests interact with the Windows Calculator through DesktopFlows and page objects. Test cases in `test_cases/test_desktop.py` exercise operations such as addition, chained computations, editing with backspace, repeated equals and the negate function[\[12\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/desktop_flows.py#L12-L24)[\[13\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_desktop.py#L10-L28). The application name and driver URL are configured via `<APPLICATION_NAME>` and `<WINAPP_DRIVER_SERVICE>` tags in the configuration file[\[14\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L41-L43).
<br>

- **Allure reporting**.<br>All workflows are annotated with @allure.step to produce detailed reports describing each action (e.g., “Verifying contact form” or “Creating user in DB”). Test titles and descriptions are defined via @allure.title and @allure.description decorators in the test files[\[15\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_web.py#L23-L40).
<br>

## <a name="project-structure"></a>Project structure
Automation\_Project/\
├─ configuration/     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   # Environment configuration (data.xml, database file)\
├─ extensions/       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # Low‑level helpers for UI, DB, API and mobile actions\
├─ utilities/      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      # Common operations (data access, page management, waits)\
├─ page\_objects/   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      # Page object models for web, mobile, electron, desktop\
├─ workflows/       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     # High‑level flows combining actions and verifications\
├─ test\_cases/         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  # PyTest test suites for web, desktop, mobile, DB and API\
└─ …

The framework separates concerns: **extensions** provide atomic actions (click, update text, REST call, DB CRUD), **utilities** manage shared resources and configuration, **page\_objects** encapsulate locators and page‑level operations, **workflows** combine multiple steps into business flows, and **test\_cases** assert expected outcomes.
## <a name="about-this-project"></a>About this project
The Automation Project demonstrates how to build a comprehensive testing framework that exercises multiple layers of a system under test. By combining UI automation for web, mobile, desktop and Electron apps with API and database validation, it showcases best practices such as Page Object Model (POM), separation of concerns between actions and verifications, data‑driven configuration and detailed Allure reporting.

-----
<a name="citations"></a>[\[1\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L7-L48) [\[5\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L19-L28) [\[11\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L37-L40) [\[14\]](https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml#L41-L43) data.xml

<https://github.com/NekroenkoS/Automation_Project/blob/master/configuration/data.xml>

[\[2\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/web_flows.py#L13-L44) [\[3\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/web_flows.py#L70-L133) web\_flows.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/web_flows.py>

[\[4\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/mobile_flows.py#L11-L88) mobile\_flows.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/mobile_flows.py>

[\[6\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/api_flows.py#L13-L49) api\_flows.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/api_flows.py>

[\[7\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_api.py#L19-L45) test\_api.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_api.py>

[\[8\]](https://github.com/NekroenkoS/Automation_Project/blob/master/extensions/db_actions.py#L11-L56) db\_actions.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/extensions/db_actions.py>

[\[9\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_db.py#L21-L47) test\_db.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_db.py>

[\[10\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/electron_flows.py#L17-L39) electron\_flows.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/electron_flows.py>

[\[12\]](https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/desktop_flows.py#L12-L24) desktop\_flows.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/workflows/desktop_flows.py>

[\[13\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_desktop.py#L10-L28) test\_desktop.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_desktop.py>

[\[15\]](https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_web.py#L23-L40) test\_web.py

<https://github.com/NekroenkoS/Automation_Project/blob/master/test_cases/test_web.py>
