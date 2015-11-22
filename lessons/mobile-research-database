---
title: |
    Creating a Mobile Research Database using Open Data Kit
authors:
- Rob Blades
date: 2015-11-22
reviewers:
-
layout: default
---
## Requirements
Before setting up a database, users must have:
  
  1. A Gmail account (you will be using [Google's App Engine](https://appengine.google.com/))
  2. A mobile device or tablet running Android 1.6 and higher. (For other mobile operating systems, such as iPhone's iOS, see the [Open Data Kit FAQ page](https://opendatakit.org/help/faq/) Alternatively, you could use the [emulator set-up page on Open Data Kit github](https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup). The emulator simulates what you would see running Open Data Kit on a mobile device.
  3. A recording app on your mobile device. I purchased [RecForge II Pro](https://play.google.com/store/apps/details?id=dje073.android.modernrecforgepro&hl=en) on the Google Play Store. RecForge allows you to control format, gain, etc. with your audio recordings, as well as view real-time sound frequency waves. There is also a free version of RecForge. In fact, there are many wonderful free recording apps on the Play Store. Shop around!
  4. [Java 7](https://java.com/en/download/) or higher on your computer.
  5. Patience

## Resources
If you want to skip the section on building forms and work with some I have already created, simply download any of these XML files by selecting `Download XML`. Then, in this tutorial, skip **Build your Form** and start at **ODK Aggregate Form Management**. We will be creating a form almost identical to my Soundscapes form for this tutorial.

1. This form is called [ArchiveFever](https://masters-research.appspot.com/www/formXml?readable=true&formId=ArchivesDig). I created it while digitizing documents in the Library and Archives Canada. You take a photo and add metadata in a text box.

2. My other form is called [Soundscapes](https://masters-research.appspot.com/www/formXml?readable=true&formId=SoundResearch). This form works similarly to ArchiveFever. Users can record or upload audio recordings and then add metadata in a text box.

## Lesson Goals
This lesson is meant to be a primer for historians to create their own functioning databases for field work, from the archives, to oral interviews, site work, etc. The beauty of Open Data Kit is its versatility and inherent mobility - Open Data Kit is designed for mobile use by research from all disciplines. In this lesson you will learn how to create a database server using Google's App Engine. While users can deploy Open Data Kit on other servers, this lesson will only focus on using Google's server dashboard. Advanced users can consult the [Aggregate install page](https://opendatakit.org/use/aggregate/#Installing_VM) for more information on other server frameworks.

## What is Open Data Kit and Why Should Historians Use it?
[Open Data Kit (ODK)](https://opendatakit.org) is a cross-platform data management system, meaning it syncs data between desktop, computer server, and mobile applications. ODK uses forms created by users to collect information on a mobile device. These forms can have any number of multiple choice questions, text fields, video, photo, or audio capture, etc. Users create their own form in a spreadsheet editor such as Excel, convert it to the markup language XML, and upload the form to their personal ODK server. Once the form is on the server it will sync across a users devices. The form instructs the mobile app to collect information based on user-defined variables. So if I build a multiple-choice questionnaire form, when I pull it up on the app, it will have the questions ready to check when I use it in the field. The app saves this data and the user sends the final form back to their server. Here they can consult all of the information they collected in the field.

ODK is not limited to historical research. In fact, it is primarily deployed in science and medicine worldwide in a [variety of applications](https://opendatakit.org/about/deployments/), from the International Space Station, to infrastructure management, medical tracking, and election fraud. However, ODK is a tool that historians can deploy widely because it is so versatile

You can see now just how much potential value ODK has for historians. We inevitably deal with large amounts of information from a variety of sources, be they textual, voice, graphical, etc. ODK helps to manage these large swaths of data. To read more about how I deployed ODK for my research, see my post *[Sonifying History Using Open Data Kit](http://bladesrob.com/digital-humanities/odk/)*.

## Getting Started
For this lesson we will use three main ODK tools.
1. ODK's official Android app to collect data into forms: [ODK Collect](https://opendatakit.org/use/collect/)
2. ODK's form management tool, working in tandem with [Google's App Engine](https://appengine.google.com/): [ODK Aggregate](https://opendatakit.org/downloads/download-category/aggregate/)
3. A spreadsheet editor such as Microsoft Excel, Numbers (on Mac OSX), [Libre Office](https://www.libreoffice.org/) or [Google Spreadsheets](https://www.google.ca/sheets/about/) to create forms.

In this lesson we will do the steps a bit differently from ODK's documentation, setting up your server before dealing with forms.

#### **Remember Usernames and Passwords**
**Remember to record any and all usernames/passwords you use in this tutorial. From Gmail to your server login information (AKA ODK Aggregate superuser account). This will save you a lot of frustration throughout the process.**

### Download the App
To begin, download the ODK Collect Android app. The easiest way to get ODK Collect on your Android device is through the [Google Play Store.](https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en) Alternatively, you could refer to the [download page](https://opendatakit.org/downloads/download-info/odk-collect-apk/) to manually install the apk (Android application file).

Once the app is working on your device, you can set it aside. We will deal with it later.

### Create a Server for your Forms and Database
Now, we will use ODK Aggregate to create a server for your forms. You will upload your blank and completed forms on your Aggregate server. ODK's installation instructions are thorough here, though I have provided further explication on certain points.

>1. Make sure Java 7 or higher is installed on the computer you plan to use. If it is not, [download and install it](https://java.com/en/download/). If you are using MacOSX, it may require special care and attention. See [MacOSX Java install](https://docs.oracle.com/javase/7/docs/webnotes/install/mac/mac-jdk.html) and [MacOSX Java FAQ](https://docs.oracle.com/javase/7/docs/webnotes/install/mac/mac-install-faq.html).

>2. You will need a Gmail account to use AppEngine. The way the upload script authenticates to AppEngine is now considered a `less secure application` usage by Gmail. You only need to enable reduced security levels during the running of the upload script (at the very end of the installer). After you have uploaded ODK Aggregate to AppEngine, you can restore the secure settings to your Gmail account. You might want to create one specifically for AppEngine if you are not comfortable with weakening your Gmail security for this brief interval of time; or, perhaps, you have already allowed less secure apps access to your Gmail account, and are therefore already running with weakened security. To weaken your security (or verify your settings), go to [Google MyAccount](https://myaccount.google.com/) and, under the `Signing in` heading, click on `Access for less secure apps` and choose `Turn on`.

**My Notes:** Under `Sign-in and Security` select `Connected apps and sites` and then turn `Allow less secure apps` from OFF to ON.

>3. You'll need to setup an [App Engine account](https://appengine.google.com/). These accounts are free [(under these terms)](https://cloud.google.com/terms/). You may need to be able to receive a text message from Google to verify your account.

>4. If you are creating an App Engine account for the first time, you will be directed to the Google Developers Console. Otherwise, you will on a screen displaying all your existing application ids, and have the option of creating a new application. These two cases are described below:

>| Developers Console (first time) | On that console (1) click on the `Create an empty project option`. (2) Enter your application's title for the Project Name (e.g., 'South Sudan Water Project'), then edit the project ID. (3) The project ID will be your App Engine application Identifier; it determines the url and can never be changed; these are globally unique, so the common ones like `test` will all have been taken. (4) Once you have created the project ID, you can go back to [App Engine Console](https://appengine.google.com/) and see a less cluttered view of your available applications.
| -- | -- |
| App Engine Console (existing/legacy) | On that console (1) click on the `Create Application` button, (2) choose an application identifier (e.g., my-app-id; the Google Developers Console project ID). The application identifier determines your url and can never be changed. (3) enter your application's title (e.g., South Sudan Water Project; Google Developers Console Project Name), and (4) click on `Save`. |

**My Notes:** On the App Engine account page, press the `Create Application button` and then follow the link to the `Google Developers Console`.

{% include figure.html src="../images/mobile-database-DeveloperConsole-ProjectId" caption="The Developer Console will contain your project information" %}

>5. Download [ODK Aggregate v1.N.N](https://opendatakit.org/downloads/). Select the latest Featured release for your operating system. These downloads are wizard-based installers for the various operating systems. If you are running OSX, you must unzip the downloaded file before running the installer within it. If you are on MacOSX Mountain Lion or onward, you will need to fiddle with [GateKeeper settings](http://osxdaily.com/2012/07/27/app-cant-be-opened-because-it-is-from-an-unidentified-developer/) in order to run the installer. Please consider using a non-Featured release during forms development (to help us identify issues prior to a production release).

**NOTE: On the ODK installer, select `Google App Engine`. When creating the ODK Aggregate Username and password, RECORD THIS INFORMATION! You will need it later**

{% include figure.html src="../images/mobile-database-Superuser-Username" caption="Remember to record this superuser information" %}

>6. The installer will guide you through configuring ODK Aggregate for App Engine and then launch a script to upload this configured ODK Aggregate to App Engine. NOTE: Beginning with Java 7 Update 51, there are security level settings [described here](https://www.java.com/en/download/help/jcp_security.xml) that may prevent the upload script from running. A reported work-around is to add the file: path (e.g., file:///) to the Exception Site list. When using a Google account with two step-authentication then the installation using the ODK Aggregate v1.x.0 installers with fail with the message `Unable to update app: Use an application-specific password instead of your regular account`. To over come this you need to enter you Google account name (myaccount@gmail.com) and obtain and use an application-specific password instead of your normal one. See [application-specific password how-to](https://support.google.com/accounts/answer/185833?hl=en).

**My notes:** You will need to add an exception in Java's security settings for the scripts to work. **Mac Users:** In System Preferences, select Java to open the Java Control Panel. Select the tab labeled `Security` and under `Exception Site List` click `Edit Site List.` Here you will add the file path to your ODK Aggregate folder you created earlier. For this tutorial, the exception I created was under `file://users/robertblades/Desktop/ODK Aggregate` Click OK to save and exit the Java Control Panel. **Windows users:** The steps are essentially the same as in Mac: Launch Windows Start menu and click on `Programs` Locate Java and then select `Configure Java` to launch the Control Panel. Under the security tab add an exception to your file path.

{% include figure.html src="../images/mobile-database-JavaExceptionList" caption="Java Exception List" %}

The installer will open your Terminal (MacOSX/Linux) or Command Prompt (Windows) and ask for your Gmail username and password. Enter your email first and then your password. **NOTE:** The Terminal will not show your password as you type. Don't worry. Your computer did not freeze. Just type your password anyways and press enter. Once you have entered the correct login information, let the Terminal run its scripts. **If you fail to add exceptions to your Java, you will get a script failure.**

>7. Finally, after successfully uploading ODK Aggregate to AppEngine, update your Gmail account using the same link in step 2, above, to not allow `less secure applications`.

### Initializing ODK Aggregate
Open your browser and go to [https://appengine.google.com/](https://appengine.google.com/). To go to your dashboard, click the link under `Application`. To go to your personal ODK server, select the link `running` under `Status`. This will open a new tab. Your page will be named `(whatever name you gave the installation).appspot.com/Aggregate.html`.

{% include figure.html src="../images/mobile-database-AppEngine-Running" caption="A List of your AppEngine servers" %}

On the top right, select `Log In`. You will be redirected to a login page. Select `Sign in with Aggregate password` and use the superusername/password from the installation that I begged you to record.

{% include figure.html src="../images/mobile-database-AggregateInitial" caption="You will see this page initially. Login to your superuser account IMMEDIATELY to secure your server" %}

You will be redirected back to the main page. You are now logged in as the site administrator. You will notice that two tabs have been added: `Form Management` and `Site Admin`. Under `Site Admin` you can change user access as you see fit. I left the settings standard.

We will work with Forms underneath the `Form Management` tab. (If you have forms, or want to use any examples I have created, skip ahead to **ODK Aggregate Form Management**.) But first let's build a form!

### Build your Form
For this tutorial we are going to build a form directly in a spreadsheet. If you do not have a spreadsheet editor, you can use [Google Spreadsheets](https://www.google.ca/sheets/about/). In fact, it is easy to turn Google Drive into a [desktop office suite](http://lifehacker.com/how-to-make-google-drive-work-like-a-desktop-suite-1557341520). If you are using Google Spreadsheets, select `File-->Download as-->Microsoft Excel` to get a copy of your form. You can also download [LibreOffice](https://www.libreoffice.org/) for a free spreadsheet editor similar to Microsoft Excel. 

**NOTE** Alternatively, you can build your form through [this drag-and-drop interface](https://opendatakit.org/use/build/). However, I strongly suggest building through XLSForm manually to understand what exactly you are doing.

#### XLSForm
We will be building our form directly from ODK's sample Excel File. [Download it now here](https://opendatakit.org/wp-content/uploads/2013/06/sample_xlsform.xls). For this tutorial, the notes within the sample form will suffice. For extensive documentation on building forms, see the [official XLSForm website](http://xlsform.org/).

Since we will be editing the sample Excel file, I suggest duplicating the file (Mac) or save as a new file (Windows).

XLSForm allows you to create forms with a variety of questions and multi-media complexity. However, for the purposes of this tutorial we will create a simple oral history form. This form is based on my own Soundscape form in the **Resources** section above.

Each form has two required worksheets, `survey` and `choices`. You can choose to include a `settings` worksheet (we will do this below). From XLSForm's documentation:

>The `survey` worksheet has 3 mandatory columns: type, name, and label.
* The `type` column specifies the type of entry you are adding.
* The `name` column specifies the unique variable name for that entry. No two entries can have the same name.
* The `label` column contains the actual text you see in the form.

>The `choices` worksheet has 3 mandatory columns as well: list name, name, and label.
* The `list name` column lets you group together a set of related answer choices, i.e., answer choices that should appear together under a question.
* The `name` column specifies the unique variable name for that answer choice.
* The `label` column shows the answer choice exactly as you want it to appear on the form. Alternatively, label translation columns can be used.

##### Survey
On your worksheet make sure the `survey` tab is selected (bottom left in Excel). (See image below for final text.) Delete the text in all of the fields. Under `type` and `name` add a start and an end.

We do not want our form to just record audio once -- if that was the case we would have to fill out a new form everytime we recorded. To workaround this problem we will 'cushion' our audio recording and metadata between a repeat function. Under `type` add begin repeat and under `name` add image_repeat (ignore the fact that this is an image variable). 

Now we can add audio to this row. Add audio under both `type` and `name`. Under `label` on the same row, add Record audio. This will prompt us in the app to begin recording. 

ODK will output each recording as a date or recording number, depending on the recording app you use. We will want to annotate our audio recordings. Under `type` add text, under `name` add MetaData, under `label` add meta, and under `hint` add Add Meta Data (this will remind us to add text to describe our audio recordings). 

To end this recording and begin the next, under `type` add end repeat.

{% include figure.html src="../images/mobile-database-XLSForm-Survey" caption="Survey Tab" %}

##### Choices
On your worksheet, select the `choices` tab. (See image below for final text.) This section is much easier. I left the sample text in the required columns (list_name, name, and label). This will not effect the oral history form. However, delete the text in the `image` column and `label::chinese` column. 

In a new column, add `audio`. This lets the form know that audio is a choice. Save your file.

{% include figure.html src="../images/mobile-database-XLSForm-Choices" caption="Choices Tab" %}

##### Settings
On your worksheet, select the `settings` tab. Unlike `survey` and `choices`, this section is not required. However, it allows us to name and organize forms on the ODK Aggregate server. (See image below for final text.) `form title` is the title of the form that is shown to users. `form id` is the name used to identify the form submission

Under `form title` add Oral History. Under `form id` add AudioResearch. 

{% include figure.html src="../images/mobile-database-XLSForm-Settings" caption="Settings Tab" %}

Save your form and place it in the ODK Aggregate folder on your computer. 

#### Convert XLS Form to XML
ODK uses [XML, a common markup language](http://www.w3schools.com/xml/xml_whatis.asp) to create working forms across platforms. To create a working form on your mobile device, upload your XLSForm to the [conversion page on the ODK website.](http://opendatakit.org/xiframe/) Because this converter parses data for XML, it notifies you whether or not the form is valid. A valid form will appear green. (**NOTE** a form is valid even if it contains warning notifications in yellow.) An invalid form will appear red, showing you where the error is in your form.

{% include figure.html src="../images/mobile-database-ConversionGreen" caption="Valid with warnings in yellow" %}

{% include figure.html src="../images/mobile-database-ConversionRed" caption="Example of an invalid error message" %}

If successful, download your valid form.

#### Example Error
Because I believe in learning through mistakes, the following is a simple example of an invalid form. Try this to familiarize yourself with mistakes.

Let us imagine that you weren't really paying attention to your form when you were creating it. You excitedly upload your form. But wait! It's invalid? 

{% include figure.html src="../images/mobile-database-ConversionRedWrongXLS" caption="Invalid XLSForm" %}


So you check your form. Spelling mistakes? No. Oh, you forgot to finish the repeat. You wrote `end` when you should have written `end repeat`.

{% include figure.html src="../images/mobile-database-ConversionRedCorrectXLS" caption="Valid XLSForm" %}


Reupload the form and it will be valid.

Remember to watch your spelling and refer to the documentation for exact taxonomy. You have to be careful with computer programming. As a teacher once told me, *Computers are the perfect idiots! They do exactly what you tell them to do.* So make sure you are giving them exact information.

The hard part is over. Now all we have to do is use your form and upload it to your server.

### ODK Aggregate Form Management
Now that you have your form and it has compiled properly, go back to your server. **Remember: Your Server is accessible by** (whatever name you gave the installation).appspot.com. **You can also go back to** [https://appengine.google.com/](https://appengine.google.com/) **and select `running` under `Status`.**

To upload your form, navigate to `Form Management` and then select `+ Add New Form`. Upload the XML form you created in the pervious steps.

## Test Drive your form
Using your form is quite easy.

1. Grab your Android device
2. Open the ODK Collect app
3. In the upper right corner tap the three dots
4. Select General Settings
5. Select Configure platform settings
6. Tap URL and enter the URL of your ODK Aggregate server (https://*yourservername*.appspot.com)
7. Tap Username and Password and enter your superuser login information for your ODK Aggregate server

Now you can go back to the main page of the app. (You can change any of the General or Admin settings as you see fit. However, the default settings should suffice.) Tap Get Blank Form. Select the form(s) you want to download. In the bottom right, tap Get Selected.

If you entered the correct information for your server URL and superuser information, ODK will connect to your server and download any forms you uploaded. If there is an error, check to make sure you entered the correct URL and username/password. 

Tap Fill Blank Form and select the form you want to fill. Follow the on-screen instructions. When you are done each section, swipe right to advance. When you see `Add One More Group` select Add Group to add another recording with metadata. When you are done with the form select Do not Add. You then have the option to Save Form and Exit. 

When you feel you have completed your form, tap Send Finalized Form, select the form you wish to send and in the bottom right tap Send Selected. 

**NOTE:** You can open a new Oral History form and add to it. ODK saves each instance of the form on your server.

## Reap what you Sow
Now that you have saved and sent the form to your server, go back to your Aggregate server (https://*yourservername*.appspot.com). **NOTE: Make sure you are logged into the superuser account.**

The examples in the images below come from my own Soundscapes form, almost exactly similar to the Oral History form we created earlier.

With the Submissions tab selected, navigate to the upper left of the screen where yu see Form and make sure you have the Oral History form selected. Depending on how many instances of the form you uploaded, you're finalized forms will appear in the middle of the screen. Select view to listen to the audio and read the metadata. 

### ODK Briefcase
While we can view our submissions on ODK Aggregate, you may want the audio files downloaded on your computer. For detailed information on issues, customization, etc., [visit ODK's official documentation](https://opendatakit.org/use/briefcase/). 

{% include figure.html src="../images/mobile-database-Aggregate-SubmissionView" caption="By selecting `View` on the submissions page, you can view your form's data" %}

Download ODK Briefcase [here](https://opendatakit.org/downloads/download-info/odk-briefcase/). Navigate to your Downloads folder and double click `ODK Briefcase v1.4.6 Production.jar`. We will be pulling data from your server in this tutorial. 

Make sure you have the `Pull` tab selected. Select Connect next to URL and add your superuser login information and URL for your ODK Aggregate server (*yourservername*.appspot.com). If you entered the correct information it will load your finalized forms to pull. Select you form and in the bottom right select Pull. If successful it will read `SUCCESS!` under Pull Status. 

{% include figure.html src="../images/mobile-database-Briefcase-Pull" caption="ODK Briefcase Pull tab" %}

Now select the `Export` tab in ODK Briefcase. Select Choose next to the Export Directory to decide where you want this data to go. I suggest you make a folder titled `ODK Data`. You can then create subfolders within that for each time you fill in the form. Once your desitination is chosen, select Export in the bottom left. 

Now navigate to your ODK Data folder. Within that folder you will see a media folder and two csv files. Open the `_image_repeat.csv` file with your spreadsheet editor. This file shows you the meta data connected with each recording. Each recording is located in the media folder.

You might want to change the names of each recording to something more human readable. Alternatively, you can pre-record audio on your Android and name the file something human readable. Then, you can choose to upload that recording in the ODK Collect app and tag it with metadata. That way when you export it to your desktop the files attached to the metadata will have human readable titles. Regardless, the csv file remains a reference for each recording. 

### Groups and Teams
You may have noticed options to allow others to download your forms or to submit data collection using your forms. This feature allows you to work with teams locally or across the world. 

Under the Site Admin tab you can also add users and change permissions. Remember, the superuser account grants you admin access over your server.

## Congratulations
You created a functional, cross-platform mobile database for your research! Keep creating forms to fit your needs and don't be afraid to make mistakes! 
