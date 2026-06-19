from database.db_manager import (
    create_database,
    save_result,
    get_results
)

create_database()

save_result(
    "Jenish",
    85.5
)

data = get_results()

print(data)