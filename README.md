Practical Tools to Pursue Open Science
======================================

This repository contains the source files for the tutorial given in [ICFO](http://icfo.eu/) on 4 June 2015.

Abstract
--------
Open science lowers barriers to access scientific work, fosters collaboration, and helps young researchers to build up reputation. While open science has many aspects, in this tutorial, we focus on sharing code and computational details in extensible and didactic forms, and on setting up an academic website. In particular, we will at the basics of open source development on GitHub along with establishing some good practices, then we will talk about literate programming and computational notebooks, and finally we show how to start a blog-aware, science-friendly website without costs or knowing web programming. While the tools to be discussed are language agnostic, we will use Python during the hands-on examples.

Files
-----

 - README.md: This file containing basic documentation in Markdown format.
 
 - practical_open_science.tex: Source file for slides. View the slides here.
 
 - improve_me.py: A Python script that could see lots of improvement.
 
 - example_notebook.ipynb: An example Jupyter notebook. View it [here](http://nbviewer.ipython.org/github/peterwittek/open_science_tutorial/blob/master/example_notebook.ipynb).

Git summary
-----------
First clone your forked repository (you only have to do it once):

    git clone https://github.com/username/open_science_tutorial.git
    
Change into the folder and make arbitrary improvements on the code or on the documentation. Then give your improvements some meaningful name in a commit:

    git commit -am "Whatever you improved"
    
Push this commit to GitHub:

    git push origin master
    
Send a pull request on GitHub to merge your changes.

There will also be changes made by others. To keep things in sync in your own repository, first add the upstream link to your repository (you only have to do this once):

    git remote add upstream https://github.com/peterwittek/open_science_tutorial.git

Next, fetch the upstream changes:

    git fetch upstream
    
Make sure you are working on your own branch:

    git checkout master

Now merge the upstream changes:

    git merge upstream/master

Pelican summary
---------------
Install Pelican and a script used for uploading your site to GitHub:

    pip install pelican
    pip install gph-import

Getting started:

    pelican-quickstart

Then edit pelicanconf.py. Start adding content, for instance, a whatever.md file:

    Title: First entry
    Date: 2015-06-04 11:45
    Category: Whatever

    Abritrary text here that you want to write.

Generate your website:

    pelican content
    
It will not look great at first. You can look at the result by starting a web server in the output folder:

    python2 -m SimpleHTTPServer
    
Navigate to [http://localhost:8000/](http://localhost:8000/) to see the result. Look at the [quickstart](http://docs.getpelican.com/en/3.5.0/quickstart.html) in the Pelican documentation for some further quick tips.

Choose a [theme](http://pelicanthemes.com/), clone the one you fancy, and edit pelicanconf.py and publishconf.py to use it. 

Put the website in git version control: 

    git init
    git add *py content Makefile
    git commit -am "Initial commit"

To publish the site on GitHub, create a repository username.github.io. Add it to your git repository:

    git remote add origin https://github.com/username/username.github.io.git

Then, whenever you make changes, push them to GitHub:

    ghp-import output
    git push git@github.com:username/username.github.io.git gh-pages:master
