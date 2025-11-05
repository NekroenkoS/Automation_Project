import sqlite3

import allure
import pytest

from extensions.verifications import Verifications
from utilities.common_ops import get_data
from workflows.db_flows import DbFlows
from workflows.web_flows import WebFlows

new_user = get_data("DB_USER")
password = get_data("DB_PASSWORD")


@pytest.mark.usefixtures("init_db_driver")
class TestDB:

    @allure.title("Test 1 - Verify Creating User In Db And Connecting To Site")
    @allure.description("This test verifies user creation in db and login to site via that user")
    def test_01_verify_user_created(self,init_web_driver):
        id = DbFlows.create_user(new_user, password)
        row = DbFlows.read_user_by_id(id)
        WebFlows.step_click_login_button()
        WebFlows.step_fill_login_information(row[1], row[2])
        WebFlows.step_click_login_button_inside_login_form()
        WebFlows.verify_login_successful(row[1])
        DbFlows.delete_user_by_id(id)

    @allure.title("Test 2 - Verify Unique Username In Db Error")
    @allure.description("This test verifies that adding duplicate names will fail")
    def test_02_verify_unique_username_enforced(self):
        if not DbFlows.read_user_by_name("sergey"):
            DbFlows.create_user("sergey", "123456")
        DbFlows.verify_unique_violation_on_create("sergey", "whatever")

    @allure.title("Test 3 - Verify Update Nonexistent User Returns Zero")
    @allure.description("This test verifies that updating a non existent row will return 0 rows affected")
    def test_03_verify_update_nonexistent_returns_zero(self):
        affected = DbFlows.update_user_name(999999, "ghost")
        Verifications.verify_equals(affected, 0)

    @allure.title("Test 4 - Verify Empty Username Is Not Allowed")
    @allure.description("This test verifies that empty usernames are rejected by the DB")
    def test_04_empty_username_not_allowed(self):
        with pytest.raises(sqlite3.IntegrityError):
            DbFlows.create_user("", "123456")
