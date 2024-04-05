"""start

Revision ID: 500ceca3dad5
Revises: 944f9e8e7c50
Create Date: 2024-04-05 02:41:27.862672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '500ceca3dad5'
down_revision: Union[str, None] = '944f9e8e7c50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
