from flask import flask , render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"

#base de datos simulada en memoria 
usuarios=[] #almacena: nombre, apellido, email, contraseña
pelicula =[
    {
    "id": 1,
    "titulo": "interestellar",
    "director": "christopher nolan",
    "estreno": "2014-11-07",
    "sinopsis": "un grupo de cientificos viaja a traves de un abujero de gusano..",
    }   "creador": "valentina"
    {
    "id":2,
    "titulo": "perdida",
    "director": "david fincher",
    "estreno": "2014-09-26",
    "sinopsis": "con la desaparicion de su esposa en su quinto aniversario de bodas...",
    "creador": "valentina"
    }
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro", methods=["post"])
def registro():
    nombre = request.form("nombre")
    apellido = request.form("apellido")
    email = request.form("email")
    contraseña = request.form("contraseña")
    conf_contrseña = request.form.get("conf_contraseña")

#validaciones del examen
if len(nombre)<2 or len(apellido) <2:
    return"error: nombre y apellido deben tener al menos 2 caracteristicas"
    if contraseña != conf_contraseña:
    return "error: las contraseñas no coinciden"

for u in ususarios:
        if u["email"]==email: 
         return "error: el email ya esta registrado"
    usuarios.append({
    "nombre": nombre,
    "apellido": apellido,
    "email": email,
    "contraseña": contraseña

        })
        return redirect(url_for("index"))

@app.route("/login", methods=["post"])
def login():
      email  = request.form.get("email")
      contraseña= resquest.form.get("contraseña")
for u in usuarios:
      if u ["email"] == email and u ["contraseña"] == contraseña:
            session["usuario"] = u["nombre"]
            return redirect(url_for("dashboard"))

      rerurn "error: credenciales invalidas o email no registrado."

@app.route("/cine")
def dashboard():
      if "usuario" not in session:
            return redirect(url_for("index"))
      return render_template("deshboard.html", peliculas=peliculas, usuario=session["usuario"])
    
@app.route("/cine/nuevo", methods=["post"])
def nueva_pelicula():
    if "usuario" not in session:
        return redirect(url_for("index"))
    if request.method =="post":
        titulo = request.form.get("titulo")
        director = request.form.get("director")
        estreno = request.form.get("estreno")
        sinopsis = request.form.get("sinopsis")

#bonus: nombre de pelicula unica
for p in peliculas:
     if p ["titulo"].lower()== titulo.lower():
            return "error: la pelicula ya existe"
     
     nueva_id = len(peliculas) + 1
     peliculas.append({
          "id":nueva_id,
          "titulo": titulo,
          "director": director,
          "estreno": estreno,
          "sinopsis": sinopsis
     })
     return redirect(url_for("dashboard"))

return render_template("nueva_pelicula.html")

@app.route("/cine/<int:id_pelicula>")
def detalle_pelicula(id_pelicula):
    if "usuario" not in session:
        return redirect(url_for("index"))
    pelicula = next((p for p in peliculas if p["id"] == id_pelicula), None)
    if not pelicula:
        return "pelicula no encontrada"
    return render_template("detalle_pelicula.html", pelicula=pelicula,)
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
     app.run(debug=True, port=5000)
