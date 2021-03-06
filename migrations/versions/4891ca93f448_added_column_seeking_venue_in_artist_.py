"""Added column seeking_venue in Artist table

Revision ID: 4891ca93f448
Revises: 95d6659df237
Create Date: 2020-07-07 07:43:15.921280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4891ca93f448'
down_revision = '95d6659df237'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('past_shows', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'past_shows')
    # ### end Alembic commands ###
