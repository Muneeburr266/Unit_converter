import streamlit as st 


st.markdown("""
    <style>
        /* Background Styling */
        body {
            background-color: #2ECBCB;
        }
        .main {
            background-color: #2f3640 !important;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        }
        .big-font {
            font-size:36px !important;
            font-weight: bold;
            text-align: center;
            color: #f5f6fa;
        }
        .small-text {
            font-size:18px;
            text-align: center;
            color: #dcdde1;
        }
        .category-box {
            background-color: #485460;
            color: white;
            padding: 10px;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
            border: 2px solid #808e9b;
        }
        .result-box {
            background-color: #dcdde1;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #2f3640;
            border: 3px solid #808e9b;
            transition: 0.3s;
        }
        .result-box:hover {
            background-color: #f5f6fa;
            color: #1e272e;
            transform: scale(1.05);
            border: 3px solid #4b6584;
        }
        .convert-button {
            background-color: #4cd137;
            color: white;
            padding: 12px 18px;
            font-size: 20px;
            font-weight: bold;
            border: 2px solid #27ae60;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
        }
        .convert-button:hover {
            background-color: #44bd32;
            transform: scale(1.05);
            border: 2px solid #2ecc71;
        }
    </style>
""", unsafe_allow_html=True)


CONVERSION_FACTORS = {
 
    "meters": 1, "kilometers": 1000, "centimeters": 0.01, "millimeters": 0.001,
    "miles": 1609.34, "yards": 0.9144, "feet": 0.3048, "inches": 0.0254,
    

    "grams": 1, "kilograms": 1000, "milligrams": 0.001, "pounds": 453.592, "ounces": 28.3495,
    

    "liters": 1, "milliliters": 0.001, "gallons": 3.78541, "quarts": 0.946353,
    "pints": 0.473176, "cups": 0.24,
}

def convert_unit(value, unit_from, unit_to):
    if unit_from not in CONVERSION_FACTORS or unit_to not in CONVERSION_FACTORS:
        return "Conversion not supported"
    
    base_value = value * CONVERSION_FACTORS[unit_from]
    converted_value = base_value / CONVERSION_FACTORS[unit_to]

    return round(converted_value, 5) 


st.markdown('<p class="big-font">🔄 Advanced Unit Converter By Muneeb</p>', unsafe_allow_html=True)
st.markdown('<p class="small-text">Convert Length, Weight, and Volume Units Easily!</p>', unsafe_allow_html=True)

st.markdown('<p class="category-box">Select a Conversion Category:</p>', unsafe_allow_html=True)
category = st.selectbox("", ["Length", "Weight", "Volume"])


unit_options = {
    "Length": ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"],
    "Weight": ["grams", "kilograms", "milligrams", "pounds", "ounces"],
    "Volume": ["liters", "milliliters", "gallons", "quarts", "pints", "cups"]
}

units = unit_options[category]


col1, col2 = st.columns([2, 2])

with col1:
    value = st.number_input("Enter the Value", min_value=0.0, format="%.5f")

with col2:
    unit_from = st.selectbox("Convert from:", units)
    unit_to = st.selectbox("Convert to:", units)


if st.button("🔁 Convert", key="convert", help="Click to convert the units"):
    result = convert_unit(value, unit_from, unit_to)
    st.markdown(f'<p class="result-box">Converted Value: {result} {unit_to}</p>', unsafe_allow_html=True)


