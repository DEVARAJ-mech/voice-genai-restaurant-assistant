from app.db.database import get_connection


def handle_reservation(text: str) -> str:
    # For demo: fixed extracted values
    name = "Customer"
    date = "Tomorrow"
    time = "19:00"
    guests = 4

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reservations (name, date, time, guests) VALUES (?, ?, ?, ?)",
        (name, date, time, guests)
    )

    conn.commit()
    conn.close()

    return (
        f"Your table for {guests} guests on {date} at {time} "
        "has been successfully reserved."
    )
