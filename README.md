## Exploratory Data Analysis - GSS Data
According to an article published by the [Economic Policy Institute](https://www.epi.org/blog/gender-wage-gap-persists-in-2023-women-are-paid-roughly-22-less-than-men-on-average/), the gender wage gap is still there in 2023. On average, women are paid approximately 21.8% less than men. The study took into account various factors such as race, ethnicity, education, age, and geographic location while comparing the pay gap between men and women in the United States. Additionally, another article by the [Pew Research Center](https://www.pewresearch.org/short-reads/2023/03/01/gender-pay-gap-facts/) also highlights that there has been little change in the pay gap in the U.S. over the past two decades. 

The [General Social Survey](https://gss.norc.org/About-The-GSS) (GSS) is a research organization that  surveys adults in the U.S. since 1972.  According to [Wikipedia](https://en.wikipedia.org/wiki/General_Social_Survey), the GSS was created by the National Opinion Research Center (NORC) at the University of Chicago and is funded by the National Science Foundation.  GSS collects data on demographic, behavioral, attitudinal trends and topics of special interest.  The GSS conducts extensive research to provide high-quality data to scholars, students, policy-makers and other audiences.  The GSS is widely regarded as one of the best sources of data on social trends.



## Deploying the Dashboard Using a Free Hosting Service
If you want to distribute your dashboard to an audience, with a manager, or with a client, sharing a URL that links to the dashboard is better than sharing a notebook or a Python script file. The best free service for hosting dashboards is called [Heroku](https://www.heroku.com/home). It can be challenging to get a dashboard running on Heroku, but once you do, your dashboard will be accessable with a URL of the form *yourappname*.herokuapp.com. For example, the ANES dashboard we designed above is available at https://anespilot2019.herokuapp.com/.

If you want to deploy an app, the following steps worked for me.

1. Make sure you have an account on [GitHub](https://github.com/). If you have an account, sign in. If you don't, create a [new Github account](https://github.com/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home).

2. Navigate to my GitHub repo for the ANES Heroku app: https://github.com/jkropko/dash-heroku-template

3. Push the button marked "Fork" in the upper-right corner of the screen. This button creates a copy of the repository under your own GitHub account. This copy belongs to you and you can manipulate it as you see fit. Just make sure you are working with your copy, not mine, by making sure your username appears in the upper-left corner and not "jkropko".

4. Collect all of the code needed to run an app, including the package import, data loading, and cleaning steps, and the code to generate the individual elements that populate the dashboard. Start a new Jupyter notebook and paste all of this code into a single cell. If you used `jupyterdash`, change the code to regular `dash` by changing `app = dash.Dash(__name__, external_stylesheets=external_stylesheets)` to `app = JupyterDash(__name__, external_stylesheets=external_stylesheets)` and `app.run_server(mode='inline', debug=True)` to `app.run_server(debug=True)`. 

5. If your code depends on any local files, upload these files to your new GitHub dash-heroku-template repository by clicking Add File and Upload Files, then pressing Commit. You will then see these files on the main page of the repository. Click on the file you want to use in your code, then click on raw. Copy the URL and paste it into your code wherever you are loading the file. That ensures that all of the code can work 100% online without any need for local storage on your computer. 

6. Run the cell that contains all of your code, and make sure it runs without any errors.

7. On your copy of the dash-heroku-template GitHub repo, click on "app.py". You will see Python code for creating a `dash` app. Press the pencil button to edit this file. Copy your code from step 6 and replace the code in this file with your own code.

8. On your dash-heroku-template page, click on "requirements.txt". If you are using any Python packages that are not already listed here, add them. Set them to be greater than or equal to the version number of the package you are using. (To check on the version number of a package, type `pip show` and the package name.) Leave the other files alone.

9. Go to https://www.heroku.com/home and sign up for a free account.

10. Once you are signed up and arrive back at the main page, click on the button in the upper-right with three horizontal bars. Click on "Dashboard". On the Dashboard page, click "New" and "Create new app".

11. Choose a name for your app. This name has to be unique from among all of the apps that are hosted on Heroku. Choose a descriptive but short name for the app.

12. Under "Deployment Method" select GitHub. Type dash-heroku-template in the repo search bar. It should appear below with a button marked "Connect". Press this button.

13. Under "Manual Deploy" click on Deploy Branch. Wait a couple minutes for Heroku to parse all of the code on your GitHub repo. 

14. With any luck, you will see a message that reads "Your app was successfully deployed." Click on View and it will take you to the URL for your app. If you can see your code, congratulations, your app is live and you can share this URL.

If your app encountered an issue, click on More in the upper-right corner of the dashboards screen, and click View Logs. That will take you to the output Heroku provides while attempting to launch your app. If there are any error messages you will see them here and you can try to debug your code. To make changes to your app, edit the "app.py" document on your dash-heroku-template GitHub repo. Once you commit these changes, your Heroku app will relaunch with the new code automatically.
