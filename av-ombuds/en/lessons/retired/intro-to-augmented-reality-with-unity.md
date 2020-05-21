---
title: Introduction to Mobile Augmented Reality Development in Unity
layout: lesson
date: 2016-07-24
authors:
- Jacob W. Greene
reviewers:
- Jason Crider
- Fred Gibbs
- Sean Morey
editors:
- Fred Gibbs
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/17
activity: presenting
topics: [website,mapping]
abstract: "This lesson serves as an introduction to creating mobile augmented reality applications. Augmented reality (AR) can be defined as the overlaying of digital content (images, video, text, sound, etc.) onto physical objects or locations, and it is typically experienced by looking through the camera lens of an electronic device such as a smartphone, tablet, or optical head-mounted display."
retired: true
retirement-reason: |
  Unity recently changed several of its components, so this lesson was rendered out of date. An [updated lesson on augmented reality in Unity is now available](/en/lessons/creating-mobile-augmented-reality-experiences-in-unity).

  [See further discussion about this retirement decision.](https://github.com/programminghistorian/jekyll/issues/717)
redirect_from:
  - /lessons/intro-to-augmented-reality-with-unity
  - /lessons/deprecated/intro-to-augmented-reality-with-unity
doi: 10.46430/phen0053
---

{% include toc.html %}





This lesson serves as an introduction to creating mobile augmented reality applications. Augmented reality (AR) can be defined as the overlaying of digital content (images, video, text, sound, etc.) onto physical objects or locations, and it is typically experienced by looking through the camera lens of an electronic device such as a smartphone, tablet, or optical head-mounted display (e.g. Microsoft Hololens). Although AR is a cutting-edge, complex technology, there are a number of user-friendly platforms that allow people with no previous coding experience to create compelling augmented reality experiences.

## Lesson Goals

In this introductory tutorial, you will learn how to:

* setup the Unity game engine for augmented reality development
* convert images to trackable data sets
* add overlays to trigger images
* build standalone augmented reality applications to Android and iOS devices

## How can Humanists use Augmented Reality?

Novel applications of AR continue to surface  within a variety of industries: [museums](https://www.youtube.com/watch?v=gx_UQxx54lo) are integrating AR content into their displays, [companies](http://www.gizmag.com/ikea-augmented-reality-catalog-app/28703/) are promoting AR apps in lieu of print or even web-based catalogs, and [engineering firms](https://www.youtube.com/watch?v=bXqe2zSepQ4) are creating AR applications showcasing their efforts to promote sustainability. [Predicted to grow](http://www.digi-capital.com/news/2015/04/augmentedvirtual-reality-to-hit-150-billion-disrupting-mobile-by-2020/#.VbetCU1VhHw) into a $120 billion industry within the next five years, augmented reality is an exciting new medium that humanists cannot afford to ignore. Indeed, many scholars within the growing field of digital humanities are beginning to explore how AR can be utilized as a viable medium of scholarly engagement within public spaces, objects, images, and texts.

{% include figure.html filename="new-ar-dev-1.png" caption="Augmented reality can be used to overlay digital information onto existing texts such as historical markers. This modified image is based on a photograph by Nicholas Henderson." %}

Since at least 2010, [digital artists](https://manifestarblog.wordpress.com/about/) have been creating AR applications for social advocacy and cultural intervention. For example, Tamiko Thiel's AR project [Clouding Green](http://www.tamikothiel.com/AR/clouding-green.html) reveals the carbon footprint of specific technology companies. Projects such as Thiel's capitalize on AR's unique rhetorical affordance to provide compelling, site-specific interactions between physical and digital spaces.

At the [Trace Initiative](http://web.archive.org/web/20180421163517/http://english.ufl.edu/trace_arcs/), a digital humanities organization in the University of Florida English Department, we seek to build upon the work of these artists by promoting the creation and circulation of humanities-focused mobile AR applications. We released our first AR application [to the Google Play store](https://play.google.com/store/apps/details?id=com.Trace.Dollars&hl=en) in spring 2016.

The augmented reality software used in this tutorial relies on image-recognition technology, meaning that it requires some kind of visual trigger (a logo, painting, etc.) to know when to display digital content. In the example application depicted in the image above, the application is programmed to only display the digital image of John C. Calhoun if the camera "recognizes" the specific historical marker with which it is associated. For this lesson, we will augment the cover of a physical book with a digital overlay that displays a picture of the author. You could use the technical skills gained throughout this tutorial to create digital overlays for a variety of texts such as historical documents or signs. For example, you might create an application that allows readers to scan the pages of a book or document and access historical context or critique related to that specific page. Humanities scholars could also use this tutorial to create site-specific AR applications to educate visitors about cultural aspects of a location that have been excluded from its historical presentation.

## A Note About AR Creation Platforms

Unity is a very powerful and complex application used to create desktop, console, and mobile games. It is not designed exclusively for augmented reality development.As a result, this lesson has many detailed, albeit necessary, steps for navigating and operating the Unity interface. Although some of the steps might not be directly related to augmented reality development, they are certainly transferrable to other tutorials on Programming Historian or elsewhere that utilize Unity. If you would prefer to gain some familiarity with the Unity Editor prior to completing this lesson, I would suggest consulting [Unity's beginner tutorial videos](https://learn.unity.com/tutorial/live-sessions-on-unity-interface-and-essentials) and the online [Unity manual](http://docs.unity3d.com/Manual/LearningtheInterface.html).

Within Unity, you can access additional functionality by importing "extensions." It is common to import extensions into Unity to gain access to additional functionality and/or pre-designed game components such as characters or game props. The extension used within this lesson is called "Vuforia," and it will provide the code necessary to create AR applications within the Unity game engine. I discuss how to download Unity and import the Vuforia extension in the section labelled "Software Requirements."

However, before you decide to dive into AR development in the Unity interface, it is important to understand that there are other (much simpler) AR creation platforms available, such as [Aurasma](https://www.aurasma.com/). Aurasma is a simple, drag-and-drop AR creation studio that allows users to augment images with digital content.

{% include figure.html filename="ar-dev-1-16.png" caption="With Aurasma, you can overlay multimedia content such as videos over the pages of a book." %}

Aurasma is a fantastic AR creation platform that can be learned fairly quickly. I would highly recommend it for classroom usage and for smaller projects with simple multimedia overlays such as images or short videos. However, online creation platforms like Aurasma have their limitations. When you create an overlay in Aurasma, users can only access it through the Aurasma application. This leaves the AR creator with no control over the design of the application interface. Moreover, Aurasma requires users to have an internet connection when accessing the application, which makes it difficult to create site-specific AR applications in places where there is little to no internet connectivity. With Vuforia, however, you can create stand-alone AR applications that can be downloaded and stored in the mobile device's memory and thus do not require that users to have internet access. Consult the table below to help you decide which platform is best suited for your AR development needs.

|            | Aurasma                                                     | Unity/Vuforia                                                                                                      |
| ---------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Type**   | online platform                                             | computer program                                                                                                   |
| **Use**    | small projects with simple overlays                         | large projects with complex overlays, site-specific applications                                                   |
| **Pros**   | users can instantly access overlays, no coding required     | create standalone applications, more control over interface design, overlays load quickly                          |
| **Cons**   | file size limits for overlays, requires internet connection | steeper learning curve, must upload completed application files to Google Play or Apple Store for others to access |
| **Access** | [Aurasma Studio](https://www.aurasma.com/)                  | [Unity](https://unity3d.com/get-unity/download/archive) [Vuforia](https://developer.vuforia.com)                   |

## Software Requirements

For this lesson, you will need to download the following software applications and SDKs (software development kits). Several of the applications used in this tutorial (Unity and Android SDK) are very large and will take some time to download and install. You might want to complete the downloads section of this tutorial while working on something else. All of the steps in this lesson can be completed using either the free or paid versions of the software.

* Unity
* Vuforia SDK
* Java Development Kit
* Android SDK Tools (if testing on an Android device)
* Xcode (if testing on an iOS device)

### Unity

* [Download Unity for Windows](https://unity3d.com/get-unity/download/archive):

If you are working on a 32-bit Windows computer, skip down to "Installing the 32-bit Unity Editor." Otherwise, select the "Unity Installer" option from the latest version of Unity in the "Downloads (Win)" dropdown menu. Unity will download the "UnityDownloadAssistant" application to guide you through the installation process. Launch this application after it downloads and follow the instructions. On the "Choose Components" page, make sure that the options for "Android Build Support" and "Windows Build Support" are both selected.

Installing the 32-bit Unity editor: Download and install the 32-bit Unity Editor from the [Unity Download Archive](https://unity3d.com/get-unity/download/archive). Then, return to the Unity Download Archive and download the Unity Installer. When you get to the "Choose Components" page, deselect everything except for "Android Build Support" and "Windows Build Support."

{% include figure.html filename="ar-dev-2-1.png" caption="Check the options for Android and Windows Build Support." %}

* [Download Unity for Mac](https://unity3d.com/get-unity/download/archive)

Select the "Unity Installer" option from the latest version of Unity in the "Downloads (Mac)" dropdown menu. Unity will download the "UnityDownloadAssistant" application to guide you through the installation process. Launch this application after it downloads and follow the instructions. On the "Choose Components" page, make sure that the options for "iOS Build Support" and "Mac Build Support" are both selected.

Start Unity and follow the setup prompts. If Unity asks if you are creating a personal or professional account, choose personal account.

### Vuforia SDK

[Download the latest Unity package from the Vuforia Developer Portal](https://developer.vuforia.com/downloads/sdk). Scroll down to the bottom of the Terms of Service Agreement to download the package.

In order to use Unity for augmented reality development, you will need access to the "Download for Unity" extension created by Vuforia. Before you can download the Unity package, Vuforia will ask you to create a user profile. This is different from the user profile that you just created for Unity. Write down your username and password because you will need them later to access other areas of the Vuforia developer website.

Next, you will need to import the augmented reality package you just downloaded from the Vuforia website into Unity. Return to Unity and go to the menu panel in the top left. Select "Assets > Import Package > Custom Package" and open the Unity extension you just downloaded from the Vuforia developer portal. A small screen will pop up listing the file contents for the Vuforia package. Click "Import."

{% include figure.html filename="ar-dev-3.png" caption="Import Vuforia's augmented reality package." %}

### Java Development Kit

Download and install the [Java Development Kit](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) for your operating system.

{% include figure.html filename="ar-dev-1-9.png" caption="Download the .exe file for your operating system." %}

Click on the file once it has finished downloading, and follow the installation guide.

### Android SDK Tools (only if testing on an Android device)

There are two options for downloading the Android SDK Tools:

* Download and install [Android Studio](https://developer.android.com/studio/index.html). Android Studio is the official IDE (integrated development environment) for creating Android applications. However, keep in mind that Android Studio is a very large program that will take longer to download, so only take this option if you are interested in developing other mobile applications with Android. If you take this option, follow the instructions in the download assistant.

* Alternatively, you can download just the [Android command line tools](https://developer.android.com/sdk/index.html#Other), which will give you access to the Android SDK but not the Android Studio IDE. if you take this option, scroll down on the Android Studio download page until you see a section labelled "Get just the command line tools."

{% include figure.html filename="new-ar-dev-27.png" caption="Download the Android command line tools that are compatible with your operating system." %}

Click on the file once it has finished downloading, and follow the installation guide. Start the SDK manager after installation.  Install any packages that are automatically selected, but make sure that the "Android SDK Platform-tools" and "Android SDK Build-tools" options are both selected. Then, scroll down to the folder labelled "Extras" and select the "Android Support Repository" and "Google USB Driver." Click "Install packages."

{% include figure.html filename="ar-dev-1-14.png" caption="Install packages within the Android SDK manager." %}

If you are trying to install the Android packages but keep getting an error about "temp" folders not being created, close the manager and go to the "android-sdk" folder on your computer. Right click the "SDK Manager" application file and select "Run as administrator."

{% include figure.html filename="ar-dev-1-13.png" caption="Start the Android SDK manager." %}

### Xcode

Because Vuforia [no longer supports](https://developer.vuforia.com/forum/unity-extension-technical-discussion/unity-invalid-pbx-project) building Xcode projects with the Windows version of Unity, you cannot test your application on an iOS device if you are working on a Windows computer. In order to build iOS applications with Unity, you need 1) an apple device (iPhone, iPad, etc.) running iOS 9 or later and 2) a Mac running OS X 10.10.5 or later. If you meet these technical requirements, download [Xcode 7 or later](https://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12) from the Apple app store.

## Connect the Android SDK and Java Development Kit to Unity

In Unity, go to "Edit > Preferences > External Tools" and point Unity to the file locations for the Android Tools (Android SDK) and Java Development Kit (JDK) you just installed. If you do not see options for adding the Android SDK and Java SDK, then you will need to close Unity and restart the Unity Download Assistant and make sure that "Android Build Support" is selected on the "Choose Components" page.

{% include figure.html filename="ar-dev-1-10.png" caption="Restart the Unity Download Assistant." %}

{% include figure.html filename="ar-dev-1-11.png" caption="Check the Android Build Support option. Check the iOS Build Support option if you working on a Mac." %}

Unity should automatically detect the location of the Java Development Kit once it has finished installing. If it does not, restart Unity and go to "Edit > Preferences." Select the "External Tools" and make sure that the "JDK" field is pointing to the Java Development Kit. Click the "Browse" button next to the JDK field and select the "jdk[version number]" folder in the "C:/Program Files/Java" folder. Leave the "NDK" field blank.

In the External Tools dialogue box in Unity, click the "Browse" button next to the "SDK" field and point it to the "android-sdk" folder on your computer. If you downloaded the SDK through the Android Studio IDE, this folder will be located in "C:/Program Files/Android" folder. If you downloaded just the command line tools, it will be in this folder: "C:/Users/[your username]/AppData/Local/Android."

{% include figure.html filename="new-ar-dev-29.png" caption="Connect the Android SDK Tools and the Java Development Kit to your Unity project." %}

If you do not see the "AppData" folder, open your file explorer and select the "View" option in the top menu. Select the box labelled "Hidden items."

{% include figure.html filename="ar-dev-28.png" caption="Check the 'Hidden items' box in your file explorer View options." %}

## Navigating the Unity Interface

This section covers some of the basic knowledge you will need while working with the Unity Editor. If you are already familiar with the Unity Interface, feel free to skip down to "Setting up Unity for AR Development."

Open Unity and create a new project. Select the "Window" option in the top menu and go to "Layouts". Select the "Default" layout option. Starting from the upper left and moving clockwise, you should see four panels labelled "Hierarchy," "Scene," "Inspector," and "Project."

{% include figure.html filename="ar-dev-2.png" caption="Default layout of the Unity interface." %}

First, navigate to the "Hierarchy" panel in the upper left. Your hierarchy panel should have a "Main Camera" and "Directional Light" included by default. If there is nothing in your hierarchy panel, select the "Create" drop-down menu directly above the panel and add a "Light > Directional Light." You do not need a "Main Camera" in your panel, but if it is already there, you can leave it.

Items that appear in the hierarchy panel are referred to as "game objects," and any game objects listed in the hierarchy panel are visually represented in the scene panel. Notice how the "Directional Light" appears in the scene panel as a sun and camera icon. To locate the position of a game object within your scene, select it in the hierarchy panel, place your cursor within the scene panel, and then strike the "F" key on your keyboard.

{% include figure.html filename="ar-dev-1-1.png" caption="The game objects in your hierarchy panel are represented visually in the scene panel." %}

In Unity, a game object is a container for different components that can be added and modified in the inspector panel. Select the "Directional Light" game object in your hierarchy panel. You should now see the properties of the Directional Light in the inspector panel on the far right. The inspector panel contains all of the "components" attached to a game object. The Directional Light game object has two components: "Transform" and "Light." You can add and modify components to change the appearance and functionality of your game objects.

{% include figure.html filename="ar-dev-1-2.png" caption="Use the inspector panel to modify the components of individual game objects." %}

Navigate to the bottom of the Unity interface where you will find a panel labelled "Project." The project panel gives you easy access to the entire file structure of your Unity project. You can access all of the media, scenes, and scripts for your project through this panel. If you use Unity to create more complex applications, you will want to organize your project with different folders to hold all of your images, scenes, sounds files, etc. You should also see a "Console" tab located next to the "Project" panel. The console panel will display any errors or warnings in your project.

## Setting up Unity for AR Development

For your AR application, you will not need the Main Camera or Directional Light game objects. Select them both, right click (or Ctrl click), and select "Delete."

Go to the project panel and navigate to the "Assets > Vuforia > Prefabs" folder. The window to the right of the project panel should display the contents of the "Prefabs" folder.

{% include figure.html filename="ar-dev-4.png" caption="Use this area to navigate around the file structure of your Unity project." %}

In Unity, a "prefab" is a game object that contains all of the information necessary to perform a specific function in your project, such as accessing the camera on a mobile device or playing a video. While in the prefabs folder, click and drag the "ARCamera" and "ImageTarget" prefabs into your hierarchy panel. Locate the directional widget in the top right corner of your scene panel. You can use this to adjust the view of your scene panel to the x, y, or z axis. Click the green y-axis option of your directional widget. This will make the green arrow  disappear and shift your perspective in the scene panel to a y-axis "birds-eye" view of your project. It will now be easier to manipulate the game objects in your scene view.

{% include figure.html filename="ar-dev-1-4.png" caption="Click the green y-axis option of your directional widget." %}

Select the ImageTarget prefab in the hierarchy panel and strike the "F" key while your cursor is within the scene view window. This should bring your ImageTarget prefab within the viewport of your scene panel. If you still can't see your ImageTarget in the scene view, make sure that the "2D" option is deselected in the scene view options menu.

{% include figure.html filename="ar-dev-3-1.png" caption="Scene view after selecting green y-axis." %}

Next, go to the [Vuforia developer portal](https://developer.vuforia.com/) and login with the same username and password you created earlier when downloading the Vuforia-Unity package. In the menu panel, select "Develop" and then "License Manager." Select "Add License Key" on the License Manager page. On the "Add License Key" page, give your application a name, then select "mobile" under the "Device" option and "Starter-No Charge" under the "License Key" option.

{% include figure.html filename="ar-dev-6.png" caption="Add license key page." %}

Click "Next" and confirm the creation of the license key. This license key grants your application access to Vuforia's augmented reality SDK. However, we still need to connect the license key to your Unity project.

To access your license key, return to the "License Manager" page in the Vuforia developer portal and click on the application name you just created. Copy the alphanumeric string in the gray box.

{% include figure.html filename="ar-dev-7.png" caption="Copy the license key." %}

Return to Unity and select the "AR Camera" prefab in the hierarchy panel. Navigate to the Inspector panel and locate the component labelled "Vuforia Behaviour" and paste the license key in the parameter "App License Key."

{% include figure.html filename="ar-dev-8.png" caption="Copy and paste your app license key into the Vuforia Behaviour script attached to your ARCamera prefab." %}

Once your license key has been added to the project, got to "File > Save Scene as..." and give your scene a name. By default, Unity will save your scenes to the "Assets" folder of your project. Feel free to leave your scene file here for now; however, for projects with more than one scene, you should create a dedicated folder to hold your scene files. To create a new folder, navigate to the "Project" panel in the lower left of the Unity editor. Right-click on the "Assets" folder and choose "Create > Folder." Give the folder a name (e.g. "Scenes"), then drag and drop your scene file into this folder.

{% include figure.html filename="ar-dev-9.png" caption="Create a dedicated 'scenes' folder for your Unity scene files." %}

## Convert your Image Target to a Dataset

For this section of the lesson, you will need a .jpg or .png image of the cover of the book. You can either take a picture of a book cover around your house or office or you can do an image search for the book cover online. In either case, make sure that you have access to a physical copy of the book.

When selecting a book cover to augment, make sure that it has stark color contrasts and a variety of complex shapes. Using a visually complex image makes it easier for your device's camera to track the Image Target for your application.

{% include figure.html filename="ar-dev-10.png" caption="This cover of John Steinbeck's *Of Mice and Men* will work well as an Image Target." %}

This cover of *Of Mice and Men* has sufficient visual complexity; however, it is not unique, and if it is used as an image target, then any copy of the book will work as an image target. Of course, this ubiquitous quality of the image might be desirable. For instance, digital artist Mark Skwarek augmented the British Petroleum logo to critique BP's complicity in the Gulf oil spill. Because the digital overlay is accessible wherever a BP logo can be scanned, Skwarek's project operates as a ubiquitous reminder of our dependence on fossil fuels.

{% include figure.html filename="ar-dev-11.png" caption="Photo courtesy of Mark Skwarek." %}

If you are taking a picture of your book cover, make sure that there are no extraneous features present in the image. In the case of the *Of Mice and Men* image above, this would be anything beyond the edge of the cover. If your image contains such extraneous features, either take another picture or open it in a photo editor such as [Gimp](http://www.gimp.org/) and
crop out these features. [Consult this video tutorial](https://www.youtube.com/watch?v=2rGGpOTSpbc) for help on cropping and resizing images in Gimp. Make sure that your image file is under 2.5 mb and that it is a .jpg or .png file.

{% include figure.html filename="ar-dev-12.png" caption="Crop out the area around the book." %}

Next, you will need to upload your book cover to Vuforia in order to code it with tracking information. Go to the [Vuforia developer portal](https://developer.vuforia.com/) and click on "Develop" in the top menu and then select "Target Manager." Next, click on the "Add Database" button on the Target Manager page. In the dialog box that appears, give your database a name and select the "Device" option. Click "Create."

{% include figure.html filename="ar-dev-13.png" caption="Name your Image Target Database." %}

Once your database has been created, return to the "Target Manager" page and click on your database. Click on the "Add Target" button. In the "Add Target" dialog box, choose "Single Image" as the type and upload your trigger image by clicking on the "Browse..." button.

{% include figure.html filename="ar-dev-14.png" caption="Image Target upload options" %}

To determine the width of your image, right-click the image file and choose "Properties." Select the "Details" tab in the dialog box that appears and scroll down to the "Image" section to find the width of the image in pixels. If you're using a Mac, Ctrl click and select "Get Info." The first number is the image's width.

{% include figure.html filename="ar-dev-15.png" caption="Properties dialog box" %}

Click "Add" in the "Add Target" options box on the Vuforia developer portal. Once your image has been processed, Vuforia will give it a feature tracking rating on a scale of 1 to 5 stars. Navigate to the Image Targets database in the Vuforia Developer Portal and select the image you just uploaded. Click on the "Show Features" link to reveal the image's trackable features.

{% include figure.html filename="ar-dev-16.png" caption="Vuforia's augmentability rating for the book cover." %}

The yellow markers represent the areas in the image that your application will use to determine if it is looking at the proper image target. If you notice that Vuforia is tracking unstable elements in your image (e.g. shadow, person, etc.), then you will need to re-edit or choose a different image.

If your image is given a good augmentability rating (anything between 2-5 stars should work), select your image and click "Download Database." If you were creating an AR application with multiple Image Targets, you would want to convert all of your images through Vuforia's developer portal before downloading them as a Unity package.

{% include figure.html filename="ar-dev-1-3.png" caption="Select the 'Download Database' button in the top right." %}

In the dialogue box that pops up, select "Unity Editor." Click "Download" and save the Unity package to an appropriate location.

{% include figure.html filename="ar-dev-17.png" caption="Download your Image Target Database" %}

## Import the Image Target

Now that you have converted your image into an image target, you need to associate it with your ImageTarget prefab in Unity. Return to Unity and import the database package you just downloaded from the Vuforia developer portal by selecting "Assets > Import Package > Custom Package."

Once the database has been imported, select the ImageTarget prefab in the project hierarchy panel. Navigate to the inspector panel and select the drop-down menu of the "Database" parameter in the "Image Target Behaviour." Select the name of the database you created earlier. The ImageTarget prefab should now be associated with your book cover.

{% include figure.html filename="ar-dev-18.png" caption="Image Target" %}

Zoom into your Image Target game object by selecting it in the hierarchy panel and striking the "F" key with your cursor hovering over the scene panel. If your scene view does not look like something similar to the image above, click on the green y-axis in the directional widget of your scene panel.

Next, select the "ARCamera" object in your project hierarchy and locate the "Database Load Behaviour" component in the inspector panel on the right. Check the "Load Database" and "Activate" parameters. The AR camera will not recognize your image target unless both of these boxes are selected, so make you check them first when troubleshooting your application.

{% include figure.html filename="ar-dev-19.png" caption="Load and activate the Image Target Database" %}

## Add an Image Overlay

You will need to add an overlay to test if your AR camera is tracking the image. The overlay is the multimedia content that your application will superimpose onto your trigger image. In Unity, you can add images, videos, audio files, and animated 3D models as overlays. For this lesson, however, we will only be covering image overlays.

First, find an image that you want to use as an overlay. If your application is augmenting a book, then you might download an image of the author but feel free to use a different image. In either case, drag the image into the "Assets" folder in the project panel at the bottom of the editor. Once the image has finished importing, select it and change its Texture Type to "Sprite (2D and UI)" in the inspector panel. Click "Apply."

{% include figure.html filename="ar-dev-20.png" caption="Convert overlay image to a sprite" %}

Next, drag the sprite you just imported onto your "Image Target" game object in the project hierarchy.

{% include figure.html filename="ar-dev-1.gif" caption="Attach your author image as a child of your ImageTarget prefab." %}

The sprite is now a "child" of the Image Target prefab and will only appear if the ARCamera recognizes the Image Target.

The position of your image overlay (the author image) in the scene view is the same position that it will appear when scanned with a mobile device camera. For example, if you place the author image at the top of the book then it will also appear at the top of the book cover when your user scans it.

Next, you will need to adjust the size and position of your author image to center it on your book cover using the translate, scale, and rotate tools located in the upper left of the Unity editor interface. Use the instructions for each of these tools below until your author image is positioned on top of your book cover. Remember to use the "F" key to locate your overlay or image target within the scene view.

To move the author image, select the "translate" tool from the button-menu directly above the hierarchy panel. Then, select the author image in your hierarchy panel. You can now move your author image in the x, y, or z axis by clicking on dragging on the red, blue, or green arrows. Use the green y-axis arrow to position your author image slightly above the book cover. Your overlay should have a slightly higher y-axis value (only about .1 or .2) than your Image Target. You can check these values in the "Transform > Position" component in your inspector panel.

{% include figure.html filename="ar-dev-2.gif" caption="Use the Translate tool to move game objects in your scene view." %}

To resize the author image, select the "scale" tool and adjust the width and height proportionally by clicking and dragging on the white cube in the center of the image.

{% include figure.html filename="ar-dev-3.gif" caption="Use the scale tool to resize game objects in your scene view." %}

To rotate the author image, select the "rotate" tool and adjust the image by clicking and dragging on the red, blue, or green circle. Alternatively, you can set the "x" axis to "90" in the image's "Transform" component to the right.

{% include figure.html filename="ar-dev-4.gif" caption="Use the Rotate tool to rotate game objects in your scene view." %}

To adjust your perspective in 3D space, hold the Alt button (Option on Mac) on your keyboard and click and drag in the scene view. Then, select the translate tool and position your author image so it is in front of the book cover.

{% include figure.html filename="ar-dev-5.gif" caption="Position your author image on top of the book cover." %}

Because Unity is optimized for 3D environments, it is sometimes difficult to work with 2D game objects such as images. If you are new to Unity, do not be alarmed if you cannot find your images or if you feel disoriented while manipulating them in your scene view. If you want to learn more about using Unity's transform tools, I would suggest checking out [this short video tutorial by Info Gamer](https://www.youtube.com/watch?v=2Ariq8vc5Vc) and reading up on [Transforms in the Unity Manual](http://docs.unity3d.com/Manual/Transforms.html).

If you cannot find your author image in the scene view, try the following steps:

* Select the author image in the hierarchy panel and navigate to its "Transform" component in the inspector panel. Click on the small cog icon in the upper right corner of the "Transform" component and select "Reset."
* Use the "F" key to search for any game object. Make sure the game object you are searching for is selected in the hierarchy panel and that your cursor is within the bounds of the scene view.
* Select the hand tool (left-most option) in the transform menu and adjust your perspective in the scene view. Hold the Alt/Option button on your keyboard to adjust your perspective in 3D space.
* Use the translate, scale, and rotate tools described above to reposition your author image on top of the book cover.

{% include figure.html filename="ar-dev-22.png" caption="Reset the position, rotation, and scale of a game object in the Transform component." %}

## Test Your Scene

If you are using the 32-bit Unity editor for Windows or you are working on a Mac, you should be able to test your application with your webcam. Unfortunately, Unity [no longer provides webcam support](https://developer.vuforia.com/forum/issues-and-bugs/camera-not-working-unity-511) for its 64-bit editor. However, webcam access is not necessary for AR development in Unity. If you do not have a webcam on your computer, are using the 64-bit editor, or want to learn how to build your application for an Android or iOS device, skip to the section "Building Your Application to a Mobile Device."

Press the play icon in the menu above the scene view. Give Unity permission to access your webcam, and return to the scene view by clicking on the "Scene" tab to the left of the "Game" tab. Hold your book cover in front of your webcam. You should see your webcam view snap to your author image and the "Sprite Renderer" component toggle on and off as you move your book cover in and out of the webcam view.

{% include figure.html filename="ar-dev-6.gif" caption="Place your book cover within the webcam view while in play mode." %}

If your overlay does not appear, double check the "Database Load Behaviour" component of your "AR Camera" game object to ensure that the "Load Data Set" and "Activate" boxes are both selected.

## Building Your Application to a Mobile Device

### Android

Before you can install your own applications on your Android device, you will need to [enable USB debugging](http://developer.android.com/tools/device.html). To do this, go to "Setting" > About Device" and tap the "Build number" seven times. Return to the previous screen and you should now see a "Developer Options" tab. Click it and make sure the option for "USB debugging" is checked.

{% include figure.html filename="ar-dev-25.png" caption="Tap the 'Build Number' seven times." %}

{% include figure.html filename="ar-dev-26.png" caption="Make sure that 'USB Debugging' is enabled." %}

In Unity, go to "File > Build Settings." In the "Platform" section of the dialog box, select "Android" and click "Switch Platform." Then, select "Add Current" (or "Add Open Scenes").

{% include figure.html filename="ar-dev-30.png" caption="Build Settings dialog box" %}

Click on "Player Settings" and navigate to the inspector panel. Change the "Product Name" to the name you want to use for your app (e.g. "Programming Historian Demo"). Scroll down in the inspector panel and select the "Other Settings" tab. Change the "Bundle Identifier" settings from "com.Company.ProductName" to a name that will be unique to your application, such as "com.Demo.Steinbeck".

{% include figure.html filename="ar-dev-31.png" caption="Change the 'Bundle Identifier' of your application in the Inspector Panel" %}

You are now ready to build your application to your mobile device. Connect your device to your computer with a USB cable. Depending on your operating system, your computer might need to download additional drivers in order to interact with your mobile device. Your computer should do this automatically. If the computer is not recognizing your device, follow the first step in the troubleshooting guide below.

In the "Build Settings" window, make sure your scene is listed and click "Build and Run." Unity will create a ".apk" (Android Application Package) file for your project. By default, your .apk file will be saved to the root folder of your Unity project. This is the file type that will be uploaded to the Google Play store once your application is complete.

When the application is finished building, you should be able to view and test your application on your Android device.

{% include figure.html filename="ar-dev-32.png" caption="Testing the application on an Android device." %}

With Android, it is very easy to share and test your completed application with other Android users without uploading it to the Google Play store. To share your application, simply send the .apk file as an email attachment to anyone with an Android device. However, before other users can download and install the .apk file, they will need to allow their Android device to install .apk files from non-Google Play sources by navigating to "Settings > Security" on their Android device and checking the box labelled "Unknown sources."

### Troubleshooting Android Builds

During the build, if you get an error from Unity saying that it cannot locate your android device, try the following in order:

* Open the device manager on your computer and right click on the Android phone attached as a device. Select "Update Driver Software."
* Open the Android SDK manager and ensure that the "Google USB Driver" is installed.
* Unplug your device from the computer. Open the "Developer Options" in the system setting of your Android device. Select the option to "Revoke USB Debugging Authorization." Plug your device back into your computer.
* Save your scene and close Unity.
* Open your file explorer and go into the "android-sdk/platform-tools" folder. Hold shift and right-click. Select the option to "Open command window here." For Mac, open a Terminal and drag the "platform-tools" folder into the window.

Type the following commands and press "Enter" after each. As you enter each command, check your Android device and authorize your computer when prompted.

```
adb kill-server
adb start-server
adb devices
```

{% include figure.html filename="ar-dev-1-15.png" caption="Once your device is authorized, the command prompt should display 'List of devices attached' along with an alpha-numeric string that represents your Android device." %}

If you are getting errors that your "Android Build Tools" are out of date, open the Android SDK manager and make sure that the "Android SDK Platform-tools" and "Android SDK Build-tools" options are both installed.

If you get an error saying that "Unity cannot install the APK!" go to your player settings and set the "Install Location" to "Automatic."

### iOS

Before you can build your application to an iOS device, you will need to create an XCode project in Unity. Go to "File > Build Settings" and switch your platform target to "iOS." Click "Build" and create a new folder named "iOS Build."

Once your project is built, open it in Finder and create a new folder named "LibrariesPlugins." Then, copy the "iOS" folder located in "Libraries > Plugins" and paste it into the "LibrariesPlugins" folder you just created.

{% include figure.html filename="ar-dev-33.png" caption="File structure of your Unity-iOS project." %}

Open your project in Xcode. When opening Xcode for the first time, you might get a warning message about an "unexpected code bundle Unty4XC.xcplugin" that "can have a negative effect on the safety and stability of Xcode or related tools." This is nothing to worry about. It just means that it has detected a third-party code bundle from Unity. If this message appears, select the "Load Bundle" option. If Xcode asks if you would like to update your project to the recommended settings, select "yes" and wait for the project to update.

{% include figure.html filename="ar-dev-2-2.png" caption="Possible Xcode error." %}

Next, you will need to register your iOS device with Xcode. First, connect it to your computer with a USB cable. This device must be registered under the same Apple ID associated with Xcode.You might have to wait a few minutes while Xcode prepares your device for app development.

In order to build your app to an iOS device, you will need to link your apple account to Xcode. Under the "General" tab, select "Team" and then "Add Account." Add the Apple ID account associated with your iOS device (this is the account you use to download apps and purchase music through iTunes). Next, scroll down to "Deployment info" and select "iPhone" or "iPad" depending on the type of device you are building to. If you are still getting the warning message "No code signing identities found," make sure that your Apple ID is selected and click on the "Fix Issue" button.

{% include figure.html filename="ar-dev-34.png" caption="Add your account in Xcode." %}

Next, you will need to add Vuforia's AR library to your project. Navigate to the "Build Phases" tab and select the "Copy Bundle Resources" section. Click on the "+" button at the bottom of the "Copy Bundle Resources" section and select "Add Other" in the dialog box that appears.

{% include figure.html filename="ar-dev-35.png" caption="Add the Vuforia library to your Xcode project." %}

After you click "Add Other," select the "QCAR" (or "Vuforia") folder, which is located in the "Data > Raw" folder of your Unity-iOS project.

{% include figure.html filename="ar-dev-36.png" caption="Locate the folder named 'QCAR' and add it to your Xcode project." %}

Finally, select "Product > Run" in the top menu and wait for your app to build to your iOS device. Once the app has finished building, you will need to authorize your Apple ID as a trusted developer. Open the "Settings" app on your device and select the "General" tab on the left. Scroll down and select "Device Management." Make sure that you are connected to the internet and give your device permission to run your app. Go to your device home screen and select the Unity application to test it on your device.

## Extending the Tutorial

You should now have a fairly good grasp of how the Unity game engine can be used to create a simple augmented reality application. In future tutorials, we will cover more advanced topics that will provide you with the necessary technical skills to create more robust mobile AR applications with dynamic, interactive overlays.
