from pedidos.models import Category, Product, User

def insertar_datos_dummy():
    # Crear Categorías
    cat1 = Category.objects.create(name="Lácteos", description="Productos lácteos como leche y queso.")
    cat2 = Category.objects.create(name="Bebidas", description="Bebidas refrescantes y jugos.")

    # Crear Productos
    Product.objects.create(category=cat1, name="Leche Entera", description="Leche entera de 1 litro.", price=1.20, stock=100)
    Product.objects.create(category=cat1, name="Queso Manchego", description="Queso manchego de 500g.", price=5.50, stock=50)
    Product.objects.create(category=cat2, name="Jugo de Naranja", description="Jugo natural de naranja de 1 litro.", price=2.00, stock=75)
    Product.objects.create(category=cat2, name="Refresco Cola", description="Refresco de cola de 2 litros.", price=1.80, stock=120)

    # Crear Usuario
    User.objects.create_user(username="cliente1", email="cliente1@example.com", password="12345")

    print("Datos dummy insertados correctamente.")
