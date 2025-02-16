"""Add confirmed bool to ride offer

Revision ID: 0f490e98ee8b
Revises: a9b2d2f2b72c
Create Date: 2025-02-11 10:41:29.931377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f490e98ee8b'
down_revision: Union[str, None] = 'a9b2d2f2b72c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rideoffer', sa.Column('confirmed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rideoffer', 'confirmed')
    # ### end Alembic commands ###
