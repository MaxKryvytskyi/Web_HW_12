"""start

Revision ID: 944f9e8e7c50
Revises: 7fea9a582b99
Create Date: 2024-04-05 02:41:06.666871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '944f9e8e7c50'
down_revision: Union[str, None] = '7fea9a582b99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
