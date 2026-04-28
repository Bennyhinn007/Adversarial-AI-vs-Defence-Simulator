<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Adversarial%20AI%20vs%20Defence%20Simulator&fontSize=36&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Where%20AI%20attacks%20meet%20AI%20defences%20—%20in%20real%20time&descAlignY=55&descSize=16"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

<br/>

![Red Team](https://img.shields.io/badge/🔴%20Red%20Team-Adversarial%20AI-FF4444?style=flat-square)
![Blue Team](https://img.shields.io/badge/🔵%20Blue%20Team-Defence%20System-4444FF?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Development-00CC66?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-FFD700?style=flat-square)

<br/>

[ 🔴 RED TEAM ]  >>>>>  ATTACK SIMULATION
        ⚔️  VS  🛡️
[ 🔵 BLUE TEAM ] <<<<<  DEFENSE & RESPONSE

> *"In AI security, if you understand both the attacker and defender — you're already ahead."*

</div>

---

## 🌐 What Is This?

<table>
<tr>
<td width="50%">

### 🔴 The Problem

Even the most powerful AI models can be **completely fooled** by inputs that look identical to the human eye.

A single pixel tweak. A barely visible noise pattern. That's all it takes to make a state-of-the-art model fail completely.

This is **adversarial AI** — and it's one of the most critical unsolved problems in modern machine learning.

</td>
<td width="50%">

### 🔵 The Solution

This project builds a **hands-on simulation lab** where:

- 🔴 Adversarial AI crafts malicious inputs
- 🔵 Defence systems try to detect or neutralize them
- ⚖️ An evaluation engine scores the battle

Think of it as a **cybersecurity gym for AI models**.

</td>
</tr>
</table>

---

## 🎯 Objectives

<div align="center">

| # | Objective | Status |
|---|-----------|--------|
| 01 | Understand adversarial attacks in real-world ML systems | ✅ |
| 02 | Simulate Red vs Blue AI attack/defence scenarios | ✅ |
| 03 | Visualize model vulnerabilities under attack | ✅ |
| 04 | Build intuition for secure AI system design | ✅ |
| 05 | Multi-agent Red vs Blue simulation | 🔄 In Progress |

</div>

---

## 🧠 Core Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   🔴 RED TEAM (Adversarial AI)          🔵 BLUE TEAM (Defence System)   │
│   ─────────────────────────────         ──────────────────────────────  │
│                                                                         │
│   ┌─────────────────────────┐           ┌──────────────────────────┐    │
│   │  Attack Generation      │           │  Denoising / Smoothing   │    │
│   │  ▸ FGSM                 │   ⚔️🛡️   │  ▸ Input preprocessing   │    │
│   │  ▸ PGD                  │◄─────────►│  ▸ Adversarial training  │    │
│   │  ▸ Custom attacks       │           │  ▸ Certified defences    │    │
│   └─────────────────────────┘           └──────────────────────────┘    │
│                          │                     │                        │
│                          └──────────┬──────────┘                        │
│                                     ▼                                   │
│                      ┌──────────────────────────┐                       │
│                      │    ⚖️ Evaluation Engine   │                       │
│                      │  Accuracy · Robustness   │                       │
│                      │  Attack Success Rate     │                       │
│                      │  Defence Effectiveness   │                       │
│                      └──────────────────────────┘                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Features

<div align="center">

|  | Feature | Description |
|--|---------|-------------|
| ✨ | **Interactive Simulation** | Run full attack-defence cycles end to end |
| 🧪 | **Multiple Attack Strategies** | FGSM, PGD, and extensible attack modules |
| 🛡️ | **Defence Mechanisms** | Denoising, input smoothing, adversarial training |
| 📊 | **Performance Dashboards** | Side-by-side accuracy comparisons before/after attack |
| 🧩 | **Modular Architecture** | Drop in new attacks or defences without touching core logic |
| 🔬 | **Notebook Experiments** | Jupyter-based exploration and visualization |

</div>

---

## 🗂️ Project Structure

```
📁 Adversarial-AI-vs-Defence-Simulator/
│
├── 🔴 attacks/               # Attack algorithm modules
│   ├── fgsm.py               # Fast Gradient Sign Method
│   ├── pgd.py                # Projected Gradient Descent
│   └── __init__.py
│
├── 🔵 defenses/              # Defence technique modules
│   ├── denoising.py          # Input denoising
│   ├── smoothing.py          # Randomized smoothing
│   └── __init__.py
│
├── 🤖 models/                # ML models used in simulation
│   └── classifier.py
│
├── 🛠️ utils/                 # Helper functions & tools
│   └── metrics.py
│
├── 📓 notebooks/             # Experiments & visualization
│   └── simulation.ipynb
│
├── main.py                   # ▶️ Entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/Bennyhinn007/Adversarial-AI-vs-Defence-Simulator.git
cd Adversarial-AI-vs-Defence-Simulator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Simulator

```bash
python main.py
```

### 4️⃣ Customize Parameters

```python
# Tweak these inside main.py or config

EPSILON = 0.1          # Attack strength — higher = stronger attack
ATTACK = "pgd"         # Choose: "fgsm" | "pgd"
DEFENSE = "smoothing"  # Choose: "denoising" | "smoothing" | "none"
MODEL = "resnet"       # Target model
```

---

## 📊 Simulation Workflow

```
   ┌──────────────────────────────────────────────────────┐
   │                                                      │
   │  Step 1 ──► Train baseline model on clean data       │
   │     │                                                │
   │  Step 2 ──► Adversary generates attack examples      │
   │     │        (FGSM / PGD with tunable epsilon)       │
   │     │                                                │
   │  Step 3 ──► Apply defence mechanism                  │
   │     │        (denoising / smoothing / adv training)  │
   │     │                                                │
   │  Step 4 ──► Evaluation Engine scores the round       │
   │              Accuracy · Robustness · Attack Success  │
   │                                                      │
   └──────────────────────────────────────────────────────┘
```

---

## 📈 Results & Insights

<div align="center">

| Scenario | Clean Accuracy | Under Attack | After Defence |
|----------|---------------|-------------|---------------|
| FGSM (ε=0.1) | ~95% | ⬇️ ~30% | ⬆️ ~78% |
| PGD (ε=0.1) | ~95% | ⬇️ ~12% | ⬆️ ~65% |
| No Defence | ~95% | ⬇️ Critical | — |

</div>

**Key Takeaways:**
- ⚡ Models drop accuracy dramatically under even weak attacks
- 🛡️ Defence mechanisms significantly recover robustness
- ⚖️ There is always a **trade-off between accuracy and security** — stronger defence can reduce clean accuracy slightly

---

## 🔬 Attack Techniques

<table>
<tr>
<td width="50%">

### ⚡ FGSM — Fast Gradient Sign Method
The foundational adversarial attack. Adds a small perturbation in the direction of the gradient to maximize model loss.

```
x_adv = x + ε · sign(∇_x J(θ, x, y))
```
**Fast. Cheap. Surprisingly effective.**

</td>
<td width="50%">

### 💥 PGD — Projected Gradient Descent
Iterative version of FGSM. Runs multiple steps and projects back into the ε-ball. Considered the **strongest first-order attack**.

```
x_{t+1} = Π_{x+S}(x_t + α · sign(∇_x J))
```
**Slower. Much stronger.**

</td>
</tr>
</table>

---

## 🛡️ Defence Techniques

<table>
<tr>
<td width="33%">

### 🌀 Input Denoising
Removes adversarial perturbations before inference using filters or autoencoders

</td>
<td width="33%">

### 🎲 Randomized Smoothing
Adds controlled noise and uses majority voting to create certified defences

</td>
<td width="33%">

### 🏋️ Adversarial Training
Trains the model directly on adversarial examples — robustness from the ground up

</td>
</tr>
</table>

---

## 🛣️ Roadmap

- [x] Core simulation engine
- [x] FGSM attack module
- [x] PGD attack module
- [x] Basic defence mechanisms
- [x] Evaluation engine & metrics
- [ ] 🔄 Real-time visualization dashboard
- [ ] 🔄 LLM-based adversarial attacks
- [ ] 🔄 SIEM / SOC integration
- [ ] 🔄 Multi-agent Red vs Blue AI simulation
- [ ] 🔄 Docker containerization

---

## 👨‍💻 Author

<div align="center">

**Bennyhinn**

🎓 B.E. Computer Science Engineering · GNDEC Bidar · VTU
🔐 Cybersecurity · AI Security · Blockchain Systems
🏅 CEHv13 Certified · TryHackMe Red Team Practitioner

[![GitHub](https://img.shields.io/badge/GitHub-Bennyhinn007-181717?style=for-the-badge&logo=github)](https://github.com/Bennyhinn007)

</div>

---

## 🤝 Contributing

Pull requests are welcome.
If you have ideas for new attack types, defence strategies, or visualization — open an issue or PR and let's build together 💯

---

## 📚 References

- [Goodfellow et al. — Explaining and Harnessing Adversarial Examples (FGSM)](https://arxiv.org/abs/1412.6572)
- [Madry et al. — Towards Deep Learning Models Resistant to Adversarial Attacks (PGD)](https://arxiv.org/abs/1706.06083)
- [IBM Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>

**⭐ Star this repo if it helped you understand AI security better**

*Built with curiosity and a healthy paranoia about AI vulnerabilities.*

</div>
