import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, "печиво", "солодке", 30)
    water_qnt = database.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, "тестові", "дані", 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення", orders)

    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_checking_table_relationships(database):
    customers_table = database.get_checking_table_relationships("customers")
    orders_table = database.get_checking_table_relationships("orders")
    products_table = database.get_checking_table_relationships("products")

    # checking relationships between tables
    assert customers_table[0][0] == orders_table[0][1]
    assert products_table[0][0] == orders_table[0][2]


@pytest.mark.database
def test_check_data_types(database):
    name_customers = database.check_data_types("customers")

    # checking the data type from the table
    assert type(name_customers[0][0]) == str


@pytest.mark.database
def test_checking_the_number_of_symbols(database):
    number_columns = database.get_checking_table_relationships("orders")

    # check whether the entered time data is correct
    assert len(number_columns[0][3]) == 8


@pytest.mark.database
def test_check_address_by_id(database):
    user = database.get_address_by_id(1)

    # address verification by id
    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"


@pytest.mark.database
def test_add_new_customer(database):
    database.insert_new_customer(
        4, "Nazarii", "Doroshenko str.", "Boryslav", "82300", "Ukraine"
    )
    new_customer = database.get_user_address_by_name("Nazarii")
    # check whether there is a new client
    assert new_customer[0][1] == "Boryslav"


@pytest.mark.database
def test_customer_delete(database):
    database.delete_customer_by_id(4)
    names_customers = database.check_data_types("customers")
    # is there a user with this name
    assert "Nazarii" not in names_customers[0]
    assert "Nazarii" not in names_customers[1]
