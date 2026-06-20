# database.py
import os
import base64
import json
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials! Add them to your local .env file or your Cloud Secrets dashboard settings.")

SUPABASE_URL = SUPABASE_URL.strip().strip('"').strip("'")
SUPABASE_KEY = SUPABASE_KEY.strip().strip('"').strip("'")

def decode_jwt_payload(token):
    try:
        payload_b64 = token.split(".")[1]
        padded = payload_b64 + "=" * (-len(payload_b64) % 4)
        return json.loads(base64.urlsafe_b64decode(padded))
    except Exception as e:
        return {"decode_error": str(e)}

st.caption(f"Debug: SUPABASE_URL = {SUPABASE_URL}")
st.caption(f"Debug: key length={len(SUPABASE_KEY)}, starts={SUPABASE_KEY[:8]}, ends={SUPABASE_KEY[-8:]}")
st.json(decode_jwt_payload(SUPABASE_KEY))

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_indian_foods(cuisine_type: str):
    """
    Queries your live Supabase cloud database table.
    Filters entries dynamically based on chosen regional culinary partitions.
    """
    try:
        response = supabase.table("indian_food_db")\
            .select("*")\
            .eq("cuisine_type", cuisine_type)\
            .execute()
        return response.data
    except Exception as e:
        st.error(f"Supabase error (fetch_indian_foods): {e}")
        return []

def fetch_targeted_workouts(segment: str):
    """Queries live workout libraries for specific body segment geometry targets."""
    try:
        response = supabase.table("workout_library")\
            .select("*")\
            .eq("target_segment", segment.lower())\
            .execute()
        return response.data
    except Exception as e:
        st.error(f"Supabase error (fetch_targeted_workouts): {e}")
        return []