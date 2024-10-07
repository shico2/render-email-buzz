Render Email Buzz v01 by Shico
Tested with Blender versions 3.5 to 4.1


A simple Blender add-on, when active, it sends you an email when a render is complete.

------------------------------------

Using the add-on:

* Before installing the add-on in Blender you need to create a new email that will act as a "sender".
  Creating a new email will eliminate the risk of unwanted access to your personal accounts.

1) head to Gmail and create a new email account.

2) Google "Gmail security" and click on "review settings" then activate "2 Step verification".

3) back in "Gmail security" search results, click on "app password".

4) Generate and new app password and note it down to be used later.


In blender:

5) Go to Edit -> Preferences -> Add-ons -> Install , navigate to where the add-on file was downloaded and select it.
   * Extract the zipped folder and select "render email buzz.py" to install

7) check the box to activate the add-on. and the go find it in the "Properties" panel under "Scene" tab.

8) Scroll down to "Enable Email Notification" and enable it if it is not checked yet.

9) Enter the "Sender" and "Receiver" emails, along with the app password you generated before.

= Now every time a render is complete, you will receive an email.

* If using a different email provider, edit the "SMTP" server in the add-on file using Notepad.

* Un-check the box, to disable the add-on when you want to do quick render tests.

* If you save the file, the details will be saved with the current project. However, if you open a new project you will have to fill the details again.
