from app.models import Order, IceCreamFlavor, db

def generate_statistics():
    """
    Generates sales statistics such as most popular flavors and total sales.
    """
    # Example: Calculate total number of ice creams sold
    total_sales = Order.query.count()

    # Example: Find the most popular flavor
    # This is a simplistic approach; for real applications, consider more efficient queries.
    flavor_counts = db.session.query(IceCreamFlavor.name, db.func.count(Order.id)).join(Order).group_by(IceCreamFlavor.name).all()
    most_popular = max(flavor_counts, key=lambda x:x[1], default=("None", 0))

    return {
        'total_sales': total_sales,
        'most_popular_flavor': most_popular[0],
        'most_popular_flavor_sales': most_popular[1]
    }
