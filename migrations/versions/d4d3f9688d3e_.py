"""empty message

Revision ID: d4d3f9688d3e
Revises: 94143c8196e6
Create Date: 2020-07-16 07:42:36.295866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d3f9688d3e'
down_revision = '94143c8196e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shows', 'artist_image_link',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shows', 'artist_image_link',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###