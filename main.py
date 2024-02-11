from flask import Flask, render_template, request, redirect, abort, flash, url_for
import sqlite3

app = Flask(__name__)




@app.route('/', methods=["GET", "POST"])
def index():
    conn = sqlite3.connect('plushi.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM plushi")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)



@app.route('/add_plush/', methods=["GET", "POST"])
def add_plush():
    if request.method == "POST":
        animal = request.form['animal']
        accessories = request.form['accessories']
        size = request.form['size']

        conn = sqlite3.connect('plushi.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO plushi (animal, accessories, size) VALUES (?, ?, ?)",
                       (animal, accessories, size))
        conn.commit()
        conn.close()

        return render_template("index.html")


'''@app.route('/save_plushi/<int:plush_id>', methods=["GET", "POST"])
def save_plushi(plush_id):
    try:
        with app.app_context():
            with sqlite3.connect('plushi.db') as conn:
                cursor = conn.cursor()
                plush = cursor.execute("SELECT * FROM plushi WHERE ID = ?", (plush_id,)).fetchone()
                if plush is None:
                    abort(404)
                cursor.execute("INSERT INTO save_plushi (plush_id, animal, accessories, size) VALUES (?, ?, ?)",
                               (plush_id, plush[1], plush[2], plush[3]))
                conn.commit()

        flash('Plush saved!')
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        flash('error')

    return redirect(url_for('index'))'''



app.run(port=73000, debug=True)