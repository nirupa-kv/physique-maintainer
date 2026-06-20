# seed_database.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Extra engineering protection layer: strip any trailing paths if they accidently leak back into the environment
if SUPABASE_URL:
    SUPABASE_URL = SUPABASE_URL.split("/rest/v1")[0].rstrip("/")

print(f"🔌 Connecting to your Supabase Cloud Database instance at: {SUPABASE_URL}")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

MASTER_FOOD_ENTRIES = [
    # ==================== SOUTH INDIAN CULINARY PARTITION ====================
    {"food_name": "Masala Dosa", "cuisine_type": "South Indian", "base_calories_per_serving": 280, "standard_portion": "1 Medium Dosa"},
    {"food_name": "Plain Dosa", "cuisine_type": "South Indian", "base_calories_per_serving": 140, "standard_portion": "1 Medium Dosa"},
    {"food_name": "Idli Sambar (2 Pcs)", "cuisine_type": "South Indian", "base_calories_per_serving": 160, "standard_portion": "1 Plate (2 Idlis + Sambar)"},
    {"food_name": "Medu Vada (2 Pcs)", "cuisine_type": "South Indian", "base_calories_per_serving": 240, "standard_portion": "1 Plate (2 Vadas)"},
    {"food_name": "Rava Uttapam", "cuisine_type": "South Indian", "base_calories_per_serving": 190, "standard_portion": "1 Medium Uttapam"},
    {"food_name": "Rava Upma", "cuisine_type": "South Indian", "base_calories_per_serving": 210, "standard_portion": "1 Plate (150g)"},
    {"food_name": "Ven Pongal", "cuisine_type": "South Indian", "base_calories_per_serving": 230, "standard_portion": "1 Bowl (150g)"},
    {"food_name": "Sambar Sadam (Rice)", "cuisine_type": "South Indian", "base_calories_per_serving": 220, "standard_portion": "1 Full Bowl"},
    {"food_name": "Thayir Sadam (Curd Rice)", "cuisine_type": "South Indian", "base_calories_per_serving": 250, "standard_portion": "1 Full Bowl"},
    {"food_name": "Pulihora (Tamarind Rice)", "cuisine_type": "South Indian", "base_calories_per_serving": 280, "standard_portion": "1 Bowl"},
    {"food_name": "Lemon Rice", "cuisine_type": "South Indian", "base_calories_per_serving": 250, "standard_portion": "1 Bowl"},
    {"food_name": "Coconut Rice", "cuisine_type": "South Indian", "base_calories_per_serving": 350, "standard_portion": "1 Bowl"},
    {"food_name": "Rasam Rice", "cuisine_type": "South Indian", "base_calories_per_serving": 180, "standard_portion": "1 Full Bowl"},
    {"food_name": "Malabar Parotta", "cuisine_type": "South Indian", "base_calories_per_serving": 200, "standard_portion": "1 Layered Parotta"},
    {"food_name": "Appam (2 Pcs) with Vegetable Stew", "cuisine_type": "South Indian", "base_calories_per_serving": 280, "standard_portion": "1 Plate"},
    {"food_name": "South Indian Fish Curry", "cuisine_type": "South Indian", "base_calories_per_serving": 220, "standard_portion": "1 Medium Bowl"},
    {"food_name": "Chicken Chettinad Curry", "cuisine_type": "South Indian", "base_calories_per_serving": 320, "standard_portion": "1 Medium Bowl"},
    {"food_name": "Vegetable Poriyal / Thoran", "cuisine_type": "South Indian", "base_calories_per_serving": 110, "standard_portion": "1 Bowl (150g)"},
    {"food_name": "Avial", "cuisine_type": "South Indian", "base_calories_per_serving": 140, "standard_portion": "1 Cup (150g)"},
    {"food_name": "Payasam / Kheer", "cuisine_type": "South Indian", "base_calories_per_serving": 210, "standard_portion": "1 Small Katori"},
    {"food_name": "Filter Coffee (With milk & sugar)", "cuisine_type": "South Indian", "base_calories_per_serving": 110, "standard_portion": "1 Tumbler (150ml)"},

    # ==================== NORTH INDIAN CULINARY PARTITION ====================
    {"food_name": "Paneer Butter Masala", "cuisine_type": "North Indian", "base_calories_per_serving": 380, "standard_portion": "1 Medium Bowl"},
    {"food_name": "Butter Naan", "cuisine_type": "North Indian", "base_calories_per_serving": 280, "standard_portion": "1 Large Naan"},
    {"food_name": "Phulka / Chapati (Without Ghee)", "cuisine_type": "North Indian", "base_calories_per_serving": 80, "standard_portion": "1 Thin Piece"},
    {"food_name": "Chapati with Ghee", "cuisine_type": "North Indian", "base_calories_per_serving": 110, "standard_portion": "1 Piece + 0.5 tsp Ghee"},
    {"food_name": "Chole Bhature (2 Bhaturas)", "cuisine_type": "North Indian", "base_calories_per_serving": 580, "standard_portion": "1 Plate Serving"},
    {"food_name": "Dal Makhani", "cuisine_type": "North Indian", "base_calories_per_serving": 210, "standard_portion": "1 Cup (200ml)"},
    {"food_name": "Dal Tadka", "cuisine_type": "North Indian", "base_calories_per_serving": 130, "standard_portion": "1 Cup (200ml)"},
    {"food_name": "Rajma Curry", "cuisine_type": "North Indian", "base_calories_per_serving": 240, "standard_portion": "1 Cup (200ml)"},
    {"food_name": "Chole Masala", "cuisine_type": "North Indian", "base_calories_per_serving": 250, "standard_portion": "1 Cup (200ml)"},
    {"food_name": "Palak Paneer", "cuisine_type": "North Indian", "base_calories_per_serving": 280, "standard_portion": "1 Cup (200ml)"},
    {"food_name": "Aloo Paratha (With Butter/Curd)", "cuisine_type": "North Indian", "base_calories_per_serving": 310, "standard_portion": "1 Stuffed Paratha"},
    {"food_name": "Methi Paratha", "cuisine_type": "North Indian", "base_calories_per_serving": 220, "standard_portion": "1 Medium Piece"},
    {"food_name": "Besan Chilla", "cuisine_type": "North Indian", "base_calories_per_serving": 120, "standard_portion": "1 Medium Piece"},
    {"food_name": "Poha (With peanuts/veggies)", "cuisine_type": "North Indian", "base_calories_per_serving": 200, "standard_portion": "1 Cooked Cup (150g)"},
    {"food_name": "Puri Bhaji (2 Puris + Sabzi)", "cuisine_type": "North Indian", "base_calories_per_serving": 380, "standard_portion": "1 Breakfast Plate"},
    {"food_name": "Jeera Rice / Plain Pulao", "cuisine_type": "North Indian", "base_calories_per_serving": 240, "standard_portion": "1 Cup (150g)"},
    {"food_name": "Chicken Biryani", "cuisine_type": "North Indian", "base_calories_per_serving": 520, "standard_portion": "1 Full Plate (300g)"},
    {"food_name": "North Indian Chicken Curry", "cuisine_type": "North Indian", "base_calories_per_serving": 280, "standard_portion": "200g serving size"},
    {"food_name": "Bhindi Masala", "cuisine_type": "North Indian", "base_calories_per_serving": 140, "standard_portion": "1 Cup (150g)"},
    {"food_name": "Aloo Gobi", "cuisine_type": "North Indian", "base_calories_per_serving": 160, "standard_portion": "1 Cup (150g)"},
    {"food_name": "Samosa", "cuisine_type": "North Indian", "base_calories_per_serving": 180, "standard_portion": "1 Medium Piece (80g)"},
    {"food_name": "Gulab Jamun", "cuisine_type": "North Indian", "base_calories_per_serving": 150, "standard_portion": "1 Medium Piece"},
    {"food_name": "Gajar Halwa", "cuisine_type": "North Indian", "base_calories_per_serving": 240, "standard_portion": "Half Cup (100g)"},
    {"food_name": "Masala Chai (With milk & sugar)", "cuisine_type": "North Indian", "base_calories_per_serving": 90, "standard_portion": "1 Cup (150ml)"}
]

try:
    print(f"🚀 Initializing push migration for {len(MASTER_FOOD_ENTRIES)} items...")
    response = supabase.table("indian_food_db").insert(MASTER_FOOD_ENTRIES).execute()
    print("✅ Success! All entries are safely inside your live Supabase table dashboard layout.")
except Exception as e:
    print(f"❌ Error during cloud data migration seed sequence: {e}")