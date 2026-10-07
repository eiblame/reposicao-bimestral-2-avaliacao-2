from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = database.buscar_usuario_por_email(email)
        if usuario:
            flash("Email já cadastrado.")
            return redirect("/registro")
        senha_hash = generate_password_hash(senha)
        database.criar_usuario(nome, email, senha_hash)
        
        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("registro"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))