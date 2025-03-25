import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_diagnosis(issue_description):
    """
    Get AI-powered diagnosis for an IT issue with fallback to mock responses
    """
    # Try to use the OpenAI API first
    try:
        print("Attempting to use OpenAI API...")
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("No API key found in environment variables")
            return get_mock_diagnosis(issue_description)
            
        print(f"Using API key: {api_key[:10]}... (truncated for security)")
        
        # Create OpenAI client with API key
        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """
                You are an expert IT support technician. Diagnose the computer issue described 
                and provide a step-by-step solution. Format your response in these sections:
                
                1. DIAGNOSIS: A brief explanation of what's likely causing the issue
                2. SOLUTION: Step-by-step instructions to fix the problem
                3. PREVENTION: Tips to prevent this issue in the future
                
                Keep your response concise and technical but understandable to non-experts.
                """},
                {"role": "user", "content": issue_description}
            ],
            max_tokens=500
        )
        
        ai_response = response.choices[0].message.content
        print("Successfully received response from OpenAI API")
        return ai_response
        
    except Exception as e:
        print(f"Error using OpenAI API: {e}")
        print("Falling back to mock diagnosis...")
        return get_mock_diagnosis(issue_description)

def get_mock_diagnosis(issue_description):
    """
    Provide mock diagnosis based on keywords in the issue description
    """
    print("Using mock diagnosis")
    
    # Create a custom response based on the issue description
    if "shuts down" in issue_description.lower():
        return """
DIAGNOSIS: Your laptop is shutting down unexpectedly when you turn it on, which suggests potential issues with power management, overheating, or hardware failure.

SOLUTION:
1. Check for overheating:
   - Ensure vents are not blocked
   - Clean dust from fans and heat sinks
   - Use laptop on hard, flat surfaces

2. Test power supply:
   - Try a different power outlet
   - Inspect power adapter for damage
   - Test with another adapter if possible

3. Check battery:
   - Remove battery and try running on AC power only
   - Check battery for physical damage or swelling

4. Run hardware diagnostics:
   - Boot into BIOS/UEFI and run built-in diagnostics
   - Check for memory or hard drive failures

PREVENTION:
- Keep laptop clean and dust-free
- Use cooling pads for extended use
- Update BIOS and drivers regularly
- Monitor temperature with software tools
"""
    elif "slow" in issue_description.lower():
        return """
DIAGNOSIS: Your computer is running slowly, which is typically caused by insufficient system resources, too many background processes, malware, or hardware limitations.

SOLUTION:
1. Clean up your system:
   - Uninstall unused programs
   - Delete temporary files (use Disk Cleanup)
   - Disable unnecessary startup programs

2. Check for malware:
   - Run a full system scan with your antivirus
   - Consider using Malwarebytes for a second opinion

3. Upgrade hardware if needed:
   - Add more RAM
   - Replace HDD with SSD
   - Check if CPU is consistently at high usage

4. Optimize Windows:
   - Defragment HDD (not needed for SSD)
   - Disable visual effects
   - Make sure Windows is up to date

PREVENTION:
- Regularly clean up your system
- Be cautious about installing new software
- Keep your antivirus updated
- Consider a fresh Windows install annually
"""
    else:
        return """
DIAGNOSIS: Based on your description, you're experiencing a technical issue that could have multiple causes. Without more specific information, I'll provide some general troubleshooting steps.

SOLUTION:
1. Restart your device:
   - Save all work and perform a complete restart
   - This clears temporary memory and can resolve many issues

2. Update your system:
   - Check for operating system updates
   - Update device drivers, especially for problematic components

3. Check connections:
   - Ensure all cables are properly connected
   - Test with alternative cables if available

4. Run diagnostics:
   - Use built-in diagnostic tools for your device
   - Check system logs for error messages

PREVENTION:
- Keep your system and software updated
- Perform regular maintenance
- Back up your data regularly
- Monitor system performance for early warning signs
""" 