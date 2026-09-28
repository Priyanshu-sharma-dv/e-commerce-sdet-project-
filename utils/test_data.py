from faker import Faker

fake = Faker()

def new_email() -> str:
    return f"{fake.user_name()}_{fake.random_int(1000, 9999)}@example.com"

def new_customer():
    return {
        "name": fake.name(),
        "email": new_email(),
    }
