"""Add surname in driver model

Revision ID: dfa1d20c9136
Revises: 0f490e98ee8b
Create Date: 2025-02-11 18:39:51.749763

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfa1d20c9136'
down_revision: Union[str, None] = '0f490e98ee8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('driver', sa.Column('surname', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('driver', 'surname')
    # ### end Alembic commands ###
