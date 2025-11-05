import sqlite3

import allure
from extensions.db_actions import DbActions
from extensions.verifications import Verifications


class DbFlows:

    @staticmethod
    @allure.step("Verifying UNIQUE violation when creating existing user: {name}")
    def verify_unique_violation_on_create(name: str, password: str):
        try:
            DbActions.create("users", {"name": name, "password": password})
            # If we got here, insert succeeded (BAD) → fail
            raise AssertionError("Expected UNIQUE constraint to fail, but insert succeeded.")
        except sqlite3.IntegrityError as e:
            allure.attach(str(e), "integrity_error", allure.attachment_type.TEXT)
            Verifications.verify_true("UNIQUE" in str(e))
            return True


    @staticmethod
    @allure.step("DB • Create user: {name}")
    def create_user(name: str, password: str) -> int:
        new_id = DbActions.create("users", {
            "name": name,
            "password": password
        })
        allure.attach(f"id={new_id}", "created_user_id", allure.attachment_type.TEXT)
        Verifications.verify_true(new_id > 0)
        return new_id

    @staticmethod
    @allure.step("DB • Read user by id: {user_id}")
    def read_user_by_id(user_id: int):
        row = DbActions.select_one("users", {"id": user_id})
        if row:
            try:
                allure.attach(str(dict(row)), "user_row", allure.attachment_type.TEXT)
            except Exception:
                allure.attach(str(row), "user_row", allure.attachment_type.TEXT)
        return row

    @staticmethod
    @allure.step("DB • Read user by name: {name}")
    def read_user_by_name(name: str):
        row = DbActions.select_one("users", {"name": name})
        if row:
            try:
                allure.attach(str(dict(row)), "user_row", allure.attachment_type.TEXT)
            except Exception:
                allure.attach(str(row), "user_row", allure.attachment_type.TEXT)
        return row

    @staticmethod
    @allure.step("DB • Update user name: id={user_id} → {new_name}")
    def update_user_name(user_id: int, new_name: str) -> int:
        affected = DbActions.update_one("users", {"name": new_name}, {"id": user_id})
        allure.attach(f"rows_affected={affected}", "update_user_name", allure.attachment_type.TEXT)
        Verifications.verify_true(affected in (0, 1))
        return affected

    @staticmethod
    @allure.step("DB • Update user password: id={user_id}")
    def update_user_password(user_id: int, new_password: str) -> int:
        affected = DbActions.update_one("users", {"password": new_password}, {"id": user_id})
        allure.attach(f"rows_affected={affected}", "update_user_password", allure.attachment_type.TEXT)
        Verifications.verify_true(affected in (0, 1))
        return affected

    @staticmethod
    @allure.step("DB • Delete user by id: {user_id}")
    def delete_user_by_id(user_id: int) -> int:
        affected = DbActions.delete_one("users", {"id": user_id})
        allure.attach(f"rows_affected={affected}", "delete_user_by_id", allure.attachment_type.TEXT)
        Verifications.verify_true(affected in (0, 1))
        return affected

    @staticmethod
    @allure.step("DB • Verify user exists by name: {name}")
    def verify_user_exists_by_name(name: str) -> bool:
        exists = DbActions.exists("users", {"name": name})
        allure.attach(str(exists), "user_exists_by_name", allure.attachment_type.TEXT)
        Verifications.verify_true(exists)
        return exists

    @staticmethod
    @allure.step("DB • Verify user NOT exists by name: {name}")
    def verify_user_not_exists_by_name(name: str) -> bool:
        exists = DbActions.exists("users", {"name": name})
        allure.attach(str(exists), "user_exists_by_name", allure.attachment_type.TEXT)
        Verifications.verify_false(exists)
        return not exists
