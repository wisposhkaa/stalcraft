from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'items.json'

def load_items():
    if not os.path.exists(DATA_FILE):
        default_items = [
            {"name": "Мякоть солевика", "price": 1900, "special_price": None, "special_threshold": None},
            {"name": "Аномальная плазма", "price": 2000, "special_price": None, "special_threshold": None},
            {"name": "Мякоть сластены", "price": 8300, "special_price": 8500, "special_threshold": 500},
            {"name": "Аномальная пыль", "price": 270, "special_price": None, "special_threshold": None},
            {"name": "Мякоть кубоарбуза", "price": 600, "special_price": None, "special_threshold": None},
            {"name": "Сахар", "price": 3900, "special_price": None, "special_threshold": None},
            {"name": "Мякоть лимонника", "price": 1000, "special_price": None, "special_threshold": None},
            {"name": "Темный лимб", "price": 135000, "special_price": None, "special_threshold": None},
            {"name": "Мультитул", "price": 3500, "special_price": None, "special_threshold": None},
            {"name": "Пурпурные минералы", "price": 300, "special_price": None, "special_threshold": None},
            {"name": "Набор болтов", "price": 4500, "special_price": None, "special_threshold": None},
            {"name": "Алые минералы", "price": 300, "special_price": None, "special_threshold": None},
            {"name": "Остатки приборов шепота", "price": 30000, "special_price": None, "special_threshold": None},
            {"name": "Батарея холодного синтеза", "price": 4000, "special_price": None, "special_threshold": None},
            {"name": "Железо", "price": 700, "special_price": None, "special_threshold": None},
            {"name": "Газовый баллон", "price": 5650, "special_price": None, "special_threshold": None},
            {"name": "Дрожжи", "price": 2000, "special_price": None, "special_threshold": None},
            {"name": "Аммиак", "price": 8000, "special_price": None, "special_threshold": None},
            {"name": "Ткань", "price": 1000, "special_price": None, "special_threshold": None},
            {"name": "Янтарная полынь", "price": 6500, "special_price": None, "special_threshold": None},
            {"name": "Сковорода/кастрюля", "price": 1800, "special_price": None, "special_threshold": None},
            {"name": "Чертоцвет", "price": 800, "special_price": None, "special_threshold": None}
        ]
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_items, f, ensure_ascii=False, indent=4)
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_items(items):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(load_items())

@app.route('/api/items', methods=['POST'])
def add_item():
    items = load_items()
    new_item = request.json
    items.append(new_item)
    save_items(items)
    return jsonify({"status": "success"})

@app.route('/api/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    items = load_items()
    if 0 <= index < len(items):
        items.pop(index)
        save_items(items)
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(debug=True)