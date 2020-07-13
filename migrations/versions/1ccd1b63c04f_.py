"""empty message

Revision ID: 1ccd1b63c04f
Revises: 0e2dbd8ee8e9
Create Date: 2020-07-12 14:06:49.895473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ccd1b63c04f'
down_revision = '0e2dbd8ee8e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('past_shows', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('upcoming_shows', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'upcoming_shows')
    op.drop_column('artists', 'past_shows')
    # ### end Alembic commands ###
