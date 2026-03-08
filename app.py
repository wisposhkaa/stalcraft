from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

app = Flask(__name__)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    response = supabase.table('items').select('*').order('id').execute()
    return jsonify(response.data)

@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json
    supabase.table('items').insert(new_item).execute()
    return jsonify({"status": "success"})

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_data = request.json
    supabase.table('items').update(updated_data).eq('id', item_id).execute()
    return jsonify({"status": "success"})

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    supabase.table('items').delete().eq('id', item_id).execute()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)