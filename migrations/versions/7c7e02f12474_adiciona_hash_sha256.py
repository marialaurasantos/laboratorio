"""adiciona hash_sha256

Revision ID: 7c7e02f12474
Revises: 0001
Create Date: 2026-10-06 16:36:24.463699
"""
from alembic import op
import sqlalchemy as sa


revision = '7c7e02f12474'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "arquivos",
        sa.Column("hash_sha256", sa.String(length=64), nullable=True)
    )

    op.create_index(
        "ix_arquivos_hash_sha256",
        "arquivos",
        ["hash_sha256"]
    )


def downgrade() -> None:
    op.drop_index(
        "ix_arquivos_hash_sha256",
        table_name="arquivos"
    )

    op.drop_column(
        "arquivos",
        "hash_sha256"
    )