# Publish Facebook Status - Coding Exercise

#### PreRequisites
1. Python3 ([Python/MAC] / [Python/Windows]) 
2. *FB_USERNAME* variable key is set in your system env vars
3. *FB_PASSWORD* variable key is set in your system env vars
4. Python Virtual Environment ([Python Virtual Environment])
4. *ChromeDriver* installed in your Python Virtual Environment ([ChromeDriver])

[Python/MAC]: https://realpython.com/installing-python/#macos-mac-os-x
[Python/Windows]: https://realpython.com/installing-python/#windows
[Python Virtual Environment]: https://docs.python.org/3/tutorial/venv.html
[ChromeDriver]: https://chromedriver.chromium.org/getting-started

#### Setup
1. Clone the repo automation_exercise <br>
`git clone https://github.com/eliran-shani/automation_exercise.git`
2. Create & Activate Virtual Environment <br>
`python3 -m venv .venv`  <br>
`source ./venv/bin/activate` <br>
2. Install requirements.txt `pip3 install -r requirements.txt`
3. Inject ChromeDriver binary into `/.venv/bin` folder


#### Usage

* Run all tests (default chrome browser): <br>
`pytest`

* Run all tests using a specific browser (only chrome supported at the moment: <br>
`pytest --browser chrome`

* Optional Facebook test user: <br>
`username: test_mkwaaug_user@tfbnw.net` / `pass: 1qaz@WSX`

#### Folder structure convention
    .
    ├── attachments                         # All attachments used throghout the test
    ├── common                              # All reuseable functions
    ├── downloads                           # All relevant downloadables while the test is running
    ├── tests                               # All related tests
    ├── .gitignore                          # Github ignore file
    ├── conftest                            # Pytest configuration file
    ├── requirements.txt                    # Python packages required to run this project                           
    └── README.md

 
