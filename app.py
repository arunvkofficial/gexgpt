import google.generativeai as genai
import streamlit as st

# Configure Google Gemini API key
genai.configure(api_key="AIzaSyBcdPnH5rEEw4Tt7RF8ucLjWZ9u7YbfHuw")

# Custom CSS for modern aesthetic and animated theme
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #f0f0f0;
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
        }
        .header {
            background: #000000; /* Set header to black */
            color: white;
            padding: 20px; /* Reduced padding */
            text-align: center;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            font-size: 24px; /* Reduced font size */
            animation: slideIn 1s ease-out;
        }
        @keyframes slideIn {
            0% {
                transform: translateY(-50px);
                opacity: 0;
            }
            100% {
                transform: translateY(0);
                opacity: 1;
            }
        }
        .output-container {
            background: #000000; /* Output box to black */
            color: #f0f0f0;
            padding: 15px; /* Reduced padding */
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            margin-top: 20px; /* Reduced margin-top */
            animation: fadeIn 1.5s ease-in;
        }
        @keyframes fadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        .output-container h4 {
            font-size: 20px; /* Reduced font size */
            margin-bottom: 10px; /* Reduced margin */
        }
        .output-container p {
            font-size: 14px; /* Reduced font size */
            line-height: 1.5;
        }
        .stTextInput textarea {
            background-color: #000000; /* Input box to black */
            color: #f0f0f0;
            border: 1px solid #444;
            border-radius: 10px;
            padding: 10px; /* Reduced padding */
            font-family: 'Roboto', sans-serif;
            font-size: 14px; /* Reduced font size */
            width: 100%;
            margin-top: 15px;
            box-sizing: border-box;
            resize: none;
            transition: all 0.3s ease-in-out;
        }
        .stTextInput textarea:focus {
            border-color: #00aaff;
            outline: none;
            box-shadow: 0 0 10px rgba(0, 170, 255, 0.5);
        }
        .stButton button {
            background: #000000; /* Generate button to black */
            color: white;
            padding: 12px 20px; /* Reduced padding */
            font-size: 14px; /* Reduced font size */
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 15px; /* Reduced margin-top */
        }
        .stButton button:hover {
            background: #333333; /* Slightly lighter black for hover */
        }
        .button-container {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)



def main():

    # Custom header section with modern aesthetic and smaller size
    st.markdown('<div class="header"><h1>GEX GPT</h1></div>', unsafe_allow_html=True)

    # Input form for the user with modern, clean UI
    user_input = st.text_area("", height=120, placeholder="Enter your prompt here...")

    # Button to generate content
    if st.button("Generate Content"):
        if user_input:
            try:
                # Create a GenerativeModel object
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Generate content using the provided prompt
                response = model.generate_content(user_input)

                # Check the response for validity
                if response and hasattr(response, 'parts') and response.parts:
                    generated_content = response.parts[0].text
                    # Display the generated content in an animated box
                    st.markdown(f'<div class="output-container"><h4>Generated Content:</h4><p>{generated_content}</p></div>', unsafe_allow_html=True)
                elif response and hasattr(response, 'finish_reason') and response.finish_reason == 4:
                    st.error("Error: The model attempted to recite copyrighted material.")
                else:
                    st.error("Error: No valid content returned.")
            
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a prompt to generate content.")
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
