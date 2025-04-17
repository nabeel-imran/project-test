# PeerGen - AI Text Generation Suite

PeerGen is a Streamlit application that offers multiple AI-driven functionalities:
- **PeerChat:** A general AI chatbot.
- **Ecom-Gen:** Generates engaging product descriptions for e-commerce.
- **ContGen:** Creates long-form content like articles and blogs.
- **PdfGen:** Summarizes PDF content and answers questions based on it.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/peer_gen.git
   cd peer_gen
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your OpenAI API Key:**

   Create a `.env` file in the project root and add:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Usage

- Use the sidebar to switch between modules: **PeerChat**, **Ecom-Gen**, **ContGen**, **PdfGen**, and **History**.
- Enter your inputs and click the corresponding buttons to generate responses.

## License

This project is licensed under the MIT License.
