"""restringe status

Revision ID: b40c66bc68c0
Revises: 7c7e02f12474
Create Date: 2026-10-06 17:20:53.606374
"""
from alembic import op
import sqlalchemy as sa


revision = 'b40c66bc68c0'
down_revision = '7c7e02f12474'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_check_constraint(
        "ck_arquivos_status",
        "arquivos",
        "status IN ('pendente', 'concluido')"
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_arquivos_status",
        "arquivos",
        type_="check"
    )