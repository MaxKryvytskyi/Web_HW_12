"""db

Revision ID: 015243ab19f0
Revises: f1c409e1271e
Create Date: 2024-04-05 02:59:02.720331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '015243ab19f0'
down_revision: Union[str, None] = 'f1c409e1271e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
