# database.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# This loads local settings when working on your computer
load_dotenv()

# Extract your credentials cleanly from either local files or Cloud Secrets
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials! Add them to your local .env file or your Cloud Secrets dashboard settings.")

# Clean up accidental quote marks or white spaces that could break the client validation check
SUPABASE_URL = SUPABASE_URL.strip().strip('"').strip("'")
SUPABASE_KEY = SUPABASE_KEY.strip().strip('"').strip("'")

# Initialize the live cloud database connection client
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
        print(f"Error communicating with live cloud table: {e}")
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
        print(f"Error fetching workouts: {e}")
        return []