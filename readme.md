How to execute pytest and generate allure reports?
    create two directories named allure-reports and allure-results under reports or target folder from the project root.
    python -m pytest --alluredir=reports/allure-results or
    pytest --alluredir=reports/allure-results
    Always save reports to allure-results folder
    To generate report use command line tool  and execute allure serve from the main folder(reports or target)
