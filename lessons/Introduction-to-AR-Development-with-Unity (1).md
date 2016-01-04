---

title: Introduction to Mobile Augmented Reality Development in Unity

author:

- Jacob W. Greene

date: 2015-1-4
layout: default

---

## Lesson Goals

In this introductory tutorial, you will learn how to:

* setup the Unity game engine for AR development
* convert images to augmentable data sets
* add audio-visual overlays to trigger images
* create and modify C# scripts in Unity
* build standalone Unity applications to Android and iOS devices

This lesson serves as an introduction to creating augmented reality applications using the Unity game engine and the Vuforia augmented reality SDK. Additionally, this lesson provides advice for incorporating augmented reality technology into humanities research.  
 
## What is Augmented Reality and Why Should I Care?

Typically experienced by looking through the camera lens of an electronic device such as a smartphone, tablet, or head-mounted display (e.g. Google Glass), augmented reality (AR) can be defined as the overlaying of digital content (images, video, text, sound, etc.) onto physical objects or locations. Novel applications of AR continue to surface  within a variety of industries: [museums](https://www.youtube.com/watch?v=gx_UQxx54lo) are integrating AR content into their displays, [companies](http://www.gizmag.com/ikea-augmented-reality-catalog-app/28703/) are promoting AR apps in lieu of print or even web-based catalogs, and [engineering firms](https://www.youtube.com/watch?v=bXqe2zSepQ4) are creating AR applications showcasing their efforts to promote sustainability. [Predicted to grow](http://www.digi-capital.com/news/2015/04/augmentedvirtual-reality-to-hit-150-billion-disrupting-mobile-by-2020/#.VbetCU1VhHw) into a $120 billion industry within the next five years, augmented reality is an exciting new medium that digital humanists cannot afford to ignore.

Since at least 2010, [digital artist](https://manifestarblog.wordpress.com/about/) have been creating AR applications that point to its potential as a medium for social and cultural intervention. For example,  Tamiko Thiel's AR project [Clouding Green](http://www.tamikothiel.com/AR/clouding-green.html) reveals the carbon footprint of specific technology companies when their buildings are viewed through her application. Projects such as Thiel's capitalize on AR's unique rhetorical affordance to provide compelling, site-specific interactions between physical and digital content.

At the [Trace Innovation Initiative](http://trace.english.ufl.edu/projects/arcs/) in the University of Florida English Department, we seek to build upon the work of these artists by promoting the creation and circulation of humanities-focused mobile augmented reality applications. For one of our first projects, we are collaborating with the Religion Department to create a mobile AR application that reveals the hidden religious history in and around the University of Florida campus. Once completed, users will be able to look at specific buildings and signs around campus through their phone or tablet camera and view multimedia content (videos, audio clips, links, etc.) informing them of the religious history related to those different locations.

{% include figure.html src="../images/ar-dev-1.png" caption="Testing the 'Religion@UF' augmented reality application." %}

 For this tutorial, I will demonstrate the process of creating an audio-visual overlay for a text-based trigger image. Scholars could use this to create digital overlays for historical documents or literary texts. For example, you might create an application that allows readers to scan the pages of a book or document and access historical context or critique related to that specific page. Humanities scholars could also use this tutorial to create site-specific AR applications that educate visitors about aspects of a location's that has been history excluded from its historical representation, such as buildings named after former slave owners.

## Software Requirements

All tutorials in the augmented reality series can be completed using either the free or paid versions of the software.

* [Download and install the latest version of Unity](https://unity3d.com/)

Unity is a game engine used to create desktop, console, and mobile games and thus is not designed exclusively for augmented reality development. Unity is a verstaile piece of software, and many of the concepts and technical skills covered in this tutorial can also be applied to other digital projects made with Unity. Feel free to download either the 64 or 32-bit version of Unity; however,
[other developers](https://developer.vuforia.com/forum/issues-and-bugs/camera-not-working-unity-511) (myself included) have found that the 32-bit version of Unity is the only one that will allow access to your computer's webcam, which will come in handy when testing your application. For more information about Unity, consult [Unity's beginner tutorial videos](https://unity3d.com/learn/tutorials/modules/beginner/editor) or the online [Unity manual](http://docs.unity3d.com/Manual/LearningtheInterface.html).

* [Download and install the latest Unity extension from Vuforia](https://developer.vuforia.com/downloads/sdk)

In order to use Unity for augmented reality development, you will first need to import an extension created by Qualcomm-Vuforia. In Unity, it is common to import extensions into your projects in order to gain access to additional functionality or multimedia assets such as images, 3D models, or audio files. Before you can download the Unity extension, Vuforia will ask you to create a user profile. Take note of your username and password as you will need them to access other areas of the Vuforia developer website.
  
## Import the Vuforia Extension into Unity

Once you have downloaded and installed Unity, you will need to import the augmented reality package you just downloaded from the Vuforia website. To do this, start Unity and open up a new scene. In the menu panel, select "Assets > Import Package > Custom Package" and open the Unity extension you just downloaded from the Vuforia developer portal. A small screen will pop up that lists the file contents for the Vuforia extension. Click "Import."

## Navigating the Unity Interface

Before we get too far, it will be helpful to establish some basic terminology that will make it easier for you to navigate the Unity interface throughout this tutorial. First, select the "Window" option in the top menu and got to "Layouts". Select the "Default" layout option.

Now that we have the same layouts, it will be easier to explain the different sections of the Unity interface and how they interact with one another. The default layout breaks up the Unity interface into four viewing areas. Starting from the upper left and moving clockwise, you should see four main areas labelled "Hierarchy," "Scene," "Inspector," and "Project."

{% include figure.html src="../images/ar-dev-2.png" caption="Default layout of the Unity interface." %}

First, navigate to the "Hierarchy" panel in the upper left. Your hierarchy panel should have a "Main Camera" and "Directional Light" included by default. Items that appear in your hierarchy panel are referred to as "game objects." Game objects that appear in your hierarchy panel are active elements of your "Scene," which is the panel directly to the right of your hierarchy panel. To locate the position of a game object within your scene, select it in the hierarchy panel, place your cursor within the "Scene" panel, and then hit the "F" key. Try to locate the two game objects in your scene.

Next, select the "Main Camera" game object in your hierarchy panel. You should now see the properties of the Main Camera in the Inspector panel on the right. The inspector panel contains all of the "components" attached to a game object. You can add components such as mp3 files and C# scripts to change how your game object interacts with other elements of your scene. Move back to your hierarchy panel and select the "Directional Light" game object. Notice how the inspector panel changes.

Lastly, move down to the bottom of the Unity interface where you will find a panel labelled "Project." The project panel gives you easy access to the entire file structure of your Unity project. You can access all of the media, scenes, and scripts for your project through this panel. If you use Unity to create more complex applications, you will want to organize your project with different folders to hold all of your images, scenes, sounds files, etc. You should also see a "Console" tab located next to the "Project" panel. The console panel will display any errors or warnings in your project.

## Setup Your Unity Project for AR Development

First, you will need to import the augmented reality package you just downloaded from the Vuforia website into Unity. In the menu, select "Assets > Import Package > Custom Package" and open the Unity extension you just downloaded from the Vuforia developer portal. A small screen will pop up that lists the file contents for the Vuforia extension. Click "Import."

{% include figure.html src="../images/ar-dev-3.png" caption="Import Vuforia's augmented reality extension" %}

For your AR application, you will not need the Main Camera or Directional Light game objects. Select them both and hit "delete."

Go to the project panel and navigate to the "Assets > Vuforia > Prefabs" folder. The window to the right of the project panel should display the contents of the "Prefabs" folder.

{% include figure.html src="../images/ar-dev-4.png" caption="Use this area to navigate around the file structure of your Unity project." %}

In Unity, a "prefab" is a game object that contains all of the information necessary to perform a specific function in your project, such as accessing the camera on a mobile device or playing a video. While in the prefabs folder, click and drag the "ARCamera" and "ImageTarget" prefabs into your hierarchy panel. To locate your image target prefab in the scene view, make sure the ImageTarget is selected in the hierarchy panel and strike the "f" key while your cursor is within the scene view window. If you still can't see your ImageTarget in the scene view, make sure that the "2D" option is deselected in the scene view options menu.

{% include figure.html src="../images/ar-dev-5.png" caption="Scene view of the ImageTarget prefab." %}

Next, go to the [Vuforia developer portal](https://developer.vuforia.com/) and login with the same username and password you created earlier when downloading the Vuforia-Unity extension. In the menu panel, select "Develop" and then "License Manager." Select "Add License Key" on the License Manager page. On the "Add License Key" page, give your application a name, then selelct "mobile" under the "Device" option and "Starter-No Charge" under the "License Key" option.

{% include figure.html src="../images/ar-dev-6.png" caption="Add license key page." %}

Click "Next" and confirm the creation of the license key. This license key grants your application access to Vuforia's augmented reality software. However, we still need to connect the license key to your Unity project.

To access your license key, return to the "License Manager" page in the Vuforia developer portal and click on the application name you just created. Copy the alphanumeric string in the gray box.

{% include figure.html src="../images/ar-dev-7.png" caption="Copy the license key." %}

Return to Unity and select the "AR Camera" prefab in the hierarchy panel. Navigate to the Inspector panel and locate the component labelled "Vuforia Behaviour" and paste the license key in the text box labelled "App License Key."

{% include figure.html src="../images/ar-dev-8.png" caption="Copy and paste your app license key into the Vuforia Behaviour script attached to your ARCamera prefab." %}

Once your license key has been added to the project, got to "File > Save Scene as..." and give your scene a name. by default, Unity will save your scenes to the "Assets" folder of your project. Feel free to leave your scene file here for now; however, for projects with more than one scene, you will want to create a dedicated folder to hold your scene files. To create a new folder, navigate to the "Project" panel in the lower left of the Unity editor. Right-click on the "Assets" folder and choose "Create > Folder." Give the folder a name (e.g. "Scenes"), then drag and drop your scene file into this folder.

{% include figure.html src="../images/ar-dev-9.png" caption="Create a dedicated 'scenes' folder for your Unity scene files." %}

## Convert your Image to a Dataset

For this next step, you will need to choose the image or object that your application will augment. To do this, take a picture of an object that you can easily access, such as the cover of a book. When choosing an image target, always make sure that it has a sufficient level of visual complexity.

{% include figure.html src="../images/ar-dev-10.png" caption="This cover of John Steinbeck's Of Mice and Men will work well as an Image Target." %}

This cover of Of Mice and Men has sufficient visual complexity; however, it is not unique, and if it is used as an ImageTarget, then any copy of the book will work as an Image Target. Of course, this ubiquitous quality of the image might be desirable. For instance, digital artist Mark Skwarek augmented the British Petroleum logo to critique BP's complicity in the Gulf oil spill.

{% include figure.html src="../images/ar-dev-11.png" caption="Photo courtesy of Mark Skwarek." %}

Next, open your image in a photo editor such as [Gimp](http://www.gimp.org/) and
crop out any unstable features, or visual elements that will not be present when someone scans your image target.

{% include figure.html src="../images/ar-dev-12.png" caption="Crop out the area around the book." %}

Make sure the image file size is under 2.5 mb and export it as a .jpg or .png file.
[Consult this video tutorial](https://www.youtube.com/watch?v=2rGGpOTSpbc) for help on cropping and resizing images in Gimp.

Navigate to the [Vuforia developer portal](https://developer.vuforia.com/) and click on "Develop" in the top menu and then select "Target Manager." Next, click on the "Add Database" button on the Target Manager page. In the dialog box that appears, give your database a name and select the "Device" option. Click "Create."

{% include figure.html src="../images/ar-dev-13.png" caption="Name your Image Target Database." %}

Once your database has been created, return to the "Target Manager" page and click on your database. Click on the "Add Target" button. In the "Add Target" dialog box, choose "Single Image" as the type and upload your trigger image by clicking on the "Browse..." button.

{% include figure.html src="../images/ar-dev-14.png" caption="Image Target upload options" %}

To determine the width of your image, right-click the image file and choose "Properties." Select the "Details" tab in the dialog box that appears and scroll down to the "Image" section to find the width of the image. 

{% include figure.html src="../images/ar-dev-15.png" caption="Properties dialog box" %}

Click "Add" in the "Add Target" options box on the Vuforia developer portal. Once your image has been processed, Vuforia will give it a feature tracking rating on a scale of 1 to 5 stars. Navigate to the Image Targets database for your application and select the image you just uploaded. Then, click on the "Show Features" link to reveal the image's trackable features.

{% include figure.html src="../images/ar-dev-16.png" caption="Vuforia's augmentability rating for the book cover." %}

The yellow markers represent the areas in the image that your application will use to determine if it is looking at the proper image target. If you notice that Vuforia is tracking unstable elements in your image (e.g. shadow, person, etc.), then you will need to re-edit or choose another the image. 

If your image is given a good augmentability rating (anything between 2-5 stars should work), select your image and click "Download Dataset." In the dialogue box that pops up, select "Unity Editor." Click "Download" and save the Unity package to an appropriate location.

{% include figure.html src="../images/ar-dev-17.png" caption="Download your Image Target Dataset" %}

## Import the Image Target 
 
Now that you have converted your image into a trackable AR dataset, you need to associate it with the Image Target prefab in your Unity Scene. In Unity, import the Image Target dataset you just downloaded from the Vuforia developer portal by selecting "Assets > Import Package > Custom Package."

Once the dataset has been imported, select the "Image Target" object in the project hierarchy panel. Navigate to the inspector panel and select the drop-down menu of the "Data Set" parameter in the "Image Target Behaviour." Select the name of the database you created earlier. The scene view should now display your Image Target.

{% include figure.html src="../images/ar-dev-18.png" caption="Image Target" %}

The image target prefab will resize according the dimensions of your image, so you might need to manually adjust the size of the image target to ensure that it fits within the view of your AR camera. Select the "ARCamera" game object in your hierarchy panel to see the view area of the camera. Then, click on the "Game" tab above your scene view to see if you need to adjust the size or location of your Image Target. Return to the scene view and use the
[transform tools](http://docs.unity3d.com/Manual/PositioningGameObjects.html) in the upper left corner of the editor to move and resize your image target so that it fits within the view of the ARCamera game object. 

Select the "ARCamera" object in your project hierarchy and check the "Load Data Set" and "Activate" parameters in the "Data Set Load Behaviour" component in the inspector panel on the right. The AR camera will not recognize your image target unless both of these boxes are selected, so make you check them first when troubleshooting your application.

{% include figure.html src="../images/ar-dev-19.png" caption="Load and activate the Image Target Database" %}

## Add an Image Overlay

You will need to add an overlay to test if your AR camera is tracking the image. The overlay is the multimedia content that your application will superimpose onto your trigger image. In Unity, you can add images, videos, audio files, and animated 3D models as overlays. For this tutorial, however, we will only be covering image and audio overlays.

First, find an image that you want to use as an overlay. If your application is augmenting a book, then you might choose an image of the author. Download an image and drag it into the "Assets" folder in the project panel at the bottom of the editor. Once the image has finished importing, select it and change its Texture Type to "Sprite (2D and UI)" in the inspector panel. Click "Apply."

{% include figure.html src="../images/ar-dev-20.png" caption="Convert overlay image to a sprite" %}

Next, drag the sprite you just imported onto your "Image Target" game object in the project hierarchy. The sprite is now a "child" of the Image Target prefab and will only appear if the ARCamera recognizes the Image Target.

{% include figure.html src="../images/ar-dev-21.png" caption="Make sure your sprite is attached as a child to your Image Target" %}

If you cannot see your overlay image in the scene view, select it in the hierarchy panel and navigate to its "Transform" component in the Inspector panel. Click on the small cog icon in the upper right corner of the "Transform" component and select "Reset." Use the
[transform tools](http://docs.unity3d.com/Manual/PositioningGameObjects.html) to position your image overlay. 

{% include figure.html src="../images/ar-dev-22.png" caption="Resest the position, rotation, and size of your overlay in the Transform component." %}

## Add an Audio Overlay

If you would also like to add an audio overlay, continue with this section. If not, feel free to skip down to the next section to test your application.

Make sure that your "ImageTarget" game object is selected in the Hierarchy panel. In in the inspector panel, scroll to the bottom and select "Add Component." Search for "audio source" and add it to your ImageTarget. Deselect the "Play On Awake" box in the audio source component. If left selected, your audio will begin playing as soon as the application starts rather than when the user scans your trigger image.

Next, you will need to find an mp3 file to test if your audio overlay is working. If you do not have any audio files handy, you can download a copyright-free mp3 at [soundbible.com](http://soundbible.com/). Once you have located your mp3, drag it into your assets folder in your project panel. Once the file has imported into Unity, drag it into the "AudioClip" section of the Audio Source component in your ImageTarget gameobject.

{% include figure.html src="../images/ar-dev-23.png" caption="Add the mp3 file to the 'AudioClip' slot and deselect the 'Play On Awake' option." %}

In order to get the audio file to play when the trigger image is scanned, you will need to create your own C# script and attach it to your ImageTarget. To do this, make sure the Image Target is selected in the scene view and click on "Add Component" in the inspector panel. Then, scroll down to the bottom of the menu to select "New Script." Make sure the scripting language is set to "C#" and rename it "PlayAudio." The new script will be added to your root "Assets" folder in the project panel. Double-click on the script to open it in Monodevelop. Copy and paste the code below into your "PlayAudio" script. Save the file and return to Unity.

```C#
using UnityEngine;
using System.Collections;
using Vuforia;

public class PlayAudio : MonoBehaviour,
ITrackableEventHandler
{
    private TrackableBehaviour mTrackableBehaviour;
    
    void Start()
    {
        mTrackableBehaviour = GetComponent<TrackableBehaviour>();
        if (mTrackableBehaviour)
        {
            mTrackableBehaviour.RegisterTrackableEventHandler(this);
        }
    }
    
    public void OnTrackableStateChanged(
        TrackableBehaviour.Status previousStatus,
        TrackableBehaviour.Status newStatus)
    {
        if (newStatus == TrackableBehaviour.Status.DETECTED ||
            newStatus == TrackableBehaviour.Status.TRACKED ||
            newStatus == TrackableBehaviour.Status.EXTENDED_TRACKED)
        {
            // Play audio when ImageTarget is found
            GetComponent<AudioSource>().Play();
        }
        else
        {
            // Stop audio when ImageTarget is lost
            GetComponent<AudioSource>().Stop();
        }
    }   
}
```

This C# script uses Vuforia's "ITrackableEventHandler" to determine if the trigger image is within the camera view. If it is, it will search for the audio source component attached to the ImageTarget game object and play it. If the camera stops tracking the trigger image, then the audio source will pause.

## Test Your Scene

Now that you have an image and/or audio overlay attached to your Image Target, you can test your scene. Press the play icon in the menu above the scene view and hold your book cover in front of your webcam. You should see your overlay appear on top of the book cover. Move the book outside of the camera frame to ensure that your "PlayAudio" script pauses your mp3 file. If your overlay does not appear, double check the "Database Load Behaviour" component of your "AR Camera" game object to ensure that the "Load Data Set" and "Activate" boxes are both selected.

{% include figure.html src="../images/ar-dev-24.png" caption="Webcam view of augmented book cover" %}

If you do not have a webcam on your computer, or if you want to learn how to build your application for an Android or iOS device, continue on to the steps below.

## Building Your Application to a Mobile Device

### Android

Before you can install your own applications on your Android device, you will need to [enable USB debugging](http://developer.android.com/tools/device.html). To do this, go to "Setting" > About Device" and tap the "Build number" seven times. Return to the previous screen and you should now see a "Developer Options" tab. Click it and make sure the option for "USB debugging" is checked.

{% include figure.html src="../images/ar-dev-25.png" caption="Tap the 'Build Number' seven times." %}

{% include figure.html src="../images/ar-dev-26.png" caption="Make sure that 'USB Debugging' is enabled." %}

Next, you will need to download and install [Android Tools](https://developer.android.com/sdk/index.html#Other) and the [Java Development Kit.](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) to your computer.

{% include figure.html src="../images/ar-dev-27.png" caption="Download the Android Tools package that is compatible with your operating system." %}

Note the location where you saved the Android Tools and Java Development Kit because your Unity project will need to access them. In the Unity menu panel, go to "Edit > Preferences > External Tools" and point Unity to the file locations for the Android Tools (Android SDK) and Java Depevelopment Kit (JDK) you just installed. By default, the Android SDK will download to this folder location on your computer: "C > Users > [your username] > AppData > Local > Android." If you do not see the "AppData" folder, open your file explorer and select the "View" option in the top menu. Select the box labelled "Hidden items." 

{% include figure.html src="../images/ar-dev-28.png" caption="Check the 'Hidden items' box in your file explorer View options." %}

{% include figure.html src="../images/ar-dev-29.png" caption="Connect Android Tools and the Java Depevelopment Kit to your Unity project." %}

Next, return to Unity, and go to "File > Build Settings." In the "Platform" section of the dialog box, select "Android" and click "Switch Platform." Then, Click "Add Current" to add your scene to the build.

{% include figure.html src="../images/ar-dev-30.png" caption="Build Settings dialog box" %}

Click on "Player Settings" and navigate to the inspector panel. Change the "Product Name" to the name you want to use for your app (e.g. "Programming Historian Demo"). Scroll down in the inspector panel and select the "Other Settings" tab. Change the "Bundle Identifier" settings from "com.Company.ProductName" to a name that will be unique to your application, such as "com.Demo.Steinbeck".

{% include figure.html src="../images/ar-dev-31.png" caption="Change the 'Bundle Identifier' of your application in the Inspector Panel" %}

You are now ready to build your application to your mobile device. Connect your device to your computer with a USB cable. Depending on your operating system, your computer might need to download special software known as "drivers" in order to interact with your mobile device. In most cases, your computer will do this automatically. If it doesn't, simply search for "drivers for [name/version of mobile device]" and download the drivers for your device from the manufacturer's website.

In the "Build Settings" window, make sure your scene is listed and click "Build and Run." When the application is finished building, you should be able to view and test your application on your Android device.

{% include figure.html src="../images/ar-dev-32.png" caption="Testing the application on an Android device." %}

### iOS

Unlike Android, iOS apps made in Unity must be built as standalone projects and then imported into Apple's development environment [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12). Ensure that you have installed Xcode 7 or higher and that your Apple device is running iOS 9 or higher. Xcode 7 allows developers to test applications on iOS devices without enrolling in the Apple Developer program.

To create an XCode project in Unity, go to "File > Build Settings" and switch your platform target to "iOS." Click "Build" and save your project to an appropriate location. Once your project is built, open it in your file explore and create a new folder named "LibrariesPlugins." Then, copy the "iOS" folder located in "Libraries > Plugins" and paste it into the "LibrariesPlugins" folder you just created.

{% include figure.html src="../images/ar-dev-33.png" caption="File structure of your Unity-iOS project." %}

Open your project in Xcode. If Xcode asks if you would like to update your project to the recommended settings, select "yes" and wait for the project to update.

In order to build your app to an iOS device, you will need to link your apple account to Xcode. Under the "General" tab, select "Team" and then "Add Account." Add the Apple ID account associated with your iOS device (this is the account you use to download apps and purchase music through iTunes). Next, scroll down to "Deployment info" and select "iPhone" or "iPad" depending on the type of device you are building to. If you are still getting the warning message "No code signing identities found," make sure that your Apple ID is selected and click on the "Fix Issue" button.

{% include figure.html src="../images/ar-dev-34.png" caption="Add your account in Xcode." %}

Next, you will need to add Vuforia's AR library to your project. Navigate to the "Build Phases" tab and select the "Copy Bundle Resources" section. Click on the "+" button at the bottom of the "Copy Bundle Resources" section and select "Add Other" in the dialog box that appears.

{% include figure.html src="../images/ar-dev-35.png" caption="Add the Vuforia library to your Xcode project." %}

After you click "Add Other," select the "QCAR" folder, which is located in the "Data > Raw" folder of your Unity-iOS project.

{% include figure.html src="../images/ar-dev-36.png" caption="Locate the folder named "QCAR" and add it to your Xcode project." %}

Unlock your iOS device and connect it to the computer. You might have to wait a few minutes while Xcode prepares your device for app development. Once it is finished, select "Product > Run" in the top menu and wait for your app to build to your iOS device.

Once the app has finished building, you will need to authorize your Apple ID as a trusted developer. Open the "Settings" app on your device and select the "General" tab on the left. Scroll down and select "Profile." Make sure that your device has an internet connection and click on "Verify" to give your device permission to run your app. Return to the app menu and select the Unity application to test it on your device.

{% include figure.html src="../images/ar-dev-37.png" caption="Your device will not start your app until it has been verified." %}

## Extending the Tutorial

You should now have a fairly good grasp of how the Unity game engine can be used to create simple augmented reality applications. In future tutorials, we will cover more advanced topics that will provide you with the necessary technical skills to create more robust mobile AR applications with dynamic user-interfaces, interactive overlays, and much more. 
 


