"""empty message

Revision ID: 0e2dbd8ee8e9
Revises: 2ac2b34251fa
Create Date: 2020-07-12 13:46:35.333117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e2dbd8ee8e9'
down_revision = '2ac2b34251fa'
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
