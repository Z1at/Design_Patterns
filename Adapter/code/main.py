# Target (Интерфейс, который ожидает клиент)
class NotificationService:
    def send_notification(self, message, recipient):
        raise NotImplementedError("Subclasses must implement this method")


# Adaptee (Класс, который нужно адаптировать)
class LegacyNotificationSystem:
    def send_legacy_notification(self, user_id, text):
        print(f"Legacy system: Sending notification '{text}' to user {user_id}")


# Adapter (Адаптер объектов)
class NotificationAdapter(NotificationService):
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def send_notification(self, message, recipient):
        # Преобразуем данные в формат, понятный для LegacyNotificationSystem
        self.legacy_system.send_legacy_notification(recipient, message)


# Использует только интерфейс NotificationService
class Client:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_message(self, message, recipient):
        self.notification_service.send_notification(message, recipient)


if __name__ == "__main__":
    legacy_system = LegacyNotificationSystem()
    adapter = NotificationAdapter(legacy_system)

    client = Client(adapter)
    client.send_message("Hello, world!", "12345")
