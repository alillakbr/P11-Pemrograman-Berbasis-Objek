from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass

class INotificationService(ABC):
    @abstractmethod
    def send(self, order: Order):
        pass

class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print(f"Payment: Memproses tagihan Rp{order.total_price} via Kartu Kredit.")
        return True

class BankTransferProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print(f"Payment: Memproses tagihan Rp{order.total_price} via Transfer Bank.")
        return True

class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Notif: Email konfirmasi dikirim ke pelanggan {order.customer_name}.")

class CheckoutService:
    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def process_checkout(self, order: Order):
        print(f"--- Memulai Checkout untuk {order.customer_name} ---")
        
        success = self.payment_processor.process(order)
        
        if success:
            order.status = "paid"
            print("Status Order: LUNAS")
            self.notifier.send(order)
            print("Checkout Selesai.\n")
            return True
        else:
            print("Checkout Gagal.\n")
            return False

if __name__ == "__main__":
    order1 = Order("Andi", 500000)
    cc_processor = CreditCardProcessor()
    email_service = EmailNotifier()
    
    service_cc = CheckoutService(cc_processor, email_service)
    service_cc.process_checkout(order1)

    order2 = Order("Budi", 750000)
    bank_processor = BankTransferProcessor()
    
    service_bank = CheckoutService(bank_processor, email_service)
    service_bank.process_checkout(order2)