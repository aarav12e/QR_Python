<h1 align="center">📱 Python QR Code Generator (GUI)</h1>
hello 

<p align="center">
A simple and user-friendly <b>QR Code Generator</b> built using <b>Python</b>, <b>Tkinter</b>, and <b>qrcode</b>.
<br>
This desktop application allows users to generate QR codes from text or URLs and save them as PNG images.
</p>

<hr>

<h2>🖼️ Application Preview</h2>


<img width="375" height="475" alt="QR Code Generator 27-12-2025 22_00_42" src="https://github.com/user-attachments/assets/4ee1c241-136d-47f0-8cbe-40e724d0efde" />

<hr>

<h2>✨ Features</h2>

<ul>
  <li>📝 Generate QR codes from text or URLs</li>
  <li>🖥️ Clean and minimal GUI using Tkinter</li>
  <li>💾 Save QR codes as <code>.png</code> files</li>
  <li>⌨️ Keyboard shortcuts:
    <ul>
      <li><b>Enter</b> → Generate QR</li>
      <li><b>Double-click on QR</b> → Save QR</li>
    </ul>
  </li>
  <li>📦 Packaged as an executable using PyInstaller</li>
  <li>🪟 Runs as a GUI app (no console window)</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li>Python 3</li>
  <li>Tkinter (GUI)</li>
  <li>qrcode</li>
  <li>Pillow (PIL)</li>
  <li>PyInstaller</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
📁 QR-Code-Generator
 ┣ 📄 app.py
 ┣ 🖼️ qr.png
 ┣ 📄 app.spec
 ┗ 📄 README.md
</pre>

<hr>

<h2>⚙️ How the Code Works</h2>

<h3>1️⃣ Resource Handling</h3>
<p>
The <code>resource_path()</code> function ensures images work correctly both during development and
after converting the app into an executable using PyInstaller.
</p>

<h3>2️⃣ QR Code Creation</h3>
<p>
The <code>create_qr_image()</code> function generates a QR code using the <b>qrcode</b> library
and resizes it for display inside the GUI.
</p>

<h3>3️⃣ Generate QR</h3>
<p>
The <code>createQR()</code> function:
</p>
<ul>
  <li>Reads user input from the text field</li>
  <li>Generates the QR code</li>
  <li>Displays it inside the application window</li>
</ul>

<h3>4️⃣ Save QR</h3>
<p>
The <code>saveQR()</code> function allows users to save the generated QR code as a PNG file
using a file dialog.
</p>

<h3>5️⃣ GUI Layout</h3>
<ul>
  <li>Top Frame → Displays QR image</li>
  <li>Bottom Frame → Input field and buttons</li>
  <li>Create, Save, and Exit buttons for easy control</li>
</ul>

<hr>

<h2>🚀 How to Run the Project</h2>

<h3>Run Using Python</h3>

<pre>
pip install qrcode pillow
python app.py
</pre>

<h3>Create Executable (.exe)</h3>

<pre>
pyinstaller --onefile --windowed app.spec
</pre>

<p>
After building, the executable will be available inside the <code>dist</code> folder.
</p>

<hr>

<h2>🎯 Use Cases</h2>

<ul>
  <li>Sharing website links</li>
  <li>Wi-Fi credentials</li>
  <li>Contact information</li>
  <li>Quick data sharing</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>
This project is open-source and free to use for learning and personal projects.
</p>

<hr>

<h2 align="center">⭐ If you like this project, don’t forget to star it!</h2>
