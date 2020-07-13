"""empty message

Revision ID: 2ac2b34251fa
Revises: 11e61ab749b9
Create Date: 2020-07-12 11:49:08.505931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ac2b34251fa'
down_revision = '11e61ab749b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_name', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'artist_name')
    # ### end Alembic commands ###
