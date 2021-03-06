"""Expanded length of genres

Revision ID: 95d6659df237
Revises: 2640c772e75b
Create Date: 2020-07-07 07:02:03.949004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95d6659df237'
down_revision = '2640c772e75b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###
