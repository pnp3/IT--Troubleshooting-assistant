# AI-Powered IT Troubleshooting Assistant

An intelligent web application that helps diagnose and resolve common IT issues using AI.

## Features

- AI-powered diagnosis of common computer issues
- Step-by-step solutions for resolving problems
- History tracking of past issues and resolutions
- User-friendly interface for both technical and non-technical users

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI**: OpenAI API (GPT-3.5/GPT-4)
- **Database**: SQLite

## Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/troubleshoot-assistant.git
   cd troubleshoot-assistant
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

## Usage

1. On the home page, describe your IT issue in detail
2. Click "Get Diagnosis" to receive an AI-powered analysis
3. Follow the suggested steps to resolve your issue
4. Add notes about how you resolved the issue and mark it as resolved
5. View your history of past issues on the History page

## Project Structure

- `app.py`: Main Flask application
- `ai_helper.py`: OpenAI API integration
- `database.py`: Database operations
- `config.py`: Configuration settings
- `templates/`: HTML templates
- `static/`: CSS and JavaScript files

## License

MIT

## Author

Prince Padi
