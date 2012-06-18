Using DOT language to produce Flowchart
#######################################
:date: 2008-12-09 10:01
:tags: graphviz, generating, dot, flowchart

better than struggling with the graphical tools.

::

    shon@ubuntu:~$ cat test.dot
    
    digraph FlowChart {
    
     node [
             fontname = "Bitstream Vera Sans"
             fontsize = 8
             shape = "record"
         ]
    
     edge [
             fontname = "Bitstream Vera Sans"
             fontsize = 8
             fontcolor = "Red"
         ]
    
    // all blocks
    greet [label="Hello, techie", shape="oval"]
    which_os [label="What OS do you use?" shape="diamond"]
    like_me [label="Great, me too!", shape="oval"]
    which_browser [label="You must be using firefox", shape="diamond"]
    ff [label="Cool", shape="oval"]
    bye [label="Bye", shape="oval"]
    
    // relations
    greet -> which_os
    which_os -> like_me [label="I use Linux"]
    which_os -> which_browser [label="I use Windows"]
    which_browser -> ff [label="Right"]
    which_browser -> bye [label="what firefox?"]
    }
    
    shon@ubuntu:~$ dot test.dot -Tpng -o test.png && eog test.png
