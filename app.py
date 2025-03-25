from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import database
import ai_helper
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    issues = database.get_all_issues()
    return render_template('history.html', issues=issues)

@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    issue_description = data.get('issue')
    
    if not issue_description:
        return jsonify({'error': 'No issue description provided'}), 400
    
    print(f"Received issue description: {issue_description}")
    
    try:
        # Get AI diagnosis
        print("Calling diagnosis function...")
        diagnosis = ai_helper.get_diagnosis(issue_description)
        print(f"Received diagnosis (first 50 chars): {diagnosis[:50]}...")
        
        # Save to database
        issue_id = database.save_issue(issue_description, diagnosis)
        print(f"Saved to database with ID: {issue_id}")
        
        return jsonify({
            'id': issue_id,
            'diagnosis': diagnosis,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    except Exception as e:
        print(f"Error in diagnose route: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/resolve', methods=['POST'])
def resolve():
    data = request.json
    issue_id = data.get('id')
    resolution = data.get('resolution')
    
    if not issue_id or not resolution:
        return jsonify({'error': 'Missing required fields'}), 400
    
    database.update_resolution(issue_id, resolution)
    return jsonify({'success': True})

if __name__ == '__main__':
    # Initialize database
    database.init_db()
    app.run(debug=True)
