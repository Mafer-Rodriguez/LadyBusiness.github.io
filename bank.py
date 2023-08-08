class Usuario:
    def __init__(self, nombre, edad, direccion, saldo_inicial=0):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo actual de {self.nombre}: {self.saldo}")


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}\nCargo: {self.cargo}\nSalario: ${self.salario}")


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.empleados = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} agregado al banco.")

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado al banco.")

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None

    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                return empleado
        return None


# Crear un banco
banco = Banco("MiBanco")

# Agregar usuarios y empleados al banco
usuario1 = Usuario("Juan", 30, "Calle 123")
usuario2 = Usuario("Maria", 25, "Avenida 456")
banco.agregar_usuario(usuario1)
banco.agregar_usuario(usuario2)

empleado1 = Empleado("Carlos", "Cajero", 2500)
empleado2 = Empleado("Ana", "Gerente", 4000)
banco.agregar_empleado(empleado1)
banco.agregar_empleado(empleado2)

# Realizar operaciones para usuarios
usuario1.depositar(500)
usuario2.retirar(200)
usuario1.consultar_saldo()

# Buscar usuario y realizar operaciones
usuario_buscar = banco.buscar_usuario("Juan")
if usuario_buscar:
    usuario_buscar.retirar(300)
else:
    print("Usuario no encontrado.")

# Mostrar información de empleados
empleado1.mostrar_informacion()
empleado2.mostrar_informacion()
