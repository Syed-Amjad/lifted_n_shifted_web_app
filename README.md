
```markdown
# 🚀 Flask Web App Migration: AWS EC2 → Azure VM

This project demonstrates a **real-world cloud migration** of a Python Flask web application — fully deployed and running on an **AWS EC2 instance**, then migrated and re-deployed to an **Azure Virtual Machine**, preserving application functionality and database integrity.

---

## 🧩 Project Overview

- ✅ Built a Flask web application with SQLite database and Bootstrap-based UI  
- 🔄 Migrated complete application (code + database) from **AWS EC2** to **Azure VM**  
- 🔐 Secured file transfer using `scp` and SSH keys  
- 🌐 Deployed the app behind **NGINX reverse proxy** (on port `8080`)  
- ⚙️ Installed and configured Python, Flask, and dependencies on Azure  
- 🧪 Verified the app is working by inserting Azure-specific records into the migrated DB  

---

## 🖥️ Live View

The application displays the following features when accessed via browser:

- Bootstrap-powered front-end served on port `8080`  
- Dynamic message rendering from SQLite database  
- Differentiation between AWS and Azure deployment using unique messages  

---

## 📂 Project Structure

```

app/
├── app.py              # Main Flask app
├── init\_db.py          # Script to initialize DB with tables and messages
├── update\_db.py        # Script to add Azure-specific messages post-migration
├── database.db         # SQLite DB file (migrated from AWS)
├── templates/
│   └── index.html      # HTML template with dynamic message rendering
├── static/
│   └── style.css       # Custom CSS for UI

````

---

## 📸 Screenshots

| Description                        | Screenshot |
|------------------------------------|------------|
| App running on AWS EC2             | ✅         |
| App migrated and running on Azure  | ✅         |
| CLI showing `scp` transfer         | ✅         |
| Azure NGINX setup confirmation     | ✅         |

---

## 🔧 Technologies Used

- 🐍 Python 3.12  
- 🧱 Flask + Flask-SQLAlchemy  
- 💾 SQLite3  
- 🌐 NGINX  
- ☁️ AWS EC2 & Azure VM (Ubuntu 24.04 LTS)  
- 🔐 SSH, SCP for secure file transfer  
- 🎨 Bootstrap 5  

---

## ⚙️ Key DevOps Concepts Demonstrated

- Infrastructure provisioning  
- Application & environment configuration  
- VM setup and maintenance  
- Port management and firewall rules  
- Web server integration (NGINX reverse proxy)  
- Cross-cloud resource migration  

---

## 📝 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/Syed-Amjad/lifted_n_shifted_web_app.git
cd flask-cloud-migration
````

2. Install requirements:

```bash
pip install flask flask_sqlalchemy
```

3. Initialize DB:

```bash
python3 init_db.py
```

4. Run Flask App:

```bash
python3 app.py
```

5. Visit in browser:

```
http://localhost:5000
```

---

## 🚀 How to Access in Browser (Cloud / NGINX Setup)

If you're running the app on a **remote cloud server** (like Azure VM), and you've configured **NGINX as a reverse proxy**, follow these steps:

1. Make sure Flask app is running:

```bash
python3 app.py
```

2. Ensure NGINX is listening on `port 8080` and pointing to Flask's internal port `5000`.

3. In your browser, go to:

```
http://<your-azure-ip>:8080
```

✅ You should see the app running with Azure-specific messages.

📌 Example:

```
http://52.168.107.114:8080
```

🛡️ Don’t forget to allow **port 8080** in Azure VM's inbound rules via the Azure portal.

---

## 🤝 Let's Connect

If you're a recruiter, engineer, or cloud enthusiast — let’s talk!

* 💼 Open to **DevOps** or **Cloud Engineering** roles (remote & on-site)
* 🔗 [LinkedIn Profile](https://www.linkedin.com/in/syed-amjad-ali-4188002a0)
* 📬 Feel free to open an issue or connect directly

---

## 📌 Author

**Syed Amjad Ali**
DevOps & Cloud Enthusiast | AI Learner | Freelancer
📍 Based in Pakistan | Working Globally 🌍

---

## ⭐️ Support

If you found this project helpful:

* ⭐ Star the repo
* 🔁 Share on LinkedIn
* 🍴 Fork and build your own migration demo!

---

```

