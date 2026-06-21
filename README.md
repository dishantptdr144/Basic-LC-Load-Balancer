# 🚀 Basic LC Load Balancer

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=00FF00&center=true&vCenter=true&width=600&lines=Basic+LC+Load+Balancer;Python+Powered;Least+Connections+Algorithm;Fast+%26+Lightweight" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

## ✨ Features

* ⚡ Least Connections Load Balancing
* 📊 Active Request Tracking
* 🔄 Automatic Server Selection
* 📝 JSON Based Server Usage Storage
* 🚀 Lightweight & Fast

---

## 📂 Project Structure

```text
Basic-LC---Load-Balancer/
│
├── main.py
├── servers_usage.json
├── README.md
```

---

## 🖥 Example Server Data

```json
{
  "sv1": {
    "url": "http://127.0.0.1:5001",
    "requests": 2
  },
  "sv2": {
    "url": "http://127.0.0.1:5002",
    "requests": 1
  },
  "sv3": {
    "url": "http://127.0.0.1:5003",
    "requests": 2
  }
}
```

---

## 🚀 How It Works

```text
Client Request
      │
      ▼
 Load Balancer
      │
      ▼
Find Server With Lowest Requests
      │
      ▼
Forward Request
      │
      ▼
Request Complete → Decrease Count
```

---

## 👨‍💻 Author

**Dishant Patidar**

⭐ If you like this project, consider giving it a star!
