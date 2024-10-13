# allowtok

https://allowtok.onrender.com/

picture this:

no tiktok on your phone by choice

your friend sends you a link to a tiktok that they thought you'd like

you decide to click on it and it brings you to your mobile browser

from here, you click the play button and **bam**, tiktok redirects you to the
app store asking you to install tiktok

annoyed, you tried looking up the fix to this and stumbled upon
https://www.reddit.com/r/Tiktokhelp/comments/1cxeaf6/comment/l5cmpow/

what a blessing but it still is annoying to have to open manually edit the
timestamps out of the query string every time

and so this was born. extremely simple web app to redirect you to a tiktok link
without the timestamps in the query string so that it just works

# local usage

utilizing `uv` - https://github.com/astral-sh/uv

```sh
uv run streamlit run start.py
```
