# core_math.py
import base64
import os

def calculate_clean_bmi(weight, w_unit, height, h_unit):
    if w_unit.lower() == "lbs":
        kg = weight * 0.453592
    else:
        kg = weight
        
    if h_unit.lower() == "ft":
        meters = height * 0.3048
    elif h_unit.lower() == "cm":
        meters = height / 100.0
    else:
        meters = height * 0.0254
        
    if meters == 0:
        return 0.0
    return round(kg / (meters ** 2), 2)

def calculate_healthy_range(height, h_unit):
    if h_unit.lower() == "ft":
        meters = height * 0.3048
    elif h_unit.lower() == "cm":
        meters = height / 100.0
    else:
        meters = height * 0.0254
        
    if meters == 0:
        return 0.0, 0.0
        
    min_kg = 18.5 * (meters ** 2)
    max_kg = 25.0 * (meters ** 2)
    return round(min_kg, 1), round(max_kg, 1)

def generate_full_body_avatar(gender, arms, chest, hips, waist, thighs, perspective="Front"):
    """
    Loads local GLB binary files and deforms target bounding zones dynamically 
    by computing bounding-box relative vertex coordinates.
    """
    # Normalize inputs to structural modification scalar variables
    arm_scale = arms / 12.0
    chest_scale = chest / 36.0
    waist_scale = waist / 32.0
    hip_scale = hips / 36.0
    thigh_scale = thighs / 20.0
    
    file_name = "femalegymmodel.glb" if gender == "Female" else "malegymmodel.glb"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_folder_path = os.path.join(current_dir, "static", file_name)
    
    if not os.path.exists(static_folder_path):
        return f"<p style='color:red;'>Missing local file asset at: {static_folder_path}</p>"
        
    try:
        with open(static_folder_path, "rb") as f:
            encoded_model = base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        return f"<p style='color:red;'>System file read violation: {str(e)}</p>"
        
    rotation_y = "0" if perspective == "Front" else "1.57"

    three_js_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/gh/mrdoob/three.js@r128/examples/js/loaders/GLTFLoader.js"></script>
        <style>
            body {{ margin: 0; background: #FAFAFA; overflow: hidden; }}
            canvas {{ width: 100%; height: 100%; }}
        </style>
    </head>
    <body>
        <script>
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0xfafafa);
            
            const camera = new THREE.PerspectiveCamera(45, 280 / 450, 0.1, 1000);
            camera.position.set(0, 0, 3.2);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(280, 450);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.body.appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, 1.4);
            scene.add(ambientLight);
            
            const mainLight = new THREE.DirectionalLight(0xffffff, 1.2);
            mainLight.position.set(2, 5, 5);
            scene.add(mainLight);

            // High-fidelity aesthetics material setup
            const modelMaterial = new THREE.MeshStandardMaterial({{ 
                color: 0xbc8a5f, 
                roughness: 0.6,
                metalness: 0.1
            }});

            let currentModel;
            const loader = new THREE.GLTFLoader();
            
            const modelData = "{encoded_model}";
            const binaryString = atob(modelData);
            const len = binaryString.length;
            const bytes = new Uint8Array(len);
            for (let i = 0; i < len; i++) {{
                bytes[i] = binaryString.charCodeAt(i);
            }}
            
            loader.parse(bytes.buffer, '', function(gltf) {{
                currentModel = gltf.scene;
                
                // Reset initial baseline coordinates
                const box = new THREE.Box3().setFromObject(currentModel);
                const center = box.getCenter(new THREE.Vector3());
                const size = box.getSize(new THREE.Vector3());
                
                currentModel.position.x += (currentModel.position.x - center.x);
                currentModel.position.y += (currentModel.position.y - center.y) - (size.y / 8);
                currentModel.position.z += (currentModel.position.z - center.z);
                
                const maxDim = Math.max(size.x, size.y, size.z);
                if (maxDim > 0) {{
                    const scaleFactor = 1.6 / maxDim;
                    currentModel.scale.set(scaleFactor, scaleFactor, scaleFactor);
                }}
                
                // AXIS-BASED VERTEX DEFORMATION ENGINE:
                // Loops through mesh geometry and distorts spatial coordinate coordinates natively
                currentModel.traverse((child) => {{
                    if (child.isMesh) {{
                        child.material = modelMaterial;
                        
                        const geometry = child.geometry;
                        const positionAttribute = geometry.attributes.position;
                        
                        for (let i = 0; i < positionAttribute.count; i++) {{
                            let x = positionAttribute.getX(i);
                            let y = positionAttribute.getY(i);
                            let z = positionAttribute.getZ(i);
                            
                            // Segment 1: Lower body zone (Legs & Thighs)
                            if (y < -0.2) {{
                                positionAttribute.setX(i, x * {thigh_scale});
                                positionAttribute.setZ(i, z * {thigh_scale});
                            }}
                            // Segment 2: Pelvis and core trunk zone (Hips & Waist)
                            else if (y >= -0.2 && y < 0.3) {{
                                let bias = (y + 0.2) / 0.5; // Smooth coordinate cross-fading
                                let dynamicWidth = ({hip_scale} * (1 - bias)) + ({waist_scale} * bias);
                                positionAttribute.setX(i, x * dynamicWidth);
                                positionAttribute.setZ(i, z * dynamicWidth);
                            }}
                            // Segment 3: Shoulder and chest muscle region (Chest & Arms)
                            else if (y >= 0.3 && y < 0.8) {{
                                let dynamicChest = ({chest_scale} * 0.7) + ({arm_scale} * 0.3);
                                positionAttribute.setX(i, x * dynamicChest);
                                positionAttribute.setZ(i, z * dynamicChest);
                            }}
                        }}
                        positionAttribute.needsUpdate = true;
                        geometry.computeVertexNormals();
                    }}
                }});

                currentModel.rotation.y = {rotation_y};
                scene.add(currentModel);
            }}, 
            function(error) {{
                console.error("Parsing breakdown check:", error);
            }});

            function animate() {{
                requestAnimationFrame(animate);
                if (currentModel) {{
                    currentModel.rotation.y += 0.005;
                }}
                renderer.render(scene, camera);
            }}
            animate();
        </script>
    </body>
    </html>
    """
    return three_js_html