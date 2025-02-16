"""Add foreign key to driver

Revision ID: 951847d038cc
Revises: cb80585cd022
Create Date: 2025-02-15 00:20:22.883542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '951847d038cc'
down_revision: Union[str, None] = 'cb80585cd022'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rideoffer', sa.Column('driver_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'rideoffer', 'driver', ['driver_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rideoffer', type_='foreignkey')
    op.drop_column('rideoffer', 'driver_id')
    # ### end Alembic commands ###
