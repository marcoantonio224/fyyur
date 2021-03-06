"""empty message

Revision ID: b15692564781
Revises: d8eee735654c
Create Date: 2020-07-11 18:03:27.787204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15692564781'
down_revision = 'd8eee735654c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('past_shows', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('upcoming_shows', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'upcoming_shows')
    op.drop_column('venues', 'past_shows')
    # ### end Alembic commands ###
