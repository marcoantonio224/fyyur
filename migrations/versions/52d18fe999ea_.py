"""empty message

Revision ID: 52d18fe999ea
Revises: 761c9188154a
Create Date: 2020-07-11 17:38:56.475452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52d18fe999ea'
down_revision = '761c9188154a'
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
