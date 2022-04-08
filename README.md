# crypto_currency_trading_bot_simulator_Ubuntu_10

# Crypto_currency_trading_bots


For whoever may wish to experiment with crypto currency pairs without having to invest real money, I hope you find this software useful. 

This software is effectively a Monte Carlo Machine in its own right as it predicts outcomes as a result of random intervention of variables i.e. changes in the price of a giving currecny pair (OHLC). This software encompasses a user interface (UI) along with a trading bot that works in repsonse to one another based off the users actions i.e. making deposits, changing STOP LOSS/PRICE THRSHOLD, restarting/ending the trading simulation, setting timestamp (used to POST to the KRAKEN API to recieve back historical data dating back a given period of time) and so forth. Along with these, the user can view live top 100 most volatile crypto currencies to use as indictor to gauge which crypto to experiment with. The user can also view account holdings and trades history along with a help menu that can be accessed to educate the user/use as a reminder on what various indicators mean/indicate. 

To run this software, instructions are provided below on related modules/imports to download along with the use of commands to navigate on Linux if you wish to run the simulation 24/7 on an Ubuntu instance using G-cloud (removes susceptibility of spontaneous loss of connection to API) i.e. internet connection down/power cut. 

If you do not wish to run 24/7, its simply a matter of cloning this repository; copy and pasting the directory name of the file over to your CLI and running: 
- python main.py 
- main2.py

, where main.py is the UI and main2.py is the trading bot. This is with the notion you already have python installed on your local machine. 

If you wish to adapt upon this software for your own personal use. You're re more than welcome to.

**### Quick pointers:** 

You will notice I have written code related to SVM (support vector machines) where I attempted to incorporate within my trading strategy this machine learning technique, but was unsuccessful giving when implemented within the backend.py file, it did not produce any results i.e. accuracy value/confidence value. Reason being is that SVM's take a short while to create a new vector space to which would be used to map out the values calculated by the indicators. Thus when testing on its own, the accuracy rate at some stages would reach 100% accuracy, but when used within a file with other related processes, it is unable to compute in time during each analyse of the anaylze method which houses our trading strategy. Thus was rendered useless. Alongside this, many of the technical indicators are not used within strategy itself as they impeded on our ability to adapt to changes on a micro scale in the change in price of a given currency pair i.e. XETH vs ZUSD. But are simply used so that you as the user can take down notes and use for your own personal use on how the indictor's change in response to the current state of the market. They can be incorporated within the trading strategy and is simply a matter of implementing the existing methods from the statistical models.py file over to the trading strategy within the backend.py file which I have personally done myself, but found this was more suitable for long term responses in relation to the change in price of a given currency pair where trading events are far less active.

**_Instructions_**

**### How to create Ubuntu instance on Google Cloud Service (free tier)** 
Create a google account if you do not already have one: https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp

Create Google Cloud account: https://cloud.google.com/free

Once Google Cloud account has been created, enable Compute Engine if it's not already enabled and then set up billing if you were not asked to provide card details upon signing up. 

Create a new instance to the closest zone you can find to your local region to reduce latency of input and output when running the trading bot simulator with the machine type f1-micro. Set up the instance as shown in the screenshots:

![image](https://user-images.githubusercontent.com/65728188/161647135-5043de63-fda2-47d9-ba97-d1765dfb1cb4.png)

Finish the server config (make sure you add the max 30GB free disk space) and spin up the server. 

![image](https://user-images.githubusercontent.com/65728188/161647188-9a93a458-e2e4-46b0-b940-b5161ca515df.png)

![image](https://user-images.githubusercontent.com/65728188/161647217-75be077e-0701-4c2a-8caa-253493636a7d.png)

Click the Connect via SSH button to log in and bob is your uncle. 

**### How to setup crypto currency trading bot simulator on G-cloud**

Access Ubuntu instance via G-cloud: 

Requires G-cloud CLI command to run on remote instance from local machine
G-cloud download link: https://cloud.google.com/sdk/docs/install

Once download installed, open gcloud and log in to your google account using your email address. 
This will require you to perform two way authentication i.e. confirm via mobile or over email when trying to sign in. 
Next, we type the command as follows to see if our instances is up and running: 

![image](https://user-images.githubusercontent.com/65728188/161647386-5cc598c4-a907-4229-b058-4bd25c482ff9.png)

![image](https://user-images.githubusercontent.com/65728188/161647401-cbad7738-7edd-42b5-bba0-e1332a94a4f5.png)

We can then type the following to view our instances list:

![image](https://user-images.githubusercontent.com/65728188/161647436-398d542a-84f5-4cbf-b727-57cfee6785b6.png)

We can then log into our Ubuntu instance via the following command: 

![image](https://user-images.githubusercontent.com/65728188/161647489-2538b39a-45b8-4b7d-86a6-73ea592d6dfa.png)

G-cloud will then generate the SSH keys required to have a secure connection to your pc and will store the keys in the instances cache. 

**### SSH connection from google chrome** 
Once all files are loaded to your instance and all relevant modules have been installed. You can open two command shells on chrome to view/run the User Interface and the trading bot. Issues associated with accessing via the terminal emulator on chrome is that you'll experience noticeable latency issues so the trade off is that you will experience poor updates in respects to viewing live events occurring during the running of the simulation. 

It is advised to download the G-cloud CLI to prevent such an occurrence and to experience live trade events without latency issues. 

**### Installing git on ubuntu server**

From your shell, install Git using apt-get: 

sudo apt-get update 

sudo apt-get install git.

**### Verify the installation was successful by typing:** 

git --version : 

$ git --version git version 2.9.2.

**### How to install python 3.10 on Ubuntu server:** 
https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

**### How to install pip (used to install python modules):** 

https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/

List of imports required for project: 

- pip3 install colorama
- pip3 install krakenex 
- pip3 install tabulate
- sudo apt install python3-pandas
- pip3 install pandas_datareader

To run main.py and main2.py use python3 before hand i.e. python3 main.py, python3 main2.py

Where main1.py is the file that runs the UI and main2.py runs the trading bot. Both share data between json files in order to perform operations in response to one another. 

**### To keep programs running after ending ssh sessions:**

sudo apt-get update 

sudo apt-get install screen

Type screen before running file so process (PID) can continue to run 

**### When re-sshing back into instance type:** 

screen -ls, to see if processes are still running. 

**### To re-run a process from where it has last left off within its runtime, simply type:**

screen -r <name of process> 

**### To completely end the process:**
Ctrl 'c' the program

**### To completely remove screen from terminal , enter:** 

screen -X -S [session # you want to kill] quit

You can kill a detached session which is not responding within the screen session by doing the following:

Type screen -list to identify the detached screen session.

~$ screen -list  
    There are screens on:  
         20751.Melvin_Peter_V42  (Detached)  
Note: 20751.Melvin_Peter_V42 is your session id.

Get attached to the detached screen session

screen -r 20751.Melvin_Peter_V42
Once connected to the session press Ctrl + A then type: quit

For further information, refer to this link: 
https://stackoverflow.com/questions/1509677/kill-detached-screen-session

To remove the directory once downloaded including all files if you wish to extend upon the current implementation then re-download onto the your Ubuntu instance, type the following: 

rm -rf crypto_currency_trading_bot_simulator
    
This will recursively remove all files along with the directory that houses the files. 
