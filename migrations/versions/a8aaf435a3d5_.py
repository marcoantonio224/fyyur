"""empty message

Revision ID: a8aaf435a3d5
Revises: 959369e0e71c
Create Date: 2020-07-11 17:07:41.906480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8aaf435a3d5'
down_revision = '959369e0e71c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'upcoming_shows_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
