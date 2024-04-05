"""db

Revision ID: f1c409e1271e
Revises: 500ceca3dad5
Create Date: 2024-04-05 02:58:55.862009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1c409e1271e'
down_revision: Union[str, None] = '500ceca3dad5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
