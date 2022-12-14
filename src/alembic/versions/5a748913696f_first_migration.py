"""first migration

Revision ID: 5a748913696f
Revises: 
Create Date: 2022-11-13 10:23:40.993335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a748913696f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('max_speed', sa.Float(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.Column('cost_per_day', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ships_id'), 'ships', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ships_id'), table_name='ships')
    op.drop_table('ships')
    # ### end Alembic commands ###
