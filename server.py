from flask import Flask, request, jsonify, send_file
from jinja2 import Template

app = Flask(__name__)

# Sample template
template_content = """
def calculate_{{operation}}(a, b):
    result = a {{operator}} b
    return result
"""

@app.route('/generate-python-file', methods=['POST'])
def generate_python_file():
    user_data = request.json  # Assuming JSON data from the form
    if not user_data:
        return jsonify({'error': 'Invalid data'}), 400

    # Replace placeholders in the template
    template = Template(template_content)
    generated_code = template.render(operation=user_data['operation'], operator=user_data['operator'])

    # Save the generated code to a .py file
    with open('generated_code.py', 'w') as file:
        file.write(generated_code)

    # Return a download link to the user
    return send_file('generated_code.py', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)