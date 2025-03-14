from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import time

# Simulated file system
file_system = {
    'projects.txt': 'Project 1: Portfolio Website\nProject 2: E-commerce Store\nProject 3: Blog Platform',
    'contact.txt': 'Email: tawfiq.said00@gmail.com\nLinkedIn: <a href="https://linkedin.com/in/tawfiqsaid" target="_blank">Tawfiq</a>',
    'funfact.txt': 'I once wrote a Python script to automate my morning coffee routine!',
}

# Simulated current directory and user
current_directory = '/home/tawfiq'
current_user = 'Tawfiq'

# Simulated uptime (in seconds)
start_time = time.time()

def home(request):
    return render(request, 'frontend/home.html')

def execute_command(request):
    command = request.GET.get('command', '').strip().lower()
    response = ""

    if command == 'help':
        response = """
            <div class="help-container">
                <h2>Available Commands</h2>
                <div class="commands-grid">
                    <div class="command-item">
                        <span class="command">about</span>
                        <span class="description">Learn more about me</span>
                    </div>
                    <div class="command-item">
                        <span class="command">skills</span>
                        <span class="description">View my skills and expertise</span>
                    </div>
                    <div class="command-item">
                        <span class="command">certs</span>
                        <span class="description">View my certifications</span>
                    </div>
                    <div class="command-item">
                        <span class="command">help</span>
                        <span class="description">Display available commands</span>
                    </div>
                    <div class="command-item">
                        <span class="command">ls</span>
                        <span class="description">List files in the current directory [-a for all files]</span>
                    </div>
                    <div class="command-item">
                        <span class="command">cat [file]</span>
                        <span class="description">Display the contents of a file</span>
                    </div>
                    <div class="command-item">
                        <span class="command">projects</span>
                        <span class="description">List my projects</span>
                    </div>
                    <div class="command-item">
                        <span class="command">contact</span>
                        <span class="description">Get in touch with me</span>
                    </div>
                    <div class="command-item">
                        <span class="command">funfact</span>
                        <span class="description">A fun fact about me</span>
                    </div>
                    <div class="command-item">
                        <span class="command">clear</span>
                        <span class="description">Clear the terminal output</span>
                    </div>
                    <div class="command-item">
                        <span class="command">pwd</span>
                        <span class="description">Display the current directory</span>
                    </div>
                    <div class="command-item">
                        <span class="command">echo [text]</span>
                        <span class="description">Display a line of text</span>
                    </div>
                    <div class="command-item">
                        <span class="command">date</span>
                        <span class="description">Show the current date and time</span>
                    </div>
                    <div class="command-item">
                        <span class="command">whoami</span>
                        <span class="description">Display the current user</span>
                    </div>
                    <div class="command-item">
                        <span class="command">resume</span>
                        <span class="description">Download my resume</span>
                    </div>
                    <div class="command-item">
                        <span class="command">system info</span>
                        <span class="description">Display system information</span>
                    </div>
                    <div class="command-item">
                        <span class="command">secret</span>
                        <span class="description">Discover something hidden</span>
                    </div>
                    <div class="command-item">
                        <span class="command">42</span>
                    </div>
                    <div class="command-item">
                        <span class="command">hello</span>
                        <span class="description">Say hello to the world</span>
                    </div>
                    <div class="command-item">
                        <span class="command">sudo make me a sandwich</span>
                        <span class="description">A playful command</span>
                    </div>
                </div>
            </div>
        """
    elif command == 'ls':  
        files = list(file_system.keys())
        response = f"<p>{' '.join(files)}</p>"
    elif command == 'ls -a': # add .secret.txt to the list of files
        files = list(file_system.keys())
        files.append('.secret.txt')
        response = f"<p>{' '.join(files)}</p>"
    elif command.startswith('cat '):
        file = command.split(' ')[1]
        if file in file_system:
            response = f"<p>{file_system[file]}</p>"
        elif file == '.secret.txt': # add a cookie to the response
            response = """ 
                <p>Congratulations! You've found a hidden file. 🎉</p>
                <p>Here's a cookie for your efforts: <span class="cookie">🍪</span></p>
            """
        else:
            response = f"<p>cat: {file}: No such file or directory</p>"
    elif command == 'about':
        response = """
                    <!-- Introduction Text -->
<p class="intro-text">
  Hi, I'm <span class="highlight">Tawfiq</span>! 👋
</p>
<p class="intro-text">
  I'm a <span class="highlight">Full Stack Developer</span> who loves turning ideas into reality through code. Whether it's building sleek websites or crafting powerful applications, I thrive on creating solutions that are both beautiful and functional.
</p>
<p class="intro-text">
  I enjoy solving problems within the computer realm, from debugging complex systems to optimizing performance and designing intuitive user interfaces.
</p>
<p class="intro-text">
  Here's a snapshot of what I bring to the table:
</p>

        """
    elif command == 'skills':
        response = """
        <!-- Skills Section -->
        <div class="skill-section">
            <h3 class="skill-heading">Skills & Expertise</h3>
            <ul class="skill-list">
                <li><span class="command">Frontend</span>: HTML, CSS, JavaScript <span class="framework">(React, Bootstrap)</span></li>
                <li><span class="command">Backend</span>: Python <span class="framework">(Django, FastAPI)</span>, PHP <span class="framework">(Laravel)</span>, Node.js</li>
                <li><span class="command">Databases</span>: SQL <span class="framework">(MySQL, PostgreSQL)</span>, NoSQL <span class="framework">(MongoDB, Redis)</span></li>
                <li><span class="command">DevOps</span>: Docker, Nginx, Apache, Git <span class="framework">(GitHub, GitLab)</span>, Gradle</li>
                <li><span class="command">Cloud</span>: Azure, AWS</li>
                <li><span class="command">System Programming</span>: C <span class="framework">(BSD & Linux System Calls)</span></li>
                <li><span class="command">Other</span>: RESTful APIs, TDD, Automation, Linux, Agile & Scrum</li>
            </ul>
        </div>    
        """
    elif command == 'certs':
        response ="""
                
        <!-- Certifications Section -->
        <div class="certification-section">
            <h3 class="skill-heading">Certifications</h3>
            <ul class="skill-list">
                <li>
                <p class="certification-title">Certified SAFe 6 Practitioner</p>
                <p class="certification-issuer">Scaled Agile (SAFe®) Training by Agile Certification Academy</p>
                <p class="certification-skills">Skills: Scaled Agile Framework</p>
                </li>
                <li>
                <p class="certification-title">Information Technology Specialist - HTML and CSS</p>
                <p class="certification-issuer">Certiport</p>
                <p class="certification-details">Issued May 2022 | Credential ID 42mp-XM3z</p>
                </li>
                <li>
                <p class="certification-title">Cisco Certified Network Associate Routing and Switching (CCNA)</p>
                <p class="certification-issuer">Cisco</p>
                <p class="certification-details">Issued May 2020</p>
                </li>
            </ul>
        </div>
        """
    elif command == 'projects':
        response = f"<p>{file_system['projects.txt']}</p>"
    elif command == 'history':
        response = """
            <p>Command History:</p>
            <ul class="history-list">
                <li>ls</li>
                <li>cat projects.txt</li>
                <li>sudo make me a sandwich</li>
                <li>ls -a</li>
                <li>rm -rf /  ## Just kidding! (;  </li>  

            </ul>
        """


    elif command == 'contact':
        response = """
            <p>Tawfiq@portfolio:~$ Contact Me</p>
            <p>Email: tawfiq.said00@gmail.com</p>
            <p>LinkedIn: <a href="https://linkedin.com/in/tawfiqsaid" target="_blank">Tawfiq</a></p>
        """
    elif command == 'funfact':
        response = f"<p>{file_system['funfact.txt']}</p>"
    elif command == 'clear':
        response = "<script>document.getElementById('command-output').innerHTML = '';</script>"
    elif command == 'pwd':
        response = f"<p>{current_directory}</p>"
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
    elif command == 'system info':
        response = """
            <p>System Information:</p>
            <p>- OS: PortfolioOS v1.0</p>
            <p>- Memory: 8GB / 16GB (50% used)</p>
            <p>- Disk: 250GB / 500GB (50% used)</p>
        """
    elif command == 'sudo make me a sandwich':
        response = "<p>What? Make it yourself.</p>"
    elif command == '42':
        response = "<p>The answer to life, the universe, and everything.</p>"
    elif command == 'hello':
        response = "<p>Hello, There!</p>"
    elif command == '':
        response = "<p></p>"
    else:
        response = f"<p>Command not found: {command}. Type <span class='command'>help</span> for a list of commands.</p>"

    return HttpResponse(response)