from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# KEY DE OPENAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chatbot:
    

    def _init_(self):
        pass

    def analyze_requirements(self, requirements):
        prompt = f"Analiza el siguiente documento de requisitos para detectar ambigüedades, inconsistencias o conflictos según las directrices de SWEBOK:\n\n{requirements}"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].text.strip()
        return formatted_response

    def generate_user_stories(self, requirements):
        prompt = f"Genera historias de usuario a partir de los siguientes requisitos funcionales, incluyendo la prioridad y los criterios de aceptación para cada historia:\n\n{requirements}"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=450
        )
        return response.choices[0].text.strip()
        return formatted_response

    def prioritize_requirements(self, requirements, additional_info):
        prompt = f"Prioriza la siguiente lista de requisitos (tanto funcionales como no funcionales) basada en la información adicional proporcionada (valor de negocio, riesgo y viabilidad técnica):\n\nRequisitos:\n{requirements}\n\nInformación adicional:\n{additional_info}"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].text.strip()
        return formatted_response
    
    
    def format_response(self, response):
        return response


chatbot = Chatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_requirements():
    if request.method == 'POST':
        user_input = request.form['requirements']
        analysis_result = chatbot.analyze_requirements(user_input)
        return render_template('result.html', result=analysis_result)
    return "Método no permitido", 405

@app.route('/generate_user_stories', methods=['POST'])
def generate_user_stories():
    if request.method == 'POST':
        user_input = request.form['requirements']
        user_stories = chatbot.generate_user_stories(user_input)
        return render_template('result.html', result=user_stories)
    return "Método no permitido", 405

@app.route('/prioritize', methods=['POST'])
def prioritize_requirements():
    if request.method == 'POST':
        requirements = request.form['requirements']
        additional_info = request.form['additional_info']
        prioritized_list = chatbot.prioritize_requirements(requirements, additional_info)
        return render_template('result.html', result=prioritized_list)
    return "Método no permitido", 405

if __name__ == '__main__':
    app.run(debug=True, port=5000)
