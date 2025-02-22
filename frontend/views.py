from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime

# Simulated file system
file_system = {
    'about.txt': 'Hi, I\'m Tawfiq. I\'m a Full Stack Developer with expertise in Python, Django, JavaScript, React, and more.',
    'projects.txt': '1. Portfolio Website\n2. E-commerce Platform\n3. Blog Application',
    'skills.txt': 'Python, Django, JavaScript, React, Linux, Docker, Git',
    'contact.txt': 'Email: tawfiq@example.com\nLinkedIn: <a href="https://linkedin.com/in/tawfiq" target="_blank">Tawfiq</a>',
    'funfact.txt': 'I once wrote a Python script to automate my morning coffee routine!',
    'secret.txt': 'You found the secret file! Here\'s a cookie: 🍪',
}

# Simulated current directory and user
current_directory = '~/portfolio'
current_user = 'Tawfiq'

# Simulated uptime (in seconds)
import time
start_time = time.time()

def home(request):
    return render(request, 'frontend/home.html')

def execute_command(request):
    command = request.GET.get('command', '').strip().lower()
    response = ""

    if command == 'help':
        response = """
            <pre>
            <span class="command">help</span> - Display available commands

            Usage: help

            Available commands:
            <span class="command">help</span>       - Show this help message
            <span class="command">ls</span>        - List files in the current directory
            <span class="command">cat [file]</span> - Display the contents of a file
            <span class="command">rm [file]</span> - Remove a file
            <span class="command">about</span>     - Learn more about me
            <span class="command">projects</span>  - List my projects
            <span class="command">skills</span>    - List my skills
            <span class="command">contact</span>   - Get in touch with me
            <span class="command">funfact</span>   - A fun fact about me
            <span class="command">clear</span>    - Clear the terminal output
            <span class="command">pwd</span>      - Display the current directory
            <span class="command">cd [dir]</span> - Change the directory
            <span class="command">mkdir [dir]</span> - Create a new directory
            <span class="command">echo [text]</span> - Display a line of text
            <span class="command">date</span>     - Show the current date and time
            <span class="command">whoami</span>   - Display the current user
            <span class="command">resume</span>   - Download my resume
            <span class="command">social</span>   - Display my social media profiles
            <span class="command">uptime</span>   - Display how long the terminal has been running
            <span class="command">system info</span> - Display system information
            <span class="command">reboot</span>   - Reboot the terminal
            <span class="command">secret</span>   - Find the secret file
            <span class="command">42</span>       - The answer to life, the universe, and everything
            <span class="command">hello</span>    - Say hello to the world
            <span class="command">sudo make me a sandwich</span> - A playful command

            Type <span class="command">[command] --help</span> for more information on a specific command.
            </pre>
        """
    elif command == 'ls':
        files = list(file_system.keys())
        response = f"<p>{' '.join(files)}</p>"
    elif command.startswith('cat '):
        file = command.split(' ')[1]
        if file in file_system:
            response = f"<p>{file_system[file]}</p>"
        else:
            response = f"<p>cat: {file}: No such file or directory</p>"
    elif command.startswith('rm '):
        file = command.split(' ')[1]
        if file in file_system:
            del file_system[file]
            response = f"<p>Removed {file}</p>"
        else:
            response = f"<p>rm: {file}: No such file or directory</p>"
    elif command == 'about':
        response = """
            <p>Hi, I'm Tawfiq.</p>
            <p>I'm a Full Stack Developer with expertise in Python, Django, JavaScript, React, and more.</p>
            <p>I love building web applications and solving complex problems.</p>
        """
    elif command == 'projects':
        response = f"<p>{file_system['projects.txt']}</p>"
    elif command == 'skills':
        response = f"<p>{file_system['skills.txt']}</p>"
    elif command == 'contact':
        response = """
            <p>Tawfiq@portfolio:~$ Contact Me</p>
            <p>Email: tawfiq@example.com</p>
            <p>LinkedIn: <a href="https://linkedin.com/in/tawfiq" target="_blank">Tawfiq</a></p>
        """
    elif command == 'funfact':
        response = f"<p>{file_system['funfact.txt']}</p>"
    elif command == 'clear':
        response = "<script>document.getElementById('command-output').innerHTML = '';</script>"
    elif command == 'pwd':
        response = f"<p>{current_directory}</p>"
    elif command.startswith('cd '):
        dir = command.split(' ')[1]
        response = f"<p>Changed directory to {dir}</p>"
    elif command.startswith('mkdir '):
        dir = command.split(' ')[1]
        response = f"<p>Created directory {dir}</p>"
    elif command.startswith('echo '):
        text = ' '.join(command.split(' ')[1:])
        response = f"<p>{text}</p>"
    elif command == 'date':
        now = datetime.now()
        response = f"<p>{now.strftime('%Y-%m-%d %H:%M:%S')}</p>"
    elif command == 'whoami':
        response = f"<p>{current_user}</p>"
    elif command == 'resume':
        response = """
            <p>Download my resume: <a href="/path/to/resume.pdf" target="_blank">Resume.pdf</a></p>
        """
    elif command == 'social':
        response = """
            <p>Follow me:</p>
            <p>- GitHub: <a href="https://github.com/tawfiq" target="_blank">tawfiq</a></p>
            <p>- Twitter: <a href="https://twitter.com/tawfiq" target="_blank">@tawfiq</a></p>
        """
    elif command == 'uptime':
        uptime_seconds = int(time.time() - start_time)
        uptime_str = f"{uptime_seconds // 3600} hours, {(uptime_seconds % 3600) // 60} minutes"
        response = f"<p>Uptime: {uptime_str}</p>"
    elif command == 'system info':
        response = """
            <p>System Information:</p>
            <p>- OS: PortfolioOS v1.0</p>
            <p>- Memory: 8GB / 16GB (50% used)</p>
            <p>- Disk: 250GB / 500GB (50% used)</p>
        """
    elif command == 'reboot':
        response = "<script>document.getElementById('command-output').innerHTML = '';</script>"
    elif command == 'secret':
        response = f"<p>{file_system['secret.txt']}</p>"
    elif command == 'sudo make me a sandwich':
        response = "<p>What? Make it yourself.</p>"
    elif command == '42':
        response = "<p>The answer to life, the universe, and everything.</p>"
    elif command == 'hello':
        response = "<p>Hello, world!</p>"
    elif command == '':
        response = ""
    else:
        response = f"<p>Command not found: {command}. Type <span class='command'>help</span> for a list of commands.</p>"

    return HttpResponse(response)