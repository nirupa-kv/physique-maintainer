# app.py
import streamlit as st
import database as db
import core_math as cm

st.set_page_config(page_title="Physique Maintainer Pro", layout="wide")

# Top Navigation Option Bar Menu
st.title("🏋️‍♂️ Physique Maintainer MVP Platform")
navigation_tab = st.radio(
    "🧭 Select Application Sub-System Module:", 
    ["1. BMI Range Calculator", "2. 2D Physique Transformer", "3. Ideal Weight Metric Range", "4. Somatotype Body Type Finder", "5. Pan-Indian Calorie Tracker"],
    horizontal=True
)
st.write("---")

# MODULE 1: BMI CALCULATOR WITH VISUAL COLOR ARCS
if navigation_tab == "1. BMI Range Calculator":
    st.header("📊 Universal Multi-Metric BMI Analyzer")
    
    col1, col2 = st.columns(2)
    with col1:
        w = st.number_input("Enter Current Weight Balance", value=70.0)
        w_u = st.selectbox("Weight Scalar Unit", ["kg", "lbs"])
    with col2:
        h = st.number_input("Enter Height Vector", value=170.0)
        h_u = st.selectbox("Height Scalar Unit", ["cm", "ft", "in"])
        
    bmi = cm.calculate_clean_bmi(w, w_u, h, h_u)
    st.write("---")
    
    col_text, col_gauge = st.columns([1, 1.2])
    
    with col_text:
        st.subheader(f"Calculated Score Metric: {bmi}")
        if bmi < 18.5:
            st.error("Status: Underweight Range Indicator Zone 🟡")
            st.caption("Consider speaking with a professional about nutrition strategy to reach equilibrium baseline parameters.")
        elif bmi <= 24.9:
            st.success("Status: Normal / Healthy Equilibrium Arc Zone 🟢")
            st.caption("Excellent status layout profile! Keep up the functional movement and dietary baseline standards.")
        elif bmi <= 29.9:
            st.warning("Status: Overweight Warning Zone 🟠")
            st.caption("Slightly elevated baseline concentration. Your customized movement pipeline can help modify your physical landmarks.")
        else:
            st.error("Status: Obesity Critical Zone 🔴")
            st.caption("Critical structural balance warning. Utilize localized tracking modules to systematically manage metabolic markers.")
            
    with col_gauge:
        import plotly.graph_objects as go
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = bmi,
            domain = {'x': [0, 1], 'y': [0, 1]},
            number = {'font': {'size': 44, 'color': '#2E3440'}},
            gauge = {
                'axis': {'range': [10, 40], 'tickwidth': 1, 'tickcolor': "#4C566A"},
                'bar': {'color': "#2E3440", 'thickness': 0.15}, 
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#D8DEE9",
                'steps': [
                    {'range': [10, 18.5], 'color': '#FFEAA7'}, 
                    {'range': [18.5, 25], 'color': '#55EFC4'},   
                    {'range': [25, 30], 'color': '#FAB1A0'},    
                    {'range': [30, 40], 'color': '#FF7675'}     
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': bmi
                }
            }
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=30, b=20),
            height=300
        )
        st.plotly_chart(fig, width='stretch')

# MODULE 2: 3D PHYSIQUE TRANSFORMER MODELLING SLIDERS
elif navigation_tab == "2. 2D Physique Transformer":
    st.header("🧍 Anthropometric Segment Anatomy Modeller")
    
    col_ui, col_gfx = st.columns([1, 1])
    with col_ui:
        gender = st.selectbox("Select Target Gender Base Shape", ["Female", "Male"])
        view = st.radio("Orientation Perspective", ["Front", "Side"])
        
        st.write("**Anatomical Measurement Metrics Configuration (Inches):**")
        arms = st.slider("Arm Size Vector (in)", 5.0, 25.0, 12.0)
        chest = st.slider("Chest Arc Circumference (in)", 20.0, 60.0, 36.0)
        hips = st.slider("Hip Contour Structure (in)", 20.0, 60.0, 36.0)
        waist = st.slider("Core Waist Perimeter (in)", 20.0, 60.0, 32.0)
        thighs = st.slider("Lower Leg Thigh Dimension (in)", 10.0, 40.0, 20.0)
        
    with col_gfx:
        st.subheader("Interactive 3D Human Model Transformation Matrix")
        model_svg = cm.generate_full_body_avatar(gender, arms, chest, hips, waist, thighs, view)
        st.components.v1.html(model_svg, height=480)

