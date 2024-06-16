class Shoe:
    def __init__(self, name, size, color, quantity, sku):
        self.name = name
        self.size = size
        self.color = color
        self.quantity = quantity
        self.sku = sku

    def __repr__(self):
        return (

            f"  name='{self.name}',\n"
            f"  size={self.size},\n"
            f"  color='{self.color}',\n"
            f"  quantity={self.quantity},\n"
            f"  sku='{self.sku}'\n"
        )


