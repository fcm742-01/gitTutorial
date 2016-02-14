<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. Introduction</a></li>
<li><a href="#orgheadline2">2. Set up your github account</a></li>
<li><a href="#orgheadline5">3. Mac and windows</a>
<ul>
<li><a href="#orgheadline3">3.1. Mac</a></li>
<li><a href="#orgheadline4">3.2. Windows</a></li>
</ul>
</li>
<li><a href="#orgheadline11">4. Configure git on your local machine [Don't skip]</a>
<ul>
<li><a href="#orgheadline10">4.1. On your machine open a terminal</a>
<ul>
<li><a href="#orgheadline6">4.1.1. Mac</a></li>
<li><a href="#orgheadline9">4.1.2. Windows</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline12">5. Command line tutorial</a></li>
<li><a href="#orgheadline15">6. The filesystem</a>
<ul>
<li><a href="#orgheadline13">6.1. Mac OS X</a></li>
<li><a href="#orgheadline14">6.2. Windows</a></li>
</ul>
</li>
<li><a href="#orgheadline16">7. Set global git variables</a></li>
<li><a href="#orgheadline17">8. Clone the repository from your github account to your local machine</a></li>
<li><a href="#orgheadline18">9. Master vs. branch</a></li>
<li><a href="#orgheadline19">10. Switch branches</a></li>
<li><a href="#orgheadline20">11. Create a directory</a></li>
<li><a href="#orgheadline21">12. Copy your picture into that directory</a></li>
<li><a href="#orgheadline22">13. Add your picture to your branch</a></li>
<li><a href="#orgheadline23">14. Commit your local changes</a></li>
<li><a href="#orgheadline26">15. See everyone's changes</a>
<ul>
<li><a href="#orgheadline24">15.1. Configure an upstream master</a></li>
<li><a href="#orgheadline25">15.2. Sync the fork</a></li>
</ul>
</li>
<li><a href="#orgheadline27">16. Pull request</a></li>
</ul>
</div>
</div>


# Introduction<a id="orgheadline1"></a>

This is the repo for FCM-742, sections 01, Spring 2016, you have to
add a directory and upload a picture of your face.

This is the README file for the repo.  Everyone is going to create
a fork of this repository and create a directory whose name is

    mkdir firstName_lastName

where your last name is separated from your first with an underscore
"\_".  For example, my name is Evan Misshula. My directory would be:

    mkdir Evan Misshula

 Once you have done this copy a picture of your face into the
directory.  Next you will send me a pull request from your branch to
add it to the repo. 

Read on for details.

# Set up your github account<a id="orgheadline2"></a>

Set up the github account.  The next thing you should do is 
fork the repository.  That means that you create your own copy of the
repository in your github account.

![img](images/fork.png)

You don't edit anything on github.  Github stores your backup.  In
order to edit your repo you have to copy it to your machine.  This
requires you to download the git program to your local machine.  You
will then need to install it.  There are several ways to do this.

# Mac and windows<a id="orgheadline5"></a>

## Mac<a id="orgheadline3"></a>

You just need to go this link:

<http://git-scm.com/download/mac>

Double click on the downloaded file and install in the usual way.

## Windows<a id="orgheadline4"></a>

You just need to go this link:

<http://git-scm.com/download/win>

Double click on the downloaded file and install in the usual way.

# Configure git on your local machine [Don't skip]<a id="orgheadline11"></a>

## On your machine open a terminal<a id="orgheadline10"></a>

### Mac<a id="orgheadline6"></a>

Left click on launchbad (the icon with the rocket on it).  In the
search bar type terminal.  Left click the terminal and you are there.

### Windows<a id="orgheadline9"></a>

1.  Windows 8 and 8.1

    Right click on the Start button. This opens the power user menu.
    There is a shortcut for the terminal on that. Left click on it and you
    are there. Here is a larger article on this:
    
    <http://pcsupport.about.com/od/windows-8/a/command-prompt-windows-8.htm>

2.  Windows 7

    Click on the Start button. In the search box, type the following:
    
    `command` 
    
    Click on Command Prompt in the search results listing. Here is a
    larger reference.
    
    <http://pcsupport.about.com/od/windows7/a/command-prompt-windows-7.htm>

# Command line tutorial<a id="orgheadline12"></a>

The command line is the primary way to interact with your operating system.  We are only going
to use a few commands but we have to use different commands depending whether you are running
windows or mac.  Mac and Linux systems have mostly the same commands since Mac OS X is built on top
of Berkley Software Distribution Unix.  Linux and Mac are sometimes called \*nix systemes. Windows
NT (the forerunner of Windows 7 and Windows 8) was built by the designers of Digital Equipment Corporation
(DEC) Vax system.

Here are the commmands we will use:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">\*nix</th>
<th scope="col" class="org-left">windows</th>
<th scope="col" class="org-left">puropse</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">pwd</td>
<td class="org-left">echo %cd%</td>
<td class="org-left">tell us what directory we are in</td>
</tr>


<tr>
<td class="org-left">ls</td>
<td class="org-left">dir</td>
<td class="org-left">list the files in the directory we are in</td>
</tr>


<tr>
<td class="org-left">cp</td>
<td class="org-left">copy</td>
<td class="org-left">copy files from one place to another</td>
</tr>


<tr>
<td class="org-left">cd</td>
<td class="org-left">cd</td>
<td class="org-left">change directory</td>
</tr>


<tr>
<td class="org-left">.</td>
<td class="org-left">.</td>
<td class="org-left">means here</td>
</tr>


<tr>
<td class="org-left">..</td>
<td class="org-left">..</td>
<td class="org-left">up one directory</td>
</tr>
</tbody>
</table>

# The filesystem<a id="orgheadline15"></a>

## Mac OS X<a id="orgheadline13"></a>

Your documents are in: 

`/Users/<your name>/Documents`  

In the terminal type:

`cd Documents`

To check where you are type:

`pwd`

This returns the present working directory.

## Windows<a id="orgheadline14"></a>

Your Documents are in C:\Users\\<your name>\Documents.  In the terminal type:

`cd Documents`

# Set global git variables<a id="orgheadline16"></a>

Tell Git your name so your commits will be properly labeled. Type
everything after the $ here:

    git config --global user.name "Your Name"

Tell Git the email address that will be associated with your Git
commits. The email you specify should be the same one you used to sign
up for GitHub.

    git config --global user.email "YOUR EMAIL ADDRESS"

# Clone the repository from your github account to your local machine<a id="orgheadline17"></a>

Now go back to your browser and open up the repo that you forked.  On
the right side of the page near the top, there is a box under
settings.  **BE CAREFUL** This is tricky. In that box is the URL of your
fork.  Here is a picture.

![img](images/url.png)

Make sure the protocol is set to https. The others require you to set
up ssh keys which are worth a whole tutorial to themselves.  Now that
you know what you are looking for.  Copy it to the clipboard by
left-clicking the button. You clone it by typing:

    git clone https@github.com:<your_github_username>/gitTutorial.git

Now you have your own copy of the repo both on your machine and in your github account.
If you want to work with the files in the `gitTutorial` directory, you should change into 
that directory. To do this you should type:

    cd gitTutorial

In an text editor, you can look at any of the files. You can also list the files by 
typing either `ls` or `dir` depending on your operating system.

# Master vs. branch<a id="orgheadline18"></a>

You actually have a copy of the master on your machine.  When you add something
for the first time, you should not add to the master you should make changes to 
your own branch. Usually the branch name is the topic.  In this case use your
first name.  Type:

`git branch <first_name>`

We can see all of the branches by typing:

`git branch`

The star means that we are still on the master branch.

# Switch branches<a id="orgheadline19"></a>

Now we are going to begin constructing the changes we want
incorporated into the main project. In the last section we made a
branch now we are going to start to change it.  To switch to your
branch, type:

`git checkout <first_name>`

# Create a directory<a id="orgheadline20"></a>

If you listed the files in the gitTutorial directory, you should see
that there is a directory called students. You should change
directories into it by typing:

    cd students/sect01

or 

    cd students/sect01

Create a directory with your first and last name from the command line:

`mkdir <firstName_LastName>`

# Copy your picture into that directory<a id="orgheadline21"></a>

You can use the command line or a gui to copy your picture into the
directory you just created.

# Add your picture to your branch<a id="orgheadline22"></a>

Make sure your image file is called your `firstName_lastName.jpg` or
`firstName_lastName.png`.  For example, my photo would be
`Evan_Misshula.jpg`.

Next add your picture to your branch.  You will do
this by adding your image file to your branch by typing:

    git add firstName_lastName.jpg

# Commit your local changes<a id="orgheadline23"></a>

You should save or commit your changes with a message.  Type the following:

    git commit -m "added my picture."

To update your copy on github you have to push your changes which are in 
your firstName branch. Before I show you how to do that, let's make sure
no one else has pushed changes that will cause a conflict with our changes.

# See everyone's changes<a id="orgheadline26"></a>

## Configure an upstream master<a id="orgheadline24"></a>

Git does not automatically know where you want to pull from.
To see where git is pulling from, type:

    git remote -v

The "-v" is a common command line flag for verbose.  Because you 
forked both the (fetch) where you pull from and where you push to
(push) are the same. Now specify a new upstream repository that will
be synced by the fork.

    git remote add upstream git://github.com/fcm742-01/gitTutorial.git

## Sync the fork<a id="orgheadline25"></a>

To see everyone's accepted changes to the master, you have to pull
from the upstream master. This requires a *fetch* command.  Make sure
that you have commited your changes.  Type:

    git fetch upstream

You have now pulled the changes from my branch to your local machine
and onto your `firstName` branch. The next step is to merge it into
your `firstName` branch.

    git merge upstream/firstName

You will want to save those to your github account as well.  So to finish, type:

    git push origin firstName

# Pull request<a id="orgheadline27"></a>

If you refresh your github page you will see that the repository now
has two braches.  Switch to the firstName branch and send a pull
request.