# MODULE 3: IDEAL MEDICAL WEIGHT SPAN TRACKER
elif navigation_tab == "3. Ideal Weight Metric Range":
    st.header("🎯 Predictive Healthy Weight Scale Matrix")
    h_val = st.number_input("Input Baseline Height Structure", value=165.0)
    h_unit = st.selectbox("Baseline Measurement System Scalar", ["cm", "ft", "in"])
    
    min_w, max_w = cm.calculate_healthy_range(h_val, h_unit)
    st.info(f"💡 Based on international health architecture parameters, your ideal standard weight metrics span between **{min_w} kg** and **{max_w} kg**.")

# MODULE 4: DIAGNOSTIC SOMATOTYPE QUIZ SYSTEM
elif navigation_tab == "4. Somatotype Body Type Finder":
    st.header("🧠 Advanced Metabolic Archetype Diagnostic Engine")
    st.write("Complete this 7-point anatomical and metabolic assessment profile to compute your precise physical architecture breakdown:")
    
    st.markdown("### 🧬 Section A: Skeletal Architecture & Structure")
    q1 = st.radio("1. Which best describes the width of your bone structure (wrists, shoulders, and hips)?", 
                  ["Narrow shoulders/hips, thin wrists (Delicate frame)", 
                   "Broad shoulders, medium wrists/joints (Athletic, square frame)", 
                   "Wide shoulders/hips, large joints (Sturdy, blocky frame)"])
                   
    q2 = st.radio("2. If you wrap your middle finger and thumb around your opposite wrist:", 
                  ["They overlap significantly", 
                   "They just barely touch each other", 
                   "There is a visible gap between them (They don't touch)"])

    st.markdown("### ⚡ Section B: Metabolic Behaviors & Weight History")
    q3 = st.radio("3. Think back to your high school or early adulthood years. Your natural physical baseline was:", 
                  ["Naturally lean, lanky, or thin (Hard to gain any mass)", 
                   "Naturally fit, muscular, compact, or athletic", 
                   "Naturally round, soft, heavy, or stocky"])

    q4 = st.radio("4. When you consume a heavy carbo-hydrate meal (bread, rice, pasta):", 
                  ["Energy remains stable or high with zero physical bloating", 
                   "Energy stays normal, muscles feel full and well-fueled", 
                   "You experience a sudden energy crash, sluggishness, or instant bloating"])

    q5 = st.radio("5. How does your body respond if you stop exercising or tracking your diet for a few weeks?", 
                  ["You lose weight rapidly or look even thinner/smaller", 
                   "Your physical conditioning stays relatively stable without major shifts", 
                   "You gain body fat and soft mass almost instantly"])

    st.markdown("### 🎯 Section C: Adipose and Lean Muscle Distribution")
    q6 = st.radio("6. When you gain weight, where does your body naturally concentrate or store the mass?", 
                  ["It distributes evenly across your entire body frame, or you rarely gain mass", 
                   "It stores cleanly on your core/chest as dense lean frame mass", 
                   "It accumulates heavily on your lower stomach, hips, and thighs"])

    q7 = st.radio("7. How easily do you put on lean, functional muscle tissue during resistance training?", 
                  ["Extremely difficult; requires massive amounts of food and heavy lifting to budge scale", 
                   "Relatively easy; your body responds fast and changes tone quickly", 
                   "You gain strength fast, but it is always layered over with soft tissue/body fat"])

    ecto_pts, meso_pts, endo_pts = 0, 0, 0

    if "Narrow" in q1: ecto_pts += 3
    elif "Broad" in q1: meso_pts += 3
    else: endo_pts += 3

    if "overlap" in q2: ecto_pts += 3
    elif "barely touch" in q2: meso_pts += 3
    else: endo_pts += 3

    if "lean" in q3: ecto_pts += 3
    elif "fit" in q3: meso_pts += 3
    else: endo_pts += 3

    if "stable" in q4: ecto_pts += 3
    elif "normal" in q4: meso_pts += 3
    else: endo_pts += 3

    if "thinner" in q5: ecto_pts += 3
    elif "stable" in q5: meso_pts += 3
    else: endo_pts += 3

    if "evenly" in q6: ecto_pts += 3
    elif "dense" in q6: meso_pts += 3
    else: endo_pts += 3

    if "difficult" in q7: ecto_pts += 3
    elif "easy" in q7: meso_pts += 3
    else: endo_pts += 3

    total_pts = ecto_pts + meso_pts + endo_pts
    ecto_pct = int((ecto_pts / total_pts) * 100)
    meso_pct = int((meso_pts / total_pts) * 100)
    endo_pct = 100 - (ecto_pct + meso_pct)  

    st.write("---")
    st.subheader("📊 Your Computed Metabolic Profile Architecture")
    
    st.write(f"❄️ **Ectomorph Blueprint Index:** {ecto_pct}%")
    st.progress(ecto_pct / 100.0)
    st.write(f"⚡ **Mesomorph Blueprint Index:** {meso_pct}%")
    st.progress(meso_pct / 100.0)
    st.write(f"🧬 **Endomorph Blueprint Index:** {endo_pct}%")
    st.progress(endo_pct / 100.0)

    st.write("---")
    st.subheader("📘 Dominant Somatotype Educational Breakdown")
    
    highest_score = max(ecto_pct, meso_pct, endo_pct)
    if highest_score == ecto_pct:
        st.info("### ❄️ Your Dominant Archetype: **Ectomorph**")
        st.markdown("""
        * **Skeletal Baseline:** Characterized by a delicate bone structure, narrow shoulders, fast neural firing rates, and long, lean limb segments.
        * **Metabolic Tendency:** Fast metabolism baseline. Your body burns incoming fuel extremely quickly as heat energy rather than storing it.
        * **Nutritional Strategy:** Requires a high-carbohydrate baseline to sustain weight. Focus on calorie-dense, low-volume meals with optimal macro-partitioning to protect muscle mass from being broken down for fuel.
        """)
    elif highest_score == meso_pct:
        st.success("### ⚡ Your Dominant Archetype: **Mesomorph**")
        st.markdown("""
        * **Skeletal Baseline:** Square, athletic architecture with wide clavicles, narrow pelvic alignments, and dense, responsive skeletal connections.
        * **Metabolic Tendency:** Balanced baseline architecture with highly efficient macro partitioning. This body type builds muscle fast and drops fat easily when target adjustments are made.
        * **Nutritional Strategy:** Responds best to a balanced macro split (40% Carbs, 30% Protein, 30% Fats). Your system processes carbohydrates cleanly for performance without experiencing blood sugar or fat-storage spikes.
        """)
    else:
        st.error("### 🧬 Your Dominant Archetype: **Endomorph**")
        st.markdown("""
        * **Skeletal Baseline:** Strong, wide bone structure, short limbs, blocky waist alignment, and wide hip structures.
        * **Metabolic Tendency:** Naturally energy-retaining baseline profile. Your system excels at preserving energy, making it highly prone to storing fat in localized areas if caloric ceilings are breached.
        * **Nutritional Strategy:** Responds best to low-carbohydrate, higher-healthy-fat nutritional profiles. Prioritize dietary fiber and protein to manage insulin sensitivity and stabilize the body's fat storage loops.
        """)

# MODULE 5: REGIONAL CALORIC DIETARY LEDGER
elif navigation_tab == "5. Pan-Indian Calorie Tracker":
    st.header("🍛 Culturally Adapted Caloric Diary Engine")
    cuisine = st.radio("Select Active Domestic Culinary Partition Environment", ["South Indian", "North Indian"], horizontal=True)
    
    foods = db.fetch_indian_foods(cuisine)
    if foods:
        names = [f['food_name'] for f in foods]
        choice = st.selectbox("Select Everyday Staple Dish", names)
        matched = next(f for f in foods if f['food_name'] == choice)
        
        oil = st.select_slider("Preparation Oil Level Factor Coefficient", ["Low Oil Baseline", "Standard Standard Prep", "Extra Ghee/Butter Addition"])
        mod = 0.85 if "Low" in oil else (1.25 if "Extra" in oil else 1.0)
        
        calories = int(matched['base_calories_per_serving'] * mod)
        st.success(f"🔥 Total Metric Logged: **{calories} kcal** per serving portion size ({matched['standard_portion']})")
    else:
        st.warning("Ensure seed rows are populated inside your Supabase Cloud Database instance schema.")