

def EvaluadorUsuario (usuario):
    if usuario.isalnum():
        if len(usuario)<5:
            return "El usuario no puede tener menos de 5 carácteres"
        elif len(usuario)>15:
            return "El usuario no puede tener mas de 15 carácteres"
        else:
            return True
    else:
        return "El usuario solo puede contener letras y numeros"

def EvaluadorContraseña (contraseña):
    mayuscula=False
    minuscula=False
    if contraseña.isalnum():
        return "La contraseña debe tener un caracter especial"
    else:
        if len(contraseña)<10:
            return "La contraseña debe tener 10 caracteres"
        else:
            for i in contraseña:
                if i.isupper(): mayuscula = True
                elif i.islower(): minuscula=True
                elif i==" ": return "La contraseña no puede tener espacios en blanco"
            if mayuscula and minuscula:
                return True 
            else: 
                "La contraseña no es segura"
            

        