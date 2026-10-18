
import streamlit as st
from supabase import create_client, Client

url = st.secrets["SUPABASE_URL"].strip()
key = st.secrets["SUPABASE_KEY"].strip()

# Temporary diagnostic checks
st.write("Supabase URL:", url.split("//")[-1].split(".")[0])
st.write("Key starts with publishable prefix:",
         key.startswith("sb_publishable_"))
st.write("Key length:", len(key))

supabase: Client = create_client(url, key)
