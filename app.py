import os
import subprocess

from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

items = [
    {
        "id": 1,
        "name": "Scientific Calculator",
        "category": "Electronics",
        "price": 450,
        "condition": "Excellent",
        "seller": "Rahul",
        "description": "Used for one semester and works perfectly.",
        "status": "Available",
    },
    {
        "id": 2,
        "name": "DBMS Textbook",
        "category": "Books",
        "price": 300,
        "condition": "Good",
        "seller": "Kalyani",
        "description": "Useful for database management exam preparation.",
        "status": "Available",
    },
]

def get_commit_sha():
    # Check environment variables provided by CI/CD or Render
    for env_var in ["GIT_SHA", "RENDER_GIT_COMMIT", "COMMIT_SHA"]:
        val = os.getenv(env_var)
        if val and val != "local":
            return val[:7]
    
    # Fallback to local git command if available
    try:
        git_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], 
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
        if git_hash:
            return git_hash[:7]
    except Exception:
        pass
        
    return "local"

COMMIT = get_commit_sha()


@app.route("/")
def home():
    query = request.args.get("search", "").strip().lower()

    if query:
        filtered_items = [
            item
            for item in items
            if query in item["name"].lower()
            or query in item["category"].lower()
            or query in item["description"].lower()
        ]
    else:
        filtered_items = items

    available_count = sum(
        1 for item in items if item["status"] == "Available"
    )

    return render_template(
        "index.html",
        items=filtered_items,
        total_count=len(items),
        available_count=available_count,
        search=query,
        commit=COMMIT,
    )


@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "GET":
        return render_template("add_item.html", commit=COMMIT)

    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()
    price_text = request.form.get("price", "").strip()
    condition = request.form.get("condition", "").strip()
    seller = request.form.get("seller", "").strip()
    description = request.form.get("description", "").strip()

    if not name or not category or not price_text or not seller:
        return "Name, category, price and seller are required.", 400

    try:
        price = int(price_text)
    except ValueError:
        return "Price must be a valid number.", 400

    if price <= 0:
        return "Price must be greater than zero.", 400
    if len(name) < 2:
        return "Item name must contain at least 2 characters.", 400

    new_item = {
        "id": max([item["id"] for item in items], default=0) + 1,
        "name": name,
        "category": category,
        "price": price,
        "condition": condition or "Good",
        "seller": seller,
        "description": description,
        "status": "Available",
    }

    items.append(new_item)

    return redirect("/")


@app.route("/sell/<int:item_id>", methods=["POST"])
def mark_sold(item_id):
    for item in items:
        if item["id"] == item_id:
            item["status"] = "Sold"
            return redirect("/")

    return "Item not found.", 404


@app.route("/api/items")
def api_items():
    return jsonify(items)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "commit": COMMIT})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
