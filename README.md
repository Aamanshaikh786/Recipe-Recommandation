# 🍽️ Recipe Recommendation System

The **Recipe Recommendation System** is a Flask-based web application that suggests recipes based on the ingredients entered by the user. It helps users discover dishes they can prepare with what they already have, reducing food waste and saving time.

The project uses a **MongoDB database** to store recipe data, which includes cleaned and preprocessed ingredients. When the user inputs a list of ingredients, the system compares them with stored recipes, calculates a **match score**, and displays the **top 5 most relevant recipes**. These recipes are ranked first by ingredient match and then sorted by total ingredients for easier preparation.

Data loading is handled by the `load_data.py` script, which processes a CSV file and inserts it into MongoDB. The main web application (`app.py`) uses Flask routes to take user input, compute recommendations, and render results dynamically through HTML templates (`index.html` and `results.html`).

---

## 🔧 Tech Stack
- **Backend:** Python (Flask)  
- **Database:** MongoDB  
- **Libraries:** Pandas, PyMongo, AST  
- **Frontend:** HTML, CSS  

---

## ⚙️ How It Works
1. Load recipe data into MongoDB using `load_data.py`.  
2. Run `app.py` to start the web server.  
3. Enter ingredients (e.g., *tomato, onion, garlic*) to get recipe suggestions.  

---

## 🌱 Future Scope
- Add recipe images and detailed cooking instructions.  
- Integrate filters for cuisine type or cooking time.  
- Deploy the app online with MongoDB Atlas.

---

⭐ **Feel free to fork, contribute, or suggest improvements!**
