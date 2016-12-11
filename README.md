# shitXsays

Once upon a time, a friend said something genius. This may have been

> no handshake
> holy shit
> so rude
> what the fuck
> report that cunt

or

> if sydney water can deal with millions of people's shit, they can deal with mine

and you may want to record these so one day you can laugh at the memories.

So I did that. First in a shitty PHP script that read from text files. Now we've upgraded into the 21st century and moved to the wonders of python. 

# Installation

This presumes you're running an NGINX stack with uwsgi emperor installed.

If you're not sure how to uwsgi, then follow this guide - [vladdik's uwsgi setup](http://vladikk.com/2013/09/12/serving-flask-with-nginx-on-ubuntu/)

and symlink the `.ini` into your vassals directory.

you'll also need to set up a virtualenv with all the requirements.

```bash
cd /wherever/you/git/cloned
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Hopefully if you have that done. pray and you should be good.

# License

        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.


Disclaimer: This does not extend to any of the softwares, binaries or libraries used in these scripts. Whatever license they have applies there
