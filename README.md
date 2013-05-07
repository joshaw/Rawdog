Rawdog
======

My copy of the Rawdog RSS reader with my configs and styles.

* This folder contains a style and script that I use to read the html outout from Rawdog.
* The `templates/` folder contains the nessessary global and item templates, and the `style.css` stylesheet is used.
* All the hard work done by [Adam Sampson](http://offog.org).
* More info on Rawdog at the [website](http://offog.org/code/rawdog.html).

To Install
---------

This folder is just my `.rawdog` folder as a git repo. So

    cd && git clone https://github.com/jaw42/rawdog .rawdog

and you'll be away. Of course, that'll leave you with all of my feeds. These are stored in the `config` file. Remove them and add your own.

###Notes###

* The plugins folder contains the plugins that I use. These are not all essential, at the moment, none of them are required.
* Go to `http://offog.org/code/rawdog.html` for more plugins.

Template
--------
The template is just that, a template for Rawdog to fill with news-y goodness from your feeds.

![Feed template](templates/example.png?raw=true)

There are controls to move up and down, or the keyboard can be used to navigate. `j` goes to next feed (older to newer) and `k` goes the other way. 

There is an early implementation of recalling read feeds. The page is written in HTML5 and uses the local storage for saving read items.

Bugs
----
* Any suggestions, please let me know.
* I know there are many bugs, any help you can offer to improve, greatly appreciated, but let me know of any bugs if you find them - and if so, thank you very much cause that means you've used it.
