from flask import Flask, render_template,url_for,request,redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from forms import SignupForm
from forms import PostForm
from forms import LoginForm
from models import *


app = Flask(__name__)

app.config['SECRET_KEY']= '8345U34FJFJRENFSDU345UR3I45734FSDF394534RE'#esto lo pide flask wtf para tener proteccion contra vulnerabilidad csrf

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost:5476/miwebFlask'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #NOS ENVIA UNA SEÑAL CUANDO HAGAMOS UN CAMBIO EN LAS TABLAS

db.init_app(app) #reconoce sqlalchemy

login_manager.init_app(app) #asi lo tenemos accesible

login_manager.login_view="login" #esto se realiza para en caso de no estar logeado te lleve a la pagina login en este caso

@app.before_request #crea la tabla antes
def create_table():
    db.create_all()


elNombre=""
LosPost=[]


@app.route("/")
@app.route("/inicio") #esto son decoradores
def inicio():
    return render_template('index.html',lista_post=LosPost)
    
@app.route("/servicios") #pagina de quienes somos
def servicios():
    return render_template('servicios.html')

@app.route("/productos") #pagina de quienes somos
@login_required #para que solo los que esten logeados vean lo que tiene dentro
def productos():
    return render_template('productos.html')

'''@app.route('/usuarios/<string:nombreusuario>')
def usuarios(nombreusuario):
    return "Bienvenido a la web " + nombreusuario'''

@app.route('/usuarios/<int:Idusuario>') #las url no tienen que tener el mismo nombre que las vistas
def usuarios(Idusuario):
    #return "Bienvenido a la web usuario numero {}" .format(Idusuario)
    return render_template('usuarios/usuarios.html',Num_usuario=Idusuario)

@app.route("/usuarios/<int:id>/<string:nombreusuario>")
def datosusuario(id,nombreusuario):
    #return "Estos son los datos del usuario. Id: {}. Nombre Usuario: {} ".format(id,nombreusuario)
    return render_template('usuarios/datosusuario.html',id=id,nombreusuario=nombreusuario)

@app.route("/post")
@app.route('/post/<int:npost>')
def post(npost=0):#se le da un valor por defecto para evitar errores coge 0 como valor por defecto
    return "Este es el post nª {}".format(npost)

@app.route('/contacto',methods =["GET","POST"])#metodo post para enviar informacion
def contacto():
    global elNombre
    form=SignupForm() #formulario de validacion

    if form.validate_on_submit():#almacenamos la informacion en estas variables y esto hace que solo guarde si esta todo validado
        nombre=form.name.data
        email=form.email.data
        contra=form.password.data

        elNombre=nombre

        return redirect(url_for("inicio")) #redirecciona a la pagina de inicio
    return render_template('contacto.html',form=form)

@app.route('/blog',methods =["GET","POST"],defaults={'post_id': None})#metodo post para enviar informacion
@app.route('/blog/<int:npost>',methods =["GET","POST"])
def blog(post_id):
    global LosPost
    form=PostForm() #formulario de validacion

    if form.validate_on_submit():#almacenamos la informacion en estas variables y esto hace que solo guarde si esta todo validado
        Titulo=form.title.data
        Contenido=form.content.data

        print(Titulo,Contenido)

        post={'title:':Titulo,'content:':Contenido}

        print(post)

        LosPost.append(post)

        print(LosPost)
        

        return redirect(url_for("inicio")) #redirecciona a la pagina de inicio
    return render_template('entradaBlog.html',form=form)

@app.route('/login',methods =["GET","POST"])#metodo post para enviar informacion
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))
    form=LoginForm() #formulario de validacion

    """if form.validate_on_submit():
        user=get_user(form.email.data)

        if user is not None and (user.check_password(form.password.data))==form.password.data:

            login_user(user,remember=form.remember_me.data)
            next_page=request.args.get("next") #si el usuario intenta acceder a una pagina restringida si no esta autenticado
            if not next_page:
                next_page=url_for("inicio")
            return redirect(next_page)"""
    
    if form.validate_on_submit():
        email=request.form["email"]
        user=User.query.filter_by(email=email).first() #fisrt es para que encuentre el primer email

        if user is not None and  user.check_password(request.form["password"]):
            login_user(user)
            return redirect("/productos")
    
    return render_template('login.html',form=form)

@app.route('/registro',methods =["GET","POST"])#metodo post para enviar informacion
def registro():
    
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))
    
    form=SignupForm() #formulario de validacion

    if form.validate_on_submit():
        nombre=form.name.data
        email=form.email.data
        contra=form.password.data

        user = User(email=email,name=nombre) #con len almacenamos los id de forma correlativa al numero de registros
        user.set_password(contra)
        

        #login_user(user,remember=True) #asi queda logeado el usuario

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('inicio'))

        
    else:
        return render_template('registro_form.html',form=form)
    


@app.route('/logout')
def logout():
    logout_user() #forma de hacer un log out
    return redirect(url_for('inicio'))

if __name__ == "__main__": #para permitir trabajar con development para ver los cambios en este caso se activa con **python app.py**

    os.environ["FLASK_ENV"]="development"
    app.run(debug=True)