"""initial

Revision ID: 0dcaa87755a2
Revises: 
Create Date: 2024-03-15 18:17:37.317590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0dcaa87755a2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "node",
        sa.Column("id", sa.Integer(), nullable=False, index=True),
        sa.Column(
            "type",
            sa.Enum(
                "START_NODE",
                "MESSAGE_NODE",
                "CONDITION_NODE",
                "END_NODE",
                name="nodetype",
            ),
            nullable=False,
        ),
        sa.Column("description", sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("type"),
    )
    op.create_table(
        "workflow",
        sa.Column("id", sa.Integer(), nullable=False, index=True),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=True),
        sa.Column("node_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["node_id"],
            ["node.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_workflow_id"), table_name="workflow")
    op.drop_table("workflow")
    op.drop_index(op.f("ix_node_id"), table_name="node")
    op.drop_table("node")
