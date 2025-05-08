from flask import Flask, render_template, abort
import json

app = Flask(__name__, static_folder='static', template_folder='templates')

def load_json_data(filename):
    try:
        with open(f'static/data/{filename}', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {str(e)}")
        return {}

def rgb_values(hex_color):
    h = hex_color.lstrip('#')
    return f"{int(h[:2], 16)}, {int(h[2:4], 16)}, {int(h[4:], 16)}"

app.jinja_env.filters['rgb_values'] = rgb_values

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    projects_data = load_json_data('projects.json')
    return render_template('projects.html', projects=projects_data)

@app.route('/experience')
def experience():
    internships = load_json_data('intern.json')
    return render_template('experience.html', data=internships['internships'])

@app.route('/hackathons')
def hackathons():
    hackathons_data = load_json_data('hack.json')
    return render_template('hackathons.html', hackathons=hackathons_data['hackathons'])

@app.route('/dsa')
def dsa():
    dsa_data = load_json_data('dsa.json')
    return render_template('dsa.html', profiles=dsa_data['profiles'])

@app.route('/project/<string:project_id>')
def project_detail(project_id):
    projects_data = load_json_data('projects.json')
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if project is None:
        abort(404)
    return render_template('project_detail.html', project=project)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
