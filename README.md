# Task 1: software configuration.
## “Subtask 1: Why did I choose to participate in the Dare IT Challenge?”

*Why did I decide to participate in the project?* — 
I was looking for a new profession. Stopped the choice on testing. I started training on manual testing courses and at that time I saw an advertisement from DareIT Challenge on automated testing. I thought it would be a great opportunity for me to learn about automation as well. 

*What was driving me?* — Desire to change my life.

*What is your goal?*
+ To get a job as a QA engineer.
+ To understand what I like more — manual or automated testing. 

*What is my expectations for the project?* —
My expectation is to gain new knowledge that will help me get a job.

# Task 2: Selectors 😃
#### Header "Scouts Panel"
- `//*[@id='__next']/form/div/div[1]/h5`
- `//h5`
- `//h5[contains(@class, 'MuiTypography-gutterBottom')]`
- `//*[contains(@class, 'MuiTypography-gutterBottom')]`
- `//*[text()='Scouts Panel']`

#### Input 'Login'
- `//*[@id='login']`
- `//input[@id='login']`
- `//input[contains(@id, 'login')]`

#### Input 'Password'
- `//*[@id='password']`
- `//input[@id='password']`
- `//input[contains(@id, 'password')]`

#### Hyperlink 'Remind password'
- `//*[@id='__next']/form/div/div[1]/a`
- `//a[@tabindex='-1']`
- `//a[contains(@tabindex, '-1')]`

#### Button 'Sign In'
- `//*[@id='__next']/form/div/div[2]/button`
- `//button`
- `//button[@type='submit']`
- `//button[contains(@type, 'submit')]`

#### Dropdown - Language
- `//*[@id='__next']/form/div/div[2]/div`
- `//div[@role='button']`
- `//*[@role='button']`
- `//div[contains(@role, 'button')]`
- `//*[contains(@role, 'button')]`

#### Menu Item 'Polski'
+ `//*[@id='menu-']/div[3]/ul/li[1]`
+ `//li[1]`
+ `//li[@data-value='pl']`
+ `//li[contains(@data-value, 'pl')]`
+ `//li[text()='Polski']`

#### Menu Item 'English'
+ `//*[@id='menu-']/div[3]/ul/li[2]`
+ `//li[2]`
+ `//li[@data-value='en']`
+ `//li[contains(@data-value, 'en')]`
+ `//li[text()='English']`
