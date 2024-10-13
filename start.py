from typing import Union

import requests
import streamlit as st


def get_removed_timestamp_url(cur_url: str) -> Union[str, None]:
    # sanity check on if tiktok.com exists within the url
    if "tiktok.com" not in cur_url:
        st.write("url provided is not from tiktok.com")
        return

    response: requests.Response = requests.get(cur_url)

    if response.status_code != 200:
        st.write("unable to reach tiktok.com, please try again")
        return

    query_index: int = response.url.find("?")

    if query_index == -1:
        st.write("url provided is not a direct link to a tiktok")
        return

    return response.url[: query_index + 1]


def open_url_in_new_window(cur_url: str) -> None:
    js_block: str = (
        "<script type='text/javascript'>"
        f"window.open('{cur_url}', '_blank').focus();"
        "</script>"
    )
    st.components.v1.html(js_block)


st.title("allowtok")
st.write("opens a tiktok url without any restrictions in a mobile browser")
st.write("*fyi: please disable pop up blockers so that we can redirect you*")

potential_url: str = st.text_input("paste tiktok url below 👇")
if potential_url:
    url_to_use: Union[str, None] = get_removed_timestamp_url(potential_url)
    if url_to_use:
        open_url_in_new_window(url_to_use)
