from extensions import db
from datetime import datetime


# =========================
# CATEGORIAS (Hombre / Mujer)
# =========================
class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    productos = db.relationship("Producto", backref="categoria", lazy=True)


# =========================
# PRODUCTOS
# =========================
class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float, nullable=False)
    imagen = db.Column(db.String(255))
    stock = db.Column(db.Integer, default=0)
    activo = db.Column(db.Boolean, default=True)

    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"))

    colecciones = db.relationship(
        "ProductoColeccion",
        back_populates="producto",
        cascade="all, delete-orphan"
    )


# =========================
# COLECCIONES
# =========================
class Coleccion(db.Model):
    __tablename__ = "colecciones"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)

    productos = db.relationship(
        "ProductoColeccion",
        back_populates="coleccion",
        cascade="all, delete-orphan"
    )


# =========================
# RELACION PRODUCTO - COLECCION
# =========================
class ProductoColeccion(db.Model):
    __tablename__ = "producto_coleccion"

    id = db.Column(db.Integer, primary_key=True)

    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))
    coleccion_id = db.Column(db.Integer, db.ForeignKey("colecciones.id"))

    producto = db.relationship("Producto", back_populates="colecciones")
    coleccion = db.relationship("Coleccion", back_populates="productos")


# =========================
# CARRITO
# =========================
class Carrito(db.Model):
    __tablename__ = "carritos"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship(
        "CarritoItem",
        back_populates="carrito",
        cascade="all, delete-orphan"
    )


# =========================
# ITEMS DEL CARRITO
# =========================
class CarritoItem(db.Model):
    __tablename__ = "carrito_items"

    id = db.Column(db.Integer, primary_key=True)

    carrito_id = db.Column(db.Integer, db.ForeignKey("carritos.id"))
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))

    cantidad = db.Column(db.Integer, default=1)
    talle = db.Column(db.String(10))

    carrito = db.relationship("Carrito", back_populates="items")
    producto = db.relationship("Producto")