from ..models.base import Base
from ..db.session import engine, SessionLocal
from ..models import user, token, market, signal, narrative, portfolio, alert, report  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)

    # Seed admin user if none exists; password printed to console once (not stored plain)
    from argon2 import PasswordHasher
    from ..models.user import User

    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.email == "admin@example.com").first()
        if not admin:
            ph = PasswordHasher()
            admin = User(email="admin@example.com", password_hash=ph.hash("admin"))
            db.add(admin)
            db.commit()
            print("Admin created: admin@example.com / password: admin")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
