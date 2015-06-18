---
title: Installing Omeka 
authors:
- Jonathan Reeve 
date: 2015-06-10
reviewers:
layout: default
next: creating-an-omeka-exhibit
---

[Omeka.net](http://omeka.net), as described in [the previous lesson](up-and-running-with-omeka.html), is a useful service for Omeka beginners, but there are a few reasons why you might want to install your own copy of Omeka. Reasons include: 

 * **Upgrades**. By installing Omeka yourself, you can use the latest versions of Omeka as soon as they're released, without having to wait for Omeka.net to upgrade their system. 
 * **Plugins and themes**. You can install any plugin or theme you want, without being restricted to those provided by Omeka.net. 
 * **Customizations**. You can buy a custom domain name, and customize your code to achieve your desired functionality. 
 * **Control**. You have control over your own backups, and you can update the server yourself so that its security is always up-to-date. 
 * **Price**. There are many low-cost Virtual Private Servers (VPSs) now, some of which cost only $5 per month.  
 * **Storage**. Many shared hosting providers now offer unlimited storage. This is useful if you have a large media library.  

In this tutorial, we'll be entering a few commands on the command line. This tutorial assumes no prior knowledge of the command line, but if you want a concise primer, consult the [Programming Historian introduction to BASH](http://programminghistorian.org/lessons/intro-to-bash). There are other ways of installing Omeka, of course, some using exclusively GUI tools. Some hosting providers even offer "[one-click installs](http://omeka.org/blog/2014/10/22/omeka-one-click-installs/)" via their control panels. Many of those methods, however, will install older versions of Omeka which are then harder to upgrade and maintain. The method outlined below may not be the easiest way to install Omeka, but it will give you some good practice with using the command line, which is a skill that will be useful if you want to manually upgrade your install. There are five steps to this process, and it should take about an hour. 

## Step 1: Get an account with a hosting provider, and set up your server. 

First, sign up for an account with a hosting provider that gives you SSH access. There are two main types of hosting providers: VPS and shared. A VPS host gives you root access, which means you have more control over the server, but your storage space is often limited. For small archives of 20GB or less, this is the best solution, but for large archives, shared hosting plans might be better suited. [DigitalOcean](https://www.digitalocean.com/signup/) is an inexpensive VPS host, and [Amazon Web Services](http://aws.amazon.com/free/) (AWS) hosts similar virtual servers on their Elastic Computing (EC2) platform, with a free trial of one year. Both [HostGator](http://www.hostgator.com/) and [DreamHost](http://www.dreamhost.com) offer inexpensive shared hosting with unlimited storage. 

If you open an account with a VPS provider, you'll first want to create a virtual server with their interface. (If you have a shared hosting provider, this is already done for you, so you can skip to step 3b.) On DigitalOcean, VPS instances are called "droplets," and you can follow Digital Ocean's guide [How To Create Your First DigitalOcean Droplet Virtual Server](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-digitalocean-droplet-virtual-server). On AWS, a VPS is called an "instance," and you can follow their guide [Launch an Amazon EC2 Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance_linux.html). In both cases, choose an Ubuntu system to install, since we'll be running Ubuntu Linux commands below. 

Now that you have a running server, connect to it with an SSH client. This is sometimes as simple as opening a terminal and typing `ssh root@hostname`, where `hostname` is your server address. Consult your host's documentation for Specific instructions for logging on via SSH. Here is a sampling of guides for VPS hosts: 
 
 * [Digital Ocean: How To Connect To Your Droplet with SSH](https://www.digitalocean.com/community/tutorials/how-to-connect-to-your-droplet-with-ssh)
 * [Amazon Web Services: Connecting to Your Linux Instance Using SSH](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

And here are a few guides for shared hosts: 

 * [DreamHost Wiki: SSH](http://wiki.dreamhost.com/SSH) 
 * [HostGator: How Do I Get and Use SSH Access?](http://support.hostgator.com/articles/hosting-guide/lets-get-started/how-do-i-get-and-use-ssh-access)

When you're connected, you should see a prompt that looks roughly like this: 

```
user@host # 
```

This is where we will be entering our commands. 

## Step 2: Install a LAMP server. 

LAMP stands for Linux, Apache, MySQL, and PHP, and it's the set of software that runs Omeka. Linux is the operating system that runs the server, Apache is the web serving software, MySQL is the database, and PHP is the language in which Omeka is written. If you're on a shared hosting provider, chances are you already have this installed, and you can skip to step 3b. If you're on a VPS, we'll install it manually. First, let's update our system:  

```bash
sudo apt-get update && sudo apt-get upgrade
```

Now that our system is up-to-date, let's install the server stack: 

```bash
sudo apt-get install lamp-server^
```

Be sure to include the caret (`^`) at the end. This should install a LAMP server, prompting you to enter a root MySQL password. Enter a secure password here, and write it down, because we'll be using it later. 

## Step 3a: Create a database (for VPSs). 

If you're using a VPS, you're in luck---setting up a new database is just a matter of running a few commands. If you're using shared hosting, there is a different process---for that, you can skip to Step 3b. 

First, log in to the MySQL database program as the root user, by entering this command: 

```bash
mysql -u root -p
```

It should ask you for the password you created in step 2. You should now see a `mysql>` prompt. Now, let's enter a command to create the database. I'm going to call my database `jonreeve_omeka`, but you can call yours whatever you like. 

```SQL
CREATE DATABASE `jonreeve_omeka` CHARACTER SET utf8 COLLATE utf8_general_ci;
```

Here, `CHARACTER SET utf8 COLLATE utf8_general_ci` ensures that you can use the full character set in your web site, and not just the Latin character set. 

Next, let's create a database user account, so that Omeka can talk to the database: 

```SQL
CREATE USER 'jonreeve_omeka'@'localhost' IDENTIFIED by '%8)&2P^TFR2C'; 
```

I've given my user the same name as my database for convenience, and I've chosen `%8)&2P^TFR2C` as my secure password. 

Now we can allow this new user to access our newly-created database by typing these commands: 

```SQL
GRANT ALL PRIVILEGES ON jonreeve_omeka.* TO 'jonreeve_omeka'@'localhost';
FLUSH PRIVILEGES; 
```

Your database should now be set up for use with Omeka. 

## Step 3b: Create a database (for shared hosting providers). 

Follow this step if you're using a shared hosting provider. If you're on a VPS, you can skip to step 4.  

Log into your hosting provider's control panel and find an item called something like "MySQL Databases." If your hosting provider uses cPanel, it looks like this: 

![New Database](../images/omeka-install-new-db.png)

In the box labeled Create New Database, enter a database name. On shared hosting providers, the prefix will typically be your user name (mine is `jonreeve`), and you'll enter the rest. In this example, I chose to call my database `omeka`, so my full database name is `jonreeve_omeka`. Click "create database." 

Once you've done that, click to go back to the previous screen. Below the Create New Database box you'll see an area for creating new MySQL users. It looks like this: 

![Create a New User](../images/omeka-install-new-user.png)

In the box labeled `Username`, enter the same thing you entered for your database name (this is just a convention, and will help you to keep everything organized). I'll enter `omeka` again, so that the full user name reads `jonreeve_omeka`. It's a good idea to click "generate password" here, since that will make a very secure password. At this point, write down the database name (`jonreeve_omeka`), the user name (which should be the same as the database name), and the generated password, since you'll need these later. 

![Generate Password](../images/omeka-install-password.png)

Next, add the user you just created to the database. Just select the user and the database you created in the dropdown menus and click "add": 

![Add User to Database](../images/omeka-install-add-to-db.png)

Your database is now set up, and you're ready to install Omeka. 

## Step 4: Download and install Omeka. 

Let's download Omeka directly to the server. This will allow us to avoid the process of downloading it locally, unzipping it there, and uploading it to the server, and we'll save a lot of time and bandwidth. To do this, let's first change in the public HTML directory. This is usually `/var/www/html`, but could also be `/var/www`, or, on some shared hosts, `~/public_html`: 

 * `cd /var/www/html` (DigitalOcean)
 * `cd ~/public_html` (HostGator) 

Now let's download Omeka. Grab the URL from http://omeka.org/download, and use it with the command `wget` like this: 

    wget http://omeka.org/files/omeka-2.2.2.zip

This will download Omeka to your public directory. Now unzip it like this: 

    unzip omeka-2.2.2.zip

This will unzip Omeka to a subdirectory on your website. Presuming you don't want your Omeka web site to have the URL `http://your-domain.com/omeka-2.2.2/`, let's change the name of the directory: 

    mv omeka-2.2.2 omeka

(Instead of `omeka-2.2.2`, substitute the version you downloaded.) Now you have an Omeka install which is ready to wire to the database. 

## Step 5: Configure Omeka to Use Your Database. 

First, go into the directory where your Omeka install lives. On a VPS, that's probably `/var/www/html/omeka`, and on shared hosting, `~/public_html/omeka`. 

    cd /var/www/html/omeka

Now let's edit the `db.ini` file. Unless you're already comfortable with a power editor like Vim, we're going to use the editor Nano: 

    nano db.ini

That will give you something that looks like this: 

![Db.ini, Before](../images/omeka-install-db-ini-before.png)

Now you can edit your file. The field `hostname` should be `localhost`, since the database is on the same server. For `username` and `dbname`, enter the user name password, and database name you generated in Step 3a or 3b. It will end up looking like this: 

![Db.ini, After](../images/omeka-install-db-ini-after.png) 

Exit (Ctrl+X) and when asked, save your changes. Now you should have a working Omeka install. You can access it at `http://your-domain.com/omeka/`, replacing `your-domain` with the name of your domain, and `omeka` with the name you gave your directory above. Go to `http://your-domain.com/omeka/admin` to get started configuring your install. If you run into any trouble along the way, consult the [Omeka Installation Guide](https://omeka.org/codex/Installation) or the [Omeka Troubleshooting Guide](https://omeka.org/codex/Troubleshooting_Omeka). 
