from typing import List, Dict

class Invoice:
    def __init__(self):
        self.items: List[Dict[str, float]] = []

    def add_item(self, name: str, price: float) -> None:
        self.items.append({"name": name, "price": price})

    def get_total(self) -> float:
        return sum(item["price"] for item in self.items)


def invoice_to_text(inv: Invoice) -> str:
    output = "Invoice:\n"
    for item in inv.items:
        output += f"{item['name']}: ${item['price']}\n"
    output += f"Total: ${inv.get_total()}\n"
    return output


def save_invoice_to_file(filename: str, inv: Invoice) -> None:
    with open(filename, "w") as f:
        f.write(invoice_to_text(inv))


# Example usage
if __name__ == "__main__":
    invoice = Invoice()
    invoice.add_item("Laptop", 1200)
    invoice.add_item("Mouse", 25)

    save_invoice_to_file("invoice.txt", invoice)
