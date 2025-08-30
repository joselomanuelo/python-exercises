class Invoice:
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float):
        self.items.append({"name": name, "price": price})

    def get_total(self) -> float:
        return sum(item["price"] for item in self.items)

    # ❌ This method is responsible for formatting the invoice as text
    def to_text(self) -> str:
        output = "Invoice:\n"
        for item in self.items:
            output += f"{item['name']}: ${item['price']}\n"
        output += f"Total: ${self.get_total()}\n"
        return output

    # ❌ This method is responsible for saving the invoice to a file
    def save_to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(self.to_text())


invoice = Invoice()
invoice.add_item("Laptop", 1200)
invoice.add_item("Mouse", 25)
invoice.save_to_file("invoice.txt")

"""
EXERCISE (Single Responsibility Principle - SRP):

Right now, the class Invoice is doing THREE different things:
1. It manages invoice items and calculates the total.
2. It formats the invoice as text.
3. It saves the invoice to a file.

⚠️ This violates SRP because a class should have ONLY ONE reason to change.

👉 Your task:
- Refactor the code into SEPARATE classes.
- One class should handle the invoice data and total calculation.
- One class should handle formatting/printing.
- One class should handle saving to a file.

After refactoring, each class must have ONLY ONE responsibility.
"""
