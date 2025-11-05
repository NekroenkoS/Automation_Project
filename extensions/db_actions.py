# extensions/db_actions.py
import sqlite3
from typing import Optional, Sequence

from test_cases import conftest as conf


class DbActions:

    @staticmethod
    def create(table: str, data: dict) -> int:
        if not data:
            raise ValueError("create() requires non-empty data")
        cols = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        params = tuple(data.values())
        q = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        cur = conf.conn.execute(q, params)
        conf.conn.commit()
        return cur.lastrowid

    @staticmethod
    def select_one(table: str, where: dict, columns: Optional[Sequence[str]] = None):
        select_cols = ", ".join(columns) if columns else "*"
        clause, params = DbActions._where_clause(where)
        q = f"SELECT {select_cols} FROM {table} {clause} LIMIT 1"
        cur = conf.conn.execute(q, params)
        return cur.fetchone()

    @staticmethod
    def update_one(table: str, data: dict, where: dict) -> int:
        if not data:
            raise ValueError("update_one() requires non-empty data")
        if not where:
            raise ValueError("update_one() requires WHERE")

        set_csv = ", ".join([f"{k}=?" for k in data.keys()])
        set_params = tuple(data.values())
        clause, where_params = DbActions._where_clause(where)
        q = f"UPDATE {table} SET {set_csv} {clause}"

        cur = conf.conn.execute(q, set_params + where_params)
        conf.conn.commit()
        return cur.rowcount

    @staticmethod
    def delete_one(table: str, where: dict) -> int:
        if not where:
            raise ValueError("delete_one() requires WHERE")

        clause, params = DbActions._where_clause(where)
        q = f"DELETE FROM {table} {clause}"

        cur = conf.conn.execute(q, params)
        conf.conn.commit()
        return cur.rowcount

    @staticmethod
    def scalar(query: str, params=()):
        cur = conf.conn.execute(query, params)
        row = cur.fetchone()
        return row[0] if row is not None else None

    @staticmethod
    def exists(table: str, where: dict) -> bool:
        clause, params = DbActions._where_clause(where)
        q = f"SELECT 1 FROM {table} {clause} LIMIT 1"
        return DbActions.scalar(q, params) is not None

    @staticmethod
    def _where_clause(where: dict):
        parts, params = [], []
        for k, v in where.items():
            if v is None:
                parts.append(f"{k} IS NULL")
            else:
                parts.append(f"{k}=?")
                params.append(v)
        clause = "WHERE " + " AND ".join(parts) if parts else ""
        return clause, tuple(params)
