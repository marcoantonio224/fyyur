"""Expanded length of genres in Venue

Revision ID: 2640c772e75b
Revises: d5feb630f87a
Create Date: 2020-07-07 07:01:35.738439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2640c772e75b'
down_revision = 'd5feb630f87a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
