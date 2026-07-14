# Unit Converter

A responsive web application built with Flask that converts between different units of measurement through a clean and user-friendly interface.

The application allows users to convert units of length, weight, and temperature 

## 📸 Demo

![Unit Converter Demo](assets/unit_converter_demo.gif)

## ✨ Features

- Convert Length units
- Convert Weight units
- Convert Temperature units
- Responsive and clean user interface
- Form validation
- Separate conversion pages for each category
- Dedicated result pages
- Session support to preserve previous input values
- Reusable Jinja template inheritance
- Navigation between conversion categories


## 📁 Project Structure

```text
.
├── assets
│   └── unit_converter_demo.gif
├── static
│   └── style.css
├── templates
│   ├── base_result.html
│   ├── index.html
│   ├── length.html
│   ├── length_result.html
│   ├── temperature.html
│   ├── temperature_result.html
│   ├── weight.html
│   └── weight_result.html
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

## 🛠 Technologies

- Python
- Flask
- HTML5
- CSS3
- Jinja2

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/danielmascian/web-unit-converter.git
```

Navigate to the project folder:

```bash
cd web-unit-converter
```

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python main.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 💡 Inspiration

This project was built as my solution to the **Unit Converter** project from **roadmap.sh**.

Project page:
https://roadmap.sh/projects/unit-converter

